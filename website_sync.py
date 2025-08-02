#!/usr/bin/env python3
"""
360TFT Website Sync System
==========================

Syncs content from automation repository to website repository,
maintaining website performance while providing fresh content.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import datetime
import logging
import yaml
import re


class WebsiteSyncManager:
    """
    Manages synchronization of content from automation repo to website repo,
    ensuring only necessary, website-ready content is transferred.
    """
    
    def __init__(self, automation_repo_path: str, website_repo_path: str):
        """
        Initialize the website sync manager.
        
        Args:
            automation_repo_path: Path to automation repository
            website_repo_path: Path to website repository
        """
        self.automation_path = Path(automation_repo_path)
        self.website_path = Path(website_repo_path)
        
        # Setup logging
        self.setup_logging()
        
        # Sync configuration
        self.sync_config = self.load_sync_config()
        
        # Content mappings
        self.sync_mappings = {
            # Blog posts: automation → website
            "blog_posts": {
                "source": "produced_content",
                "target": "_posts",
                "pattern": "**/Blog_Post_*.md",
                "transform": "blog_post_to_jekyll"
            },
            # Cheatsheets: automation → website assets
            "cheatsheets": {
                "source": "cheatsheets",
                "target": "assets/cheatsheets", 
                "pattern": "*.html",
                "transform": "cheatsheet_to_asset"
            },
            # Academy resources: automation → website
            "academy_resources": {
                "source": "output_for_website/academy_content",
                "target": "academy",
                "pattern": "*.md",
                "transform": "academy_content"
            },
            # Downloadable resources
            "resources": {
                "source": "output_for_website/resources",
                "target": "resources",
                "pattern": "*",
                "transform": "copy_direct"
            }
        }
        
        print(f"Website sync: {self.automation_path} → {self.website_path}")
    
    def setup_logging(self):
        """Setup sync logging."""
        log_dir = self.automation_path / "logs" / "website_sync"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"sync_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Website sync manager initialized")
    
    def load_sync_config(self) -> Dict:
        """Load sync configuration."""
        config_file = self.automation_path / "config" / "website_sync_config.json"
        
        default_config = {
            "sync_schedule": "daily",
            "sync_items": ["cheatsheets", "blog_posts", "resources"],
            "blog_post_settings": {
                "auto_publish": False,
                "require_review": True,
                "default_layout": "post",
                "default_category": "coaching"
            },
            "cheatsheet_settings": {
                "auto_publish": True,
                "generate_thumbnails": False,
                "update_vault": True
            },
            "performance_settings": {
                "max_file_size_mb": 10,
                "compress_images": True,
                "minify_html": False
            },
            "safety_settings": {
                "backup_before_sync": True,
                "dry_run_first": False,
                "verify_after_sync": True
            }
        }
        
        if config_file.exists():
            with open(config_file, 'r') as f:
                loaded_config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in loaded_config:
                        loaded_config[key] = value
                return loaded_config
        else:
            # Create default config
            config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def analyze_sync_scope(self) -> Dict:
        """Analyze what content is available for sync."""
        self.logger.info("Analyzing sync scope...")
        
        analysis = {
            "available_content": {},
            "sync_candidates": {},
            "total_files": 0,
            "total_size_mb": 0,
            "last_sync": None
        }
        
        # Check each sync mapping
        for content_type, mapping in self.sync_mappings.items():
            source_path = self.automation_path / mapping["source"]
            analysis["available_content"][content_type] = {
                "source_exists": source_path.exists(),
                "file_count": 0,
                "size_mb": 0,
                "files": []
            }
            
            if source_path.exists():
                # Find matching files
                if mapping["pattern"] == "*":
                    files = list(source_path.rglob("*"))
                else:
                    files = list(source_path.glob(mapping["pattern"]))
                    files.extend(list(source_path.rglob(mapping["pattern"])))
                
                # Filter to actual files
                files = [f for f in files if f.is_file()]
                
                # Calculate stats
                total_size = sum(f.stat().st_size for f in files)
                
                analysis["available_content"][content_type].update({
                    "file_count": len(files),
                    "size_mb": round(total_size / (1024 * 1024), 2),
                    "files": [str(f.relative_to(source_path)) for f in files[:10]]  # First 10
                })
                
                analysis["total_files"] += len(files)
                analysis["total_size_mb"] += total_size / (1024 * 1024)
        
        analysis["total_size_mb"] = round(analysis["total_size_mb"], 2)
        
        # Check last sync
        last_sync_file = self.automation_path / "logs" / "website_sync" / "last_sync.json"
        if last_sync_file.exists():
            with open(last_sync_file, 'r') as f:
                analysis["last_sync"] = json.load(f)
        
        self.logger.info(f"Sync scope: {analysis['total_files']} files, {analysis['total_size_mb']} MB")
        return analysis
    
    def sync_blog_posts(self, dry_run: bool = False) -> Dict:
        """Sync blog posts from automation to website."""
        self.logger.info("Syncing blog posts...")
        
        sync_result = {
            "synced_files": [],
            "skipped_files": [],
            "errors": [],
            "total_synced": 0
        }
        
        # Find blog posts in produced content
        produced_content_path = self.automation_path / "produced_content"
        blog_posts = []
        
        if produced_content_path.exists():
            blog_posts = list(produced_content_path.rglob("Blog_Post_*.md"))
        
        # Target directory
        posts_dir = self.website_path / "_posts"
        posts_dir.mkdir(exist_ok=True)
        
        for blog_post in blog_posts:
            try:
                # Transform to Jekyll format
                jekyll_content = self._transform_blog_post_to_jekyll(blog_post)
                
                # Generate Jekyll filename
                jekyll_filename = self._generate_jekyll_filename(blog_post)
                target_file = posts_dir / jekyll_filename
                
                # Check if should sync
                if self._should_sync_file(blog_post, target_file):
                    if not dry_run:
                        with open(target_file, 'w', encoding='utf-8') as f:
                            f.write(jekyll_content)
                    
                    sync_result["synced_files"].append(jekyll_filename)
                    sync_result["total_synced"] += 1
                    self.logger.info(f"Synced blog post: {jekyll_filename}")
                else:
                    sync_result["skipped_files"].append(jekyll_filename)
                    
            except Exception as e:
                error_msg = f"Error syncing {blog_post.name}: {str(e)}"
                sync_result["errors"].append(error_msg)
                self.logger.error(error_msg)
        
        return sync_result
    
    def sync_cheatsheets(self, dry_run: bool = False) -> Dict:
        """Sync cheatsheets from automation to website assets."""
        self.logger.info("Syncing cheatsheets...")
        
        sync_result = {
            "synced_files": [],
            "skipped_files": [],
            "errors": [],
            "total_synced": 0
        }
        
        # Source and target directories
        cheatsheets_source = self.automation_path / "cheatsheets"
        cheatsheets_target = self.website_path / "assets" / "cheatsheets"
        cheatsheets_target.mkdir(parents=True, exist_ok=True)
        
        if not cheatsheets_source.exists():
            return sync_result
        
        # Find cheatsheet files
        cheatsheet_files = list(cheatsheets_source.glob("*.html"))
        cheatsheet_files.extend(list(cheatsheets_source.glob("*.pdf")))
        cheatsheet_files.extend(list(cheatsheets_source.glob("*.png")))
        
        for cheatsheet in cheatsheet_files:
            try:
                target_file = cheatsheets_target / cheatsheet.name
                
                if self._should_sync_file(cheatsheet, target_file):
                    if not dry_run:
                        shutil.copy2(cheatsheet, target_file)
                    
                    sync_result["synced_files"].append(cheatsheet.name)
                    sync_result["total_synced"] += 1
                    self.logger.info(f"Synced cheatsheet: {cheatsheet.name}")
                else:
                    sync_result["skipped_files"].append(cheatsheet.name)
                    
            except Exception as e:
                error_msg = f"Error syncing {cheatsheet.name}: {str(e)}"
                sync_result["errors"].append(error_msg)
                self.logger.error(error_msg)
        
        # Update cheatsheet vault if enabled
        if self.sync_config["cheatsheet_settings"]["update_vault"]:
            self._update_cheatsheet_vault(dry_run)
        
        return sync_result
    
    def sync_resources(self, dry_run: bool = False) -> Dict:
        """Sync general resources from automation to website."""
        self.logger.info("Syncing resources...")
        
        sync_result = {
            "synced_files": [],
            "skipped_files": [],
            "errors": [],
            "total_synced": 0
        }
        
        # Source and target directories
        resources_source = self.automation_path / "output_for_website" / "resources"
        resources_target = self.website_path / "resources"
        
        if not resources_source.exists():
            return sync_result
        
        resources_target.mkdir(exist_ok=True)
        
        # Sync all resource files
        for resource_file in resources_source.rglob("*"):
            if resource_file.is_file():
                try:
                    # Maintain directory structure
                    relative_path = resource_file.relative_to(resources_source)
                    target_file = resources_target / relative_path
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    if self._should_sync_file(resource_file, target_file):
                        if not dry_run:
                            shutil.copy2(resource_file, target_file)
                        
                        sync_result["synced_files"].append(str(relative_path))
                        sync_result["total_synced"] += 1
                        self.logger.info(f"Synced resource: {relative_path}")
                    else:
                        sync_result["skipped_files"].append(str(relative_path))
                        
                except Exception as e:
                    error_msg = f"Error syncing {resource_file.name}: {str(e)}"
                    sync_result["errors"].append(error_msg)
                    self.logger.error(error_msg)
        
        return sync_result
    
    def _transform_blog_post_to_jekyll(self, blog_post_path: Path) -> str:
        """Transform automation blog post to Jekyll format."""
        with open(blog_post_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract topic from filename or content
        topic = self._extract_topic_from_blog(blog_post_path, content)
        
        # Generate Jekyll front matter
        front_matter = self._generate_jekyll_front_matter(topic, blog_post_path)
        
        # Clean content for Jekyll
        clean_content = self._clean_content_for_jekyll(content)
        
        # Combine front matter and content
        jekyll_content = f"---\n{yaml.dump(front_matter, default_flow_style=False)}---\n\n{clean_content}"
        
        return jekyll_content
    
    def _extract_topic_from_blog(self, blog_post_path: Path, content: str) -> str:
        """Extract topic from blog post."""
        # Try to extract from filename
        filename = blog_post_path.name
        if "Blog_Post_" in filename:
            topic = filename.replace("Blog_Post_", "").replace(".md", "").replace("_", " ")
            return topic.strip()
        
        # Try to extract from content title
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# ') and len(line) > 2:
                title = line[2:].strip()
                # Remove subtitle if present
                if ':' in title:
                    title = title.split(':')[0].strip()
                return title
        
        return "Coaching Insight"
    
    def _generate_jekyll_front_matter(self, topic: str, blog_post_path: Path) -> Dict:
        """Generate Jekyll front matter for blog post."""
        # Get creation date from file
        creation_time = datetime.datetime.fromtimestamp(blog_post_path.stat().st_ctime)
        
        front_matter = {
            "layout": self.sync_config["blog_post_settings"]["default_layout"],
            "title": topic,
            "date": creation_time.strftime('%Y-%m-%d %H:%M:%S %z') or creation_time.strftime('%Y-%m-%d'),
            "categories": [self.sync_config["blog_post_settings"]["default_category"]],
            "tags": ["coaching", "football", "development"],
            "author": "Kevin Middleton",
            "excerpt": f"Discover Kevin's systematic approach to {topic.lower()} and transform your coaching sessions.",
            "image": "/assets/images/kevin-middleton-coach.jpg",
            "published": not self.sync_config["blog_post_settings"]["require_review"]
        }
        
        return front_matter
    
    def _clean_content_for_jekyll(self, content: str) -> str:
        """Clean content for Jekyll compatibility."""
        # Remove metadata header if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].strip()
        
        # Fix image paths for Jekyll
        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'![\\1]({{ site.baseurl }}/assets/images/\\2)', content)
        
        # Fix internal links
        content = re.sub(r'\[([^\]]+)\]\(\.\.\/([^)]+)\)', r'[\\1]({{ site.baseurl }}/\\2)', content)
        
        # Ensure proper markdown formatting
        content = content.replace('\r\n', '\n')
        
        return content
    
    def _generate_jekyll_filename(self, blog_post_path: Path) -> str:
        """Generate Jekyll-compatible filename."""
        # Get date from file creation or current date
        try:
            creation_time = datetime.datetime.fromtimestamp(blog_post_path.stat().st_ctime)
        except:
            creation_time = datetime.datetime.now()
        
        date_str = creation_time.strftime('%Y-%m-%d')
        
        # Extract topic and clean for filename
        filename = blog_post_path.name
        if "Blog_Post_" in filename:
            topic = filename.replace("Blog_Post_", "").replace(".md", "")
        else:
            topic = filename.replace(".md", "")
        
        # Clean topic for URL
        clean_topic = re.sub(r'[^\w\s-]', '', topic).strip()
        clean_topic = re.sub(r'[-\s]+', '-', clean_topic).lower()
        
        return f"{date_str}-{clean_topic}.md"
    
    def _should_sync_file(self, source_file: Path, target_file: Path) -> bool:
        """Determine if file should be synced."""
        # Always sync if target doesn't exist
        if not target_file.exists():
            return True
        
        # Check modification times
        source_mtime = source_file.stat().st_mtime
        target_mtime = target_file.stat().st_mtime
        
        # Sync if source is newer
        return source_mtime > target_mtime
    
    def _update_cheatsheet_vault(self, dry_run: bool = False):
        """Update the cheatsheet vault page with new cheatsheets."""
        vault_file = self.website_path / "coaching-cheatsheet-vault.html"
        if not vault_file.exists():
            return
        
        # Get list of cheatsheets
        cheatsheets_dir = self.website_path / "assets" / "cheatsheets"
        if not cheatsheets_dir.exists():
            return
        
        cheatsheet_files = list(cheatsheets_dir.glob("*.html"))
        
        # Read current vault content
        with open(vault_file, 'r', encoding='utf-8') as f:
            vault_content = f.read()
        
        # Generate cheatsheet list HTML
        cheatsheet_html = self._generate_cheatsheet_list_html(cheatsheet_files)
        
        # Update vault content (this would need specific implementation based on vault structure)
        # For now, just log the update
        if not dry_run:
            self.logger.info(f"Would update cheatsheet vault with {len(cheatsheet_files)} cheatsheets")
    
    def _generate_cheatsheet_list_html(self, cheatsheet_files: List[Path]) -> str:
        """Generate HTML list of cheatsheets."""
        html_items = []
        
        for cheatsheet in cheatsheet_files:
            name = cheatsheet.stem.replace('_', ' ').title()
            relative_path = f"/assets/cheatsheets/{cheatsheet.name}"
            
            html_items.append(f"""
            <div class="cheatsheet-item">
                <h3>{name}</h3>
                <a href="{relative_path}" target="_blank" class="download-btn">Download</a>
            </div>
            """)
        
        return '\n'.join(html_items)
    
    def sync_all(self, dry_run: bool = False) -> Dict:
        """Sync all configured content types."""
        self.logger.info("Starting complete website sync...")
        
        sync_results = {
            "blog_posts": {},
            "cheatsheets": {},
            "resources": {},
            "errors": [],
            "summary": {
                "total_synced": 0,
                "total_errors": 0,
                "sync_time": datetime.datetime.now().isoformat()
            }
        }
        
        # Backup website if enabled
        if self.sync_config["safety_settings"]["backup_before_sync"] and not dry_run:
            self._create_sync_backup()
        
        # Sync each content type
        sync_operations = {
            "blog_posts": self.sync_blog_posts,
            "cheatsheets": self.sync_cheatsheets,
            "resources": self.sync_resources
        }
        
        for content_type, sync_func in sync_operations.items():
            if content_type in self.sync_config["sync_items"]:
                try:
                    result = sync_func(dry_run)
                    sync_results[content_type] = result
                    sync_results["summary"]["total_synced"] += result["total_synced"]
                    sync_results["summary"]["total_errors"] += len(result["errors"])
                    
                except Exception as e:
                    error_msg = f"Error syncing {content_type}: {str(e)}"
                    sync_results["errors"].append(error_msg)
                    self.logger.error(error_msg)
        
        # Save sync record
        if not dry_run:
            self._save_sync_record(sync_results)
        
        # Verify sync if enabled
        if self.sync_config["safety_settings"]["verify_after_sync"] and not dry_run:
            self._verify_sync_integrity()
        
        self.logger.info(f"Sync completed: {sync_results['summary']['total_synced']} files synced")
        return sync_results
    
    def _create_sync_backup(self):
        """Create backup before sync."""
        backup_dir = self.website_path.parent / f"website_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Backup critical directories
        backup_items = ["_posts", "assets/cheatsheets", "resources"]
        backup_dir.mkdir(exist_ok=True)
        
        for item in backup_items:
            source_path = self.website_path / item
            if source_path.exists():
                target_path = backup_dir / item
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                if source_path.is_dir():
                    shutil.copytree(source_path, target_path, ignore_dangling_symlinks=True)
                else:
                    shutil.copy2(source_path, target_path)
        
        self.logger.info(f"Sync backup created: {backup_dir}")
    
    def _save_sync_record(self, sync_results: Dict):
        """Save sync record for tracking."""
        sync_record = {
            "sync_time": datetime.datetime.now().isoformat(),
            "automation_repo": str(self.automation_path),
            "website_repo": str(self.website_path),
            "results": sync_results
        }
        
        # Save last sync record
        last_sync_file = self.automation_path / "logs" / "website_sync" / "last_sync.json"
        with open(last_sync_file, 'w') as f:
            json.dump(sync_record, f, indent=2)
        
        # Save detailed sync log
        sync_log_file = self.automation_path / "logs" / "website_sync" / f"sync_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(sync_log_file, 'w') as f:
            json.dump(sync_record, f, indent=2)
    
    def _verify_sync_integrity(self):
        """Verify sync integrity."""
        self.logger.info("Verifying sync integrity...")
        
        # Check critical files exist
        critical_files = [
            self.website_path / "_posts",
            self.website_path / "assets" / "cheatsheets"
        ]
        
        for critical_file in critical_files:
            if not critical_file.exists():
                self.logger.warning(f"Critical file missing after sync: {critical_file}")
    
    def setup_sync_automation(self):
        """Setup automated sync schedule."""
        print("Setting up website sync automation...")
        
        # Create sync automation script
        sync_script_content = f"""#!/usr/bin/env python3
# Automated Website Sync Script
# Generated: {datetime.datetime.now().isoformat()}

import sys
from pathlib import Path

# Add automation repo to path
sys.path.append(str(Path(__file__).parent))

from website_sync import WebsiteSyncManager

def main():
    automation_repo = "{self.automation_path}"
    website_repo = "{self.website_path}"
    
    sync_manager = WebsiteSyncManager(automation_repo, website_repo)
    
    # Run sync
    results = sync_manager.sync_all()
    
    print(f"Sync completed: {{results['summary']['total_synced']}} files synced")
    
    if results['summary']['total_errors'] > 0:
        print(f"Errors: {{results['summary']['total_errors']}}")
        sys.exit(1)

if __name__ == "__main__":
    main()
"""
        
        # Save sync automation script
        sync_script_path = self.automation_path / "automation_scripts" / "daily_website_sync.py"
        with open(sync_script_path, 'w') as f:
            f.write(sync_script_content)
        
        # Make executable (on Unix systems)
        if os.name != 'nt':
            os.chmod(sync_script_path, 0o755)
        
        print(f"✅ Sync automation script created: {sync_script_path}")
        print("📋 To schedule daily sync:")
        print(f"   Add to crontab: 0 8 * * * python {sync_script_path}")


def main():
    """Main entry point for website sync."""
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python website_sync.py <automation_repo_path> <website_repo_path> [command]")
        print("Commands:")
        print("  analyze    - Analyze sync scope")
        print("  sync-all   - Sync all content (default)")
        print("  sync-blogs - Sync blog posts only")
        print("  sync-cheatsheets - Sync cheatsheets only")
        print("  dry-run    - Show what would be synced")
        print("  setup      - Setup sync automation")
        return
    
    automation_path = sys.argv[1]
    website_path = sys.argv[2]
    command = sys.argv[3] if len(sys.argv) > 3 else "sync-all"
    
    # Validate paths
    if not Path(automation_path).exists():
        print(f"❌ Automation repository not found: {automation_path}")
        return
    
    if not Path(website_path).exists():
        print(f"❌ Website repository not found: {website_path}")
        return
    
    # Initialize sync manager
    sync_manager = WebsiteSyncManager(automation_path, website_path)
    
    # Execute command
    if command == "analyze":
        analysis = sync_manager.analyze_sync_scope()
        print("\n📊 Sync Scope Analysis")
        print("=" * 30)
        for content_type, data in analysis["available_content"].items():
            print(f"{content_type}: {data['file_count']} files ({data['size_mb']} MB)")
        print(f"\nTotal: {analysis['total_files']} files ({analysis['total_size_mb']} MB)")
        
    elif command == "sync-all":
        print("🔄 Syncing all content...")
        results = sync_manager.sync_all()
        print(f"✅ Sync completed: {results['summary']['total_synced']} files synced")
        
    elif command == "sync-blogs":
        print("📝 Syncing blog posts...")
        results = sync_manager.sync_blog_posts()
        print(f"✅ Blog sync completed: {results['total_synced']} files synced")
        
    elif command == "sync-cheatsheets":
        print("📄 Syncing cheatsheets...")
        results = sync_manager.sync_cheatsheets()
        print(f"✅ Cheatsheet sync completed: {results['total_synced']} files synced")
        
    elif command == "dry-run":
        print("🔍 Running dry-run sync...")
        results = sync_manager.sync_all(dry_run=True)
        print("📋 Would sync:")
        for content_type, data in results.items():
            if isinstance(data, dict) and "synced_files" in data:
                print(f"  {content_type}: {len(data['synced_files'])} files")
        
    elif command == "setup":
        sync_manager.setup_sync_automation()
        
    else:
        print(f"❌ Unknown command: {command}")


if __name__ == "__main__":
    main()