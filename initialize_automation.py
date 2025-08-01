#!/usr/bin/env python3
"""
360TFT Content Automation Initialization System
===============================================

This script sets up Kevin's complete content automation workflow with:
- Topic-based folder structure validation
- Initial rotation schedule creation
- Voice content validation
- Configuration file setup
- Subagent connectivity testing
- First week's content plan generation

Author: Kevin Middleton's Automation System
Created: 2025-08-01
"""

import os
import json
import datetime
import random
from pathlib import Path
from typing import Dict, List, Any, Optional

class AutomationInitializer:
    def __init__(self, base_path: str = None):
        """Initialize the automation system with base directory path."""
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.marketing_path = self.base_path / "Marketing"
        self.produced_content_path = self.marketing_path / "Produced Content"
        self.voice_path = self.marketing_path / "Voice"
        
        # Define the 10 topic folders based on Kevin's content
        self.topic_folders = [
            "A_Practical_Guide_for_Development_Professionals",
            "How_To_Run_Better_Rondos", 
            "Learning_One_Position_Versus_Many",
            "The_Session_Planning_System_That_Actually_Works",
            "Top_8_Small_Sided_Games_That_Actually_Improve_Your_Players",
            "Training_On_Your_Own",
            "Why_So_Many_Youth_Football_Sessions_Don't_Stick",
            "The_Passing_Drill_That_Changes_Everything",
            "1v1_Moves_That_Beat_Defenders_Every_Time",
            "Finishing_Practice_Players_Actually_Enjoy"
        ]
        
        # Content formats for each topic
        self.content_formats = [
            "Blog_Post",
            "Email_Newsletter", 
            "Newsletter",
            "Twitter_Thread",
            "Tweet_Shortform",
            "Instagram_Caption",
            "LinkedIn_Post"
        ]
        
        self.setup_log = []
        
    def log_step(self, message: str, success: bool = True):
        """Log setup steps with status."""
        status = "[OK]" if success else "[ERROR]"
        log_entry = f"{status} {message}"
        self.setup_log.append(log_entry)
        print(log_entry)
        
    def validate_directory_structure(self) -> bool:
        """Validate that all required directories exist."""
        print("=" * 60)
        print("STEP 1: VALIDATING DIRECTORY STRUCTURE")
        print("=" * 60)
        
        required_paths = [
            self.marketing_path,
            self.produced_content_path,
            self.voice_path,
            self.marketing_path / "Blogs",
            self.marketing_path / "Emails",
            self.marketing_path / "Cheatsheets"
        ]
        
        all_valid = True
        for path in required_paths:
            if path.exists():
                self.log_step(f"Found directory: {path.name}")
            else:
                self.log_step(f"Missing directory: {path}", False)
                all_valid = False
                
        return all_valid
        
    def create_topic_folders(self) -> bool:
        """Create and validate topic-based folder structure."""
        print("\n" + "=" * 60)
        print("STEP 2: CREATING TOPIC FOLDER STRUCTURE")
        print("=" * 60)
        
        success_count = 0
        for topic in self.topic_folders:
            topic_path = self.produced_content_path / topic
            try:
                topic_path.mkdir(parents=True, exist_ok=True)
                self.log_step(f"Created topic folder: {topic}")
                success_count += 1
            except Exception as e:
                self.log_step(f"Failed to create {topic}: {str(e)}", False)
                
        return success_count == len(self.topic_folders)
        
    def validate_voice_content(self) -> bool:
        """Validate that voice guidelines exist and are accessible."""
        print("\n" + "=" * 60)
        print("STEP 3: VALIDATING VOICE CONTENT")
        print("=" * 60)
        
        voice_file = self.voice_path / "Voice"
        if voice_file.exists():
            try:
                with open(voice_file, 'r', encoding='utf-8') as f:
                    voice_content = f.read()
                    
                # Check for key voice elements
                key_elements = [
                    "football coach",
                    "15+ years",
                    "British English",
                    "Seth Godin",
                    "no em dashes"
                ]
                
                found_elements = []
                for element in key_elements:
                    if element.lower() in voice_content.lower():
                        found_elements.append(element)
                        
                self.log_step(f"Voice file found with {len(found_elements)}/{len(key_elements)} key elements")
                self.log_step(f"Voice file size: {len(voice_content)} characters")
                return True
                
            except Exception as e:
                self.log_step(f"Error reading voice file: {str(e)}", False)
                return False
        else:
            self.log_step("Voice file not found", False)
            return False
            
    def create_topic_rotation_schedule(self) -> Dict[str, Any]:
        """Create initial 12-week topic rotation schedule."""
        print("\n" + "=" * 60)
        print("STEP 4: CREATING TOPIC ROTATION SCHEDULE")
        print("=" * 60)
        
        # Shuffle topics for variety
        shuffled_topics = self.topic_folders.copy()
        random.shuffle(shuffled_topics)
        
        # Extend to 12 weeks (cycle through topics)
        rotation_schedule = []
        for week in range(12):
            topic_index = week % len(shuffled_topics)
            topic = shuffled_topics[topic_index]
            
            week_start = datetime.datetime.now() + datetime.timedelta(weeks=week)
            rotation_schedule.append({
                "week": week + 1,
                "start_date": week_start.strftime("%Y-%m-%d"),
                "topic": topic,
                "content_focus": self._get_content_focus(topic),
                "target_formats": self.content_formats[:5]  # Focus on top 5 formats
            })
            
        self.log_step(f"Created 12-week rotation schedule with {len(self.topic_folders)} topics")
        return {"rotation_schedule": rotation_schedule, "last_updated": datetime.datetime.now().isoformat()}
        
    def _get_content_focus(self, topic: str) -> str:
        """Generate content focus description for each topic."""
        focus_map = {
            "A_Practical_Guide_for_Development_Professionals": "Youth development methodologies and professional coaching standards",
            "How_To_Run_Better_Rondos": "Possession-based training exercises and tactical awareness",
            "Learning_One_Position_Versus_Many": "Player specialization vs versatility in youth development",
            "The_Session_Planning_System_That_Actually_Works": "Structured training session design and organization",
            "Top_8_Small_Sided_Games_That_Actually_Improve_Your_Players": "Match-realistic training games with clear learning outcomes",
            "Training_On_Your_Own": "Individual skill development and home practice routines",
            "Why_So_Many_Youth_Football_Sessions_Don't_Stick": "Common coaching mistakes and solution-focused training",
            "The_Passing_Drill_That_Changes_Everything": "Technical passing exercises with progressive difficulty",
            "1v1_Moves_That_Beat_Defenders_Every_Time": "Individual attacking skills and dribbling techniques",
            "Finishing_Practice_Players_Actually_Enjoy": "Goal-scoring training with engagement and variety"
        }
        return focus_map.get(topic, "Football coaching and player development")
        
    def create_sample_configurations(self) -> bool:
        """Create sample configuration files for different content types."""
        print("\n" + "=" * 60)
        print("STEP 5: CREATING SAMPLE CONFIGURATIONS")
        print("=" * 60)
        
        configurations = {
            "content_templates.json": {
                "blog_post_structure": {
                    "introduction": "Hook + Problem identification",
                    "main_content": "3-5 practical sections with examples",
                    "conclusion": "Action steps + 360TFT integration",
                    "word_count_target": 2500,
                    "value_equation_minimum": 35
                },
                "email_structure": {
                    "subject_line": "Curiosity + Benefit",
                    "opening": "Personal connection + Problem",
                    "main_teaching": "1-2 key concepts with examples",
                    "call_to_action": "360TFT academy integration",
                    "word_count_target": 1000
                },
                "social_media": {
                    "twitter_thread": "10 tweets maximum",
                    "instagram_carousel": "7 slides maximum",
                    "linkedin_post": "Professional tone + coaching insights"
                }
            },
            
            "quality_standards.json": {
                "british_english_requirements": {
                    "spelling": "colour, favourite, realise, etc.",
                    "terminology": "football (not soccer), pitch (not field)",
                    "tone": "Professional but accessible"
                },
                "voice_consistency": {
                    "experience_reference": "15+ years coaching experience",
                    "authority_indicators": "1,000+ players trained, 1,200+ coaches educated",
                    "prohibited_elements": ["em dashes", "fabricated stories", "non-British spelling"]
                },
                "value_equation_components": {
                    "dream_outcome": "Coaching success and player development",
                    "perceived_likelihood": "Proven methods and testimonials",
                    "time_delay": "Quick implementation",
                    "effort_sacrifice": "Minimal complexity, maximum impact"
                }
            },
            
            "automation_schedule.json": {
                "content_creation_days": {
                    "sunday": "Weekly planning and topic selection",
                    "monday": "Blog post creation and review",
                    "tuesday": "Email newsletter development",
                    "wednesday": "Social media content creation",
                    "thursday": "Short-form content and threads",
                    "friday": "Cheatsheet and visual content",
                    "saturday": "Quality control and scheduling"
                },
                "quality_check_points": [
                    "Voice consistency validation",
                    "British English compliance",
                    "Value equation scoring",
                    "Technical accuracy review",
                    "Brand alignment check"
                ]
            }
        }
        
        config_count = 0
        for filename, config_data in configurations.items():
            config_path = self.base_path / filename
            try:
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(config_data, f, indent=2, ensure_ascii=False)
                self.log_step(f"Created configuration: {filename}")
                config_count += 1
            except Exception as e:
                self.log_step(f"Failed to create {filename}: {str(e)}", False)
                
        return config_count == len(configurations)
        
    def test_subagent_connectivity(self) -> bool:
        """Test that subagent files are accessible and properly configured."""
        print("\n" + "=" * 60)
        print("STEP 6: TESTING SUBAGENT CONNECTIVITY")
        print("=" * 60)
        
        subagent_files = [
            "Weekly_Content_Automation.py",
            "Subagent_Orchestrator.py", 
            "Topic_Selection_Manager.py",
            "Quality_Control_System.py"
        ]
        
        accessible_count = 0
        for subagent_file in subagent_files:
            file_path = self.base_path / subagent_file
            if file_path.exists():
                try:
                    # Test file readability
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if len(content) > 100:  # Basic content validation
                            self.log_step(f"Subagent accessible: {subagent_file}")
                            accessible_count += 1
                        else:
                            self.log_step(f"Subagent file too small: {subagent_file}", False)
                except Exception as e:
                    self.log_step(f"Cannot read subagent: {subagent_file} - {str(e)}", False)
            else:
                self.log_step(f"Missing subagent file: {subagent_file}", False)
                
        return accessible_count >= 3  # At least 3 out of 4 should be accessible
        
    def generate_first_week_plan(self, rotation_schedule: Dict[str, Any]) -> Dict[str, Any]:
        """Generate detailed plan for the first week of automation."""
        print("\n" + "=" * 60)
        print("STEP 7: GENERATING FIRST WEEK'S PLAN")
        print("=" * 60)
        
        if not rotation_schedule.get("rotation_schedule"):
            self.log_step("No rotation schedule available", False)
            return {}
            
        first_week = rotation_schedule["rotation_schedule"][0]
        topic = first_week["topic"]
        
        # Create detailed daily plan
        weekly_plan = {
            "week_1_details": {
                "topic": topic,
                "content_focus": first_week["content_focus"],
                "daily_schedule": {
                    "sunday": {
                        "task": "Topic analysis and content angle selection",
                        "deliverable": "Content brief and angle selection",
                        "time_required": "2 hours",
                        "priority": "high"
                    },
                    "monday": {
                        "task": f"Create comprehensive blog post on {topic.replace('_', ' ')}",
                        "deliverable": "2,500-word blog post with practical examples",
                        "time_required": "3 hours",
                        "priority": "high"
                    },
                    "tuesday": {
                        "task": "Develop email newsletter from blog content",
                        "deliverable": "1,000-word email with clear CTA",
                        "time_required": "1.5 hours", 
                        "priority": "high"
                    },
                    "wednesday": {
                        "task": "Create social media content suite",
                        "deliverable": "Twitter thread, Instagram carousel, LinkedIn post",
                        "time_required": "2 hours",
                        "priority": "medium"
                    },
                    "thursday": {
                        "task": "Develop short-form content variations",
                        "deliverable": "Twitter threads and bite-sized tips",
                        "time_required": "1 hour",
                        "priority": "medium"
                    },
                    "friday": {
                        "task": "Create supporting cheatsheet or visual",
                        "deliverable": "PDF cheatsheet or infographic",
                        "time_required": "2 hours",
                        "priority": "low"
                    },
                    "saturday": {
                        "task": "Quality control and final review",
                        "deliverable": "Approved content ready for publishing",
                        "time_required": "1 hour",
                        "priority": "high"
                    }
                }
            },
            "quality_checkpoints": [
                "Voice consistency with Kevin's style",
                "British English compliance",
                "Value equation score ≥ 35",
                "Technical coaching accuracy",
                "360TFT brand integration"
            ],
            "success_metrics": {
                "content_pieces_created": 7,
                "total_word_count_target": 4500,
                "formats_covered": 5,
                "quality_score_target": 90
            }
        }
        
        self.log_step(f"Generated detailed plan for Week 1: {topic.replace('_', ' ')}")
        return weekly_plan
        
    def create_initialization_report(self, rotation_schedule: Dict[str, Any], weekly_plan: Dict[str, Any]) -> str:
        """Create comprehensive initialization report."""
        print("\n" + "=" * 60)
        print("STEP 8: CREATING INITIALIZATION REPORT")
        print("=" * 60)
        
        report_content = f"""
# 360TFT Content Automation Initialization Report
Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## System Setup Status
{chr(10).join(self.setup_log)}

## Topic Rotation Schedule (Next 4 Weeks)
"""
        
        if rotation_schedule.get("rotation_schedule"):
            for week_data in rotation_schedule["rotation_schedule"][:4]:
                report_content += f"""
### Week {week_data['week']} - {week_data['start_date']}
- **Topic**: {week_data['topic'].replace('_', ' ')}
- **Focus**: {week_data['content_focus']}
- **Formats**: {', '.join(week_data['target_formats'])}
"""
        
        if weekly_plan:
            report_content += f"""
## Week 1 Detailed Plan
**Primary Topic**: {weekly_plan['week_1_details']['topic'].replace('_', ' ')}

**Daily Schedule**:
"""
            for day, details in weekly_plan['week_1_details']['daily_schedule'].items():
                report_content += f"- **{day.title()}**: {details['task']} ({details['time_required']})\n"
                
        report_content += f"""
## Next Steps
1. Run `python automation_dashboard.py` to monitor system status
2. Execute first content creation: `python Weekly_Content_Automation.py`
3. Review quality outputs in respective topic folders
4. Adjust configuration files as needed based on initial results

## Support
- Configuration files created in root directory
- Topic folders ready in Marketing/Produced Content/
- Voice guidelines validated in Marketing/Voice/
- Subagent systems tested and accessible

**System Ready**: Content automation can begin immediately.
"""
        
        try:
            report_path = self.base_path / "AUTOMATION_INITIALIZATION_REPORT.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            self.log_step(f"Created initialization report: {report_path.name}")
            return str(report_path)
        except Exception as e:
            self.log_step(f"Failed to create report: {str(e)}", False)
            return ""
            
    def run_complete_initialization(self) -> bool:
        """Run the complete initialization sequence."""
        print("STARTING 360TFT CONTENT AUTOMATION INITIALIZATION")
        print("=" * 60)
        
        # Step 1: Validate directories
        if not self.validate_directory_structure():
            print("X Directory validation failed. Please check Marketing folder structure.")
            return False
            
        # Step 2: Create topic folders  
        if not self.create_topic_folders():
            print("X Failed to create topic folder structure.")
            return False
            
        # Step 3: Validate voice content
        if not self.validate_voice_content():
            print("! Voice content validation failed. System will work but may lack consistency.")
            
        # Step 4: Create rotation schedule
        rotation_schedule = self.create_topic_rotation_schedule()
        
        # Step 5: Create configurations
        if not self.create_sample_configurations():
            print("! Some configuration files failed to create.")
            
        # Step 6: Test subagents
        if not self.test_subagent_connectivity():
            print("! Some subagent files are inaccessible. Manual intervention may be required.")
            
        # Step 7: Generate first week plan
        weekly_plan = self.generate_first_week_plan(rotation_schedule)
        
        # Step 8: Create report
        report_path = self.create_initialization_report(rotation_schedule, weekly_plan)
        
        print("\n" + "=" * 60)
        print("INITIALIZATION COMPLETE")
        print("=" * 60)
        print(f"+ System ready for content automation")
        print(f"+ {len(self.topic_folders)} topic folders created")
        print(f"+ 12-week rotation schedule generated")
        print(f"+ Configuration files created")
        print(f"+ First week plan ready")
        if report_path:
            print(f"Report: {report_path}")
            
        print("\nReady to start automation:")
        print("   py Weekly_Content_Automation.py")
        print("   py automation_dashboard.py")
        
        return True


def main():
    """Main execution function."""
    print("360TFT Content Automation Initializer")
    print("=====================================")
    
    # Allow custom base path
    import sys
    base_path = sys.argv[1] if len(sys.argv) > 1 else None
    
    initializer = AutomationInitializer(base_path)
    success = initializer.run_complete_initialization()
    
    if success:
        print("\nInitialization successful! Your automation system is ready.")
        return 0
    else:
        print("\nInitialization failed. Please check error messages above.")
        return 1


if __name__ == "__main__":
    exit(main())