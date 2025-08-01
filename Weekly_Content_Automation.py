#!/usr/bin/env python3
"""
360TFT Weekly Content Automation System
=======================================

Main automation script for Kevin Middleton's 360TFT weekly content creation.
Manages 27-topic rotation, triggers subagent workflows, tracks progress, and implements quality control.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import json
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import schedule
import time

from Topic_Selection_Manager import TopicSelectionManager
from Subagent_Orchestrator import SubagentOrchestrator
from Quality_Control_System import QualityControlSystem


class WeeklyContentAutomation:
    """
    Main automation controller for 360TFT weekly content creation.
    
    Manages the complete workflow from topic selection through content publication,
    ensuring consistency with Kevin's voice and 360TFT methodology.
    """
    
    def __init__(self, config_path: str = "automation_config.json"):
        """
        Initialize the automation system.
        
        Args:
            config_path: Path to configuration file
        """
        # Setup paths relative to script location
        self.base_path = Path(__file__).parent
        self.marketing_path = self.base_path / "Marketing"
        self.produced_content_path = self.marketing_path / "Produced Content"
        self.cheatsheets_path = self.marketing_path / "Cheatsheets"
        self.voice_path = self.marketing_path / "Voice"
        
        # Ensure required directories exist
        self._create_required_directories()
        
        # Setup logging
        self._setup_logging()
        
        # Load configuration
        self.config = self._load_config(config_path)
        
        # Initialize components
        self.topic_manager = TopicSelectionManager(self.marketing_path)
        self.orchestrator = SubagentOrchestrator(self.base_path)
        self.quality_control = QualityControlSystem(self.voice_path)
        
        # Track current week's progress
        self.current_week_progress = self._load_progress()
        
        self.logger.info("360TFT Weekly Content Automation System initialized")
    
    def _create_required_directories(self):
        """Create necessary directory structure if it doesn't exist."""
        required_dirs = [
            self.produced_content_path,
            self.cheatsheets_path,
            self.base_path / "logs",
            self.base_path / "progress",
            self.base_path / "Content_Templates"
        ]
        
        for directory in required_dirs:
            directory.mkdir(parents=True, exist_ok=True)
    
    def _setup_logging(self):
        """Configure logging system."""
        log_dir = self.base_path / "logs"
        log_file = log_dir / f"automation_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def _load_config(self, config_path: str) -> Dict:
        """Load automation configuration."""
        default_config = {
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
            }
        }
        
        config_file = self.base_path / config_path
        if config_file.exists():
            with open(config_file, 'r') as f:
                loaded_config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in loaded_config:
                        loaded_config[key] = value
                return loaded_config
        else:
            # Create default config file
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def _load_progress(self) -> Dict:
        """Load current week's progress tracking."""
        progress_file = self.base_path / "progress" / f"week_{self._get_current_week_number()}.json"
        
        if progress_file.exists():
            with open(progress_file, 'r') as f:
                return json.load(f)
        
        # Initialize new week progress
        return {
            "week_number": self._get_current_week_number(),
            "start_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "selected_topic": None,
            "content_pieces": {
                "blog_post": {"status": "pending", "file_path": None, "quality_score": None},
                "email_newsletter": {"status": "pending", "file_path": None, "quality_score": None},
                "twitter_thread": {"status": "pending", "file_path": None, "quality_score": None},
                "linkedin_article": {"status": "pending", "file_path": None, "quality_score": None},
                "instagram_carousel": {"status": "pending", "file_path": None, "quality_score": None},
                "short_form_tweets": {"status": "pending", "file_path": None, "quality_score": None},
                "youtube_short": {"status": "pending", "file_path": None, "quality_score": None},
                "cheat_sheet": {"status": "pending", "file_path": None, "quality_score": None}
            },
            "overall_status": "planning",
            "quality_control_passed": False,
            "publication_ready": False
        }
    
    def _save_progress(self):
        """Save current progress to file."""
        progress_file = self.base_path / "progress" / f"week_{self._get_current_week_number()}.json"
        with open(progress_file, 'w') as f:
            json.dump(self.current_week_progress, f, indent=2)
    
    def _get_current_week_number(self) -> int:
        """Get current week number for tracking."""
        # Use ISO week number
        return datetime.datetime.now().isocalendar()[1]
    
    def _get_week_folder_name(self, topic: str) -> str:
        """Generate standardized folder name for the week's content."""
        # Clean topic name for folder
        clean_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '_')).rstrip()
        clean_topic = clean_topic.replace(' ', '_')
        week_num = self._get_current_week_number()
        return f"Week_{week_num}_{clean_topic}"
    
    # PHASE 1: SUNDAY PLANNING
    def run_sunday_planning(self):
        """Execute Sunday planning phase - topic selection and strategy."""
        self.logger.info("Starting Sunday Planning Phase")
        
        try:
            # Select this week's topic
            selected_topic = self.topic_manager.select_weekly_topic()
            self.current_week_progress["selected_topic"] = selected_topic
            self.current_week_progress["overall_status"] = "planning_complete"
            
            # Create folder structure for this week
            week_folder = self.produced_content_path / self._get_week_folder_name(selected_topic)
            week_folder.mkdir(exist_ok=True)
            
            # Generate strategic content brief
            content_brief = self.orchestrator.create_strategic_brief(selected_topic)
            
            # Save brief to week folder
            brief_file = week_folder / "Strategic_Content_Brief.md"
            with open(brief_file, 'w', encoding='utf-8') as f:
                f.write(content_brief)
            
            self._save_progress()
            self.logger.info(f"Sunday planning complete. Selected topic: {selected_topic}")
            
            return True, f"Planning complete for topic: {selected_topic}"
            
        except Exception as e:
            self.logger.error(f"Sunday planning failed: {str(e)}")
            return False, f"Planning failed: {str(e)}"
    
    # PHASE 2: MONDAY BLOG CREATION
    def run_monday_blog_creation(self):
        """Execute Monday blog creation phase."""
        self.logger.info("Starting Monday Blog Creation Phase")
        
        if not self.current_week_progress["selected_topic"]:
            return False, "No topic selected. Run Sunday planning first."
        
        try:
            topic = self.current_week_progress["selected_topic"]
            week_folder = self.produced_content_path / self._get_week_folder_name(topic)
            
            # Create blog post
            blog_content = self.orchestrator.create_blog_post(topic)
            
            # Save blog post
            blog_file = week_folder / f"Blog_Post_{topic.replace(' ', '_')}.md"
            with open(blog_file, 'w', encoding='utf-8') as f:
                f.write(blog_content)
            
            # Quality check
            quality_score = self.quality_control.evaluate_content(blog_content, "blog")
            
            # Update progress
            self.current_week_progress["content_pieces"]["blog_post"] = {
                "status": "completed" if quality_score >= self.config["quality_thresholds"]["value_equation_minimum"] else "needs_revision",
                "file_path": str(blog_file),
                "quality_score": quality_score
            }
            
            self._save_progress()
            self.logger.info(f"Blog creation complete. Quality score: {quality_score}")
            
            return True, f"Blog post created with quality score: {quality_score}"
            
        except Exception as e:
            self.logger.error(f"Blog creation failed: {str(e)}")
            return False, f"Blog creation failed: {str(e)}"
    
    # PHASE 3: TUESDAY EMAIL ADAPTATION
    def run_tuesday_email_adaptation(self):
        """Execute Tuesday email newsletter adaptation phase."""
        self.logger.info("Starting Tuesday Email Adaptation Phase")
        
        try:
            topic = self.current_week_progress["selected_topic"]
            week_folder = self.produced_content_path / self._get_week_folder_name(topic)
            
            # Load blog post for adaptation
            blog_file = week_folder / f"Blog_Post_{topic.replace(' ', '_')}.md"
            if not blog_file.exists():
                return False, "Blog post not found. Complete Monday phase first."
            
            with open(blog_file, 'r', encoding='utf-8') as f:
                blog_content = f.read()
            
            # Create email newsletter
            email_content = self.orchestrator.create_email_newsletter(topic, blog_content)
            
            # Save email newsletter
            email_file = week_folder / f"Email_Newsletter_{topic.replace(' ', '_')}.md"
            with open(email_file, 'w', encoding='utf-8') as f:
                f.write(email_content)
            
            # Quality check
            quality_score = self.quality_control.evaluate_content(email_content, "email")
            
            # Update progress
            self.current_week_progress["content_pieces"]["email_newsletter"] = {
                "status": "completed" if quality_score >= self.config["quality_thresholds"]["value_equation_minimum"] else "needs_revision",
                "file_path": str(email_file),
                "quality_score": quality_score
            }
            
            self._save_progress()
            self.logger.info(f"Email adaptation complete. Quality score: {quality_score}")
            
            return True, f"Email newsletter created with quality score: {quality_score}"
            
        except Exception as e:
            self.logger.error(f"Email adaptation failed: {str(e)}")
            return False, f"Email adaptation failed: {str(e)}"
    
    # PHASE 4: WEDNESDAY SOCIAL MEDIA
    def run_wednesday_social_media(self):
        """Execute Wednesday social media content creation phase."""
        self.logger.info("Starting Wednesday Social Media Phase")
        
        try:
            topic = self.current_week_progress["selected_topic"]
            week_folder = self.produced_content_path / self._get_week_folder_name(topic)
            
            # Create social media content
            social_content = self.orchestrator.create_social_media_content(topic)
            
            # Save individual social media pieces
            for platform, content in social_content.items():
                social_file = week_folder / f"{platform.title()}_{topic.replace(' ', '_')}.md"
                with open(social_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Quality check for primary platforms
                if platform in ["twitter_thread", "linkedin_article"]:
                    quality_score = self.quality_control.evaluate_content(content, platform)
                    
                    self.current_week_progress["content_pieces"][platform] = {
                        "status": "completed" if quality_score >= self.config["quality_thresholds"]["value_equation_minimum"] else "needs_revision",
                        "file_path": str(social_file),
                        "quality_score": quality_score
                    }
            
            self._save_progress()
            self.logger.info("Social media content creation complete")
            
            return True, "Social media content created successfully"
            
        except Exception as e:
            self.logger.error(f"Social media creation failed: {str(e)}")
            return False, f"Social media creation failed: {str(e)}"
    
    # PHASE 5: THURSDAY SHORT-FORM
    def run_thursday_shortform(self):
        """Execute Thursday short-form content creation phase."""
        self.logger.info("Starting Thursday Short-form Phase")
        
        try:
            topic = self.current_week_progress["selected_topic"]
            week_folder = self.produced_content_path / self._get_week_folder_name(topic)
            
            # Create short-form content
            shortform_content = self.orchestrator.create_shortform_content(topic)
            
            # Save short-form content
            shortform_file = week_folder / f"Shortform_Content_{topic.replace(' ', '_')}.md"
            with open(shortform_file, 'w', encoding='utf-8') as f:
                f.write(shortform_content)
            
            # Quality check
            quality_score = self.quality_control.evaluate_content(shortform_content, "shortform")
            
            # Update progress
            self.current_week_progress["content_pieces"]["short_form_tweets"] = {
                "status": "completed" if quality_score >= self.config["quality_thresholds"]["value_equation_minimum"] else "needs_revision",
                "file_path": str(shortform_file),
                "quality_score": quality_score
            }
            
            self._save_progress()
            self.logger.info(f"Short-form creation complete. Quality score: {quality_score}")
            
            return True, f"Short-form content created with quality score: {quality_score}"
            
        except Exception as e:
            self.logger.error(f"Short-form creation failed: {str(e)}")
            return False, f"Short-form creation failed: {str(e)}"
    
    # PHASE 6: FRIDAY CHEAT SHEET
    def run_friday_cheatsheet(self):
        """Execute Friday cheat sheet creation phase."""
        self.logger.info("Starting Friday Cheat Sheet Phase")
        
        try:
            topic = self.current_week_progress["selected_topic"]
            week_folder = self.produced_content_path / self._get_week_folder_name(topic)
            
            # Create cheat sheet
            cheatsheet_content = self.orchestrator.create_cheatsheet(topic)
            
            # Save cheat sheet (HTML format for A4 printing)
            cheatsheet_file = week_folder / f"Cheatsheet_{topic.replace(' ', '_')}_A4.html"
            with open(cheatsheet_file, 'w', encoding='utf-8') as f:
                f.write(cheatsheet_content)
            
            # Also save to main cheatsheets folder
            main_cheatsheet_file = self.cheatsheets_path / f"{topic.replace(' ', '_')}_A4.html"
            with open(main_cheatsheet_file, 'w', encoding='utf-8') as f:
                f.write(cheatsheet_content)
            
            # Quality check
            quality_score = self.quality_control.evaluate_content(cheatsheet_content, "cheatsheet")
            
            # Update progress
            self.current_week_progress["content_pieces"]["cheat_sheet"] = {
                "status": "completed" if quality_score >= self.config["quality_thresholds"]["value_equation_minimum"] else "needs_revision",
                "file_path": str(cheatsheet_file),
                "quality_score": quality_score
            }
            
            self._save_progress()
            self.logger.info(f"Cheat sheet creation complete. Quality score: {quality_score}")
            
            return True, f"Cheat sheet created with quality score: {quality_score}"
            
        except Exception as e:
            self.logger.error(f"Cheat sheet creation failed: {str(e)}")
            return False, f"Cheat sheet creation failed: {str(e)}"
    
    # PHASE 7: SATURDAY QUALITY CONTROL
    def run_saturday_quality_control(self):
        """Execute Saturday quality control and optimization phase."""
        self.logger.info("Starting Saturday Quality Control Phase")
        
        try:
            topic = self.current_week_progress["selected_topic"]
            week_folder = self.produced_content_path / self._get_week_folder_name(topic)
            
            # Comprehensive quality review
            quality_report = self.quality_control.comprehensive_review(week_folder)
            
            # Save quality report
            report_file = week_folder / "Quality_Control_Report.md"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(quality_report)
            
            # Check if all content meets standards
            all_passed = all(
                piece["quality_score"] and piece["quality_score"] >= self.config["quality_thresholds"]["value_equation_minimum"]
                for piece in self.current_week_progress["content_pieces"].values()
                if piece["quality_score"] is not None
            )
            
            # Update final status
            self.current_week_progress["quality_control_passed"] = all_passed
            self.current_week_progress["publication_ready"] = all_passed
            self.current_week_progress["overall_status"] = "completed" if all_passed else "needs_revision"
            
            self._save_progress()
            
            status_msg = "All content passed quality control" if all_passed else "Some content needs revision"
            self.logger.info(f"Quality control complete. {status_msg}")
            
            return True, status_msg
            
        except Exception as e:
            self.logger.error(f"Quality control failed: {str(e)}")
            return False, f"Quality control failed: {str(e)}"
    
    # AUTOMATION SCHEDULING
    def setup_weekly_schedule(self):
        """Setup automated weekly schedule."""
        schedule_config = self.config["schedule"]
        
        # Schedule weekly tasks
        schedule.every().sunday.at(schedule_config["sunday_planning"]).do(self.run_sunday_planning)
        schedule.every().monday.at(schedule_config["monday_blog"]).do(self.run_monday_blog_creation)
        schedule.every().tuesday.at(schedule_config["tuesday_email"]).do(self.run_tuesday_email_adaptation)
        schedule.every().wednesday.at(schedule_config["wednesday_social"]).do(self.run_wednesday_social_media)
        schedule.every().thursday.at(schedule_config["thursday_shortform"]).do(self.run_thursday_shortform)
        schedule.every().friday.at(schedule_config["friday_cheatsheet"]).do(self.run_friday_cheatsheet)
        schedule.every().saturday.at(schedule_config["saturday_qc"]).do(self.run_saturday_quality_control)
        
        self.logger.info("Weekly automation schedule configured")
    
    def run_automation_loop(self):
        """Run the main automation loop."""
        self.logger.info("Starting 360TFT Weekly Content Automation Loop")
        
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            except KeyboardInterrupt:
                self.logger.info("Automation stopped by user")
                break
            except Exception as e:
                self.logger.error(f"Automation loop error: {str(e)}")
                time.sleep(300)  # Wait 5 minutes before retrying
    
    # MANUAL EXECUTION METHODS
    def run_complete_week_manually(self):
        """Run complete week's content creation manually."""
        self.logger.info("Starting manual complete week execution")
        
        phases = [
            ("Sunday Planning", self.run_sunday_planning),
            ("Monday Blog Creation", self.run_monday_blog_creation),
            ("Tuesday Email Adaptation", self.run_tuesday_email_adaptation),
            ("Wednesday Social Media", self.run_wednesday_social_media),
            ("Thursday Short-form", self.run_thursday_shortform),
            ("Friday Cheat Sheet", self.run_friday_cheatsheet),
            ("Saturday Quality Control", self.run_saturday_quality_control)
        ]
        
        results = []
        for phase_name, phase_function in phases:
            self.logger.info(f"Executing {phase_name}")
            success, message = phase_function()
            results.append((phase_name, success, message))
            
            if not success:
                self.logger.error(f"{phase_name} failed: {message}")
                break
            
            self.logger.info(f"{phase_name} completed: {message}")
        
        return results
    
    def get_progress_summary(self) -> Dict:
        """Get current week's progress summary."""
        return {
            "week_number": self.current_week_progress["week_number"],
            "selected_topic": self.current_week_progress["selected_topic"],
            "overall_status": self.current_week_progress["overall_status"],
            "completion_percentage": self._calculate_completion_percentage(),
            "quality_control_passed": self.current_week_progress["quality_control_passed"],
            "publication_ready": self.current_week_progress["publication_ready"],
            "content_pieces_status": {
                piece: data["status"] 
                for piece, data in self.current_week_progress["content_pieces"].items()
            }
        }
    
    def _calculate_completion_percentage(self) -> float:
        """Calculate completion percentage for current week."""
        completed_pieces = sum(
            1 for piece in self.current_week_progress["content_pieces"].values()
            if piece["status"] == "completed"
        )
        total_pieces = len(self.current_week_progress["content_pieces"])
        
        return (completed_pieces / total_pieces) * 100 if total_pieces > 0 else 0


def main():
    """Main entry point for the automation system."""
    automation = WeeklyContentAutomation()
    
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "run-week":
            # Run complete week manually
            results = automation.run_complete_week_manually()
            print("\n=== WEEK EXECUTION RESULTS ===")
            for phase, success, message in results:
                status = "✅ SUCCESS" if success else "❌ FAILED"
                print(f"{status}: {phase} - {message}")
            
        elif command == "status":
            # Show current status
            progress = automation.get_progress_summary()
            print("\n=== CURRENT PROGRESS ===")
            print(f"Week: {progress['week_number']}")
            print(f"Topic: {progress['selected_topic']}")
            print(f"Status: {progress['overall_status']}")
            print(f"Completion: {progress['completion_percentage']:.1f}%")
            print(f"Quality Control: {'✅ Passed' if progress['quality_control_passed'] else '❌ Pending'}")
            print(f"Publication Ready: {'✅ Yes' if progress['publication_ready'] else '❌ No'}")
            
        elif command == "schedule":
            # Run automated scheduling
            automation.setup_weekly_schedule()
            automation.run_automation_loop()
            
        else:
            print("Usage: python Weekly_Content_Automation.py [run-week|status|schedule]")
    
    else:
        print("360TFT Weekly Content Automation System")
        print("Usage: python Weekly_Content_Automation.py [run-week|status|schedule]")
        print("  run-week: Execute complete week manually")
        print("  status:   Show current progress")
        print("  schedule: Start automated scheduling")


if __name__ == "__main__":
    main()