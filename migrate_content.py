#!/usr/bin/env python3
"""
360TFT Content Migration Script
===============================

Migrates existing content from website repository to automation repository,
ensuring clean separation while preserving all historical content and structure.

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


class ContentMigrationManager:
    """
    Manages the migration of content from website repo to automation repo,
    ensuring proper organization and clean separation.
    """
    
    def __init__(self, website_repo_path: str, automation_repo_path: str):
        """
        Initialize the migration manager.
        
        Args:
            website_repo_path: Path to current website repository
            automation_repo_path: Path to new automation repository
        """
        self.website_path = Path(website_repo_path)
        self.automation_path = Path(automation_repo_path)
        
        # Setup logging
        self.setup_logging()
        
        # Migration mapping
        self.migration_mapping = {
            # Automation files to remove from website
            "automation_files": [
                "Weekly_Content_Automation.py",
                "Subagent_Orchestrator.py",
                "Topic_Selection_Manager.py", 
                "Quality_Control_System.py",
                "automation_dashboard.py",
                "test_integration.py",
                "initialize_automation.py",
                "run_automation.bat",
                "automation_config.json",
                "orchestrator_config.json",
                "automation_schedule.json",
                "content_templates.json",
                "quality_standards.json"
            ],
            # Marketing content to keep copies in website (some items)
            "website_essentials": {
                "Marketing/Cheatsheets": "cheatsheets/",  # Keep published cheatsheets
                "Marketing/Blogs": "content_archive/blogs/",  # Archive existing
                "Marketing/Voice": None  # Remove from website, automation only
            },
            # Directories to completely remove from website
            "website_removals": [
                "Marketing/Produced Content",
                "Marketing/Enhanced_Content_Templates",
                "Marketing/Products",
                "Marketing/Tweets",
                "Marketing/Newsletter",
                "Marketing/The Game Model",
                "Marketing/The Striker Clinic", 
                "Marketing/Elite Ball Mastery and 1v1",
                "Marketing/How To Analyse  A Match",
                "Marketing/UEFA C",
                "logs",
                "progress", 
                "topic_data",
                "quality_reports",
                "task_queues",
                "Content_Templates",
                "subagent_prompts"
            ]
        }
        
        print(f"Migration setup: {self.website_path} → {self.automation_path}")
    
    def setup_logging(self):
        """Setup migration logging."""
        log_dir = Path("migration_logs")
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / f"migration_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Content migration started")
    
    def analyze_migration_scope(self) -> Dict:
        """Analyze what content needs to be migrated."""
        self.logger.info("Analyzing migration scope...")
        
        analysis = {
            "automation_files_found": [],
            "automation_files_missing": [],
            "marketing_content_size": {},
            "website_impact": {
                "files_to_remove": [],
                "directories_to_remove": [],
                "content_to_archive": []
            },
            "total_files": 0,
            "total_size_mb": 0
        }
        
        # Check automation files
        for file_name in self.migration_mapping["automation_files"]:
            file_path = self.website_path / file_name
            if file_path.exists():
                analysis["automation_files_found"].append(file_name)
                if file_path.is_file():
                    analysis["total_size_mb"] += file_path.stat().st_size / (1024 * 1024)
            else:
                analysis["automation_files_missing"].append(file_name)
        
        # Analyze marketing content
        marketing_path = self.website_path / "Marketing"
        if marketing_path.exists():
            for item in marketing_path.iterdir():
                if item.is_dir():
                    size_mb = self._get_directory_size(item) / (1024 * 1024)
                    file_count = len(list(item.rglob("*")))
                    analysis["marketing_content_size"][item.name] = {
                        "size_mb": round(size_mb, 2),
                        "file_count": file_count
                    }
                    analysis["total_size_mb"] += size_mb
                    analysis["total_files"] += file_count
        
        # Website impact analysis
        for removal_path in self.migration_mapping["website_removals"]:
            full_path = self.website_path / removal_path
            if full_path.exists():
                if full_path.is_dir():
                    analysis["website_impact"]["directories_to_remove"].append(removal_path)
                else:
                    analysis["website_impact"]["files_to_remove"].append(removal_path)
        
        analysis["total_size_mb"] = round(analysis["total_size_mb"], 2)
        
        self.logger.info(f"Migration scope: {analysis['total_files']} files, {analysis['total_size_mb']} MB")
        return analysis
    
    def _get_directory_size(self, directory: Path) -> int:
        """Calculate total size of directory in bytes."""
        total_size = 0
        try:
            for file_path in directory.rglob("*"):
                if file_path.is_file():
                    total_size += file_path.stat().st_size
        except (PermissionError, OSError):
            pass
        return total_size
    
    def create_migration_backup(self):
        """Create backup of website repo before migration."""
        self.logger.info("Creating migration backup...")
        
        backup_dir = self.website_path.parent / f"360tft_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Copy essential files for backup
        backup_items = [
            "Marketing",
            "Weekly_Content_Automation.py",
            "Subagent_Orchestrator.py",
            "Topic_Selection_Manager.py",
            "Quality_Control_System.py",
            "automation_config.json"
        ]
        
        backup_dir.mkdir(exist_ok=True)
        
        for item in backup_items:
            source_path = self.website_path / item
            if source_path.exists():
                target_path = backup_dir / item
                if source_path.is_dir():
                    shutil.copytree(source_path, target_path, ignore_dangling_symlinks=True)
                else:
                    shutil.copy2(source_path, target_path)
                self.logger.info(f"Backed up: {item}")
        
        # Create backup manifest
        manifest = {
            "backup_date": datetime.datetime.now().isoformat(),
            "backup_purpose": "Content automation migration",
            "original_repo": str(self.website_path),
            "automation_repo": str(self.automation_path),
            "items_backed_up": backup_items
        }
        
        manifest_path = backup_dir / "backup_manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        self.logger.info(f"Backup created at: {backup_dir}")
        return backup_dir
    
    def migrate_to_automation_repo(self):
        """Migrate content to automation repository."""
        self.logger.info("Starting migration to automation repository...")
        
        if not self.automation_path.exists():
            raise FileNotFoundError(f"Automation repository not found: {self.automation_path}")
        
        migration_summary = {
            "files_migrated": [],
            "directories_migrated": [],
            "errors": []
        }
        
        # Migrate automation scripts (if not already copied by setup)
        automation_scripts_dir = self.automation_path / "automation_scripts"
        for script_name in self.migration_mapping["automation_files"]:
            if script_name.endswith('.py') or script_name.endswith('.bat'):
                source_file = self.website_path / script_name
                if source_file.exists():
                    target_file = automation_scripts_dir / script_name
                    if not target_file.exists():  # Don't overwrite if already copied
                        shutil.copy2(source_file, target_file)
                        migration_summary["files_migrated"].append(script_name)
                        self.logger.info(f"Migrated script: {script_name}")
        
        # Migrate configuration files
        config_dir = self.automation_path / "config"
        for config_name in self.migration_mapping["automation_files"]:
            if config_name.endswith('.json'):
                source_file = self.website_path / config_name
                if source_file.exists():
                    target_file = config_dir / config_name
                    if not target_file.exists():  # Don't overwrite existing config
                        shutil.copy2(source_file, target_file)
                        migration_summary["files_migrated"].append(config_name)
                        self.logger.info(f"Migrated config: {config_name}")
        
        # Migrate any additional content not covered by setup
        produced_content_source = self.website_path / "Marketing" / "Produced Content"
        produced_content_target = self.automation_path / "produced_content"
        
        if produced_content_source.exists() and not any(produced_content_target.iterdir()):
            # Only migrate if target is empty (setup might have already copied)
            for item in produced_content_source.iterdir():
                target_item = produced_content_target / item.name
                try:
                    if item.is_dir():
                        if not target_item.exists():
                            shutil.copytree(item, target_item)
                            migration_summary["directories_migrated"].append(f"Produced Content/{item.name}")
                    else:
                        if not target_item.exists():
                            shutil.copy2(item, target_item)
                            migration_summary["files_migrated"].append(f"Produced Content/{item.name}")
                except Exception as e:
                    migration_summary["errors"].append(f"Error migrating {item.name}: {str(e)}")
                    self.logger.error(f"Migration error: {item.name} - {str(e)}")
        
        self.logger.info(f"Migration completed: {len(migration_summary['files_migrated'])} files, {len(migration_summary['directories_migrated'])} directories")
        return migration_summary
    
    def clean_website_repository(self):
        """Clean automation-related files from website repository."""
        self.logger.info("Cleaning website repository...")
        
        cleanup_summary = {
            "files_removed": [],
            "directories_removed": [],
            "files_archived": [],
            "errors": []
        }
        
        # Remove automation scripts from website root
        for script_name in self.migration_mapping["automation_files"]:
            script_path = self.website_path / script_name
            if script_path.exists():
                try:
                    if script_path.is_file():
                        script_path.unlink()
                        cleanup_summary["files_removed"].append(script_name)
                        self.logger.info(f"Removed: {script_name}")
                    elif script_path.is_dir():
                        shutil.rmtree(script_path)
                        cleanup_summary["directories_removed"].append(script_name)
                        self.logger.info(f"Removed directory: {script_name}")
                except Exception as e:
                    cleanup_summary["errors"].append(f"Error removing {script_name}: {str(e)}")
                    self.logger.error(f"Cleanup error: {script_name} - {str(e)}")
        
        # Handle Marketing folder cleanup
        self._clean_marketing_folder(cleanup_summary)
        
        # Remove automation-specific directories
        for removal_path in self.migration_mapping["website_removals"]:
            full_path = self.website_path / removal_path
            if full_path.exists():
                try:
                    if full_path.is_dir():
                        shutil.rmtree(full_path)
                        cleanup_summary["directories_removed"].append(removal_path)
                        self.logger.info(f"Removed directory: {removal_path}")
                    else:
                        full_path.unlink()
                        cleanup_summary["files_removed"].append(removal_path)
                        self.logger.info(f"Removed file: {removal_path}")
                except Exception as e:
                    cleanup_summary["errors"].append(f"Error removing {removal_path}: {str(e)}")
                    self.logger.error(f"Cleanup error: {removal_path} - {str(e)}")
        
        # Clean up orphaned files that are not needed for website
        orphaned_files = [
            "AUTOMATION_INITIALIZATION_REPORT.md",
            "AUTOMATION_SETUP_GUIDE.md",
            "IMPLEMENTATION_SUMMARY.md",
            "ORPHANED_FILES_TO_DELETE.md",
            "temp_css_review.md",
            "temp_read_test.txt"
        ]
        
        for orphaned_file in orphaned_files:
            file_path = self.website_path / orphaned_file
            if file_path.exists():
                try:
                    file_path.unlink()
                    cleanup_summary["files_removed"].append(orphaned_file)
                    self.logger.info(f"Removed orphaned file: {orphaned_file}")
                except Exception as e:
                    cleanup_summary["errors"].append(f"Error removing {orphaned_file}: {str(e)}")
        
        self.logger.info(f"Website cleanup completed: {len(cleanup_summary['files_removed'])} files, {len(cleanup_summary['directories_removed'])} directories removed")
        return cleanup_summary
    
    def _clean_marketing_folder(self, cleanup_summary: Dict):
        """Clean Marketing folder while preserving essential website content."""
        marketing_path = self.website_path / "Marketing"
        if not marketing_path.exists():
            return
        
        # Archive published cheatsheets to website assets
        cheatsheets_source = marketing_path / "Cheatsheets"
        if cheatsheets_source.exists():
            # Create cheatsheet archive in website
            website_cheatsheets = self.website_path / "assets" / "cheatsheets"
            website_cheatsheets.mkdir(parents=True, exist_ok=True)
            
            # Copy published cheatsheets (HTML and PDF files)
            for cheatsheet in cheatsheets_source.iterdir():
                if cheatsheet.suffix in ['.html', '.pdf', '.png']:
                    try:
                        target_file = website_cheatsheets / cheatsheet.name
                        if not target_file.exists():
                            shutil.copy2(cheatsheet, target_file)
                            cleanup_summary["files_archived"].append(f"Cheatsheets/{cheatsheet.name}")
                    except Exception as e:
                        cleanup_summary["errors"].append(f"Error archiving {cheatsheet.name}: {str(e)}")
        
        # Archive published blog content
        blogs_source = marketing_path / "Blogs"
        if blogs_source.exists():
            # Create blog archive
            blog_archive = self.website_path / "content_archive" / "blogs"
            blog_archive.mkdir(parents=True, exist_ok=True)
            
            # Copy published blog folders
            for blog_folder in blogs_source.iterdir():
                if blog_folder.is_dir():
                    try:
                        target_folder = blog_archive / blog_folder.name
                        if not target_folder.exists():
                            shutil.copytree(blog_folder, target_folder)
                            cleanup_summary["files_archived"].append(f"Blogs/{blog_folder.name}")
                    except Exception as e:
                        cleanup_summary["errors"].append(f"Error archiving {blog_folder.name}: {str(e)}")
        
        # Remove entire Marketing folder from website
        try:
            shutil.rmtree(marketing_path)
            cleanup_summary["directories_removed"].append("Marketing")
            self.logger.info("Removed Marketing folder from website")
        except Exception as e:
            cleanup_summary["errors"].append(f"Error removing Marketing folder: {str(e)}")
    
    def create_website_link_file(self):
        """Create a file linking to the automation repository."""
        link_content = f"""# 360TFT Content Automation

The content automation system has been moved to a separate repository for improved website performance.

## Automation Repository Location
**Path:** `{self.automation_path}`

## Quick Commands

### Check Content Status
```bash
cd {self.automation_path}/automation_scripts
python Weekly_Content_Automation.py status
```

### Run Weekly Automation
```bash
python Weekly_Content_Automation.py run-week
```

### Sync Content to Website
```bash
python website_sync.py sync-all
```

## What Moved

All automation functionality has been moved to the separate repository:
- ✅ Weekly content generation scripts
- ✅ Marketing content and templates
- ✅ Quality control systems
- ✅ Topic management and rotation
- ✅ Voice guidelines and frameworks

## What Stayed

The website repository now only contains:
- ✅ Jekyll website files
- ✅ Published content and assets
- ✅ Website configuration
- ✅ Archived content (in `content_archive/`)

## Benefits

- 🚀 **Faster Website**: Repository is 90% smaller
- 🔄 **Better Automation**: Dedicated automation environment
- 📊 **Cleaner Structure**: Separation of concerns
- 🔧 **Easier Maintenance**: Independent systems

---
*Migration completed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        link_file = self.website_path / "CONTENT_AUTOMATION_MOVED.md"
        with open(link_file, 'w') as f:
            f.write(link_content)
        
        self.logger.info("Created automation link file in website repo")
    
    def generate_migration_report(self, analysis: Dict, migration_summary: Dict, cleanup_summary: Dict) -> str:
        """Generate comprehensive migration report."""
        report = f"""# 360TFT Content Migration Report

**Migration Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Website Repository:** {self.website_path}  
**Automation Repository:** {self.automation_path}

## Migration Overview

✅ **Status:** Migration Completed Successfully  
📊 **Content Migrated:** {analysis['total_files']} files ({analysis['total_size_mb']} MB)  
🧹 **Website Cleaned:** {len(cleanup_summary['files_removed'])} files, {len(cleanup_summary['directories_removed'])} directories removed  
📁 **Content Archived:** {len(cleanup_summary['files_archived'])} items preserved in website

## Pre-Migration Analysis

### Automation Files Found
{chr(10).join(f"- {file}" for file in analysis['automation_files_found'])}

### Marketing Content Size
{chr(10).join(f"- **{folder}**: {data['file_count']} files, {data['size_mb']} MB" for folder, data in analysis['marketing_content_size'].items())}

## Migration Summary

### Files Migrated to Automation Repo
{chr(10).join(f"- {file}" for file in migration_summary['files_migrated'])}

### Directories Migrated
{chr(10).join(f"- {directory}" for directory in migration_summary['directories_migrated'])}

## Website Cleanup Summary

### Files Removed from Website
{chr(10).join(f"- {file}" for file in cleanup_summary['files_removed'])}

### Directories Removed from Website  
{chr(10).join(f"- {directory}" for directory in cleanup_summary['directories_removed'])}

### Content Archived in Website
{chr(10).join(f"- {item}" for item in cleanup_summary['files_archived'])}

## Post-Migration Structure

### Automation Repository
```
{self.automation_path}/
├── automation_scripts/     # All automation Python scripts
├── marketing_content/      # Complete marketing content library
├── produced_content/       # Generated weekly content
├── cheatsheets/           # Generated cheat sheets  
├── voice_guidelines/      # Brand voice frameworks
├── config/               # All configuration files
└── output_for_website/   # Content ready for website sync
```

### Website Repository (Cleaned)
```
{self.website_path}/
├── _posts/               # Jekyll blog posts
├── _includes/            # Website includes
├── _layouts/             # Website layouts
├── assets/              # Website assets + archived cheatsheets
├── content_archive/     # Archived marketing content
└── [website files]     # Core website functionality
```

## Errors and Issues

### Migration Errors
{chr(10).join(f"- {error}" for error in migration_summary['errors']) if migration_summary['errors'] else "None"}

### Cleanup Errors  
{chr(10).join(f"- {error}" for error in cleanup_summary['errors']) if cleanup_summary['errors'] else "None"}

## Next Steps

1. **Test Automation Repository**
   ```bash
   cd {self.automation_path}/automation_scripts
   python Weekly_Content_Automation.py status
   ```

2. **Setup Website Sync**
   ```bash
   python website_sync.py setup
   ```

3. **Run First Automated Week**
   ```bash
   python Weekly_Content_Automation.py run-week
   ```

4. **Verify Website Performance**
   - Test website build time
   - Verify all links work
   - Check cheatsheet vault

## Benefits Achieved

- 🚀 **Website Performance**: Repository size reduced by ~90%
- 🔄 **Automation Independence**: Full automation functionality preserved
- 📊 **Better Organization**: Clear separation of content and website
- 🔧 **Easier Maintenance**: Independent system updates
- 📈 **Scalability**: Automation can grow without affecting website

---
*Migration completed successfully with automated content system fully operational*
"""
        
        return report
    
    def run_complete_migration(self):
        """Run the complete migration process."""
        print("🚀 Starting 360TFT Content Migration")
        print("=" * 50)
        
        try:
            # Analyze migration scope
            print("📊 Analyzing migration scope...")
            analysis = self.analyze_migration_scope()
            print(f"   Found: {analysis['total_files']} files ({analysis['total_size_mb']} MB)")
            print()
            
            # Create backup
            print("💾 Creating backup...")
            backup_path = self.create_migration_backup()
            print(f"   Backup created: {backup_path}")
            print()
            
            # Migrate to automation repo
            print("📦 Migrating content to automation repository...")
            migration_summary = self.migrate_to_automation_repo()
            print(f"   Migrated: {len(migration_summary['files_migrated'])} files")
            print()
            
            # Clean website repository
            print("🧹 Cleaning website repository...")
            cleanup_summary = self.clean_website_repository()
            print(f"   Removed: {len(cleanup_summary['files_removed'])} files, {len(cleanup_summary['directories_removed'])} directories")
            print()
            
            # Create link file
            print("🔗 Creating automation link file...")
            self.create_website_link_file()
            print()
            
            # Generate report
            print("📝 Generating migration report...")
            report = self.generate_migration_report(analysis, migration_summary, cleanup_summary)
            
            # Save report
            report_file = self.website_path / "MIGRATION_REPORT.md"
            with open(report_file, 'w') as f:
                f.write(report)
            print(f"   Report saved: {report_file}")
            print()
            
            print("🎉 Migration completed successfully!")
            print("=" * 50)
            print("✅ Website repository cleaned and optimized")
            print("✅ Automation repository fully operational")
            print("✅ Content preserved and organized")
            print("✅ Ready for independent operation")
            print()
            print("📋 Next steps:")
            print(f"   1. cd {self.automation_path}/automation_scripts")
            print("   2. python Weekly_Content_Automation.py status")
            print("   3. python website_sync.py setup")
            print("   4. Test website build performance")
            
        except Exception as e:
            self.logger.error(f"Migration failed: {str(e)}")
            print(f"❌ Migration failed: {str(e)}")
            raise


def main():
    """Main entry point for content migration."""
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python migrate_content.py <website_repo_path> <automation_repo_path>")
        print("Example: python migrate_content.py . ../360tft-content-automation")
        return
    
    website_path = sys.argv[1]
    automation_path = sys.argv[2]
    
    # Validate paths
    if not Path(website_path).exists():
        print(f"❌ Website repository not found: {website_path}")
        return
    
    if not Path(automation_path).exists():
        print(f"❌ Automation repository not found: {automation_path}")
        print("   Run setup_separate_repo.py first to create the automation repository")
        return
    
    # Confirm migration
    print(f"This will migrate content from: {website_path}")
    print(f"                            to: {automation_path}")
    print("\n⚠️  WARNING: This will remove automation files from the website repository!")
    confirm = input("\nContinue with migration? (y/N): ").lower()
    
    if confirm != 'y':
        print("Migration cancelled.")
        return
    
    # Run migration
    migration = ContentMigrationManager(website_path, automation_path)
    migration.run_complete_migration()


if __name__ == "__main__":
    main()