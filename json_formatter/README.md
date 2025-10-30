# JSON Formatter and Validator

A Python tool to format and validate JSON files with support for large files and streaming processing.

## Features

- 🚀 Memory Efficient: Handles large JSON files through streaming
- ⚡ Fast Processing: Uses orjson for high-performance JSON operations
- 🎨 Pretty Printing: Customizable indentation and formatting
- ✅ Validation: JSON syntax validation with detailed error messages
- 📊 Progress Tracking: Visual progress bar for large files
- 🎯 Syntax Highlighting: Beautiful terminal output
- 🔍 Key Sorting: Optional alphabetical sorting of JSON keys

## Installation

1. Clone this repository:
```bash
git clone https://github.com/parth-k1tech/json-formatter-validator.git
cd json-formatter-validator
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

1. Validate a JSON file:
```bash
python json_formatter.py input.json --validate
```

2. Format a JSON file:
```bash
python json_formatter.py input.json -o output.json
```

3. Format and display with syntax highlighting:
```bash
python json_formatter.py input.json -o output.json --display
```

4. Format with custom indentation:
```bash
python json_formatter.py input.json -o output.json --indent 4
```

### Command Line Options

```bash
python json_formatter.py --help
```

Available options:
- `--validate`: Only validate the JSON without formatting
- `--display`: Display the formatted JSON with syntax highlighting
- `--indent N`: Number of spaces for indentation (default: 2)
- `--sort-keys`: Sort dictionary keys alphabetically
- `-o, --output`: Output file for formatted JSON

## Features in Detail

### Memory Efficient Processing
- Uses streaming parser (ijson) for handling large JSON files
- Processes JSON in chunks to minimize memory usage
- Perfect for large JSON files that don't fit in memory

### Fast JSON Processing
- Utilizes orjson for faster JSON serialization
- Efficient validation and formatting algorithms
- Optimized for performance

### Rich Terminal Output
- Syntax highlighting for JSON
- Progress bar for large files
- Color-coded error messages
- Beautiful terminal formatting

## Examples

### Sample JSON Input
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
    },
    "boolean": true,
    "null": null
}
```

## Dependencies

- ijson: For streaming JSON parsing
- orjson: For fast JSON processing
- rich: For beautiful terminal output

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.