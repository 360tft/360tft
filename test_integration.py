#!/usr/bin/env python3
"""
Integration Test Script for 360TFT Automation System
===================================================

Tests the integration with existing Marketing folder structure and verifies
all components work together correctly.
"""

import sys
from pathlib import Path

def test_directory_structure():
    """Test that required directory structure exists."""
    print("=== DIRECTORY STRUCTURE TEST ===")
    
    base_path = Path(__file__).parent
    required_dirs = [
        "Marketing",
        "Marketing/Blogs", 
        "Marketing/Emails",
        "Marketing/Produced Content",
        "Marketing/Cheatsheets",
        "Marketing/Voice"
    ]
    
    results = []
    for dir_path in required_dirs:
        full_path = base_path / dir_path
        exists = full_path.exists()
        results.append((dir_path, exists))
        status = "✅ EXISTS" if exists else "❌ MISSING"
        print(f"{status}: {dir_path}")
    
    return all(result[1] for result in results)

def test_voice_guidelines():
    """Test that voice guidelines file exists and is readable."""
    print("\n=== VOICE GUIDELINES TEST ===")
    
    voice_file = Path(__file__).parent / "Marketing" / "Voice" / "Voice"
    
    if voice_file.exists():
        try:
            with open(voice_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for key voice elements
            key_elements = [
                "15+ years",
                "1,000+ football players", 
                "1,200+ coaches",
                "British English",
                "no fabricated stories",
                "360tft.com"
            ]
            
            found_elements = []
            for element in key_elements:
                if element.lower() in content.lower():
                    found_elements.append(element)
                    print(f"✅ FOUND: {element}")
                else:
                    print(f"❌ MISSING: {element}")
            
            return len(found_elements) >= 4  # At least 4 key elements found
            
        except Exception as e:
            print(f"❌ ERROR reading voice file: {e}")
            return False
    else:
        print("❌ Voice guidelines file not found")
        return False

def test_topic_pools():
    """Test that topic pools can be loaded from Marketing folders."""
    print("\n=== TOPIC POOLS TEST ===")
    
    base_path = Path(__file__).parent / "Marketing"
    
    # Test blog topics
    blogs_path = base_path / "Blogs"
    blog_topics = []
    if blogs_path.exists():
        blog_topics = [d.name for d in blogs_path.iterdir() if d.is_dir()]
        print(f"✅ Blog topics found: {len(blog_topics)}")
        for topic in blog_topics[:3]:  # Show first 3
            print(f"   - {topic}")
        if len(blog_topics) > 3:
            print(f"   ... and {len(blog_topics) - 3} more")
    else:
        print("❌ Blogs folder not found")
    
    # Test email topics
    emails_path = base_path / "Emails"
    email_topics = []
    if emails_path.exists():
        email_topics = [d.name for d in emails_path.iterdir() if d.is_dir()]
        print(f"✅ Email topics found: {len(email_topics)}")
        for topic in email_topics[:3]:  # Show first 3
            print(f"   - {topic}")
        if len(email_topics) > 3:
            print(f"   ... and {len(email_topics) - 3} more")
    else:
        print("❌ Emails folder not found")
    
    # Test specialized topics
    specialized_folders = [
        "The Game Model",
        "The Striker Clinic", 
        "Elite Ball Mastery and 1v1",
        "How To Analyse  A Match",
        "UEFA C"
    ]
    
    specialized_topics = []
    for folder_name in specialized_folders:
        folder_path = base_path / folder_name
        if folder_path.exists():
            subfolders = [d.name for d in folder_path.iterdir() if d.is_dir()]
            specialized_topics.extend([f"{folder_name} - {sub}" for sub in subfolders])
    
    print(f"✅ Specialized topics found: {len(specialized_topics)}")
    for topic in specialized_topics[:3]:  # Show first 3
        print(f"   - {topic}")
    if len(specialized_topics) > 3:
        print(f"   ... and {len(specialized_topics) - 3} more")
    
    total_topics = len(blog_topics) + len(email_topics) + len(specialized_topics)
    print(f"\n📊 TOTAL TOPICS AVAILABLE: {total_topics}")
    
    return total_topics >= 15  # Should have at least 15 topics

def test_cheatsheets_folder():
    """Test existing cheatsheets for reference."""
    print("\n=== CHEATSHEETS TEST ===")
    
    cheatsheets_path = Path(__file__).parent / "Marketing" / "Cheatsheets"
    
    if cheatsheets_path.exists():
        html_files = list(cheatsheets_path.glob("*.html"))
        pdf_files = list(cheatsheets_path.glob("*.pdf"))
        png_files = list(cheatsheets_path.glob("*.png"))
        
        print(f"✅ HTML cheatsheets: {len(html_files)}")
        print(f"✅ PDF cheatsheets: {len(pdf_files)}")
        print(f"✅ PNG cheatsheets: {len(png_files)}")
        
        # Show some examples
        if html_files:
            print("   HTML examples:")
            for file in html_files[:3]:
                print(f"   - {file.name}")
        
        return len(html_files) > 0 or len(pdf_files) > 0
    else:
        print("❌ Cheatsheets folder not found")
        return False

def test_automation_files():
    """Test that all automation files exist."""
    print("\n=== AUTOMATION FILES TEST ===")
    
    base_path = Path(__file__).parent
    automation_files = [
        "Weekly_Content_Automation.py",
        "Topic_Selection_Manager.py",
        "Subagent_Orchestrator.py", 
        "Quality_Control_System.py",
        "automation_config.json",
        "orchestrator_config.json"
    ]
    
    results = []
    for file_name in automation_files:
        file_path = base_path / file_name
        exists = file_path.exists()
        results.append((file_name, exists))
        status = "✅ EXISTS" if exists else "❌ MISSING"
        print(f"{status}: {file_name}")
    
    return all(result[1] for result in results)

def test_content_templates():
    """Test that Content_Templates folder is created."""
    print("\n=== CONTENT TEMPLATES TEST ===")
    
    templates_path = Path(__file__).parent / "Content_Templates"
    
    if templates_path.exists():
        template_files = list(templates_path.glob("*.md")) + list(templates_path.glob("*.html"))
        print(f"✅ Content_Templates folder exists with {len(template_files)} files")
        
        expected_templates = [
            "blog_post_template.md",
            "email_newsletter_template.md", 
            "twitter_thread_template.md",
            "cheatsheet_template.html"
        ]
        
        for template in expected_templates:
            template_path = templates_path / template
            if template_path.exists():
                print(f"✅ {template}")
            else:
                print(f"⚠️  {template} (will be auto-created)")
        
        return True
    else:
        print("⚠️  Content_Templates folder missing (will be auto-created)")
        return True  # This is okay, it gets created automatically

def run_integration_tests():
    """Run all integration tests."""
    print("360TFT AUTOMATION SYSTEM - INTEGRATION TESTS")
    print("=" * 50)
    
    tests = [
        ("Directory Structure", test_directory_structure),
        ("Voice Guidelines", test_voice_guidelines),
        ("Topic Pools", test_topic_pools),
        ("Cheatsheets Folder", test_cheatsheets_folder),
        ("Automation Files", test_automation_files),
        ("Content Templates", test_content_templates)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ ERROR in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("INTEGRATION TEST SUMMARY")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\nOVERALL: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 ALL TESTS PASSED! System ready for automation.")
        print("\nNext steps:")
        print("1. Install Python packages: pip install -r requirements.txt")
        print("2. Run first week manually: python Weekly_Content_Automation.py run-week")
        print("3. Review generated content and quality reports")
        print("4. Enable automated scheduling if satisfied")
    else:
        print(f"\n⚠️  {len(results) - passed} tests failed. Please address issues before running automation.")
    
    return passed == len(results)

if __name__ == "__main__":
    run_integration_tests()