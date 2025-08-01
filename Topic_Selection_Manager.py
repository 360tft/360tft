#!/usr/bin/env python3
"""
360TFT Topic Selection Manager
=============================

Manages the 27-topic pool from Marketing folders, implements 12-week rotation cycles,
prevents topic repetition, adapts for seasonal content, and tracks topic performance.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import json
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import random


class TopicSelectionManager:
    """
    Manages topic selection for 360TFT weekly content automation.
    
    Handles the 27-topic rotation cycle, prevents repetition within cycles,
    adapts for seasonal content, and tracks performance metrics.
    """
    
    def __init__(self, marketing_path: Path):
        """
        Initialize the Topic Selection Manager.
        
        Args:
            marketing_path: Path to Marketing folder
        """
        self.marketing_path = Path(marketing_path)
        self.data_path = Path(__file__).parent / "topic_data"
        self.data_path.mkdir(exist_ok=True)
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Load topic pools from Marketing folders
        self.topic_pools = self._load_topic_pools()
        
        # Load rotation history and performance data
        self.rotation_history = self._load_rotation_history()
        self.performance_data = self._load_performance_data()
        
        # Configuration
        self.config = {
            "cycle_length_weeks": 12,
            "min_gap_between_repeats": 4,
            "seasonal_boost_factor": 1.5,
            "performance_weight": 0.3
        }
        
        self.logger.info(f"Topic Selection Manager initialized with {len(self.topic_pools['all_topics'])} topics")
    
    def _load_topic_pools(self) -> Dict[str, List[Dict]]:
        """Load all available topics from Marketing folder structure."""
        topic_pools = {
            "blog_topics": [],
            "email_topics": [],
            "specialized_topics": [],
            "cheatsheet_topics": [],
            "all_topics": []
        }
        
        # Load Blog Topics
        blogs_path = self.marketing_path / "Blogs"
        if blogs_path.exists():
            for blog_folder in blogs_path.iterdir():
                if blog_folder.is_dir():
                    topic = {
                        "title": blog_folder.name,
                        "type": "blog",
                        "source_path": str(blog_folder),
                        "category": "foundational",
                        "complexity": "medium",
                        "target_audience": ["grassroots", "academy", "parent_coaches"]
                    }
                    topic_pools["blog_topics"].append(topic)
                    topic_pools["all_topics"].append(topic)
        
        # Load Email Topics
        emails_path = self.marketing_path / "Emails"
        if emails_path.exists():
            for email_folder in emails_path.iterdir():
                if email_folder.is_dir():
                    topic = {
                        "title": email_folder.name,
                        "type": "email",
                        "source_path": str(email_folder),
                        "category": "engagement",
                        "complexity": "simple",
                        "target_audience": ["grassroots", "parent_coaches"]
                    }
                    topic_pools["email_topics"].append(topic)
                    topic_pools["all_topics"].append(topic)
        
        # Load Specialized Program Topics
        specialized_folders = [
            "The Game Model",
            "The Striker Clinic", 
            "Elite Ball Mastery and 1v1",
            "How To Analyse  A Match",
            "UEFA C"
        ]
        
        for folder_name in specialized_folders:
            folder_path = self.marketing_path / folder_name
            if folder_path.exists():
                for subfolder in folder_path.iterdir():
                    if subfolder.is_dir():
                        topic = {
                            "title": f"{folder_name} - {subfolder.name}",
                            "type": "specialized",
                            "source_path": str(subfolder),
                            "category": "advanced",
                            "complexity": "high",
                            "target_audience": ["academy", "professional"]
                        }
                        topic_pools["specialized_topics"].append(topic)
                        topic_pools["all_topics"].append(topic)
        
        # Load existing cheat sheet topics for reference
        cheatsheets_path = self.marketing_path / "Cheatsheets"
        if cheatsheets_path.exists():
            for file in cheatsheets_path.iterdir():
                if file.suffix in ['.html', '.pdf']:
                    topic_name = file.stem.replace('_A4', '').replace('_', ' ')
                    topic = {
                        "title": topic_name,
                        "type": "cheatsheet",
                        "source_path": str(file),
                        "category": "practical",
                        "complexity": "simple",
                        "target_audience": ["grassroots", "academy", "parent_coaches"]
                    }
                    topic_pools["cheatsheet_topics"].append(topic)
                    # Don't add to all_topics to avoid duplication
        
        # Add seasonal adaptation topics
        seasonal_topics = self._get_seasonal_topics()
        topic_pools["all_topics"].extend(seasonal_topics)
        
        self.logger.info(f"Loaded topic pools: {len(topic_pools['blog_topics'])} blog, "
                        f"{len(topic_pools['email_topics'])} email, "
                        f"{len(topic_pools['specialized_topics'])} specialized topics")
        
        return topic_pools
    
    def _get_seasonal_topics(self) -> List[Dict]:
        """Generate seasonal topic variations."""
        seasonal_topics = []
        
        # Pre-season topics (July-August)
        pre_season = {
            "title": "Pre-Season Preparation Masterclass",
            "type": "seasonal",
            "category": "seasonal",
            "complexity": "medium",
            "season": "pre_season",
            "months": [7, 8],
            "target_audience": ["grassroots", "academy"]
        }
        seasonal_topics.append(pre_season)
        
        # In-season topics (September-April)
        in_season = {
            "title": "Mid-Season Player Development Focus",
            "type": "seasonal", 
            "category": "seasonal",
            "complexity": "medium",
            "season": "in_season",
            "months": [9, 10, 11, 12, 1, 2, 3, 4],
            "target_audience": ["grassroots", "academy"]
        }
        seasonal_topics.append(in_season)
        
        # End of season topics (May-June)
        end_season = {
            "title": "Season Review and Summer Planning",
            "type": "seasonal",
            "category": "seasonal", 
            "complexity": "medium",
            "season": "end_season",
            "months": [5, 6],
            "target_audience": ["grassroots", "academy", "parent_coaches"]
        }
        seasonal_topics.append(end_season)
        
        return seasonal_topics
    
    def _load_rotation_history(self) -> Dict:
        """Load topic rotation history."""
        history_file = self.data_path / "rotation_history.json"
        
        if history_file.exists():
            with open(history_file, 'r') as f:
                return json.load(f)
        
        # Initialize new history
        return {
            "current_cycle": 1,
            "cycle_start_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "used_topics_this_cycle": [],
            "last_used_dates": {},
            "cycle_history": []
        }
    
    def _load_performance_data(self) -> Dict:
        """Load topic performance tracking data."""
        performance_file = self.data_path / "performance_data.json"
        
        if performance_file.exists():
            with open(performance_file, 'r') as f:
                return json.load(f)
        
        # Initialize performance tracking
        return {
            "topic_scores": {},
            "engagement_metrics": {},  
            "conversion_metrics": {},
            "quality_scores": {},
            "last_updated": datetime.datetime.now().strftime('%Y-%m-%d')
        }
    
    def _save_rotation_history(self):
        """Save rotation history to file."""
        history_file = self.data_path / "rotation_history.json"
        with open(history_file, 'w') as f:
            json.dump(self.rotation_history, f, indent=2)
    
    def _save_performance_data(self):
        """Save performance data to file."""
        performance_file = self.data_path / "performance_data.json"
        with open(performance_file, 'w') as f:
            json.dump(self.performance_data, f, indent=2)
    
    def select_weekly_topic(self) -> str:
        """
        Select the optimal topic for this week based on rotation cycle,
        performance data, and seasonal relevance.
        
        Returns:
            Selected topic title
        """
        self.logger.info("Starting weekly topic selection")
        
        # Check if we need to start a new cycle
        if len(self.rotation_history["used_topics_this_cycle"]) >= self.config["cycle_length_weeks"]:
            self._start_new_cycle()
        
        # Get candidate topics
        candidate_topics = self._get_candidate_topics()
        
        # Score topics based on various factors
        scored_topics = self._score_topics(candidate_topics)
        
        # Select best topic
        selected_topic = self._select_best_topic(scored_topics)
        
        # Update rotation history
        self._update_rotation_history(selected_topic)
        
        self.logger.info(f"Selected topic for week: {selected_topic}")
        return selected_topic
    
    def _get_candidate_topics(self) -> List[Dict]:
        """Get topics that are eligible for selection."""
        current_month = datetime.datetime.now().month
        used_this_cycle = set(self.rotation_history["used_topics_this_cycle"])
        
        candidates = []
        
        for topic in self.topic_pools["all_topics"]:
            # Skip if used in current cycle
            if topic["title"] in used_this_cycle:
                continue
            
            # Check if topic was used too recently
            last_used = self.rotation_history["last_used_dates"].get(topic["title"])
            if last_used:
                last_used_date = datetime.datetime.strptime(last_used, '%Y-%m-%d')
                weeks_since_used = (datetime.datetime.now() - last_used_date).days / 7
                if weeks_since_used < self.config["min_gap_between_repeats"]:
                    continue
            
            # Add seasonal relevance check
            if topic.get("type") == "seasonal":
                if "months" in topic and current_month not in topic["months"]:
                    continue
            
            candidates.append(topic)
        
        self.logger.info(f"Found {len(candidates)} candidate topics")
        return candidates
    
    def _score_topics(self, topics: List[Dict]) -> List[Tuple[Dict, float]]:
        """Score topics based on multiple factors."""
        scored_topics = []
        current_month = datetime.datetime.now().month
        
        for topic in topics:
            score = 0.0
            
            # Base score
            score += 1.0
            
            # Seasonal boost
            if topic.get("type") == "seasonal":
                if "months" in topic and current_month in topic["months"]:
                    score += self.config["seasonal_boost_factor"]
            
            # Performance score (if available)
            topic_title = topic["title"]
            if topic_title in self.performance_data["topic_scores"]:
                performance_score = self.performance_data["topic_scores"][topic_title]
                score += performance_score * self.config["performance_weight"]
            
            # Complexity balance (prefer variety)
            complexity_bonus = {
                "simple": 0.8,
                "medium": 1.0, 
                "high": 0.6
            }
            score += complexity_bonus.get(topic.get("complexity", "medium"), 1.0)
            
            # Category variety bonus
            used_categories = [
                self._get_topic_by_title(used_title).get("category", "unknown")
                for used_title in self.rotation_history["used_topics_this_cycle"][-3:]  # Last 3 topics
            ]
            
            if topic.get("category") not in used_categories:
                score += 0.5
            
            # Audience diversity bonus
            target_audiences = topic.get("target_audience", [])
            audience_score = len(target_audiences) * 0.1
            score += audience_score
            
            scored_topics.append((topic, score))
        
        # Sort by score (highest first)
        scored_topics.sort(key=lambda x: x[1], reverse=True)
        
        return scored_topics
    
    def _select_best_topic(self, scored_topics: List[Tuple[Dict, float]]) -> str:
        """Select the best topic from scored candidates."""
        if not scored_topics:
            # Fallback: select any unused topic
            all_titles = [topic["title"] for topic in self.topic_pools["all_topics"]]
            used_this_cycle = set(self.rotation_history["used_topics_this_cycle"])
            unused = [title for title in all_titles if title not in used_this_cycle]
            
            if unused:
                return random.choice(unused)
            else:
                # Start new cycle if all topics used
                self._start_new_cycle()
                return random.choice(all_titles)
        
        # Select from top 3 scored topics with some randomization
        top_candidates = scored_topics[:min(3, len(scored_topics))]
        weights = [score for _, score in top_candidates]
        
        # Weighted random selection
        total_weight = sum(weights)
        if total_weight > 0:
            rand_val = random.uniform(0, total_weight)
            current_weight = 0
            
            for topic, weight in top_candidates:
                current_weight += weight
                if rand_val <= current_weight:
                    return topic["title"]
        
        # Fallback to highest scored
        return scored_topics[0][0]["title"]
    
    def _update_rotation_history(self, selected_topic: str):
        """Update rotation history with selected topic."""
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        
        # Add to current cycle
        self.rotation_history["used_topics_this_cycle"].append(selected_topic)
        
        # Update last used date
        self.rotation_history["last_used_dates"][selected_topic] = current_date
        
        # Save history
        self._save_rotation_history()
    
    def _start_new_cycle(self):
        """Start a new rotation cycle."""
        # Archive current cycle
        cycle_data = {
            "cycle_number": self.rotation_history["current_cycle"],
            "start_date": self.rotation_history["cycle_start_date"],
            "end_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "topics_used": self.rotation_history["used_topics_this_cycle"].copy()
        }
        
        if "cycle_history" not in self.rotation_history:
            self.rotation_history["cycle_history"] = []
        
        self.rotation_history["cycle_history"].append(cycle_data)
        
        # Start new cycle
        self.rotation_history["current_cycle"] += 1
        self.rotation_history["cycle_start_date"] = datetime.datetime.now().strftime('%Y-%m-%d')
        self.rotation_history["used_topics_this_cycle"] = []
        
        self.logger.info(f"Started new rotation cycle #{self.rotation_history['current_cycle']}")
    
    def _get_topic_by_title(self, title: str) -> Dict:
        """Get topic data by title."""
        for topic in self.topic_pools["all_topics"]:
            if topic["title"] == title:
                return topic
        return {}
    
    def update_topic_performance(self, topic_title: str, metrics: Dict):
        """
        Update performance metrics for a topic.
        
        Args:
            topic_title: Title of the topic
            metrics: Dictionary containing performance metrics
        """
        # Calculate composite score
        engagement_weight = 0.4
        conversion_weight = 0.4
        quality_weight = 0.2
        
        engagement_score = metrics.get("engagement_score", 0.5)  # 0-1 scale
        conversion_score = metrics.get("conversion_score", 0.5)   # 0-1 scale  
        quality_score = metrics.get("quality_score", 0.5)        # 0-1 scale
        
        composite_score = (
            engagement_score * engagement_weight +
            conversion_score * conversion_weight +
            quality_score * quality_weight
        )
        
        # Update performance data
        self.performance_data["topic_scores"][topic_title] = composite_score
        self.performance_data["engagement_metrics"][topic_title] = engagement_score
        self.performance_data["conversion_metrics"][topic_title] = conversion_score
        self.performance_data["quality_scores"][topic_title] = quality_score
        self.performance_data["last_updated"] = datetime.datetime.now().strftime('%Y-%m-%d')
        
        # Save performance data
        self._save_performance_data()
        
        self.logger.info(f"Updated performance for {topic_title}: {composite_score:.2f}")
    
    def get_topic_suggestions(self, category: Optional[str] = None, 
                            complexity: Optional[str] = None) -> List[Dict]:
        """
        Get topic suggestions based on filters.
        
        Args:
            category: Filter by category (foundational, engagement, advanced, etc.)
            complexity: Filter by complexity (simple, medium, high)
            
        Returns:
            List of matching topics
        """
        suggestions = []
        
        for topic in self.topic_pools["all_topics"]:
            # Apply filters
            if category and topic.get("category") != category:
                continue
            
            if complexity and topic.get("complexity") != complexity:
                continue
            
            # Add performance data if available
            topic_with_performance = topic.copy()
            if topic["title"] in self.performance_data["topic_scores"]:
                topic_with_performance["performance_score"] = self.performance_data["topic_scores"][topic["title"]]
            
            suggestions.append(topic_with_performance)
        
        # Sort by performance score if available
        suggestions.sort(
            key=lambda x: x.get("performance_score", 0.5), 
            reverse=True
        )
        
        return suggestions
    
    def get_cycle_report(self) -> Dict:
        """Get detailed report on current rotation cycle."""
        current_cycle = self.rotation_history["current_cycle"]
        used_topics = self.rotation_history["used_topics_this_cycle"]
        
        # Calculate cycle progress
        progress_percentage = (len(used_topics) / self.config["cycle_length_weeks"]) * 100
        
        # Get unused topics
        all_titles = [topic["title"] for topic in self.topic_pools["all_topics"]]
        unused_topics = [title for title in all_titles if title not in used_topics]
        
        # Category distribution
        category_dist = {}
        for topic_title in used_topics:
            topic = self._get_topic_by_title(topic_title)
            category = topic.get("category", "unknown")
            category_dist[category] = category_dist.get(category, 0) + 1
        
        # Performance summary
        used_topic_scores = {
            title: self.performance_data["topic_scores"].get(title, "N/A")
            for title in used_topics
        }
        
        return {
            "cycle_number": current_cycle,
            "start_date": self.rotation_history["cycle_start_date"],
            "progress_percentage": progress_percentage,
            "topics_used": len(used_topics),
            "topics_remaining": len(unused_topics),
            "used_topics": used_topics,
            "unused_topics": unused_topics[:10],  # Show first 10
            "category_distribution": category_dist,
            "performance_scores": used_topic_scores,
            "next_cycle_starts_in": self.config["cycle_length_weeks"] - len(used_topics)
        }
    
    def force_topic_selection(self, topic_title: str) -> bool:
        """
        Force selection of a specific topic (for manual override).
        
        Args:
            topic_title: Title of topic to select
            
        Returns:
            Success status
        """
        # Check if topic exists
        topic_exists = any(
            topic["title"] == topic_title 
            for topic in self.topic_pools["all_topics"]
        )
        
        if not topic_exists:
            self.logger.error(f"Topic '{topic_title}' not found in topic pools")
            return False
        
        # Check if already used in cycle
        if topic_title in self.rotation_history["used_topics_this_cycle"]:
            self.logger.warning(f"Topic '{topic_title}' already used in current cycle")
        
        # Update rotation history
        self._update_rotation_history(topic_title)
        
        self.logger.info(f"Forced selection of topic: {topic_title}")
        return True


def main():
    """Main entry point for testing Topic Selection Manager."""
    import sys
    
    # Setup for testing
    marketing_path = Path(__file__).parent / "Marketing"
    
    if not marketing_path.exists():
        print("Marketing folder not found. Please run from 360tft directory.")
        return
    
    manager = TopicSelectionManager(marketing_path)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "select":
            # Select next topic
            topic = manager.select_weekly_topic()
            print(f"Selected topic: {topic}")
            
        elif command == "report":
            # Show cycle report
            report = manager.get_cycle_report()
            print("\n=== CYCLE REPORT ===")
            print(f"Cycle: {report['cycle_number']}")
            print(f"Progress: {report['progress_percentage']:.1f}%")
            print(f"Topics used: {report['topics_used']}/{report['topics_used'] + report['topics_remaining']}")
            print(f"Recent topics: {report['used_topics'][-5:]}")
            
        elif command == "suggest":
            # Show topic suggestions
            suggestions = manager.get_topic_suggestions()
            print("\n=== TOP TOPIC SUGGESTIONS ===")
            for i, topic in enumerate(suggestions[:10], 1):
                score = topic.get("performance_score", "N/A")
                print(f"{i}. {topic['title']} (Score: {score})")
                
        else:
            print("Usage: python Topic_Selection_Manager.py [select|report|suggest]")
    
    else:
        print("360TFT Topic Selection Manager")
        print("Usage: python Topic_Selection_Manager.py [select|report|suggest]")


if __name__ == "__main__":
    main()