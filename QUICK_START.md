# 360TFT Content Automation - Quick Start Guide

**Get your content automation running in 5 minutes**

## Prerequisites
✅ Python 3.8+ installed  
✅ Marketing folder with Voice, Blogs, and Emails directories  
✅ Existing subagent files (Weekly_Content_Automation.py, etc.)  

---

## 🚀 5-Minute Setup

### Step 1: Initialize the System (2 minutes)
```bash
# Run the initialization script
python initialize_automation.py

# This will:
# - Create 10 topic folders in Marketing/Produced Content/
# - Validate your voice guidelines
# - Create rotation schedule for 12 weeks
# - Test subagent connectivity
# - Generate Week 1 detailed plan
```

### Step 2: Verify Setup (1 minute)
```bash
# Check the setup worked
ls "Marketing/Produced Content/"
# Should show 10 topic folders

# Check for configuration files
ls *.json
# Should show content_templates.json, quality_standards.json, automation_schedule.json
```

### Step 3: Start Content Creation (2 minutes)
```bash
# Create your first week's content
python Weekly_Content_Automation.py

# Monitor progress
python automation_dashboard.py
```

---

## 📁 What Gets Created

### Topic Folders (10 total)
```
Marketing/Produced Content/
├── A_Practical_Guide_for_Development_Professionals/
├── How_To_Run_Better_Rondos/
├── Learning_One_Position_Versus_Many/
├── The_Session_Planning_System_That_Actually_Works/
├── Top_8_Small_Sided_Games_That_Actually_Improve_Your_Players/
├── Training_On_Your_Own/
├── Why_So_Many_Youth_Football_Sessions_Don't_Stick/
├── The_Passing_Drill_That_Changes_Everything/
├── 1v1_Moves_That_Beat_Defenders_Every_Time/
└── Finishing_Practice_Players_Actually_Enjoy/
```

### Configuration Files
- `content_templates.json` - Blog, email, social media structures
- `quality_standards.json` - British English and voice requirements
- `automation_schedule.json` - Weekly creation schedule
- `AUTOMATION_INITIALIZATION_REPORT.md` - Full setup report

---

## 🎯 First Week Walkthrough

### Sunday: Planning (2 hours)
- **What happens**: System selects topic and creates content angles
- **Output**: Content brief for the week
- **Action needed**: Review and approve topic selection

### Monday: Blog Creation (3 hours)  
- **What happens**: 2,500-word blog post created
- **Output**: `Blog_Post_[Topic].md` in topic folder
- **Action needed**: Review for technical accuracy

### Tuesday: Email Newsletter (1.5 hours)
- **What happens**: 1,000-word email newsletter created
- **Output**: `Email_Newsletter_[Topic].md` in topic folder  
- **Action needed**: Review call-to-action alignment

### Wednesday: Social Media (2 hours)
- **What happens**: Twitter thread, Instagram carousel, LinkedIn post
- **Output**: Multiple social files in topic folder
- **Action needed**: Schedule in your social media tools

### Thursday: Short-form Content (1 hour)
- **What happens**: Tweet variations and bite-sized tips
- **Output**: `Tweet_Shortform_[Topic].md` in topic folder
- **Action needed**: Queue for daily posting

### Friday: Visual Content (2 hours)
- **What happens**: Cheatsheet or infographic creation
- **Output**: PDF or image file in topic folder
- **Action needed**: Review visual design

### Saturday: Quality Control (1 hour)
- **What happens**: Final review and quality scoring
- **Output**: Quality report and approved content
- **Action needed**: Approve for publishing

---

## 🔧 Common Issues & Solutions

### Issue: "Voice file not found"
**Solution**: 
```bash
# Check voice file exists
ls "Marketing/Voice/Voice"

# If missing, create voice guidelines file
echo "Your voice guidelines here" > "Marketing/Voice/Voice"
```

### Issue: "Topic folders not created"
**Solution**:
```bash
# Manually create missing folders
mkdir -p "Marketing/Produced Content/[Topic_Name]"

# Or re-run initialization
python initialize_automation.py
```

### Issue: "Subagent files not accessible"
**Solution**:
```bash
# Check all automation files exist
ls Weekly_Content_Automation.py
ls Subagent_Orchestrator.py
ls Topic_Selection_Manager.py
ls Quality_Control_System.py

# If missing, you'll need to create them or get them from backup
```

### Issue: "Low quality scores"
**Solutions**:
- Review `quality_standards.json` settings
- Check British English compliance
- Verify voice consistency in `Marketing/Voice/Voice`
- Ensure 360TFT brand elements are included

### Issue: "Content not being created"
**Debug steps**:
```bash
# Check current directory
pwd
# Should be in your 360tft root folder

# Check Python path
python --version
# Should be 3.8+

# Run dashboard for status
python automation_dashboard.py
```

---

## 📊 Quality Standards

### Voice Requirements
- ✅ British English spelling (colour, favourite, realise)
- ✅ Football terminology (not soccer)
- ✅ Professional but accessible tone
- ✅ 15+ years experience references
- ✅ 1,000+ players, 1,200+ coaches statistics
- ❌ No em dashes
- ❌ No fabricated stories

### Content Standards
- **Blog posts**: 2,500 words target
- **Email newsletters**: 1,000 words target  
- **Twitter threads**: 10 tweets maximum
- **Instagram carousels**: 7 slides maximum
- **Value equation score**: 35+ minimum

### Brand Integration
- 360TFT academy mentions
- Kevin Middleton authority references
- Community size indicators (1,000+ members)
- Clear call-to-actions to courses/academy

---

## 🔄 Weekly Maintenance (15 minutes)

### Every Sunday
1. Check `automation_dashboard.py` for system status
2. Review previous week's quality scores
3. Adjust topic rotation if needed
4. Update configuration files if required

### Every Month
1. Review all topic folder content
2. Update voice guidelines if coaching style evolves
3. Analyze performance metrics
4. Back up all produced content

---

## 📈 Performance Monitoring

### Dashboard Metrics
- **Content creation status**: Shows daily progress
- **Quality scores**: Voice, British English, value equation
- **Topic rotation**: Current and upcoming topics
- **Weekly stats**: Words written, formats created

### Quality Alerts
- Voice consistency below 90%
- British English compliance issues
- Value equation scores under 35
- Missing brand integration

---

## 🆘 Emergency Procedures

### If automation stops working:
1. Check `AUTOMATION_INITIALIZATION_REPORT.md` for last status
2. Run `python automation_dashboard.py` for current state
3. Re-run `python initialize_automation.py` to reset
4. Contact system administrator if issues persist

### If quality drops significantly:
1. Review recent changes to voice guidelines
2. Check configuration files for modifications
3. Manually review and edit problematic content
4. Update quality thresholds in `automation_config.json`

### If content doesn't match Kevin's style:
1. Update `Marketing/Voice/Voice` with specific examples
2. Review `quality_standards.json` voice settings
3. Manually edit recent content to set examples
4. Re-run quality control on previous week's content

---

## 🎯 Success Checklist

After setup, you should have:
- [ ] 10 topic folders created and accessible
- [ ] Configuration files properly generated
- [ ] Voice guidelines validated and loaded
- [ ] First week's content plan ready
- [ ] Quality control system operational
- [ ] Dashboard showing system status
- [ ] Rotation schedule for next 12 weeks

**System Status**: ✅ Ready for automated content creation

---

## 📞 Support & Next Steps

### Immediate Actions
1. Run your first automation cycle
2. Review output quality in topic folders
3. Adjust settings based on initial results
4. Set up weekly monitoring routine

### Advanced Configuration
- Modify `content_templates.json` for custom structures
- Update `quality_standards.json` for stricter requirements
- Adjust `automation_schedule.json` for different timing
- Customize topic rotation in dashboard

### Getting Help
- Check `AUTOMATION_INITIALIZATION_REPORT.md` for detailed logs
- Use `automation_dashboard.py` for real-time status
- Review topic folders for content examples
- Consult configuration files for current settings

**Ready to automate**: Your 360TFT content system is now operational and ready to produce consistent, high-quality coaching content across all formats.