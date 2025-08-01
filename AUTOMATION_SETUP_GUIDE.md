# 360TFT Weekly Content Automation System - Setup Guide

## Overview

This comprehensive automation system generates 10 high-quality content pieces plus 1 cheat sheet weekly for Kevin Middleton's 360TFT platform, maintaining authentic voice and methodology across all formats.

## System Components

### Core Files Created
- **`Weekly_Content_Automation.py`** - Main automation controller
- **`Topic_Selection_Manager.py`** - 27-topic rotation management  
- **`Subagent_Orchestrator.py`** - Content creation coordination
- **`Quality_Control_System.py`** - Automated quality assurance
- **`Content_Templates/`** - Template folder (auto-created with defaults)

### Integration Points
- **`Marketing/`** folder - Source content and voice guidelines
- **`Marketing/Produced Content/`** - Output destination
- **`Marketing/Cheatsheets/`** - Cheat sheet publishing
- **`Marketing/Voice/Voice`** - Voice consistency reference

## Installation & Setup

### Prerequisites
```bash
# Required Python packages
pip install schedule
pip install pathlib
pip install asyncio
```

### Directory Structure Verification
The system will automatically create required directories, but ensure these exist:
```
360tft/
├── Weekly_Content_Automation.py
├── Topic_Selection_Manager.py  
├── Subagent_Orchestrator.py
├── Quality_Control_System.py
├── Marketing/
│   ├── Voice/Voice
│   ├── Blogs/
│   ├── Emails/
│   ├── Produced Content/
│   └── Cheatsheets/
└── Content_Templates/ (auto-created)
```

### Configuration Files
The system creates default configuration files on first run:
- `automation_config.json` - Main automation settings
- `orchestrator_config.json` - Content creation settings
- `topic_data/` - Topic rotation tracking (auto-created)

## Usage Instructions

### 1. Manual Week Execution (Recommended for Testing)
```bash
# Run complete week's content creation
python Weekly_Content_Automation.py run-week

# Check current progress
python Weekly_Content_Automation.py status
```

### 2. Automated Scheduling
```bash
# Start automated weekly schedule
python Weekly_Content_Automation.py schedule
```

### 3. Topic Management
```bash
# Select next topic manually
python Topic_Selection_Manager.py select

# View cycle report
python Topic_Selection_Manager.py report

# Get topic suggestions
python Topic_Selection_Manager.py suggest
```

### 4. Quality Control Testing
```bash
# Test content quality
python Quality_Control_System.py test-content "Your test content here"

# Test file quality
python Quality_Control_System.py test-file "path/to/content.md"

# Review folder quality
python Quality_Control_System.py test-review "path/to/content/folder"
```

## Weekly Workflow

### Automated Schedule (Default Times)
- **Sunday 09:00** - Topic selection and strategic planning
- **Monday 10:00** - Blog post creation (2,500 words)
- **Tuesday 10:00** - Email newsletter adaptation (1,000 words)
- **Wednesday 10:00** - Social media content (Twitter, LinkedIn, Instagram)
- **Thursday 10:00** - Short-form content (tweets, YouTube shorts)
- **Friday 10:00** - Cheat sheet creation (A4 HTML format)
- **Saturday 10:00** - Quality control and optimization

### Content Output Structure
Each week creates a folder in `Marketing/Produced Content/`:
```
Week_32_Ball_Mastery_Under_Pressure/
├── Strategic_Content_Brief.md
├── Blog_Post_Ball_Mastery_Under_Pressure.md
├── Email_Newsletter_Ball_Mastery_Under_Pressure.md
├── Twitter_Thread_Ball_Mastery_Under_Pressure.md
├── LinkedIn_Ball_Mastery_Under_Pressure.md
├── Instagram_Carousel_Ball_Mastery_Under_Pressure.md
├── Shortform_Content_Ball_Mastery_Under_Pressure.md
├── Cheatsheet_Ball_Mastery_Under_Pressure_A4.html
└── Quality_Control_Report.md
```

## Topic Rotation System

### 27-Topic Pool Management
The system automatically manages topics from:
- **Blog Topics (7)** - From `Marketing/Blogs/` folders
- **Email Topics (10)** - From `Marketing/Emails/` folders  
- **Specialized Topics (10)** - From program folders (Game Model, Striker Clinic, etc.)
- **Seasonal Topics** - Dynamically generated based on football calendar

### 12-Week Rotation Cycles
- Prevents topic repetition within 12-week cycles
- Tracks performance metrics for optimization
- Adapts for seasonal relevance (pre-season, in-season, end-season)
- Maintains minimum 4-week gap between topic repeats

## Quality Control Standards

### Automated Quality Checks
- **British English Compliance** - Flags American spellings
- **Voice Consistency** - Checks authority markers and community focus
- **Value Equation Scoring** - Evaluates dream outcome, likelihood, time delay, effort
- **Fabrication Detection** - Prevents fake stories or testimonials
- **Word Count Validation** - Ensures appropriate length for each format
- **Structure Verification** - Confirms format-specific requirements
- **Academy Integration** - Ensures natural community promotion

### Quality Thresholds
- **Minimum Overall Score:** 35/100
- **British English:** 80/100
- **Voice Consistency:** 85/100
- **Authority Positioning:** 70/100
- **Zero Fabrication Tolerance**

## Content Templates

### Template System
All templates are auto-created with Kevin's voice and style:
- **Blog Post Template** - Complete 8-section structure
- **Email Newsletter Template** - Conversion-optimized format
- **Social Media Templates** - Platform-specific formats
- **Cheat Sheet Template** - Professional A4 HTML layout

### Customization
Templates can be modified in the `Content_Templates/` folder:
- `blog_post_template.md`
- `email_newsletter_template.md`
- `twitter_thread_template.md`
- `linkedin_article_template.md`
- `instagram_carousel_template.md`
- `shortform_tweets_template.md`
- `youtube_short_template.md`
- `cheatsheet_template.html`

## Error Handling & Recovery

### Automatic Recovery Features
- **Retry Logic** - Up to 3 attempts for failed operations
- **Error Logging** - Detailed logs in `logs/` directory
- **Progress Tracking** - Resume from last successful stage
- **Quality Gate Enforcement** - Prevents low-quality content publication

### Manual Recovery Options
```bash
# Force specific topic selection
python Topic_Selection_Manager.py force-select "Topic Name"

# Regenerate failed content piece
python Subagent_Orchestrator.py test-blog "Topic Name"

# Review quality issues
python Quality_Control_System.py test-review "Week_Folder"
```

## Performance Monitoring

### Weekly Progress Tracking
- Real-time progress updates in `progress/` folder
- Completion percentage calculation
- Quality score tracking per content piece
- Publication readiness assessment

### Topic Performance Analytics
- Engagement metrics by topic
- Conversion tracking
- Quality score trends
- Community response analysis

## Troubleshooting

### Common Issues

#### 1. "Marketing folder not found"
**Solution:** Ensure you're running from the main 360tft directory with Marketing/ folder present.

#### 2. "Topic pool empty"
**Solution:** Verify Marketing/Blogs/ and Marketing/Emails/ folders contain topic folders.

#### 3. "Quality scores below threshold"
**Solution:** Review Quality_Control_Report.md for specific improvement suggestions.

#### 4. "Voice guidelines not loaded"
**Solution:** Ensure Marketing/Voice/Voice file exists with Kevin's voice guidelines.

### Debug Mode
Enable detailed logging by setting:
```python
logging.basicConfig(level=logging.DEBUG)
```

## Customization Options

### Schedule Modification
Edit `automation_config.json`:
```json
{
  "schedule": {
    "sunday_planning": "09:00",
    "monday_blog": "10:00",
    "tuesday_email": "10:00"
  }
}
```

### Quality Thresholds
Modify `quality_thresholds` in config:
```json
{
  "quality_thresholds": {
    "value_equation_minimum": 35,
    "british_english_compliance": 1.0,
    "voice_consistency_minimum": 0.9
  }
}
```

### Content Parameters
Adjust target lengths in `orchestrator_config.json`:
```json
{
  "content_templates": {
    "blog_word_count_target": 2500,
    "email_word_count_target": 1000,
    "twitter_thread_length": 10
  }
}
```

## Integration with Existing Workflow

### Existing Content Integration
- Reads existing blog and email topics from Marketing/ folders
- Maintains consistency with established voice guidelines
- Integrates with existing cheat sheet library
- Preserves current folder structure

### Academy Integration Points
- Natural Football Coaching Academy promotion
- Community size references (1,000+ coaches)
- Resource linking and value propositions
- Member benefit highlighting

## Backup & Data Management

### Important Data Locations
- **Topic rotation history:** `topic_data/rotation_history.json`
- **Performance metrics:** `topic_data/performance_data.json`
- **Progress tracking:** `progress/week_*.json`
- **Quality reports:** Content folders and `quality_reports/`

### Backup Recommendations
- Weekly backup of `topic_data/` folder
- Archive completed week folders
- Export performance analytics monthly
- Backup configuration files before changes

## Support & Maintenance

### Regular Maintenance Tasks
- **Weekly:** Review quality reports and performance metrics
- **Monthly:** Analyze topic performance and optimize rotation
- **Quarterly:** Update voice guidelines and templates
- **Annually:** Review and refresh topic pool

### System Updates
The automation system is designed for easy updates:
- Template modifications take effect immediately
- Configuration changes apply to next execution
- Voice guideline updates improve quality scoring
- Topic pool additions are auto-detected

## Success Metrics

### Weekly Output Targets
- **10 content pieces** per week minimum
- **1 cheat sheet** in A4 format
- **35+ quality score** for all pieces
- **100% British English compliance**
- **Zero fabricated content**

### Long-term Objectives
- **Consistent brand voice** across all platforms
- **Systematic topic coverage** over 12-week cycles
- **Community growth** through quality content
- **Improved conversion rates** via Value Equation optimization

---

## Quick Start Checklist

1. ✅ Verify directory structure and Marketing/ folder exists
2. ✅ Install required Python packages
3. ✅ Run first manual week execution: `python Weekly_Content_Automation.py run-week`
4. ✅ Review generated content and quality report
5. ✅ Adjust configuration if needed
6. ✅ Set up automated scheduling: `python Weekly_Content_Automation.py schedule`
7. ✅ Monitor weekly progress and quality metrics

The 360TFT Weekly Content Automation System is now ready to generate consistent, high-quality content that maintains Kevin's authentic voice while scaling content production across all platforms.

**Next Steps:** Run your first week manually to test the system, then enable automated scheduling for hands-free operation.

---
*360TFT Content Automation System v1.0 - Created for Kevin Middleton*