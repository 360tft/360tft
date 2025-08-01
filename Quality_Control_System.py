#!/usr/bin/env python3
"""
360TFT Quality Control System
=============================

Automated QC system for voice consistency, British English usage, Value Equation scoring,
fabricated content detection, and quality report generation.

Author: Kevin Middleton (360TFT)
Version: 1.0
"""

import os
import json
import logging
import datetime
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import statistics


class QualityControlSystem:
    """
    Comprehensive quality control system for 360TFT content automation.
    
    Ensures voice consistency, British English compliance, Value Equation scoring,
    and generates detailed quality reports for all content pieces.
    """
    
    def __init__(self, voice_path: Path):
        """
        Initialize the Quality Control System.
        
        Args:
            voice_path: Path to voice guidelines folder
        """
        self.voice_path = Path(voice_path)
        self.base_path = Path(__file__).parent
        self.reports_path = self.base_path / "quality_reports"
        self.reports_path.mkdir(exist_ok=True)
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Load voice guidelines and quality standards
        self.voice_guidelines = self._load_voice_guidelines()
        self.quality_standards = self._load_quality_standards()
        
        # Initialize quality dictionaries
        self.british_terms = self._load_british_terms()
        self.american_terms = self._load_american_terms()
        self.authority_markers = self._load_authority_markers()
        self.fabrication_indicators = self._load_fabrication_indicators()
        self.value_equation_keywords = self._load_value_equation_keywords()
        
        self.logger.info("Quality Control System initialized")
    
    def _load_voice_guidelines(self) -> Dict:
        """Load voice guidelines from Voice folder."""
        voice_file = self.voice_path / "Voice"
        
        if voice_file.exists():
            with open(voice_file, 'r', encoding='utf-8') as f:
                voice_content = f.read()
            
            # Parse voice guidelines
            guidelines = {
                "experience_years": "15+",
                "players_trained": "1,000+", 
                "coaches_educated": "1,200+",
                "no_em_dashes": True,
                "british_english_only": True,
                "no_fabricated_stories": True,
                "authority_positioning": True,
                "community_focus": True,
                "seth_godin_style": True,
                "doug_lemov_influence": True,
                "hormozi_influence": True
            }
            
            return guidelines
        
        return {}
    
    def _load_quality_standards(self) -> Dict:
        """Load quality standards and thresholds."""
        return {
            "value_equation_minimum": 35,
            "british_english_score_minimum": 0.8,
            "voice_consistency_minimum": 0.85,
            "authority_score_minimum": 0.7,
            "fabrication_tolerance": 0.0,
            "word_count_ranges": {
                "blog": (1500, 3000),
                "email": (800, 1200),
                "twitter_thread": (200, 400),
                "linkedin": (800, 1200),
                "instagram": (100, 300),
                "shortform": (50, 150),
                "cheatsheet": (500, 1500)
            }
        }
    
    def _load_british_terms(self) -> Dict[str, str]:
        """Load British English terms and their American counterparts."""
        return {
            # Spelling variations
            "colour": "color",
            "favourite": "favorite", 
            "realise": "realize",
            "analyse": "analyze",
            "centre": "center",
            "defence": "defense",
            "offence": "offense",
            "organised": "organized",
            "recognised": "recognized",
            "specialised": "specialized",
            "emphasise": "emphasize",
            "criticise": "criticize",
            "theatre": "theater",
            "metre": "meter",
            "litre": "liter",
            # Football-specific terms
            "football": "soccer",
            "pitch": "field",
            "kit": "uniform",
            "boots": "cleats",
            "nil": "zero",
            "match": "game",
            "fixture": "game",
            "squad": "team",
            "keeper": "goalie",
            "midfielder": "midfield player"
        }
    
    def _load_american_terms(self) -> List[str]:
        """Load American English terms to flag."""
        return list(self.british_terms.values())
    
    def _load_authority_markers(self) -> Dict[str, float]:
        """Load authority positioning markers with weights."""
        return {
            "15+ years": 2.0,
            "1,000+ players": 2.0,
            "1,200+ coaches": 1.5,
            "experience": 1.0,
            "worked with": 1.0,
            "trained": 1.0,
            "coached": 1.0,
            "360TFT": 1.5,
            "methodology": 1.0,
            "system": 1.0,
            "systematic": 1.0,
            "proven": 1.0,
            "academy": 1.5,
            "professional": 1.0,
            "grassroots": 1.0
        }
    
    def _load_fabrication_indicators(self) -> List[str]:
        """Load indicators of fabricated content."""
        return [
            # Specific names without context
            r'\b[A-Z][a-z]+ from [A-Z][a-z]+\b',  # "John from Manchester"
            r'\bcoach [A-Z][a-z]+\b',  # "coach Smith"
            r'\bplayer [A-Z][a-z]+\b',  # "player Jones"
            # Overly specific scenarios
            r'last week.*player.*scored.*goal',
            r'yesterday.*session.*transformed',
            r'just received.*email.*coach',
            # Fabricated testimonials
            r'".*" - [A-Z][a-z]+ [A-Z][a-z]+',  # Quoted testimonial with name
            r'parent.*told me.*amazing',
            r'coach.*emailed.*results'
        ]
    
    def _load_value_equation_keywords(self) -> Dict[str, Dict[str, float]]:
        """Load Value Equation component keywords with weights."""
        return {
            "dream_outcome": {
                "transform": 2.0,
                "master": 2.0,
                "confident": 1.5,
                "development": 1.0,
                "improvement": 1.0,
                "progress": 1.0,
                "success": 1.5,
                "results": 1.5,
                "performance": 1.0,
                "match-winner": 2.0,
                "begging to stay": 2.0,
                "remember forever": 2.0
            },
            "perceived_likelihood": {
                "proven": 2.0,
                "guaranteed": 1.5,
                "works": 1.5,
                "tested": 1.0,
                "evidence": 1.5,
                "research": 1.0,
                "community": 1.0,
                "testimonial": 1.5,
                "case study": 1.5,
                "success story": 1.5,
                "never fails": 2.0,
                "always works": 1.5
            },
            "time_delay": {
                "immediate": 2.0,
                "instant": 2.0,
                "tonight": 3.0,
                "today": 2.0,
                "this week": 1.5,
                "next session": 2.0,
                "first session": 2.5,
                "ready to use": 2.0,
                "quick": 1.5,
                "fast": 1.0,
                "soon": 0.5
            },
            "effort_sacrifice": {
                "simple": 2.0,
                "easy": 1.5,
                "effortless": 2.0,
                "3-step": 2.5,
                "copy-paste": 2.0,
                "done-for-you": 2.0,
                "no prep": 2.5,
                "zero preparation": 2.5,
                "ready-made": 2.0,
                "systematic": 1.5,
                "organized": 1.0
            }
        }
    
    def evaluate_content(self, content: str, content_type: str) -> float:
        """
        Evaluate content quality with comprehensive scoring.
        
        Args:
            content: Content to evaluate
            content_type: Type of content (blog, email, etc.)
            
        Returns:
            Overall quality score (0-100)
        """
        self.logger.info(f"Evaluating {content_type} content quality")
        
        try:
            # Run all quality checks
            scores = {
                "british_english": self._check_british_english(content),
                "voice_consistency": self._check_voice_consistency(content),
                "authority_positioning": self._check_authority_positioning(content),
                "fabrication_check": self._check_fabrication(content),
                "value_equation": self._score_value_equation(content),
                "word_count": self._check_word_count(content, content_type),
                "structure": self._check_structure(content, content_type),
                "academy_integration": self._check_academy_integration(content)
            }
            
            # Calculate weighted overall score
            weights = {
                "british_english": 0.15,
                "voice_consistency": 0.20,
                "authority_positioning": 0.15,
                "fabrication_check": 0.15,
                "value_equation": 0.20,
                "word_count": 0.05,
                "structure": 0.05,
                "academy_integration": 0.05
            }
            
            overall_score = sum(
                scores[component] * weights[component] 
                for component in scores
            )
            
            self.logger.info(f"Quality evaluation complete. Score: {overall_score:.1f}")
            return overall_score
            
        except Exception as e:
            self.logger.error(f"Quality evaluation failed: {str(e)}")
            return 0.0
    
    def _check_british_english(self, content: str) -> float:
        """Check British English compliance."""
        content_lower = content.lower()
        
        # Count British terms
        british_count = sum(
            content_lower.count(british_term) 
            for british_term in self.british_terms.keys()
        )
        
        # Count American terms
        american_count = sum(
            content_lower.count(american_term)
            for american_term in self.american_terms
        )
        
        # Calculate ratio
        total_terms = british_count + american_count
        if total_terms == 0:
            return 80.0  # Neutral score if no specific terms found
        
        british_ratio = british_count / total_terms
        score = british_ratio * 100
        
        # Penalty for American terms
        if american_count > 0:
            score = max(score - (american_count * 10), 0)
        
        return min(score, 100.0)
    
    def _check_voice_consistency(self, content: str) -> float:
        """Check consistency with Kevin's voice guidelines."""
        score = 0.0
        
        # Check for em dashes (should not be present)
        if "—" not in content:
            score += 20
        
        # Check for authority positioning
        if any(marker in content for marker in ["15+ years", "1,000+ players", "experience"]):
            score += 25
        
        # Check for community focus
        community_terms = ["community", "coaches", "academy", "together", "support"]
        if any(term in content.lower() for term in community_terms):
            score += 20
        
        # Check for systematic approach
        system_terms = ["system", "systematic", "methodology", "approach", "framework"]
        if any(term in content.lower() for term in system_terms):
            score += 20
        
        # Check for practical implementation
        practical_terms = ["implementation", "session", "training", "practice", "apply"]
        if any(term in content.lower() for term in practical_terms):
            score += 15
        
        return min(score, 100.0)
    
    def _check_authority_positioning(self, content: str) -> float:
        """Check authority positioning markers."""
        content_lower = content.lower()
        authority_score = 0.0
        
        for marker, weight in self.authority_markers.items():
            if marker.lower() in content_lower:
                authority_score += weight
        
        # Normalize to 100-point scale
        max_possible = 10.0  # Estimated maximum score
        normalized_score = min((authority_score / max_possible) * 100, 100.0)
        
        return normalized_score
    
    def _check_fabrication(self, content: str) -> float:
        """Check for fabricated content indicators."""
        fabrication_count = 0
        
        for pattern in self.fabrication_indicators:
            matches = re.findall(pattern, content, re.IGNORECASE)
            fabrication_count += len(matches)
        
        # Return penalty score (100 - penalties)
        penalty = fabrication_count * 20  # 20 points per fabrication
        return max(100.0 - penalty, 0.0)
    
    def _score_value_equation(self, content: str) -> float:
        """Score content based on Value Equation components."""
        content_lower = content.lower()
        component_scores = {}
        
        for component, keywords in self.value_equation_keywords.items():
            component_score = 0.0
            
            for keyword, weight in keywords.items():
                if keyword in content_lower:
                    component_score += weight
            
            # Normalize to 25-point scale (100/4 components)
            max_possible = 10.0  # Estimated maximum per component
            normalized = min((component_score / max_possible) * 25, 25.0)
            component_scores[component] = normalized
        
        # Sum all component scores
        total_score = sum(component_scores.values())
        return min(total_score, 100.0)
    
    def _check_word_count(self, content: str, content_type: str) -> float:
        """Check if word count is within acceptable range."""
        word_count = len(content.split())
        
        # Get target range for content type
        ranges = self.quality_standards["word_count_ranges"]
        target_range = ranges.get(content_type, (100, 2000))
        
        min_words, max_words = target_range
        
        if min_words <= word_count <= max_words:
            return 100.0
        elif word_count < min_words:
            # Penalty for being too short
            ratio = word_count / min_words
            return max(ratio * 100, 20.0)
        else:
            # Penalty for being too long
            ratio = max_words / word_count
            return max(ratio * 100, 20.0)
    
    def _check_structure(self, content: str, content_type: str) -> float:
        """Check content structure appropriateness."""
        score = 0.0
        
        if content_type == "blog":
            # Check for headers
            if "#" in content:
                score += 30
            # Check for bullet points or lists
            if any(indicator in content for indicator in ["- ", "* ", "1. ", "2. "]):
                score += 25
            # Check for conclusion
            if any(word in content.lower() for word in ["conclusion", "summary", "transform"]):
                score += 25
            # Check for CTA
            if any(cta in content.lower() for cta in ["academy", "join", "ready", "transform"]):
                score += 20
                
        elif content_type == "email":
            # Check for subject line
            if "subject" in content.lower():
                score += 25
            # Check for personal greeting
            if any(greeting in content.lower() for greeting in ["hi", "hello", "dear"]):
                score += 25
            # Check for CTA
            if any(cta in content.lower() for cta in ["click", "join", "academy"]):
                score += 25
            # Check for sign-off
            if "kevin" in content.lower():
                score += 25
                
        elif content_type in ["twitter_thread", "shortform"]:
            # Check for engagement elements
            if any(engagement in content for engagement in ["?", "!", "💬", "🧵"]):
                score += 50
            # Check for hashtags
            if "#" in content:
                score += 25
            # Check for community interaction
            if any(interaction in content.lower() for interaction in ["comment", "share", "save"]):
                score += 25
                
        else:
            # Default structure check
            score = 75.0
        
        return min(score, 100.0)
    
    def _check_academy_integration(self, content: str) -> float:
        """Check for natural Academy integration."""
        content_lower = content.lower()
        
        academy_terms = [
            "football coaching academy",
            "academy",
            "community",
            "members",
            "resources",
            "support"
        ]
        
        integration_score = 0.0
        for term in academy_terms:
            if term in content_lower:
                integration_score += 1
        
        # Check if integration feels natural (not just mentioned)
        natural_integration = any(
            phrase in content_lower for phrase in [
                "academy members",
                "community support", 
                "complete resources",
                "join the academy",
                "academy provides"
            ]
        )
        
        if natural_integration:
            integration_score += 2
        
        # Normalize to 100-point scale
        max_score = 8.0
        normalized = min((integration_score / max_score) * 100, 100.0)
        
        return normalized
    
    def comprehensive_review(self, content_folder: Path) -> str:
        """
        Perform comprehensive quality review of all content in folder.
        
        Args:
            content_folder: Path to folder containing week's content
            
        Returns:
            Formatted quality report
        """
        self.logger.info(f"Starting comprehensive review of {content_folder}")
        
        report_data = {
            "review_date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "content_folder": str(content_folder),
            "files_reviewed": [],
            "overall_scores": {},
            "detailed_scores": {},
            "recommendations": [],
            "passed_quality_gates": True,
            "summary": {}
        }
        
        # Review all content files
        content_files = list(content_folder.glob("*.md")) + list(content_folder.glob("*.html"))
        
        for file_path in content_files:
            if file_path.name.startswith("Quality_Control_Report"):
                continue  # Skip existing reports
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Determine content type from filename
                content_type = self._determine_content_type(file_path.name)
                
                # Evaluate content
                overall_score = self.evaluate_content(content, content_type)
                
                # Detailed component scores
                detailed_scores = self._get_detailed_scores(content, content_type)
                
                # Store results
                report_data["files_reviewed"].append(file_path.name)
                report_data["overall_scores"][file_path.name] = overall_score
                report_data["detailed_scores"][file_path.name] = detailed_scores
                
                # Check if passed quality gate
                if overall_score < self.quality_standards["value_equation_minimum"]:
                    report_data["passed_quality_gates"] = False
                    report_data["recommendations"].append(
                        f"{file_path.name}: Score {overall_score:.1f} below minimum {self.quality_standards['value_equation_minimum']}"
                    )
                
            except Exception as e:
                self.logger.error(f"Error reviewing {file_path}: {str(e)}")
                report_data["recommendations"].append(f"Error reviewing {file_path.name}: {str(e)}")
        
        # Calculate summary statistics
        if report_data["overall_scores"]:
            scores = list(report_data["overall_scores"].values())
            report_data["summary"] = {
                "average_score": statistics.mean(scores),
                "min_score": min(scores),
                "max_score": max(scores),
                "files_passed": sum(1 for score in scores if score >= self.quality_standards["value_equation_minimum"]),
                "total_files": len(scores)
            }
        
        # Generate formatted report
        formatted_report = self._format_quality_report(report_data)
        
        # Save report
        report_file = content_folder / "Quality_Control_Report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(formatted_report)
        
        self.logger.info("Comprehensive review completed")
        return formatted_report
    
    def _determine_content_type(self, filename: str) -> str:
        """Determine content type from filename."""
        filename_lower = filename.lower()
        
        if "blog" in filename_lower:
            return "blog"
        elif "email" in filename_lower:
            return "email"
        elif "twitter" in filename_lower:
            return "twitter_thread"
        elif "linkedin" in filename_lower:
            return "linkedin"
        elif "instagram" in filename_lower:
            return "instagram"
        elif "shortform" in filename_lower:
            return "shortform"
        elif "cheatsheet" in filename_lower:
            return "cheatsheet"
        else:
            return "general"
    
    def _get_detailed_scores(self, content: str, content_type: str) -> Dict[str, float]:
        """Get detailed component scores for content."""
        return {
            "british_english": self._check_british_english(content),
            "voice_consistency": self._check_voice_consistency(content),
            "authority_positioning": self._check_authority_positioning(content),
            "fabrication_check": self._check_fabrication(content),
            "value_equation": self._score_value_equation(content),
            "word_count": self._check_word_count(content, content_type),
            "structure": self._check_structure(content, content_type),
            "academy_integration": self._check_academy_integration(content)
        }
    
    def _format_quality_report(self, report_data: Dict) -> str:
        """Format quality report as markdown."""
        report = f"""# 360TFT Quality Control Report

**Generated:** {report_data['review_date']}  
**Content Folder:** {report_data['content_folder']}  
**Files Reviewed:** {len(report_data['files_reviewed'])}

## Summary

"""
        
        if report_data["summary"]:
            summary = report_data["summary"]
            report += f"""- **Average Score:** {summary['average_score']:.1f}/100
- **Score Range:** {summary['min_score']:.1f} - {summary['max_score']:.1f}
- **Quality Gate Status:** {'✅ PASSED' if report_data['passed_quality_gates'] else '❌ FAILED'}
- **Files Passed:** {summary['files_passed']}/{summary['total_files']}

"""
        
        # Overall scores
        report += "## Overall Scores\n\n"
        for filename, score in report_data["overall_scores"].items():
            status = "✅" if score >= self.quality_standards["value_equation_minimum"] else "❌"
            report += f"- {status} **{filename}:** {score:.1f}/100\n"
        
        # Detailed breakdown
        report += "\n## Detailed Component Scores\n\n"
        for filename, scores in report_data["detailed_scores"].items():
            report += f"### {filename}\n\n"
            for component, score in scores.items():
                component_name = component.replace('_', ' ').title()
                report += f"- **{component_name}:** {score:.1f}/100\n"
            report += "\n"
        
        # Recommendations
        if report_data["recommendations"]:
            report += "## Recommendations\n\n"
            for recommendation in report_data["recommendations"]:
                report += f"- {recommendation}\n"
        
        # Quality standards reference
        report += f"""
## Quality Standards Reference

- **Minimum Overall Score:** {self.quality_standards['value_equation_minimum']}/100
- **British English Minimum:** {self.quality_standards['british_english_score_minimum']*100:.0f}/100
- **Voice Consistency Minimum:** {self.quality_standards['voice_consistency_minimum']*100:.0f}/100
- **Authority Score Minimum:** {self.quality_standards['authority_score_minimum']*100:.0f}/100
- **Fabrication Tolerance:** {self.quality_standards['fabrication_tolerance']*100:.0f}/100

## Component Weights

- **British English:** 15%
- **Voice Consistency:** 20%
- **Authority Positioning:** 15%
- **Fabrication Check:** 15%
- **Value Equation:** 20%
- **Word Count:** 5%
- **Structure:** 5%
- **Academy Integration:** 5%

---
*Generated by 360TFT Quality Control System v1.0*
"""
        
        return report
    
    def generate_improvement_suggestions(self, content: str, content_type: str) -> List[str]:
        """
        Generate specific improvement suggestions for content.
        
        Args:
            content: Content to analyze
            content_type: Type of content
            
        Returns:
            List of improvement suggestions
        """
        suggestions = []
        detailed_scores = self._get_detailed_scores(content, content_type)
        
        # British English suggestions
        if detailed_scores["british_english"] < 80:
            american_found = []
            for american_term in self.american_terms:
                if american_term in content.lower():
                    british_equivalent = next(
                        (british for british, american in self.british_terms.items() if american == american_term),
                        None
                    )
                    if british_equivalent:
                        american_found.append(f"'{american_term}' → '{british_equivalent}'")
            
            if american_found:
                suggestions.append(f"British English: Replace {', '.join(american_found)}")
        
        # Voice consistency suggestions
        if detailed_scores["voice_consistency"] < 80:
            if "15+ years" not in content and "1,000+ players" not in content:
                suggestions.append("Voice: Add authority markers (15+ years, 1,000+ players)")
            
            if not any(term in content.lower() for term in ["system", "systematic", "methodology"]):
                suggestions.append("Voice: Include systematic approach language")
        
        # Authority positioning suggestions
        if detailed_scores["authority_positioning"] < 70:
            suggestions.append("Authority: Strengthen credibility with experience references and 360TFT methodology")
        
        # Value Equation suggestions
        if detailed_scores["value_equation"] < 70:
            ve_suggestions = []
            if "transform" not in content.lower():
                ve_suggestions.append("Add transformation language")
            if "tonight" not in content.lower() and "immediate" not in content.lower():
                ve_suggestions.append("Add urgency/immediate implementation")
            if "simple" not in content.lower() and "3-step" not in content.lower():
                ve_suggestions.append("Emphasize simplicity")
            
            if ve_suggestions:
                suggestions.append(f"Value Equation: {', '.join(ve_suggestions)}")
        
        # Academy integration suggestions
        if detailed_scores["academy_integration"] < 60:
            suggestions.append("Academy: Add natural integration with community benefits")
        
        # Structure suggestions
        if detailed_scores["structure"] < 70:
            if content_type == "blog" and "#" not in content:
                suggestions.append("Structure: Add section headers with #")
            elif content_type == "email" and "subject" not in content.lower():
                suggestions.append("Structure: Include subject line options")
        
        return suggestions


def main():
    """Main entry point for testing Quality Control System."""
    import sys
    
    # Setup for testing
    voice_path = Path(__file__).parent / "Marketing" / "Voice"
    
    if not voice_path.exists():
        print("Voice folder not found. Please run from 360tft directory.")
        return
    
    qc_system = QualityControlSystem(voice_path)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "test-content" and len(sys.argv) > 2:
            test_content = " ".join(sys.argv[2:])
            score = qc_system.evaluate_content(test_content, "blog")
            print(f"Quality Score: {score:.1f}/100")
            
            suggestions = qc_system.generate_improvement_suggestions(test_content, "blog")
            if suggestions:
                print("\nImprovement Suggestions:")
                for suggestion in suggestions:
                    print(f"- {suggestion}")
            
        elif command == "test-file" and len(sys.argv) > 2:
            file_path = Path(sys.argv[2])
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content_type = qc_system._determine_content_type(file_path.name)
                score = qc_system.evaluate_content(content, content_type)
                
                print(f"File: {file_path.name}")
                print(f"Type: {content_type}")
                print(f"Quality Score: {score:.1f}/100")
                
                # Detailed scores
                detailed = qc_system._get_detailed_scores(content, content_type)
                print("\nDetailed Scores:")
                for component, component_score in detailed.items():
                    print(f"- {component.replace('_', ' ').title()}: {component_score:.1f}/100")
                
            else:
                print(f"File not found: {file_path}")
                
        elif command == "test-review" and len(sys.argv) > 2:
            folder_path = Path(sys.argv[2])
            if folder_path.exists() and folder_path.is_dir():
                report = qc_system.comprehensive_review(folder_path)
                print("=== QUALITY CONTROL REPORT ===")
                print(report)
            else:
                print(f"Folder not found: {folder_path}")
                
        else:
            print("Usage: python Quality_Control_System.py [test-content|test-file|test-review] [content/file/folder]")
    
    else:
        print("360TFT Quality Control System")
        print("Usage: python Quality_Control_System.py [test-content|test-file|test-review] [content/file/folder]")


if __name__ == "__main__":
    main()