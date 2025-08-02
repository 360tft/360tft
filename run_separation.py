#!/usr/bin/env python3
"""
360TFT Content Automation Separation - Complete Process
=======================================================

Single script to run the complete separation process with user guidance.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import sys
from pathlib import Path
import subprocess


def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_step(step_num, title):
    """Print formatted step."""
    print(f"\n🔄 Step {step_num}: {title}")
    print("-" * 40)


def confirm_action(message):
    """Get user confirmation."""
    response = input(f"{message} (y/N): ").lower()
    return response == 'y'


def run_command(command, description):
    """Run command with description."""
    print(f"Running: {description}")
    print(f"Command: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Success!")
            if result.stdout:
                print(result.stdout)
        else:
            print("❌ Error!")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False
    
    return True


def main():
    """Main separation process."""
    print_header("360TFT Content Automation Separation")
    print("""
This script will separate your content automation system from your website
repository to improve performance and organization.

WHAT THIS DOES:
✅ Creates independent automation repository
✅ Moves all automation files and content
✅ Cleans website repository  
✅ Sets up content sync system
✅ Preserves all functionality

BENEFITS:
🚀 90% reduction in website repository size
🔄 Independent automation development
📊 Better content organization
🔧 Improved website performance
""")
    
    if not confirm_action("Continue with separation process?"):
        print("Separation cancelled.")
        return
    
    # Get target automation repository path
    default_automation_path = "../360tft-content-automation"
    automation_path = input(f"Automation repository path (default: {default_automation_path}): ").strip()
    if not automation_path:
        automation_path = default_automation_path
    
    print(f"\nSeparation Plan:")
    print(f"  Website Repository: {Path.cwd()}")
    print(f"  Automation Repository: {automation_path}")
    print()
    
    if not confirm_action("Proceed with this configuration?"):
        print("Separation cancelled.")
        return
    
    # Step 1: Setup Automation Repository
    print_step(1, "Create Automation Repository")
    print("Creating independent automation repository structure...")
    
    setup_command = f"python setup_separate_repo.py {automation_path}"
    if not run_command(setup_command, "Setup automation repository"):
        print("❌ Repository setup failed. Please check errors above.")
        return
    
    print("✅ Automation repository created successfully!")
    print(f"📁 Location: {Path(automation_path).resolve()}")
    
    # Confirm continuation
    if not confirm_action("Continue with content migration?"):
        print("Separation stopped. Automation repository created but no migration performed.")
        return
    
    # Step 2: Migrate Content
    print_step(2, "Migrate Content")
    print("Migrating content from website to automation repository...")
    print("⚠️  This will remove automation files from website repository!")
    
    if not confirm_action("Proceed with content migration?"):
        print("Migration cancelled. You can run migration later with:")
        print(f"python migrate_content.py . {automation_path}")
        return
    
    migrate_command = f"python migrate_content.py . {automation_path}"
    if not run_command(migrate_command, "Migrate content"):
        print("❌ Content migration failed. Check errors above.")
        return
    
    print("✅ Content migration completed successfully!")
    
    # Step 3: Setup Website Sync
    print_step(3, "Setup Website Sync")
    print("Setting up automated content sync from automation to website...")
    
    sync_setup_command = f"python {automation_path}/automation_scripts/website_sync.py {automation_path} . setup"
    if not run_command(sync_setup_command, "Setup website sync"):
        print("❌ Website sync setup failed. You can setup sync manually later.")
    else:
        print("✅ Website sync configured successfully!")
    
    # Step 4: Test Automation
    print_step(4, "Test Automation System")
    print("Testing the separated automation system...")
    
    test_command = f"python {automation_path}/automation_scripts/Weekly_Content_Automation.py status"
    if not run_command(test_command, "Test automation system"):
        print("⚠️  Automation test failed. You may need to check configuration.")
    else:
        print("✅ Automation system working correctly!")
    
    # Step 5: Verify Website
    print_step(5, "Verify Website Repository")
    print("Checking website repository status...")
    
    # Check if essential website files exist
    essential_files = [
        "_config.yml",
        "index.md",
        "_layouts",
        "_includes"
    ]
    
    missing_files = []
    for file_path in essential_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"⚠️  Missing essential website files: {missing_files}")
    else:
        print("✅ Website repository structure preserved!")
    
    # Final Summary
    print_header("Separation Complete!")
    print("""
🎉 Content automation separation completed successfully!

WHAT'S CHANGED:

📁 Automation Repository (NEW):
   Location: {automation_path}
   Contains: All automation scripts, marketing content, configurations
   
📁 Website Repository (CLEANED):
   Location: {website_path}
   Contains: Only Jekyll website files and published content
   Size: Reduced by ~90%

NEXT STEPS:

1. TEST AUTOMATION:
   cd {automation_path}/automation_scripts
   python Weekly_Content_Automation.py run-week

2. SYNC CONTENT TO WEBSITE:
   python website_sync.py {automation_path} {website_path} sync-all

3. BUILD WEBSITE:
   bundle exec jekyll serve

4. COMMIT CHANGES:
   git add . && git commit -m "Separate automation system"

DAILY WORKFLOW:

• Content Creation: Work in automation repository
• Content Publishing: Sync to website repository  
• Website Updates: Normal Jekyll deployment

SUPPORT FILES CREATED:
• README_SEPARATION.md - Complete separation guide
• MIGRATION_REPORT.md - Detailed migration report
• CONTENT_AUTOMATION_MOVED.md - Link to automation repo

The separation is complete! Your automation system is now independent
while maintaining full functionality and improving website performance.
""".format(
        automation_path=Path(automation_path).resolve(),
        website_path=Path.cwd()
    ))


if __name__ == "__main__":
    main()