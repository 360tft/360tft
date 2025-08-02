#!/usr/bin/env python3
"""
360TFT Content Automation Repository Setup
==========================================

Creates an independent content automation repository structure separate from the website.
This allows the website to stay lightweight while maintaining full automation functionality.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import datetime


class ContentAutomationRepoSetup:
    """
    Sets up a separate repository structure for content automation,
    independent of the website repository.
    """
    
    def __init__(self, target_repo_path: str):
        """
        Initialize the repository setup system.
        
        Args:
            target_repo_path: Path where the new automation repo should be created
        """
        self.target_path = Path(target_repo_path)
        self.source_path = Path(__file__).parent  # Current 360tft directory
        
        # Define the new repository structure
        self.repo_structure = {
            "automation_scripts": [
                "Weekly_Content_Automation.py",
                "Subagent_Orchestrator.py", 
                "Topic_Selection_Manager.py",
                "Quality_Control_System.py",
                "automation_dashboard.py",
                "test_integration.py"
            ],
            "marketing_content": {
                "Blogs": "source",
                "Emails": "source", 
                "Cheatsheets": "source",
                "Enhanced_Content_Templates": "source",
                "Produced Content": "source",
                "Voice": "source",
                "The Game Model": "source",
                "The Striker Clinic": "source",
                "Elite Ball Mastery and 1v1": "source",
                "How To Analyse  A Match": "source",
                "UEFA C": "source",
                "Products": "source",
                "Tweets": "source",
                "Newsletter": "source"
            },
            "config": [
                "automation_config.json",
                "orchestrator_config.json", 
                "automation_schedule.json",
                "content_templates.json",
                "quality_standards.json"
            ],
            "voice_guidelines": [
                "Subagent_Prompt_Templates.md",
                "Content_Analysis_and_Process_Improvements.md",
                "Content_Creation_Framework_Value_Equation.md",
                "Value_Equation_Analysis_Small_Sided_Games.md",
                "Value_Equation_Quick_Reference.md"
            ],
            "output_for_website": {},
            "logs": {},
            "progress": {},
            "topic_data": {},
            "quality_reports": {},
            "task_queues": {},
            "Content_Templates": {},
            "subagent_prompts": {}
        }
        
        print(f"Setting up automation repository at: {self.target_path}")
    
    def create_repository_structure(self):
        """Create the complete directory structure for the automation repo."""
        print("Creating repository directory structure...")
        
        # Create main directories
        main_dirs = [
            "automation_scripts",
            "marketing_content", 
            "produced_content",
            "cheatsheets",
            "voice_guidelines",
            "config",
            "output_for_website",
            "logs",
            "progress", 
            "topic_data",
            "quality_reports",
            "task_queues",
            "Content_Templates",
            "subagent_prompts"
        ]
        
        for directory in main_dirs:
            dir_path = self.target_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created: {directory}/")
        
        # Create output subdirectories
        output_subdirs = [
            "output_for_website/blog_posts",
            "output_for_website/cheatsheets", 
            "output_for_website/resources",
            "output_for_website/academy_content"
        ]
        
        for subdir in output_subdirs:
            subdir_path = self.target_path / subdir
            subdir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created: {subdir}/")
        
        print("✅ Repository structure created successfully")
    
    def copy_automation_scripts(self):
        """Copy all automation Python scripts to the new repository."""
        print("Copying automation scripts...")
        
        scripts_to_copy = [
            "Weekly_Content_Automation.py",
            "Subagent_Orchestrator.py",
            "Topic_Selection_Manager.py", 
            "Quality_Control_System.py",
            "automation_dashboard.py",
            "test_integration.py",
            "initialize_automation.py"
        ]
        
        automation_dir = self.target_path / "automation_scripts"
        
        for script in scripts_to_copy:
            source_file = self.source_path / script
            if source_file.exists():
                target_file = automation_dir / script
                shutil.copy2(source_file, target_file)
                print(f"Copied: {script}")
            else:
                print(f"⚠️  Not found: {script}")
        
        # Copy batch files
        batch_files = ["run_automation.bat"]
        for batch_file in batch_files:
            source_file = self.source_path / batch_file
            if source_file.exists():
                target_file = automation_dir / batch_file
                shutil.copy2(source_file, target_file)
                print(f"Copied: {batch_file}")
        
        print("✅ Automation scripts copied successfully")
    
    def copy_marketing_content(self):
        """Copy all marketing content to the new repository."""
        print("Copying marketing content...")
        
        marketing_source = self.source_path / "Marketing"
        marketing_target = self.target_path / "marketing_content"
        
        if marketing_source.exists():
            # Copy entire Marketing folder structure
            for item in marketing_source.iterdir():
                if item.is_dir():
                    target_dir = marketing_target / item.name
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.copytree(item, target_dir)
                    print(f"Copied: Marketing/{item.name}/")
                elif item.is_file():
                    target_file = marketing_target / item.name
                    shutil.copy2(item, target_file)
                    print(f"Copied: Marketing/{item.name}")
        
        print("✅ Marketing content copied successfully")
    
    def copy_configuration_files(self):
        """Copy all configuration files to the new repository."""
        print("Copying configuration files...")
        
        config_files = [
            "automation_config.json",
            "orchestrator_config.json",
            "automation_schedule.json", 
            "content_templates.json",
            "quality_standards.json"
        ]
        
        config_dir = self.target_path / "config"
        
        for config_file in config_files:
            source_file = self.source_path / config_file
            if source_file.exists():
                target_file = config_dir / config_file
                shutil.copy2(source_file, target_file)
                print(f"Copied: {config_file}")
            else:
                # Create default config if not exists
                self._create_default_config(config_dir / config_file, config_file)
                print(f"Created default: {config_file}")
        
        # Copy requirements.txt
        req_source = self.source_path / "requirements.txt"
        req_target = self.target_path / "requirements.txt"
        if req_source.exists():
            shutil.copy2(req_source, req_target)
            print("Copied: requirements.txt")
        
        print("✅ Configuration files copied successfully")
    
    def copy_voice_guidelines(self):
        """Copy voice guidelines and content framework files."""
        print("Copying voice guidelines...")
        
        voice_files = [
            "Marketing/Subagent_Prompt_Templates.md",
            "Marketing/Content_Analysis_and_Process_Improvements.md", 
            "Marketing/Content_Creation_Framework_Value_Equation.md",
            "Marketing/Value_Equation_Analysis_Small_Sided_Games.md",
            "Marketing/Value_Equation_Quick_Reference.md"
        ]
        
        voice_dir = self.target_path / "voice_guidelines"
        
        for voice_file in voice_files:
            source_file = self.source_path / voice_file
            if source_file.exists():
                target_file = voice_dir / Path(voice_file).name
                shutil.copy2(source_file, target_file)
                print(f"Copied: {Path(voice_file).name}")
        
        # Copy Voice folder
        voice_source = self.source_path / "Marketing" / "Voice"
        if voice_source.exists():
            voice_target = voice_dir / "Voice"
            if voice_target.exists():
                shutil.rmtree(voice_target)
            shutil.copytree(voice_source, voice_target)
            print("Copied: Voice/ folder")
        
        print("✅ Voice guidelines copied successfully")
    
    def create_git_repository(self):
        """Initialize git repository with appropriate .gitignore."""
        print("Setting up git repository...")
        
        # Create .gitignore
        gitignore_content = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt

# Logs
logs/
*.log

# Progress and temporary files
progress/
topic_data/
quality_reports/
task_queues/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Sensitive data
*.key
*.secret
api_keys.json

# Large output files
output_for_website/archives/
marketing_content/Produced Content/archives/
"""
        
        gitignore_path = self.target_path / ".gitignore"
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)
        print("Created: .gitignore")
        
        # Create README
        readme_content = self._create_readme_content()
        readme_path = self.target_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print("Created: README.md")
        
        print("✅ Git repository files created successfully")
    
    def update_automation_paths(self):
        """Update file paths in automation scripts to work with new structure."""
        print("Updating automation script paths...")
        
        # Files that need path updates
        scripts_to_update = [
            "automation_scripts/Weekly_Content_Automation.py",
            "automation_scripts/Subagent_Orchestrator.py",
            "automation_scripts/Topic_Selection_Manager.py",
            "automation_scripts/Quality_Control_System.py"
        ]
        
        for script_path in scripts_to_update:
            full_path = self.target_path / script_path
            if full_path.exists():
                self._update_script_paths(full_path)
                print(f"Updated paths in: {script_path}")
        
        print("✅ Automation paths updated successfully")
    
    def _update_script_paths(self, script_path: Path):
        """Update paths in a specific script file."""
        with open(script_path, 'r') as f:
            content = f.read()
        
        # Path mappings for the new structure
        path_updates = {
            'self.marketing_path = self.base_path / "Marketing"': 
                'self.marketing_path = self.base_path / "marketing_content"',
            'self.produced_content_path = self.marketing_path / "Produced Content"':
                'self.produced_content_path = self.base_path / "produced_content"',
            'self.cheatsheets_path = self.marketing_path / "Cheatsheets"':
                'self.cheatsheets_path = self.base_path / "cheatsheets"',
            'self.voice_path = self.marketing_path / "Voice"':
                'self.voice_path = self.base_path / "voice_guidelines" / "Voice"',
            'marketing_path / "Marketing"':
                'base_path / "marketing_content"',
            '"Marketing"':
                '"marketing_content"'
        }
        
        for old_path, new_path in path_updates.items():
            content = content.replace(old_path, new_path)
        
        with open(script_path, 'w') as f:
            f.write(content)
    
    def _create_default_config(self, config_path: Path, config_name: str):
        """Create default configuration files."""
        default_configs = {
            "automation_config.json": {
                "schedule": {
                    "sunday_planning": "09:00",
                    "monday_blog": "10:00", 
                    "tuesday_email": "10:00",
                    "wednesday_social": "10:00",
                    "thursday_shortform": "10:00",
                    "friday_cheatsheet": "10:00",
                    "saturday_qc": "10:00"
                },
                "quality_thresholds": {
                    "value_equation_minimum": 35,
                    "british_english_compliance": 1.0,
                    "voice_consistency_minimum": 0.9
                },
                "topic_rotation": {
                    "cycle_length_weeks": 12,
                    "prevent_repetition_weeks": 4
                },
                "output_settings": {
                    "blog_word_count_target": 2500,
                    "email_word_count_target": 1000,
                    "twitter_thread_length": 10,
                    "instagram_carousel_slides": 7
                },
                "website_sync": {
                    "enabled": True,
                    "website_repo_path": "../360tft",
                    "sync_schedule": "daily",
                    "sync_items": ["cheatsheets", "blog_posts", "resources"]
                }
            },
            "orchestrator_config.json": {
                "max_retries": 3,
                "retry_delay_seconds": 30,
                "quality_gate_threshold": 35,
                "dependency_timeout_minutes": 60,
                "parallel_execution": False,
                "content_templates": {
                    "blog_word_count_target": 2500,
                    "email_word_count_target": 1000,
                    "twitter_thread_length": 10,
                    "instagram_slides": 7,
                    "youtube_short_duration": 90
                }
            },
            "quality_standards.json": {
                "value_equation_minimum": 35,
                "british_english_score_minimum": 0.8,
                "voice_consistency_minimum": 0.85,
                "authority_score_minimum": 0.7,
                "fabrication_tolerance": 0.0,
                "word_count_ranges": {
                    "blog": [1500, 3000],
                    "email": [800, 1200],
                    "twitter_thread": [200, 400],
                    "linkedin": [800, 1200],
                    "instagram": [100, 300],
                    "shortform": [50, 150],
                    "cheatsheet": [500, 1500]
                }
            }
        }
        
        if config_name in default_configs:
            with open(config_path, 'w') as f:
                json.dump(default_configs[config_name], f, indent=2)
    
    def _create_readme_content(self) -> str:
        """Create README content for the automation repository."""
        return """# 360TFT Content Automation System

Independent content automation system for Kevin Middleton's 360TFT brand.

## Repository Structure

```
360tft-content-automation/
├── automation_scripts/     # Main automation Python scripts
├── marketing_content/      # All source marketing content 
├── produced_content/       # Generated weekly content
├── cheatsheets/           # Generated cheat sheets
├── voice_guidelines/      # Brand voice and content frameworks
├── config/               # Configuration files
├── output_for_website/   # Content ready for website sync
├── logs/                # Automation logs
└── progress/            # Weekly progress tracking
```

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Weekly Automation**
   ```bash
   cd automation_scripts
   python Weekly_Content_Automation.py run-week
   ```

3. **Check Status**
   ```bash
   python Weekly_Content_Automation.py status
   ```

4. **Sync to Website**
   ```bash
   python website_sync.py sync-all
   ```

## Features

- **Automated Content Creation**: 10 weekly content pieces + 1 cheat sheet
- **Quality Control**: Comprehensive QC with Value Equation scoring
- **Topic Management**: 27-topic rotation with performance tracking
- **Website Sync**: Export only necessary content to website repo
- **Voice Consistency**: Maintains Kevin's authentic coaching voice
- **British English**: Ensures proper British English throughout

## Weekly Automation Schedule

- **Sunday**: Topic selection and strategic planning
- **Monday**: Blog post creation
- **Tuesday**: Email newsletter adaptation  
- **Wednesday**: Social media content
- **Thursday**: Short-form content
- **Friday**: Cheat sheet creation
- **Saturday**: Quality control and optimization

## Content Output

Each week generates:
- 1 x Comprehensive blog post (2,500 words)
- 1 x Email newsletter (1,000 words)
- 1 x Twitter thread (10 tweets)
- 1 x LinkedIn article (1,200 words) 
- 1 x Instagram carousel (7 slides)
- 5 x Short-form tweets
- 1 x YouTube Short script
- 1 x A4 cheat sheet (HTML/PDF)

## Website Integration

The `website_sync.py` script handles exporting content to the main website:
- Copies published blog posts to `_posts/`
- Updates cheat sheet vault
- Syncs Academy resources
- Maintains website performance by keeping automation separate

## Configuration

All settings are stored in `config/`:
- `automation_config.json` - Main automation settings
- `orchestrator_config.json` - Content generation settings  
- `quality_standards.json` - QC thresholds and standards

## Voice Guidelines

The system maintains Kevin's authentic voice through:
- 15+ years coaching experience positioning
- 1,000+ players trained authority markers
- British English compliance
- 360TFT methodology integration
- Community-focused messaging
- No fabricated stories or examples

## Quality Control

Automated QC system scores content on:
- Value Equation optimization (35+ required)
- British English compliance
- Voice consistency
- Authority positioning
- Fabricated content detection
- Academy integration
- Structural requirements

## Support

This system was designed to keep Kevin's website fast while maintaining comprehensive content automation. The separation allows for:

- ✅ Lightweight website repository
- ✅ Full automation functionality
- ✅ Quality content generation
- ✅ Efficient website sync
- ✅ Independent scaling

---

*Created for Kevin Middleton | 360TFT | Football Coaching Academy*
"""
    
    def run_complete_setup(self):
        """Run the complete repository setup process."""
        print("🚀 Starting 360TFT Content Automation Repository Setup")
        print("=" * 60)
        
        try:
            # Create directory structure
            self.create_repository_structure()
            print()
            
            # Copy automation scripts
            self.copy_automation_scripts()
            print()
            
            # Copy marketing content
            self.copy_marketing_content()
            print()
            
            # Copy configuration files
            self.copy_configuration_files()
            print()
            
            # Copy voice guidelines
            self.copy_voice_guidelines()
            print()
            
            # Update automation paths
            self.update_automation_paths()
            print()
            
            # Setup git repository
            self.create_git_repository()
            print()
            
            print("🎉 Repository setup completed successfully!")
            print("=" * 60)
            print(f"📁 Automation repository created at: {self.target_path}")
            print("📝 Next steps:")
            print("   1. cd into the new repository")
            print("   2. Run: pip install -r requirements.txt")
            print("   3. Test with: python automation_scripts/Weekly_Content_Automation.py status")
            print("   4. Run migration script to move content from website repo")
            print("   5. Setup website sync for ongoing content flow")
            
        except Exception as e:
            print(f"❌ Setup failed: {str(e)}")
            raise


def main():
    """Main entry point for repository setup."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python setup_separate_repo.py <target_repository_path>")
        print("Example: python setup_separate_repo.py ../360tft-content-automation")
        return
    
    target_path = sys.argv[1]
    
    # Confirm setup
    print(f"This will create a new content automation repository at: {target_path}")
    confirm = input("Continue? (y/N): ").lower()
    
    if confirm != 'y':
        print("Setup cancelled.")
        return
    
    # Run setup
    setup = ContentAutomationRepoSetup(target_path)
    setup.run_complete_setup()


if __name__ == "__main__":
    main()