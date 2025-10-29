# GitHub Issue and PR Templates Generator

A Python tool to automatically generate GitHub Issue and Pull Request templates for your repositories.

## Features

- Generates standard templates for:
  - Bug reports
  - Feature requests
  - Pull requests
- Customizable output directory
- Option to generate specific templates or all templates
- Command-line interface
- Automatic directory creation
- UTF-8 encoding support

## Installation

1. Clone this repository:
```bash
git clone https://github.com/parth-k1tech/issue-pr-templates.git
cd issue-pr-templates
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

1. Generate all templates (default):
```bash
python template_generator.py
```

2. Generate specific templates:
```bash
python template_generator.py --templates bug_report feature_request
```

3. Generate templates in a custom directory:
```bash
python template_generator.py --output-dir custom/path/.github
```

### Using as a Module

You can also use the `TemplateGenerator` class in your own Python scripts:

```python
from template_generator import TemplateGenerator

# Initialize the generator
generator = TemplateGenerator()

# Generate all templates
generator.generate_templates()

# Or generate specific templates
generator.generate_templates(['bug_report', 'pull_request'])
```

## Template Types

### Bug Report Template
- Standard template for reporting bugs
- Includes sections for:
  - Bug description
  - Reproduction steps
  - Expected behavior
  - Screenshots
  - Environment details
  - Additional context

### Feature Request Template
- Template for suggesting new features
- Includes sections for:
  - Problem description
  - Proposed solution
  - Alternative solutions
  - Additional context

### Pull Request Template
- Comprehensive PR template
- Includes sections for:
  - Description
  - Type of change
  - Testing details
  - Checklist for contributors

## Command Line Options

```bash
python template_generator.py --help
```

Available options:
- `--output-dir`: Specify the output directory (default: `.github`)
- `--templates`: Specify which templates to generate (choices: `bug_report`, `feature_request`, `pull_request`)

## Directory Structure

The generated templates will be created in the following structure:
```
.github/
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
└── PULL_REQUEST_TEMPLATE.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
