#!/usr/bin/env python3
"""
360TFT Subagent Orchestrator
============================

Coordinates subagent task queues, manages handoffs between agents, monitors quality control gates,
handles error recovery, and coordinates timing and dependencies for weekly content creation.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import json
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import time
import asyncio
from enum import Enum


class TaskStatus(Enum):
    """Task execution status enumeration."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    NEEDS_REVISION = "needs_revision"
    BLOCKED = "blocked"


class ContentType(Enum):
    """Content type enumeration for templates."""
    BLOG_POST = "blog_post"
    EMAIL_NEWSLETTER = "email_newsletter"
    TWITTER_THREAD = "twitter_thread"
    LINKEDIN_ARTICLE = "linkedin_article"
    INSTAGRAM_CAROUSEL = "instagram_carousel"
    SHORTFORM_TWEETS = "shortform_tweets"
    YOUTUBE_SHORT = "youtube_short"
    CHEATSHEET = "cheatsheet"
    STRATEGIC_BRIEF = "strategic_brief"


class SubagentOrchestrator:
    """
    Coordinates all subagent workflows for 360TFT weekly content automation.
    
    Manages task queues, ensures proper handoffs, monitors quality gates,
    handles error recovery, and maintains content creation dependencies.
    """
    
    def __init__(self, base_path: Path):
        """
        Initialize the Subagent Orchestrator.
        
        Args:
            base_path: Base path for the automation system
        """
        self.base_path = Path(base_path)
        self.templates_path = self.base_path / "Content_Templates"
        self.prompts_path = self.base_path / "subagent_prompts"
        self.queue_path = self.base_path / "task_queues"
        
        # Ensure required directories exist
        self._create_directories()
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.config = self._load_config()
        
        # Initialize task queues
        self.task_queues = self._initialize_task_queues()
        
        # Load content templates and prompts
        self.templates = self._load_templates()
        self.prompts = self._load_prompts()
        
        # Track current execution context
        self.current_context = None
        
        self.logger.info("Subagent Orchestrator initialized")
    
    def _create_directories(self):
        """Create required directory structure."""
        directories = [
            self.templates_path,
            self.prompts_path,
            self.queue_path,
            self.base_path / "logs" / "orchestrator"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict:
        """Load orchestrator configuration."""
        default_config = {
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
        }
        
        config_file = self.base_path / "orchestrator_config.json"
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
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def _initialize_task_queues(self) -> Dict:
        """Initialize task execution queues."""
        return {
            "strategic_planning": [],
            "content_creation": [],
            "content_adaptation": [],
            "quality_control": [],
            "completed": [],
            "failed": []
        }
    
    def _load_templates(self) -> Dict[str, str]:
        """Load content templates from templates directory."""
        templates = {}
        
        # Check if templates exist, create if needed
        template_files = {
            "blog_post_template.md": self._get_blog_template(),
            "email_newsletter_template.md": self._get_email_template(),
            "twitter_thread_template.md": self._get_twitter_template(),
            "linkedin_article_template.md": self._get_linkedin_template(),
            "instagram_carousel_template.md": self._get_instagram_template(),
            "shortform_tweets_template.md": self._get_shortform_template(),
            "youtube_short_template.md": self._get_youtube_template(),
            "cheatsheet_template.html": self._get_cheatsheet_template(),
            "strategic_brief_template.md": self._get_strategic_brief_template()
        }
        
        for filename, default_content in template_files.items():
            template_file = self.templates_path / filename
            
            if not template_file.exists():
                with open(template_file, 'w', encoding='utf-8') as f:
                    f.write(default_content)
            
            with open(template_file, 'r', encoding='utf-8') as f:
                template_key = filename.replace('_template.md', '').replace('_template.html', '')
                templates[template_key] = f.read()
        
        return templates
    
    def _load_prompts(self) -> Dict[str, str]:
        """Load subagent prompts from prompts directory."""
        prompts = {}
        
        # Default prompts for each content type
        prompt_files = {
            "strategic_brief_prompt.txt": self._get_strategic_brief_prompt(),
            "blog_post_prompt.txt": self._get_blog_post_prompt(),
            "email_newsletter_prompt.txt": self._get_email_newsletter_prompt(),
            "twitter_thread_prompt.txt": self._get_twitter_thread_prompt(),
            "linkedin_article_prompt.txt": self._get_linkedin_article_prompt(),
            "instagram_carousel_prompt.txt": self._get_instagram_carousel_prompt(),
            "shortform_tweets_prompt.txt": self._get_shortform_tweets_prompt(),
            "youtube_short_prompt.txt": self._get_youtube_short_prompt(),
            "cheatsheet_prompt.txt": self._get_cheatsheet_prompt()
        }
        
        for filename, default_content in prompt_files.items():
            prompt_file = self.prompts_path / filename
            
            if not prompt_file.exists():
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(default_content)
            
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt_key = filename.replace('_prompt.txt', '')
                prompts[prompt_key] = f.read()
        
        return prompts
    
    # STRATEGIC BRIEF CREATION
    def create_strategic_brief(self, topic: str) -> str:
        """
        Create strategic content brief for the week's topic.
        
        Args:
            topic: Selected topic for the week
            
        Returns:
            Strategic brief content
        """
        self.logger.info(f"Creating strategic brief for topic: {topic}")
        
        try:
            # Create execution context
            self.current_context = {
                "topic": topic,
                "phase": "strategic_planning",
                "start_time": datetime.datetime.now()
            }
            
            # Use strategic brief template and prompt
            template = self.templates.get("strategic_brief", "")
            prompt = self.prompts.get("strategic_brief", "")
            
            # Generate strategic brief content
            brief_content = self._execute_content_generation(
                content_type=ContentType.STRATEGIC_BRIEF,
                topic=topic,
                template=template,
                prompt=prompt
            )
            
            # Add metadata
            metadata = self._generate_content_metadata(topic, ContentType.STRATEGIC_BRIEF)
            full_brief = f"{metadata}\n\n{brief_content}"
            
            self.logger.info("Strategic brief created successfully")
            return full_brief
            
        except Exception as e:
            self.logger.error(f"Strategic brief creation failed: {str(e)}")
            raise
    
    # BLOG POST CREATION
    def create_blog_post(self, topic: str) -> str:
        """
        Create comprehensive blog post.
        
        Args:
            topic: Topic for the blog post
            
        Returns:
            Blog post content
        """
        self.logger.info(f"Creating blog post for topic: {topic}")
        
        try:
            self.current_context = {
                "topic": topic,
                "phase": "blog_creation",
                "start_time": datetime.datetime.now()
            }
            
            template = self.templates.get("blog_post", "")
            prompt = self.prompts.get("blog_post", "")
            
            # Generate blog content
            blog_content = self._execute_content_generation(
                content_type=ContentType.BLOG_POST,
                topic=topic,
                template=template,
                prompt=prompt,
                target_word_count=self.config["content_templates"]["blog_word_count_target"]
            )
            
            # Add SEO metadata
            metadata = self._generate_content_metadata(topic, ContentType.BLOG_POST)
            full_blog = f"{metadata}\n\n{blog_content}"
            
            self.logger.info("Blog post created successfully")
            return full_blog
            
        except Exception as e:
            self.logger.error(f"Blog post creation failed: {str(e)}")
            raise
    
    # EMAIL NEWSLETTER CREATION
    def create_email_newsletter(self, topic: str, blog_content: str) -> str:
        """
        Create email newsletter adapted from blog post.
        
        Args:
            topic: Topic for the newsletter
            blog_content: Source blog post content
            
        Returns:
            Email newsletter content
        """
        self.logger.info(f"Creating email newsletter for topic: {topic}")
        
        try:
            self.current_context = {
                "topic": topic,
                "phase": "email_adaptation",
                "start_time": datetime.datetime.now(),
                "source_content": "blog_post"
            }
            
            template = self.templates.get("email_newsletter", "")
            prompt = self.prompts.get("email_newsletter", "")
            
            # Generate email content
            email_content = self._execute_content_adaptation(
                content_type=ContentType.EMAIL_NEWSLETTER,
                topic=topic,
                source_content=blog_content,
                template=template,
                prompt=prompt,
                target_word_count=self.config["content_templates"]["email_word_count_target"]
            )
            
            # Add email metadata
            metadata = self._generate_content_metadata(topic, ContentType.EMAIL_NEWSLETTER)
            full_email = f"{metadata}\n\n{email_content}"
            
            self.logger.info("Email newsletter created successfully")
            return full_email
            
        except Exception as e:
            self.logger.error(f"Email newsletter creation failed: {str(e)}")
            raise
    
    # SOCIAL MEDIA CONTENT CREATION
    def create_social_media_content(self, topic: str) -> Dict[str, str]:
        """
        Create all social media content variations.
        
        Args:
            topic: Topic for social media content
            
        Returns:
            Dictionary of social media content by platform
        """
        self.logger.info(f"Creating social media content for topic: {topic}")
        
        social_content = {}
        
        try:
            self.current_context = {
                "topic": topic,
                "phase": "social_media_creation",
                "start_time": datetime.datetime.now()
            }
            
            # Create Twitter thread
            social_content["twitter_thread"] = self._create_twitter_thread(topic)
            
            # Create LinkedIn article
            social_content["linkedin_article"] = self._create_linkedin_article(topic)
            
            # Create Instagram carousel
            social_content["instagram_carousel"] = self._create_instagram_carousel(topic)
            
            self.logger.info("Social media content created successfully")
            return social_content
            
        except Exception as e:
            self.logger.error(f"Social media content creation failed: {str(e)}")
            raise
    
    def _create_twitter_thread(self, topic: str) -> str:
        """Create Twitter thread content."""
        template = self.templates.get("twitter_thread", "")
        prompt = self.prompts.get("twitter_thread", "")
        
        return self._execute_content_generation(
            content_type=ContentType.TWITTER_THREAD,
            topic=topic,
            template=template,
            prompt=prompt,
            target_length=self.config["content_templates"]["twitter_thread_length"]
        )
    
    def _create_linkedin_article(self, topic: str) -> str:
        """Create LinkedIn article content."""
        template = self.templates.get("linkedin_article", "")
        prompt = self.prompts.get("linkedin_article", "")
        
        return self._execute_content_generation(
            content_type=ContentType.LINKEDIN_ARTICLE,
            topic=topic,
            template=template,
            prompt=prompt
        )
    
    def _create_instagram_carousel(self, topic: str) -> str:
        """Create Instagram carousel content."""
        template = self.templates.get("instagram_carousel", "")
        prompt = self.prompts.get("instagram_carousel", "")
        
        return self._execute_content_generation(
            content_type=ContentType.INSTAGRAM_CAROUSEL,
            topic=topic,
            template=template,
            prompt=prompt,
            target_slides=self.config["content_templates"]["instagram_slides"]
        )
    
    # SHORT-FORM CONTENT CREATION
    def create_shortform_content(self, topic: str) -> str:
        """
        Create short-form content (tweets, YouTube shorts).
        
        Args:
            topic: Topic for short-form content
            
        Returns:
            Short-form content
        """
        self.logger.info(f"Creating short-form content for topic: {topic}")
        
        try:
            self.current_context = {
                "topic": topic,
                "phase": "shortform_creation",
                "start_time": datetime.datetime.now()
            }
            
            # Create standalone tweets
            tweets_template = self.templates.get("shortform_tweets", "")
            tweets_prompt = self.prompts.get("shortform_tweets", "")
            
            tweets_content = self._execute_content_generation(
                content_type=ContentType.SHORTFORM_TWEETS,
                topic=topic,
                template=tweets_template,
                prompt=tweets_prompt
            )
            
            # Create YouTube short script
            youtube_template = self.templates.get("youtube_short", "")
            youtube_prompt = self.prompts.get("youtube_short", "")
            
            youtube_content = self._execute_content_generation(
                content_type=ContentType.YOUTUBE_SHORT,
                topic=topic,
                template=youtube_template,
                prompt=youtube_prompt,
                target_duration=self.config["content_templates"]["youtube_short_duration"]
            )
            
            # Combine content
            combined_content = f"# Short-form Content: {topic}\n\n"
            combined_content += f"## Standalone Tweets\n\n{tweets_content}\n\n"
            combined_content += f"## YouTube Short Script\n\n{youtube_content}"
            
            self.logger.info("Short-form content created successfully")
            return combined_content
            
        except Exception as e:
            self.logger.error(f"Short-form content creation failed: {str(e)}")
            raise
    
    # CHEAT SHEET CREATION
    def create_cheatsheet(self, topic: str) -> str:
        """
        Create HTML cheat sheet for A4 printing.
        
        Args:
            topic: Topic for the cheat sheet
            
        Returns:
            HTML cheat sheet content
        """
        self.logger.info(f"Creating cheat sheet for topic: {topic}")
        
        try:
            self.current_context = {
                "topic": topic,
                "phase": "cheatsheet_creation",
                "start_time": datetime.datetime.now()
            }
            
            template = self.templates.get("cheatsheet", "")
            prompt = self.prompts.get("cheatsheet", "")
            
            # Generate cheat sheet content
            cheatsheet_content = self._execute_content_generation(
                content_type=ContentType.CHEATSHEET,
                topic=topic,
                template=template,
                prompt=prompt
            )
            
            self.logger.info("Cheat sheet created successfully")
            return cheatsheet_content
            
        except Exception as e:
            self.logger.error(f"Cheat sheet creation failed: {str(e)}")
            raise
    
    # CONTENT GENERATION ENGINE
    def _execute_content_generation(self, content_type: ContentType, topic: str, 
                                   template: str, prompt: str, **kwargs) -> str:
        """
        Execute content generation using template and prompt.
        
        Args:
            content_type: Type of content being generated
            topic: Topic for the content
            template: Content template
            prompt: Generation prompt
            **kwargs: Additional parameters
            
        Returns:
            Generated content
        """
        # This is a placeholder for the actual content generation
        # In a real implementation, this would interface with an AI model
        # or content generation service
        
        # For now, return template-based content with topic substitution
        generated_content = self._apply_template_substitutions(
            template, topic, content_type, **kwargs
        )
        
        return generated_content
    
    def _execute_content_adaptation(self, content_type: ContentType, topic: str,
                                   source_content: str, template: str, 
                                   prompt: str, **kwargs) -> str:
        """
        Execute content adaptation from source content.
        
        Args:
            content_type: Type of content being adapted
            topic: Topic for the content
            source_content: Source content to adapt from
            template: Adaptation template
            prompt: Adaptation prompt
            **kwargs: Additional parameters
            
        Returns:
            Adapted content
        """
        # This would interface with AI model for adaptation
        # For now, return template-based adaptation
        
        adapted_content = self._apply_template_substitutions(
            template, topic, content_type, source_content=source_content, **kwargs
        )
        
        return adapted_content
    
    def _apply_template_substitutions(self, template: str, topic: str, 
                                     content_type: ContentType, **kwargs) -> str:
        """Apply template variable substitutions."""
        # Get current date info
        now = datetime.datetime.now()
        current_date = now.strftime('%Y-%m-%d')
        current_week = now.isocalendar()[1]
        
        # Basic substitutions
        substitutions = {
            "{TOPIC}": topic,
            "{CONTENT_TYPE}": content_type.value,
            "{DATE}": current_date,
            "{WEEK_NUMBER}": str(current_week),
            "{EXPERIENCE_YEARS}": "15+",
            "{PLAYERS_TRAINED}": "1,000+",
            "{COACHES_EDUCATED}": "1,200+",
            "{COMMUNITY_SIZE}": "1,000+",
            "{BRAND_NAME}": "360TFT",
            "{AUTHOR}": "Kevin Middleton",
            "{ACADEMY_NAME}": "Football Coaching Academy"
        }
        
        # Apply substitutions
        content = template
        for placeholder, value in substitutions.items():
            content = content.replace(placeholder, value)
        
        # Apply any additional kwargs
        for key, value in kwargs.items():
            placeholder = f"{{{key.upper()}}}"
            content = content.replace(placeholder, str(value))
        
        return content
    
    def _generate_content_metadata(self, topic: str, content_type: ContentType) -> str:
        """Generate content metadata header."""
        now = datetime.datetime.now()
        
        metadata = f"""---
title: "{topic}"
content_type: "{content_type.value}"
created_date: "{now.strftime('%Y-%m-%d')}"
created_time: "{now.strftime('%H:%M:%S')}"
week_number: {now.isocalendar()[1]}
author: "Kevin Middleton"
brand: "360TFT"
automation_version: "1.0"
---"""
        
        return metadata
    
    # ERROR HANDLING AND RECOVERY
    def handle_execution_error(self, error: Exception, context: Dict) -> bool:
        """
        Handle execution errors with retry logic.
        
        Args:
            error: Exception that occurred
            context: Execution context
            
        Returns:
            True if recovery successful, False otherwise
        """
        self.logger.error(f"Execution error in {context.get('phase', 'unknown')}: {str(error)}")
        
        # Log error details
        error_log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "phase": context.get("phase"),
            "topic": context.get("topic"),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context
        }
        
        # Save error log
        error_file = self.base_path / "logs" / "orchestrator" / f"error_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(error_file, 'w') as f:
            json.dump(error_log, f, indent=2)
        
        # Attempt recovery based on error type
        if "timeout" in str(error).lower():
            return self._handle_timeout_error(context)
        elif "api" in str(error).lower() or "connection" in str(error).lower():
            return self._handle_api_error(context)
        else:
            return self._handle_generic_error(context)
    
    def _handle_timeout_error(self, context: Dict) -> bool:
        """Handle timeout errors."""
        self.logger.info("Attempting timeout error recovery")
        # Implement timeout-specific recovery
        time.sleep(self.config["retry_delay_seconds"])
        return True
    
    def _handle_api_error(self, context: Dict) -> bool:
        """Handle API/connection errors."""
        self.logger.info("Attempting API error recovery")
        # Implement API-specific recovery
        time.sleep(self.config["retry_delay_seconds"] * 2)
        return True
    
    def _handle_generic_error(self, context: Dict) -> bool:
        """Handle generic errors."""
        self.logger.info("Attempting generic error recovery")
        # Implement generic recovery
        time.sleep(self.config["retry_delay_seconds"])
        return True
    
    # QUALITY CONTROL INTEGRATION
    def validate_content_quality(self, content: str, content_type: ContentType) -> Tuple[bool, float, str]:
        """
        Validate content quality before handoff.
        
        Args:
            content: Content to validate
            content_type: Type of content
            
        Returns:
            Tuple of (passed, score, feedback)
        """
        # Basic quality checks
        quality_score = 0.0
        feedback_items = []
        
        # Length check
        word_count = len(content.split())
        if content_type == ContentType.BLOG_POST:
            target_range = (1500, 3000)
        elif content_type == ContentType.EMAIL_NEWSLETTER:
            target_range = (800, 1200)
        else:
            target_range = (100, 2000)
        
        if target_range[0] <= word_count <= target_range[1]:
            quality_score += 20
        else:
            feedback_items.append(f"Word count {word_count} outside target range {target_range}")
        
        # British English check (basic)
        british_terms = ["colour", "favour", "realise", "analyse", "centre"]
        american_terms = ["color", "favor", "realize", "analyze", "center"]
        
        british_score = sum(1 for term in british_terms if term in content.lower())
        american_score = sum(1 for term in american_terms if term in content.lower())
        
        if british_score >= american_score:
            quality_score += 10
        else:
            feedback_items.append("Consider using British English spelling")
        
        # Authority indicators check
        authority_indicators = ["15+ years", "1,000+ players", "experience", "360TFT"]
        authority_score = sum(1 for indicator in authority_indicators if indicator in content)
        
        if authority_score >= 2:
            quality_score += 10
        else:
            feedback_items.append("Include more authority indicators")
        
        # Academy integration check
        academy_terms = ["Academy", "Football Coaching Academy", "community", "members"]
        academy_score = sum(1 for term in academy_terms if term in content)
        
        if academy_score >= 1:
            quality_score += 5
        else:
            feedback_items.append("Include Academy integration")
        
        # Basic structure check
        if content_type == ContentType.BLOG_POST:
            required_sections = ["#", "##", "implementation", "system"]
            structure_score = sum(1 for section in required_sections if section.lower() in content.lower())
            quality_score += min(structure_score * 2, 10)
        
        # Calculate final score
        quality_score = min(quality_score, 100)
        passed = quality_score >= self.config["quality_gate_threshold"]
        
        feedback = "; ".join(feedback_items) if feedback_items else "Quality checks passed"
        
        return passed, quality_score, feedback
    
    # TEMPLATE DEFINITIONS
    def _get_blog_template(self) -> str:
        """Get default blog post template."""
        return """# {TOPIC}: The Complete {BRAND_NAME} Guide

## Introduction

After {EXPERIENCE_YEARS} years of coaching and training {PLAYERS_TRAINED} players, I've discovered that most coaches struggle with {TOPIC}.

Here's what actually works.

## The Challenge

[Describe the core problem coaches face with this topic]

## The {BRAND_NAME} Solution

### Phase 1: Foundation
[Detailed explanation of foundational approach]

### Phase 2: Development  
[Progressive development strategies]

### Phase 3: Application
[Match-realistic application methods]

## Age-Appropriate Applications

### Foundation Phase (Ages 6-10)
[Specific adaptations for young players]

### Development Phase (Ages 11-14)
[Increased complexity strategies]

### Specialisation Phase (Ages 15+)
[Advanced applications]

## Implementation Guide

### Week 1-2: Foundation Building
[Specific implementation steps]

### Week 3-4: Progressive Development
[Development progression]

### Week 5-8: System Integration
[Full integration strategies]

## {ACADEMY_NAME} Resources

The {ACADEMY_NAME} provides complete resources for {TOPIC} development:

✅ Progressive session plans for every age group
✅ Implementation guides with step-by-step progressions  
✅ Assessment tools to measure development
✅ Community discussion with {COMMUNITY_SIZE} coaches

## Conclusion

Transform your approach to {TOPIC} with systematic development rather than random training.

Ready to implement this system? Join the {ACADEMY_NAME} for complete resources and community support.

---
*Created by {AUTHOR} | {BRAND_NAME} | Week {WEEK_NUMBER}*"""

    def _get_email_template(self) -> str:
        """Get default email newsletter template."""
        return """Subject: Why [common approach] creates [negative outcome]

Hi there,

"[Common coaching instruction]"

Sound familiar?

After {EXPERIENCE_YEARS} years, I've discovered this approach actually creates the opposite of what we want.

## The {TOPIC} Problem

Most coaches [describe common problem] which leads to:
- [Negative outcome 1]
- [Negative outcome 2]  
- [Negative outcome 3]

## The {BRAND_NAME} Solution

Instead of [old approach], the {BRAND_NAME} methodology transforms {TOPIC} through:

**Phase 1: [Foundation]**
[Brief description]

**Phase 2: [Development]**
[Progressive approach]  

**Phase 3: [Application]**
[Match integration]

## Academy Advantage

{ACADEMY_NAME} members get:
✅ Complete {TOPIC} session library
✅ Progressive implementation guides
✅ Community support from {COMMUNITY_SIZE} coaches
✅ Direct access to ask questions

## This Week's Action Step

[One specific actionable step]

Ready to transform {TOPIC} development?

**[Join the {ACADEMY_NAME}]**

Questions? Hit reply - I read every email.

Transform {TOPIC}. Transform results.

{AUTHOR}  
{BRAND_NAME} | Creator of the {ACADEMY_NAME}

P.S. [Additional value proposition]"""

    def _get_twitter_template(self) -> str:
        """Get default Twitter thread template."""
        return """🧵 THREAD: Why [common approach] fails for {TOPIC} development (and what actually works)

1/ [Problem statement with specific example]

2/ After {EXPERIENCE_YEARS} years coaching {PLAYERS_TRAINED} players, I've identified the real issue: [core insight]

3/ Most coaches [describe common mistake] which creates [negative outcome]

4/ The {BRAND_NAME} approach: [Solution point 1 with brief explanation]

5/ [Solution point 2 with specific application]

6/ [Solution point 3 with expected results]

7/ Implementation timeline:
Week 1: [Action]
Week 2: [Action]  
Week 3: [Action]

8/ Expected results: [Specific transformation coaches can expect]

9/ {ACADEMY_NAME} members get complete {TOPIC} resources + community support from {COMMUNITY_SIZE} coaches.

10/ Your players deserve systematic {TOPIC} development.

Save this thread and transform your approach. 

What's your experience with {TOPIC}? 💬

#{BRAND_NAME} #FootballCoaching #YouthDevelopment"""

    def _get_linkedin_template(self) -> str:
        """Get default LinkedIn article template."""
        return """# After {EXPERIENCE_YEARS} Years: What I've Learned About {TOPIC} in Youth Football Development

After working with {PLAYERS_TRAINED} players and educating {COACHES_EDUCATED} coaches, I've observed a consistent pattern in {TOPIC} development.

## The Challenge in Professional Context

[Industry-relevant problem description with professional insight]

## Evidence-Based Solution

The {BRAND_NAME} methodology addresses this through systematic progression:

**Foundation Phase:** [Professional approach to basics]
**Development Phase:** [Progressive complexity with assessment]  
**Application Phase:** [Match-realistic integration]

## Implementation in Professional Environments

[How this applies to academy/professional settings]

## Measuring Success

[Assessment and tracking methods used in professional development]

## Community Impact

The {ACADEMY_NAME} has grown to {COMMUNITY_SIZE} coaches implementing these methods across grassroots to professional levels.

**Discussion:** How do you approach {TOPIC} development in your coaching environment?

#FootballDevelopment #YouthCoaching #{BRAND_NAME} #ProfessionalDevelopment"""

    def _get_instagram_template(self) -> str:
        """Get default Instagram carousel template."""
        return """# Instagram Carousel: {TOPIC}

## Slide 1 (Hook)
Why [common approach] isn't working ➡️
[Preview of solution]
Save this for better {TOPIC} training 📌

## Slide 2-6 (Content)
[Each slide focuses on one key point with visual elements]

**Slide 2:** [Key Point 1]
- [Bullet point]
- [Bullet point]

**Slide 3:** [Key Point 2]  
- [Bullet point]
- [Bullet point]

**Slide 4:** [Key Point 3]
- [Bullet point]
- [Bullet point]

**Slide 5:** [Key Point 4]
- [Bullet point]
- [Bullet point]

**Slide 6:** [Key Point 5]
- [Bullet point]
- [Bullet point]

## Slide 7 (Implementation)
How to start:
Week 1: [Action]
Week 2: [Action]
Week 3: [Action]
Results: [Expected outcome]

## Caption
[Hook question] ➡️

[Brief problem description]

Here's the {TOPIC} system that [outcome] (swipe to see each step)

Save this for [specific application] 📌

#FootballCoaching #{TOPIC} #{BRAND_NAME} #YouthSoccer"""

    def _get_shortform_template(self) -> str:
        """Get default short-form tweets template."""
        return """# Short-form Tweets: {TOPIC}

## Tweet 1 (Problem/Solution)
Most coaches [problem] which creates [negative outcome].

Here's what actually works: [brief solution]

## Tweet 2 (Controversial Opinion)  
Unpopular opinion: [controversial statement about topic]

After {EXPERIENCE_YEARS} years, I've learned [insight that challenges conventional thinking]

## Tweet 3 (Quick Tip)
{TOPIC} tip that transforms training:

[Specific actionable advice]

Try this in your next session.

## Tweet 4 (Community Question)
Coaches: What's your biggest challenge with {TOPIC}?

After working with {COMMUNITY_SIZE} coaches, I've found [common pattern]

## Tweet 5 (Behind Scenes)
15 years ago I thought [old belief about topic].

Now I know [new understanding].

Your players deserve [better approach]."""

    def _get_youtube_template(self) -> str:
        """Get default YouTube Short script template."""
        return """# YouTube Short Script: {TOPIC}

**Duration:** 60-90 seconds

## Hook (0-3 seconds)
[Problem statement or controversial claim]

## Problem (3-15 seconds)  
Most coaches [common mistake] which creates [negative outcome]

## Solution Preview (15-25 seconds)
Here's what actually works: [brief system overview]

## Specific Steps (25-50 seconds)
Step 1: [Action with visual demonstration]
Step 2: [Action with visual demonstration]  
Step 3: [Action with visual demonstration]

## Result (50-60 seconds)
This creates [specific outcome] instead of [old outcome]

## CTA (60-90 seconds)
Try this in your next session and let me know how it goes.
Link in bio for complete {TOPIC} resources.
Follow for more coaching insights.

## Visual Cues
- On-screen text for key points
- Demonstration of techniques
- Before/after comparisons
- Call-to-action graphics"""

    def _get_cheatsheet_template(self) -> str:
        """Get default cheat sheet HTML template."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TOPIC} - {BRAND_NAME} Cheat Sheet</title>
    <style>
        @page { size: A4; margin: 20mm; }
        body { font-family: Arial, sans-serif; font-size: 12pt; line-height: 1.4; }
        .header { text-align: center; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px; }
        .title { font-size: 24pt; font-weight: bold; color: #333; margin-bottom: 5px; }
        .subtitle { font-size: 14pt; color: #666; }
        .section { margin-bottom: 20px; }
        .section-title { font-size: 16pt; font-weight: bold; color: #333; border-left: 4px solid #007acc; padding-left: 10px; margin-bottom: 10px; }
        .content { margin-left: 15px; }
        .bullet-list { list-style-type: none; padding-left: 0; }
        .bullet-list li { margin-bottom: 8px; position: relative; padding-left: 20px; }
        .bullet-list li:before { content: "✓"; position: absolute; left: 0; color: #007acc; font-weight: bold; }
        .footer { position: fixed; bottom: 10mm; left: 0; right: 0; text-align: center; font-size: 10pt; color: #666; }
        .highlight { background-color: #f0f8ff; padding: 10px; border-left: 3px solid #007acc; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">{TOPIC}</div>
        <div class="subtitle">The Complete {BRAND_NAME} System</div>
    </div>

    <div class="section">
        <div class="section-title">The Challenge</div>
        <div class="content">
            [Brief description of the core problem this system solves]
        </div>
    </div>

    <div class="section">
        <div class="section-title">The {BRAND_NAME} Solution</div>
        <div class="content">
            <div class="highlight">
                <strong>3-Phase System for {TOPIC} Development</strong>
            </div>
            
            <h4>Phase 1: Foundation</h4>
            <ul class="bullet-list">
                <li>[Key point 1]</li>
                <li>[Key point 2]</li>
                <li>[Key point 3]</li>
            </ul>

            <h4>Phase 2: Development</h4>
            <ul class="bullet-list">
                <li>[Key point 1]</li>
                <li>[Key point 2]</li>
                <li>[Key point 3]</li>
            </ul>

            <h4>Phase 3: Application</h4>
            <ul class="bullet-list">
                <li>[Key point 1]</li>
                <li>[Key point 2]</li>
                <li>[Key point 3]</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Implementation Guide</div>
        <div class="content">
            <ul class="bullet-list">
                <li><strong>Week 1-2:</strong> [Foundation implementation]</li>
                <li><strong>Week 3-4:</strong> [Development progression]</li>
                <li><strong>Week 5-8:</strong> [Application integration]</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Age Adaptations</div>
        <div class="content">
            <p><strong>Ages 6-10:</strong> [Foundation adaptations]</p>
            <p><strong>Ages 11-14:</strong> [Development adaptations]</p>
            <p><strong>Ages 15+:</strong> [Advanced applications]</p>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Key Success Indicators</div>
        <div class="content">
            <ul class="bullet-list">
                <li>[Success indicator 1]</li>
                <li>[Success indicator 2]</li>
                <li>[Success indicator 3]</li>
                <li>[Success indicator 4]</li>
            </ul>
        </div>
    </div>

    <div class="footer">
        <p>{AUTHOR} | {BRAND_NAME} | Complete resources available at {ACADEMY_NAME}</p>
        <p>Created: {DATE} | Week {WEEK_NUMBER} | © {BRAND_NAME}</p>
    </div>
</body>
</html>"""

    def _get_strategic_brief_template(self) -> str:
        """Get default strategic brief template."""
        return """# Strategic Content Brief: {TOPIC}

## Content Overview
- **Topic:** {TOPIC}
- **Week:** {WEEK_NUMBER}
- **Created:** {DATE}
- **Target Audience:** Grassroots coaches, Academy professionals, Parent coaches

## Content Objectives
- [ ] Education and skill development
- [ ] Problem-solving for common challenges  
- [ ] {BRAND_NAME} methodology integration
- [ ] {ACADEMY_NAME} community building

## Key Messaging Pillars
1. **Authority Positioning:** {EXPERIENCE_YEARS} years, {PLAYERS_TRAINED} players trained
2. **Systematic Approach:** {BRAND_NAME} methodology over random training
3. **Community Focus:** {COMMUNITY_SIZE} coaches in {ACADEMY_NAME}
4. **Practical Implementation:** Immediate, actionable guidance

## Content Angles
### Primary Angle: Problem-Solution Focus
[Why current approaches fail and what works instead]

### Secondary Angle: Community Engagement  
[How this connects to broader coaching community challenges]

### Tertiary Angle: Professional Development
[How this advances coaching knowledge and skills]

## Cross-Platform Content Map
- **Blog Post:** Comprehensive guide (2,500 words)
- **Email Newsletter:** Nurture sequence adaptation (1,000 words)
- **Twitter Thread:** Engagement driver (10 tweets)
- **LinkedIn Article:** Professional credibility (1,200 words)
- **Instagram Carousel:** Visual appeal (7 slides)
- **Short-form Content:** Viral potential (5 tweets + YouTube short)
- **Cheat Sheet:** Practical resource (A4 format)

## Value Equation Optimization
- **Dream Outcome:** [Specific player/team transformation]
- **Perceived Likelihood:** [Authority + community proof]
- **Time Delay:** "Immediate implementation" language
- **Effort & Sacrifice:** "Simple 3-step system" approach

## Quality Control Requirements
- [x] British English throughout
- [x] No fabricated stories or examples
- [x] Natural {ACADEMY_NAME} integration
- [x] Value Equation score 35+
- [x] Age-appropriate applications included

## Success Metrics
- Blog: 5+ minute time on page, email sign-ups
- Email: 30%+ open rate, 5%+ CTR
- Social: 4%+ engagement rate
- Cheat Sheet: 100+ downloads

---
*Strategic brief prepared by {BRAND_NAME} Content Automation System*"""

    # PROMPT DEFINITIONS
    def _get_strategic_brief_prompt(self) -> str:
        """Get strategic brief generation prompt."""
        return """You are Kevin Middleton, creator of 360TFT and the Football Coaching Academy. You have 15+ years experience coaching over 1,000 players and educating 1,200+ coaches.

Create a strategic content brief for the topic: {TOPIC}

The brief should establish the week's content strategy including:
1. Target audience analysis
2. Key messaging pillars  
3. Content angles for different platforms
4. Value Equation optimization points
5. Cross-platform integration strategy

Voice Requirements:
- British English only
- Authoritative but not arrogant
- Community-focused
- Practical and implementation-oriented
- No fabricated stories or examples

The brief will guide all content creation for the week, ensuring consistency across blog posts, emails, social media, and cheat sheets."""

    def _get_blog_post_prompt(self) -> str:
        """Get blog post generation prompt."""
        return """You are Kevin Middleton, creator of 360TFT and the Football Coaching Academy. You have 15+ years experience coaching over 1,000 players and educating 1,200+ coaches.

Create a comprehensive blog post on: {TOPIC}

Structure Requirements:
1. Hook with coaching scenario (150 words)
2. Authority establishment (100 words)  
3. Problem deep-dive (500 words)
4. The 360TFT Solution System (1,200 words)
5. Age-appropriate applications (600 words)
6. Implementation guide (400 words)
7. Academy integration (300 words)
8. Conclusion with CTA (200 words)

Voice Requirements:
- British English only
- No fabricated stories - use general coaching scenarios
- Reference 15+ years experience and 1,000+ players trained
- Include 360TFT methodology and systematic approach
- Natural Academy promotion without being pushy
- Maintain Seth Godin-style memorable messaging

Value Equation Optimization:
- Dream Outcome: Specific player transformations
- Perceived Likelihood: Experience credentials + community size
- Time Delay: "Tonight's session" implementation language  
- Effort & Sacrifice: Simple, systematic approach

Target: 2,500 words, Value Equation score 35+"""

    def _get_email_newsletter_prompt(self) -> str:
        """Get email newsletter generation prompt."""
        return """Transform the blog post on {TOPIC} into an engaging email newsletter following Kevin's voice and style.

Target Length: 800-1,200 words

Structure Required:
1. Subject line (5 options focusing on problem/solution)
2. Personal greeting
3. Scenario-based opening  
4. Problem identification with bullet points
5. Reality check section
6. The 360TFT System (3-phase breakdown)
7. Academy comparison section
8. Real results testimonials (general, not fabricated)
9. Implementation strategy (weekly breakdown)
10. Common mistakes section
11. Action step for this week
12. CTA for Academy/resources
13. Personal sign-off

Voice Requirements:
- Conversational, coach-to-coach tone
- British English
- Authority without arrogance
- Community-focused
- Problem-solution framework

Email Optimization:
- Subject lines that increase open rates
- Scannable format with bullet points
- Clear value before any promotion
- Personal connection elements
- Strong, specific CTA"""

    def _get_twitter_thread_prompt(self) -> str:
        """Get Twitter thread generation prompt."""
        return """Create an 8-12 tweet thread from the blog post on {TOPIC}.

Thread Structure:
Tweet 1: Hook with problem statement + thread emoji
Tweet 2-3: Problem expansion with specific examples
Tweet 4: Authority positioning (experience/results)
Tweets 5-8: Solution points (one per tweet)
Tweet 9: Implementation timeline
Tweet 10: Expected results
Tweet 11: Community engagement + Academy CTA
Tweet 12: Save/share encouragement

Requirements:
- Each tweet under 280 characters
- Hook that stops scrolling
- Value in every tweet
- Natural Academy mention
- Community engagement focus
- Consistent with Kevin's voice
- British English
- No fabricated examples
- Use relevant hashtags"""

    def _get_linkedin_article_prompt(self) -> str:
        """Get LinkedIn article generation prompt."""
        return """Transform blog content into professional LinkedIn article (800-1,200 words).

Professional Structure:
- Industry-relevant headline
- Professional experience opening
- Evidence-based approach
- Academy/professional environment context
- Discussion-generating conclusion
- Professional hashtags
- Industry connections/mentions

Tone: More formal but still authentic Kevin voice
Focus: Professional development angle
CTA: Academy for systematic approach
Voice: British English, authoritative but collaborative
Community: Encourage professional discussion"""

    def _get_instagram_carousel_prompt(self) -> str:
        """Get Instagram carousel generation prompt."""
        return """Create 6-8 slide Instagram carousel from blog content.

Slide Requirements:
Slide 1: Hook + save encouragement
Slides 2-6: Key points with visual elements
Slide 7: Implementation steps
Slide 8: CTA + community engagement

Visual Descriptions:
- Each slide needs visual element description
- Consistent branding elements
- Text overlay specifications
- Color scheme alignment
- Coach/player scenario visuals

Caption: Hook + value + hashtags + community question
Voice: British English, engaging, visual-friendly
Focus: Quick value delivery with save appeal"""

    def _get_shortform_tweets_prompt(self) -> str:
        """Get short-form tweets generation prompt."""
        return """Create 5 standalone tweets from the blog content on {TOPIC}.

Formats:
1. Problem/Solution tweet
2. Controversial opinion tweet
3. Quick tip tweet
4. Community question tweet
5. Behind-scenes insight tweet

Requirements:
- Under 280 characters each
- High engagement potential
- Value in every tweet
- Kevin's authentic voice
- Call for community interaction
- British English
- No fabricated examples
- Relevant hashtags"""

    def _get_youtube_short_prompt(self) -> str:
        """Get YouTube Short script generation prompt."""
        return """Create 60-90 second YouTube Short script from blog content.

Structure:
0-3s: Problem hook
3-15s: Problem explanation
15-25s: Solution preview
25-50s: 3-step system
50-60s: Results promise
60-90s: CTA + follow

Visual Cues:
- On-screen text elements
- Demonstration suggestions
- Transition moments
- Engagement prompts

Voice: British English, energetic but authentic
Focus: Quick value delivery with clear call-to-action
Style: Educational but entertaining"""

    def _get_cheatsheet_prompt(self) -> str:
        """Get cheat sheet generation prompt."""
        return """Create a comprehensive A4 cheat sheet for {TOPIC}.

Structure:
- Title with outcome promise
- Brief problem/solution overview
- 3-phase system breakdown with visual elements
- Implementation timeline
- Age adaptations
- Success indicators
- 360TFT branding

Requirements:
- A4 printable format
- Visual hierarchy with clear sections
- Bullet points for scanability
- Professional design elements
- Practical, immediately usable
- British English
- 360TFT methodology integration
- Academy CTA inclusion"""


def main():
    """Main entry point for testing Subagent Orchestrator."""
    import sys
    
    # Setup for testing
    base_path = Path(__file__).parent
    orchestrator = SubagentOrchestrator(base_path)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "test-brief" and len(sys.argv) > 2:
            topic = " ".join(sys.argv[2:])
            brief = orchestrator.create_strategic_brief(topic)
            print("=== STRATEGIC BRIEF ===")
            print(brief)
            
        elif command == "test-blog" and len(sys.argv) > 2:
            topic = " ".join(sys.argv[2:])
            blog = orchestrator.create_blog_post(topic)
            print("=== BLOG POST ===")  
            print(blog)
            
        elif command == "test-templates":
            print("=== AVAILABLE TEMPLATES ===")
            for template_name in orchestrator.templates.keys():
                print(f"- {template_name}")
            
        else:
            print("Usage: python Subagent_Orchestrator.py [test-brief|test-blog|test-templates] [topic]")
    
    else:
        print("360TFT Subagent Orchestrator")
        print("Usage: python Subagent_Orchestrator.py [test-brief|test-blog|test-templates] [topic]")


if __name__ == "__main__":
    main()