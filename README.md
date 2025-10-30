# JSON Formatter and Validator

A high-performance Python tool for formatting and validating JSON files, designed to handle large files efficiently through streaming processing.

## Features

- **Memory Efficient**: Process large JSON files through streaming
- **High Performance**: Powered by `orjson` for fast JSON operations
- **Pretty Printing**: Customizable indentation and formatting
- **Validation**: Comprehensive JSON syntax validation
- **Progress Tracking**: Visual progress bar for large files
- **Syntax Highlighting**: Beautiful terminal output
- **Key Sorting**: Optional alphabetical sorting of keys

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/parth-k1tech/json-formatter-validator.git
cd json-formatter-validator

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

1. **Validate a JSON file**:
```bash
python json_formatter.py input.json --validate
```

2. **Format a JSON file**:
```bash
python json_formatter.py input.json -o output.json
```

3. **Format with syntax highlighting**:
```bash
python json_formatter.py input.json -o output.json --display
```

4. **Custom indentation**:
```bash
python json_formatter.py input.json -o output.json --indent 4
```

## Command Line Options

```bash
python json_formatter.py --help
```

| Option | Description |
|--------|-------------|
| `--validate` | Only validate without formatting |
| `--display` | Show formatted JSON with highlighting |
| `--indent N` | Set indentation spaces (default: 2) |
| `--sort-keys` | Sort JSON object keys alphabetically |
| `-o, --output` | Specify output file path |

## Performance Features

### Memory Efficient Processing
- Uses `ijson` for streaming large JSON files
- Processes data in chunks to minimize memory usage
- Perfect for files that don't fit in memory

### Fast Processing
- Utilizes `orjson` for rapid JSON operations
- Optimized validation algorithms
- Efficient string handling

### Rich Output
- Syntax highlighting for JSON content
- Progress tracking for large files
- Color-coded error messages
- Beautiful terminal formatting

## Example

Input JSON:
```json
{
    "name": "Sample Project",
    "version": "1.0.0",
    "nested": {
        "array": [1, 2, 3, 4, 5],
        "object": {
            "key1": "value1",
            "key2": "value2"
        }
    }
}
```

Format with display:
```bash
python json_formatter.py sample.json -o formatted.json --display
```

## Dependencies

- `ijson`: Streaming JSON parser
- `orjson`: High-performance JSON library
- `rich`: Terminal formatting and highlighting

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- `ijson` for efficient JSON streaming
- `orjson` for high-performance JSON operations
- `rich` for beautiful terminal output
