#!/usr/bin/env python3
"""
360TFT Content Automation Dashboard
===================================

Real-time monitoring and analytics system for Kevin's content automation workflow.
Provides:
- Current automation status
- Weekly progress tracking  
- Quality scores and metrics
- Upcoming topics preview
- Performance analytics
- System health monitoring

Author: Kevin Middleton's Automation System
Created: 2025-08-01
"""

import os
import json
import datetime
import glob
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict
import time

class AutomationDashboard:
    def __init__(self, base_path: str = None):
        """Initialize dashboard with base directory path."""
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.marketing_path = self.base_path / "Marketing"
        self.produced_content_path = self.marketing_path / "Produced Content"
        
        # Load configuration if available
        self.config = self._load_config()
        
        # Topic folders for monitoring
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
        
        # Content format types
        self.content_formats = [
            "Blog_Post",
            "Email_Newsletter",
            "Newsletter", 
            "Twitter_Thread",
            "Tweet_Shortform",
            "Instagram_Caption",
            "LinkedIn_Post"
        ]
        
    def _load_config(self) -> Dict[str, Any]:
        """Load automation configuration."""
        config_files = [
            "automation_config.json",
            "content_templates.json", 
            "quality_standards.json",
            "automation_schedule.json"
        ]
        
        config_data = {}
        for config_file in config_files:
            config_path = self.base_path / config_file
            if config_path.exists():
                try:
                    with open(config_path, 'r', encoding='utf-8') as f:
                        file_config = json.load(f)
                        config_data[config_file.replace('.json', '')] = file_config
                except Exception as e:
                    print(f"Warning: Could not load {config_file}: {e}")
                    
        return config_data
        
    def get_system_status(self) -> Dict[str, Any]:
        """Get current system operational status."""
        status = {
            "timestamp": datetime.datetime.now().isoformat(),
            "system_health": "operational",
            "components": {},
            "alerts": []
        }
        
        # Check core components
        components = {
            "topic_folders": self._check_topic_folders(),
            "voice_guidelines": self._check_voice_guidelines(),
            "subagent_files": self._check_subagent_files(),
            "configuration": self._check_configuration(),
            "content_pipeline": self._check_content_pipeline()
        }
        
        status["components"] = components
        
        # Determine overall health
        healthy_components = sum(1 for comp in components.values() if comp["status"] == "healthy")
        total_components = len(components)
        
        if healthy_components == total_components:
            status["system_health"] = "optimal"
        elif healthy_components >= total_components * 0.8:
            status["system_health"] = "operational"
        elif healthy_components >= total_components * 0.6:
            status["system_health"] = "degraded"
        else:
            status["system_health"] = "critical"
            
        # Generate alerts for unhealthy components
        for name, component in components.items():
            if component["status"] != "healthy":
                status["alerts"].append({
                    "component": name,
                    "severity": "high" if component["status"] == "critical" else "medium",
                    "message": component.get("message", f"{name} requires attention")
                })
                
        return status
        
    def _check_topic_folders(self) -> Dict[str, Any]:
        """Check topic folder structure and content."""
        if not self.produced_content_path.exists():
            return {"status": "critical", "message": "Produced Content directory missing"}
            
        existing_folders = 0
        folder_content_counts = {}
        
        for topic in self.topic_folders:
            topic_path = self.produced_content_path / topic
            if topic_path.exists():
                existing_folders += 1
                # Count content files in this topic
                content_files = list(topic_path.glob("*.md"))
                folder_content_counts[topic] = len(content_files)
            else:
                folder_content_counts[topic] = 0
                
        total_content_files = sum(folder_content_counts.values())
        
        if existing_folders == len(self.topic_folders):
            status = "healthy"
            message = f"All {existing_folders} topic folders exist with {total_content_files} content files"
        elif existing_folders >= len(self.topic_folders) * 0.8:
            status = "operational"
            message = f"{existing_folders}/{len(self.topic_folders)} topic folders exist"
        else:
            status = "critical"
            message = f"Only {existing_folders}/{len(self.topic_folders)} topic folders exist"
            
        return {
            "status": status,
            "message": message,
            "details": {
                "folders_existing": existing_folders,
                "folders_total": len(self.topic_folders),
                "content_files_total": total_content_files,
                "folder_content_counts": folder_content_counts
            }
        }
        
    def _check_voice_guidelines(self) -> Dict[str, Any]:
        """Check voice guidelines availability and quality."""
        voice_path = self.marketing_path / "Voice" / "Voice"
        
        if not voice_path.exists():
            return {
                "status": "critical",
                "message": "Voice guidelines file not found",
                "details": {"file_path": str(voice_path)}
            }
            
        try:
            with open(voice_path, 'r', encoding='utf-8') as f:
                voice_content = f.read()
                
            # Check for key voice elements
            key_elements = [
                "football coach", "15+ years", "british english", 
                "seth godin", "no em dashes", "1,000", "360tft"
            ]
            
            found_elements = [elem for elem in key_elements 
                            if elem.lower() in voice_content.lower()]
            
            element_coverage = len(found_elements) / len(key_elements)
            
            if element_coverage >= 0.8:
                status = "healthy"
                message = f"Voice guidelines complete ({len(found_elements)}/{len(key_elements)} elements)"
            elif element_coverage >= 0.6:
                status = "operational"
                message = f"Voice guidelines partial ({len(found_elements)}/{len(key_elements)} elements)"
            else:
                status = "degraded"
                message = f"Voice guidelines incomplete ({len(found_elements)}/{len(key_elements)} elements)"
                
            return {
                "status": status,
                "message": message,
                "details": {
                    "file_size": len(voice_content),
                    "elements_found": found_elements,
                    "elements_coverage": element_coverage
                }
            }
            
        except Exception as e:
            return {
                "status": "critical",
                "message": f"Cannot read voice guidelines: {str(e)}",
                "details": {"error": str(e)}
            }
            
    def _check_subagent_files(self) -> Dict[str, Any]:
        """Check subagent file accessibility."""
        subagent_files = [
            "Weekly_Content_Automation.py",
            "Subagent_Orchestrator.py",
            "Topic_Selection_Manager.py", 
            "Quality_Control_System.py"
        ]
        
        file_status = {}
        accessible_count = 0
        
        for subagent_file in subagent_files:
            file_path = self.base_path / subagent_file
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if len(content) > 100:
                            file_status[subagent_file] = "accessible"
                            accessible_count += 1
                        else:
                            file_status[subagent_file] = "empty"
                except Exception:
                    file_status[subagent_file] = "unreadable"
            else:
                file_status[subagent_file] = "missing"
                
        if accessible_count == len(subagent_files):
            status = "healthy"
            message = f"All {accessible_count} subagent files accessible"
        elif accessible_count >= len(subagent_files) * 0.75:
            status = "operational"
            message = f"{accessible_count}/{len(subagent_files)} subagent files accessible"
        else:
            status = "critical"
            message = f"Only {accessible_count}/{len(subagent_files)} subagent files accessible"
            
        return {
            "status": status,
            "message": message,
            "details": {
                "file_statuses": file_status,
                "accessible_count": accessible_count,
                "total_count": len(subagent_files)
            }
        }
        
    def _check_configuration(self) -> Dict[str, Any]:
        """Check configuration file completeness."""
        required_configs = [
            "automation_config.json",
            "content_templates.json",
            "quality_standards.json",
            "automation_schedule.json"
        ]
        
        config_status = {}
        valid_count = 0
        
        for config_file in required_configs:
            config_path = self.base_path / config_file
            if config_path.exists():
                try:
                    with open(config_path, 'r', encoding='utf-8') as f:
                        config_data = json.load(f)
                        if config_data:  # Not empty
                            config_status[config_file] = "valid"
                            valid_count += 1
                        else:
                            config_status[config_file] = "empty"
                except Exception:
                    config_status[config_file] = "invalid"
            else:
                config_status[config_file] = "missing"
                
        if valid_count == len(required_configs):
            status = "healthy"
            message = f"All {valid_count} configuration files valid"
        elif valid_count >= len(required_configs) * 0.75:
            status = "operational"
            message = f"{valid_count}/{len(required_configs)} configuration files valid"
        else:
            status = "degraded"
            message = f"Only {valid_count}/{len(required_configs)} configuration files valid"
            
        return {
            "status": status,
            "message": message,
            "details": {
                "config_statuses": config_status,
                "valid_count": valid_count,
                "total_count": len(required_configs)
            }
        }
        
    def _check_content_pipeline(self) -> Dict[str, Any]:
        """Check content creation pipeline status.""" 
        # Check for recent content creation activity
        recent_files = []
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=7)
        
        if self.produced_content_path.exists():
            try:
                for topic_folder in self.topic_folders:
                    topic_path = self.produced_content_path / topic_folder
                    if topic_path.exists():
                        for content_file in topic_path.glob("*.md"):
                            try:
                                file_mtime = datetime.datetime.fromtimestamp(content_file.stat().st_mtime)
                                if file_mtime >= cutoff_date:
                                    recent_files.append({
                                        "file": content_file.name,
                                        "topic": topic_folder,
                                        "modified": file_mtime.isoformat()
                                    })
                            except Exception:
                                pass  # Skip files we can't read stats for
                                
                recent_count = len(recent_files)
                
                if recent_count >= 5:  # At least 5 files in past week
                    status = "healthy"
                    message = f"Active pipeline with {recent_count} recent content files"
                elif recent_count >= 1:
                    status = "operational"
                    message = f"Some activity with {recent_count} recent content files"
                else:
                    status = "degraded"
                    message = "No recent content creation activity"
                    
            except Exception as e:
                status = "critical"
                message = f"Cannot analyze content pipeline: {str(e)}"
                recent_files = []
                
        else:
            status = "critical"
            message = "Content directory does not exist"
            recent_files = []
            
        return {
            "status": status,
            "message": message,
            "details": {
                "recent_files_count": len(recent_files),
                "recent_files": recent_files[:10]  # Show first 10
            }
        }
        
    def get_weekly_progress(self) -> Dict[str, Any]:
        """Get current week's content creation progress."""
        current_week_start = datetime.datetime.now() - datetime.timedelta(
            days=datetime.datetime.now().weekday()
        )
        
        progress = {
            "week_start": current_week_start.strftime("%Y-%m-%d"),
            "current_topic": self._get_current_topic(),
            "daily_progress": {},
            "completion_percentage": 0,
            "content_created": 0,
            "content_planned": 0
        }
        
        # Define daily schedule
        daily_schedule = {
            "monday": {"task": "Blog Post Creation", "formats": ["Blog_Post"]},
            "tuesday": {"task": "Email Newsletter", "formats": ["Email_Newsletter"]},
            "wednesday": {"task": "Social Media Suite", "formats": ["Twitter_Thread", "Instagram_Caption", "LinkedIn_Post"]},
            "thursday": {"task": "Short-form Content", "formats": ["Tweet_Shortform"]},
            "friday": {"task": "Visual Content", "formats": ["Cheatsheet", "Infographic"]},
            "saturday": {"task": "Quality Control", "formats": []},
            "sunday": {"task": "Next Week Planning", "formats": []}
        }
        
        current_topic = progress["current_topic"]
        if current_topic and self.produced_content_path.exists():
            topic_path = self.produced_content_path / current_topic
            
            total_planned = sum(len(day_info["formats"]) for day_info in daily_schedule.values())
            content_created = 0
            
            # Check each day's progress
            for day, day_info in daily_schedule.items():
                day_progress = {
                    "task": day_info["task"],
                    "planned_formats": day_info["formats"],
                    "completed_formats": [],
                    "completion_status": "pending"
                }
                
                if topic_path.exists():
                    for format_type in day_info["formats"]:
                        # Look for files matching this format
                        format_files = list(topic_path.glob(f"{format_type}*.md"))
                        if format_files:
                            day_progress["completed_formats"].append(format_type)
                            content_created += 1
                            
                # Determine completion status
                if len(day_progress["completed_formats"]) == len(day_progress["planned_formats"]):
                    if len(day_progress["planned_formats"]) > 0:
                        day_progress["completion_status"] = "completed"
                    else:
                        day_progress["completion_status"] = "not_applicable"
                elif len(day_progress["completed_formats"]) > 0:
                    day_progress["completion_status"] = "partial"
                else:
                    day_progress["completion_status"] = "pending"
                    
                progress["daily_progress"][day] = day_progress
                
            progress["content_created"] = content_created
            progress["content_planned"] = total_planned
            progress["completion_percentage"] = (content_created / total_planned * 100) if total_planned > 0 else 0
            
        return progress
        
    def _get_current_topic(self) -> Optional[str]:
        """Determine current week's topic based on rotation schedule."""
        # Try to load rotation schedule
        schedule_file = self.base_path / "topic_rotation_schedule.json"
        if schedule_file.exists():
            try:
                with open(schedule_file, 'r', encoding='utf-8') as f:
                    schedule_data = json.load(f)
                    
                current_date = datetime.datetime.now().date()
                
                # Find current week's topic
                for week_data in schedule_data.get("rotation_schedule", []):
                    week_start = datetime.datetime.strptime(week_data["start_date"], "%Y-%m-%d").date()
                    week_end = week_start + datetime.timedelta(days=6)
                    
                    if week_start <= current_date <= week_end:
                        return week_data["topic"]
                        
            except Exception:
                pass  # Fall back to heuristic
                
        # Fallback: use most recently modified topic folder
        if self.produced_content_path.exists():
            most_recent_topic = None
            most_recent_time = 0
            
            for topic in self.topic_folders:
                topic_path = self.produced_content_path / topic
                if topic_path.exists():
                    try:
                        topic_mtime = topic_path.stat().st_mtime
                        if topic_mtime > most_recent_time:
                            most_recent_time = topic_mtime
                            most_recent_topic = topic
                    except Exception:
                        pass
                        
            return most_recent_topic
            
        return None
        
    def get_quality_scores(self) -> Dict[str, Any]:
        """Calculate quality scores for recent content."""
        scores = {
            "overall_score": 0,
            "voice_consistency": 0,
            "british_english_compliance": 0,
            "value_equation_average": 0,
            "brand_integration": 0,
            "content_analysis": [],
            "recommendations": []
        }
        
        # Analyze recent content files
        analyzed_files = 0
        total_scores = {"voice": 0, "british": 0, "value": 0, "brand": 0}
        
        if self.produced_content_path.exists():
            for topic_folder in self.topic_folders:
                topic_path = self.produced_content_path / topic_folder
                if topic_path.exists():
                    for content_file in topic_path.glob("*.md"):
                        try:
                            file_scores = self._analyze_content_quality(content_file)
                            if file_scores:
                                scores["content_analysis"].append({
                                    "file": content_file.name,
                                    "topic": topic_folder,
                                    "scores": file_scores
                                })
                                
                                # Add to totals
                                for key in total_scores:
                                    total_scores[key] += file_scores.get(key, 0)
                                analyzed_files += 1
                                
                        except Exception:
                            pass  # Skip files we can't analyze
                            
        # Calculate averages
        if analyzed_files > 0:
            scores["voice_consistency"] = total_scores["voice"] / analyzed_files
            scores["british_english_compliance"] = total_scores["british"] / analyzed_files  
            scores["value_equation_average"] = total_scores["value"] / analyzed_files
            scores["brand_integration"] = total_scores["brand"] / analyzed_files
            
            scores["overall_score"] = (
                scores["voice_consistency"] + 
                scores["british_english_compliance"] + 
                scores["value_equation_average"] + 
                scores["brand_integration"]
            ) / 4
            
        # Generate recommendations
        if scores["voice_consistency"] < 80:
            scores["recommendations"].append("Review voice guidelines and ensure consistent tone")
        if scores["british_english_compliance"] < 90:
            scores["recommendations"].append("Check spelling: use colour, favourite, realise, football")
        if scores["value_equation_average"] < 35:
            scores["recommendations"].append("Increase value proposition and practical benefits")
        if scores["brand_integration"] < 70:
            scores["recommendations"].append("Include more 360TFT academy references and CTAs")
            
        scores["files_analyzed"] = analyzed_files
        return scores
        
    def _analyze_content_quality(self, file_path: Path) -> Optional[Dict[str, float]]:
        """Analyze quality of a single content file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                
            scores = {}
            
            # Voice consistency (check for key elements)
            voice_elements = ["football", "coach", "player", "session", "training"]
            voice_found = sum(1 for elem in voice_elements if elem in content)
            scores["voice"] = (voice_found / len(voice_elements)) * 100
            
            # British English compliance
            british_words = ["colour", "favourite", "realise", "centre", "defence"]
            american_words = ["color", "favorite", "realize", "center", "defense"]
            
            british_found = sum(1 for word in british_words if word in content)
            american_found = sum(1 for word in american_words if word in content)
            
            if british_found + american_found > 0:
                scores["british"] = (british_found / (british_found + american_found)) * 100
            else:
                scores["british"] = 100  # No relevant words found, assume compliant
                
            # Value equation elements
            value_elements = ["improve", "better", "develop", "effective", "results"]
            value_found = sum(1 for elem in value_elements if elem in content)
            scores["value"] = min((value_found / len(value_elements)) * 100, 100)
            
            # Brand integration
            brand_elements = ["360tft", "kevin middleton", "academy", "coach", "community"]
            brand_found = sum(1 for elem in brand_elements if elem in content)
            scores["brand"] = (brand_found / len(brand_elements)) * 100
            
            return scores
            
        except Exception:
            return None
            
    def get_upcoming_topics(self, weeks: int = 4) -> List[Dict[str, Any]]:
        """Get upcoming topic schedule."""
        upcoming = []
        
        # Try to load rotation schedule
        schedule_file = self.base_path / "topic_rotation_schedule.json"
        if schedule_file.exists():
            try:
                with open(schedule_file, 'r', encoding='utf-8') as f:
                    schedule_data = json.load(f)
                    
                current_date = datetime.datetime.now().date()
                
                for week_data in schedule_data.get("rotation_schedule", []):
                    week_start = datetime.datetime.strptime(week_data["start_date"], "%Y-%m-%d").date()
                    
                    if week_start >= current_date and len(upcoming) < weeks:
                        upcoming.append({
                            "week": week_data.get("week", ""),
                            "start_date": week_data["start_date"],
                            "topic": week_data["topic"],
                            "content_focus": week_data.get("content_focus", ""),
                            "days_until": (week_start - current_date).days
                        })
                        
            except Exception:
                pass  # Fall back to default schedule
                
        # Fallback: create a simple upcoming schedule
        if not upcoming:
            current_topic_index = 0
            if hasattr(self, '_current_topic_index'):
                current_topic_index = self._current_topic_index
                
            for i in range(weeks):
                topic_index = (current_topic_index + i) % len(self.topic_folders)
                week_start = datetime.datetime.now().date() + datetime.timedelta(weeks=i)
                
                upcoming.append({
                    "week": i + 1,
                    "start_date": week_start.strftime("%Y-%m-%d"),
                    "topic": self.topic_folders[topic_index],
                    "content_focus": "Content creation and marketing",
                    "days_until": i * 7
                })
                
        return upcoming
        
    def get_performance_analytics(self) -> Dict[str, Any]:
        """Get performance analytics and trends."""
        analytics = {
            "content_production": {
                "total_files": 0,
                "files_by_format": defaultdict(int),
                "files_by_topic": defaultdict(int),
                "recent_activity": []
            },
            "quality_trends": {
                "average_scores": [],
                "improvement_areas": []
            },
            "system_usage": {
                "automation_runs": 0,
                "success_rate": 0,
                "last_run": None
            }
        }
        
        if self.produced_content_path.exists():
            # Analyze all content files
            for topic_folder in self.topic_folders:
                topic_path = self.produced_content_path / topic_folder
                if topic_path.exists():
                    topic_files = list(topic_path.glob("*.md"))
                    analytics["content_production"]["files_by_topic"][topic_folder] = len(topic_files)
                    analytics["content_production"]["total_files"] += len(topic_files)
                    
                    # Categorize by format
                    for content_file in topic_files:
                        file_name = content_file.name
                        for format_type in self.content_formats:
                            if format_type.lower() in file_name.lower():
                                analytics["content_production"]["files_by_format"][format_type] += 1
                                break
                        else:
                            analytics["content_production"]["files_by_format"]["Other"] += 1
                            
                        # Track recent activity (last 30 days)
                        try:
                            file_mtime = datetime.datetime.fromtimestamp(content_file.stat().st_mtime)
                            if file_mtime >= datetime.datetime.now() - datetime.timedelta(days=30):
                                analytics["content_production"]["recent_activity"].append({
                                    "file": file_name,
                                    "topic": topic_folder,
                                    "created": file_mtime.strftime("%Y-%m-%d %H:%M")
                                })
                        except Exception:
                            pass
                            
        # Sort recent activity by date
        analytics["content_production"]["recent_activity"].sort(
            key=lambda x: x["created"], reverse=True
        )
        
        # Convert defaultdicts to regular dicts for JSON serialization
        analytics["content_production"]["files_by_format"] = dict(analytics["content_production"]["files_by_format"])
        analytics["content_production"]["files_by_topic"] = dict(analytics["content_production"]["files_by_topic"])
        
        return analytics
        
    def display_dashboard(self):
        """Display the complete dashboard in terminal."""
        print("=" * 80)
        print("360TFT CONTENT AUTOMATION DASHBOARD")
        print("=" * 80)
        print(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # System Status
        print("SYSTEM STATUS")
        print("-" * 40)
        status = self.get_system_status()
        
        health_status = {
            "optimal": "[OPTIMAL]",
            "operational": "[OPERATIONAL]", 
            "degraded": "[DEGRADED]",
            "critical": "[CRITICAL]"
        }
        
        print(f"Overall Health: {health_status.get(status['system_health'], '[UNKNOWN]')} {status['system_health'].upper()}")
        
        for component, details in status["components"].items():
            status_indicator = "[OK]" if details["status"] == "healthy" else "[WARN]" if details["status"] == "operational" else "[ERROR]"
            print(f"{status_indicator} {component.replace('_', ' ').title()}: {details['message']}")
            
        if status["alerts"]:
            print("\nALERTS:")
            for alert in status["alerts"]:
                severity_indicator = "[HIGH]" if alert["severity"] == "high" else "[MED]"
                print(f"  {severity_indicator} {alert['component']}: {alert['message']}")
                
        print()
        
        # Weekly Progress
        print("CURRENT WEEK PROGRESS")
        print("-" * 40)
        progress = self.get_weekly_progress()
        
        if progress["current_topic"]:
            topic_display = progress["current_topic"].replace("_", " ")
            print(f"Current Topic: {topic_display}")
            print(f"Week Starting: {progress['week_start']}")
            print(f"Completion: {progress['completion_percentage']:.1f}% ({progress['content_created']}/{progress['content_planned']} pieces)")
            print()
            
            for day, day_info in progress["daily_progress"].items():
                status_indicator = {
                    "completed": "[DONE]",
                    "partial": "[PARTIAL]", 
                    "pending": "[PENDING]",
                    "not_applicable": "[N/A]"
                }.get(day_info["completion_status"], "[?]")
                
                print(f"  {status_indicator} {day.title()}: {day_info['task']}")
                if day_info["completed_formats"]:
                    print(f"    Completed: {', '.join(day_info['completed_formats'])}")
        else:
            print("No current topic identified. Run initialization to set up rotation schedule.")
            
        print()
        
        # Quality Scores
        print("QUALITY METRICS")
        print("-" * 40)
        quality = self.get_quality_scores()
        
        if quality["files_analyzed"] > 0:
            print(f"Overall Score: {quality['overall_score']:.1f}/100 (based on {quality['files_analyzed']} files)")
            print(f"- Voice Consistency: {quality['voice_consistency']:.1f}/100")
            print(f"- British English: {quality['british_english_compliance']:.1f}/100")
            print(f"- Value Equation: {quality['value_equation_average']:.1f}/100") 
            print(f"- Brand Integration: {quality['brand_integration']:.1f}/100")
            
            if quality["recommendations"]:
                print("\nRECOMMENDATIONS:")
                for rec in quality["recommendations"]:
                    print(f"  > {rec}")
        else:
            print("No content files found for quality analysis.")
            
        print()
        
        # Upcoming Topics
        print("UPCOMING TOPICS")
        print("-" * 40)
        upcoming = self.get_upcoming_topics(4)
        
        for topic_info in upcoming:
            days_text = "today" if topic_info["days_until"] == 0 else f"in {topic_info['days_until']} days"
            topic_display = topic_info["topic"].replace("_", " ")
            print(f"Week {topic_info['week']}: {topic_display} ({days_text})")
            if topic_info.get("content_focus"):
                print(f"  Focus: {topic_info['content_focus']}")
                
        print()
        
        # Performance Analytics
        print("PERFORMANCE ANALYTICS")
        print("-" * 40)
        analytics = self.get_performance_analytics()
        
        production = analytics["content_production"]
        print(f"Total Content Files: {production['total_files']}")
        
        if production["files_by_format"]:
            print("By Format:")
            for format_type, count in sorted(production["files_by_format"].items(), key=lambda x: x[1], reverse=True):
                print(f"  - {format_type}: {count}")
                
        if production["recent_activity"]:
            print(f"\nRecent Activity ({len(production['recent_activity'])} files in last 30 days):")
            for activity in production["recent_activity"][:5]:  # Show top 5
                topic_short = activity["topic"].replace("_", " ")[:30] + "..." if len(activity["topic"]) > 30 else activity["topic"].replace("_", " ")
                print(f"  - {activity['created']}: {activity['file']} ({topic_short})")
                
        print()
        
        # Quick Actions
        print("QUICK ACTIONS")
        print("-" * 40)
        print("Start content creation: py Weekly_Content_Automation.py")
        print("Re-initialize system: py initialize_automation.py")
        print("View this dashboard: py automation_dashboard.py")
        print("Run quality check: py Quality_Control_System.py")
        
        print("\n" + "=" * 80)
        
    def export_status_report(self, filename: str = None) -> str:
        """Export comprehensive status report to file."""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"automation_status_report_{timestamp}.json"
            
        report_data = {
            "generated_at": datetime.datetime.now().isoformat(),
            "system_status": self.get_system_status(),
            "weekly_progress": self.get_weekly_progress(),
            "quality_scores": self.get_quality_scores(),
            "upcoming_topics": self.get_upcoming_topics(8),
            "performance_analytics": self.get_performance_analytics()
        }
        
        report_path = self.base_path / filename
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            return str(report_path)
        except Exception as e:
            print(f"Failed to export report: {e}")
            return ""


def main():
    """Main execution function."""
    import sys
    
    # Allow custom base path
    base_path = sys.argv[1] if len(sys.argv) > 1 else None
    
    dashboard = AutomationDashboard(base_path)
    
    # Check for command line options
    if len(sys.argv) > 1 and sys.argv[-1] in ["--export", "-e"]:
        report_path = dashboard.export_status_report()
        if report_path:
            print(f"Status report exported to: {report_path}")
        else:
            print("Failed to export status report")
    else:
        # Display interactive dashboard
        dashboard.display_dashboard()
        
        # Offer export option
        try:
            export_choice = input("\nExport detailed report? (y/N): ").strip().lower()
            if export_choice in ['y', 'yes']:
                report_path = dashboard.export_status_report()
                if report_path:
                    print(f"[OK] Report exported to: {report_path}")
        except (KeyboardInterrupt, EOFError):
            print("\nDashboard closed.")


if __name__ == "__main__":
    main()