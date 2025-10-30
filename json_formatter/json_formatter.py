#!/usr/bin/env python3

import json
import argparse
import sys
from pathlib import Path
from typing import Union, TextIO
import ijson  # For streaming large JSON files
from rich.console import Console
from rich.syntax import Syntax
from rich.progress import Progress
import orjson  # For faster JSON processing

class JSONFormatter:
    def __init__(self, indent: int = 2, sort_keys: bool = False):
        """
        Initialize the JSON formatter
        
        Args:
            indent (int): Number of spaces for indentation
            sort_keys (bool): Whether to sort dictionary keys
        """
        self.indent = indent
        self.sort_keys = sort_keys
        self.console = Console()

    def validate_json_stream(self, file_obj: TextIO) -> tuple[bool, str]:
        """
        Validate JSON by streaming it (memory efficient for large files)
        
        Args:
            file_obj: File object to read from
            
        Returns:
            tuple: (is_valid, error_message)
        """
        try:
            parser = ijson.parse(file_obj)
            for _ in parser:
                pass
            return True, "JSON is valid"
        except ijson.JSONError as e:
            return False, f"JSON validation error: {str(e)}"
        except Exception as e:
            return False, f"Error during validation: {str(e)}"

    def format_json_stream(self, input_file: Union[str, Path], output_file: Union[str, Path]) -> tuple[bool, str]:
        """
        Format JSON file by streaming it in chunks
        
        Args:
            input_file: Path to input JSON file
            output_file: Path to output JSON file
            
        Returns:
            tuple: (success, message)
        """
        try:
            # First validate the JSON
            with open(input_file, 'rb') as f:
                is_valid, error_message = self.validate_json_stream(f)
                if not is_valid:
                    return False, error_message

            # Process the file in chunks using ijson for memory efficiency
            with open(input_file, 'rb') as infile, \
                 open(output_file, 'wb') as outfile, \
                 Progress() as progress:
                
                # Get file size for progress bar
                file_size = Path(input_file).stat().st_size
                task = progress.add_task("[cyan]Formatting JSON...", total=file_size)

                # Parse and format the JSON
                parser = ijson.parse(infile)
                builder = ijson.ObjectBuilder()
                
                for prefix, event, value in parser:
                    builder.event(event, value)
                    progress.update(task, advance=len(str(value).encode()))

                # Get the complete object
                result = builder.value

                # Use orjson for faster serialization
                json_bytes = orjson.dumps(
                    result,
                    option=orjson.OPT_INDENT_2 if self.indent else 0,
                    default=str
                )
                
                outfile.write(json_bytes)

            return True, f"JSON formatted successfully and saved to {output_file}"

        except Exception as e:
            return False, f"Error during formatting: {str(e)}"

    def display_json(self, json_file: Union[str, Path]):
        """
        Display formatted JSON with syntax highlighting
        
        Args:
            json_file: Path to JSON file
        """
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                content = f.read()
                syntax = Syntax(content, "json", theme="monokai", line_numbers=True)
                self.console.print(syntax)
        except Exception as e:
            self.console.print(f"[red]Error displaying JSON: {str(e)}[/red]")

def main():
    parser = argparse.ArgumentParser(
        description='JSON Formatter and Validator for large files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Validate a JSON file:
    python json_formatter.py input.json --validate
    
  Format a JSON file:
    python json_formatter.py input.json -o output.json
    
  Format and display:
    python json_formatter.py input.json -o output.json --display
    
  Format with custom indentation:
    python json_formatter.py input.json -o output.json --indent 4
        """
    )
    
    parser.add_argument('input_file', help='Input JSON file to process')
    parser.add_argument('-o', '--output', help='Output file for formatted JSON')
    parser.add_argument('--validate', action='store_true', help='Only validate the JSON without formatting')
    parser.add_argument('--display', action='store_true', help='Display the formatted JSON with syntax highlighting')
    parser.add_argument('--indent', type=int, default=2, help='Number of spaces for indentation (default: 2)')
    parser.add_argument('--sort-keys', action='store_true', help='Sort dictionary keys alphabetically')
    
    args = parser.parse_args()
    
    formatter = JSONFormatter(indent=args.indent, sort_keys=args.sort_keys)
    console = Console()
    
    # Validate JSON
    with open(args.input_file, 'r') as f:
        is_valid, message = formatter.validate_json_stream(f)
        
        if not is_valid:
            console.print(f"[red]{message}[/red]")
            sys.exit(1)
        elif args.validate:
            console.print(f"[green]{message}[/green]")
            sys.exit(0)
    
    # Format JSON
    if args.output:
        success, message = formatter.format_json_stream(args.input_file, args.output)
        if success:
            console.print(f"[green]{message}[/green]")
            if args.display:
                formatter.display_json(args.output)
        else:
            console.print(f"[red]{message}[/red]")
            sys.exit(1)

if __name__ == '__main__':
    main()