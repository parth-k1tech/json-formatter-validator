import os
import argparse
from pathlib import Path

class TemplateGenerator:
    def __init__(self, output_dir=".github"):
        self.output_dir = output_dir
        self.templates = {
            "bug_report": {
                "path": "ISSUE_TEMPLATE/bug_report.md",
                "content": '''---
name: Bug Report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows, macOS, Linux]
 - Browser: [e.g. Chrome, Firefox, Safari]
 - Version: [e.g. 22]

**Additional context**
Add any other context about the problem here.'''
            },
            "feature_request": {
                "path": "ISSUE_TEMPLATE/feature_request.md",
                "content": '''---
name: Feature Request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.'''
            },
            "pull_request": {
                "path": "PULL_REQUEST_TEMPLATE.md",
                "content": '''## Description
Please include a summary of the changes and which issue is fixed. Please also include relevant motivation and context.

Fixes # (issue)

## Type of change
Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

## How Has This Been Tested?
Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce.

## Checklist:
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes'''
            }
        }

    def create_directory_if_not_exists(self, path):
        """Create directory if it doesn't exist"""
        if not os.path.exists(path):
            os.makedirs(path)

    def generate_templates(self, templates=None):
        """Generate the specified templates or all templates if none specified"""
        if templates is None:
            templates = list(self.templates.keys())

        # Create base .github directory
        github_dir = Path(self.output_dir)
        self.create_directory_if_not_exists(github_dir)

        # Create ISSUE_TEMPLATE directory
        issue_template_dir = github_dir / "ISSUE_TEMPLATE"
        self.create_directory_if_not_exists(issue_template_dir)

        generated_files = []
        for template_name in templates:
            if template_name in self.templates:
                template = self.templates[template_name]
                file_path = github_dir / template["path"]
                
                # Create any necessary parent directories
                self.create_directory_if_not_exists(file_path.parent)
                
                # Write the template content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(template["content"])
                generated_files.append(str(file_path))
            else:
                print(f"Warning: Template '{template_name}' not found")

        return generated_files

def main():
    parser = argparse.ArgumentParser(description='Generate GitHub Issue and PR templates')
    parser.add_argument('--output-dir', default='.github',
                      help='Output directory for templates (default: .github)')
    parser.add_argument('--templates', nargs='*',
                      choices=['bug_report', 'feature_request', 'pull_request'],
                      help='Specific templates to generate (default: all)')
    
    args = parser.parse_args()
    
    generator = TemplateGenerator(output_dir=args.output_dir)
    generated_files = generator.generate_templates(args.templates)
    
    print("Generated templates:")
    for file_path in generated_files:
        print(f"- {file_path}")

if __name__ == "__main__":
    main()
