# iForms JSON Converter

A Python utility to transform JSON data from iForms JSON feed output format to a format compatible with POST trigger endpoints. The tool processes nested JSON structures, handles 'record' keys, and converts all keys to lowercase.

## Features

- Processes nested JSON structures recursively
- Extracts and flattens 'record' objects
- Converts all keys to lowercase
- Preserves data types and nested arrays
- Handles errors gracefully with informative messages

## Installation

1. Ensure you have Python 3.6 or higher installed
2. Clone this repository:

```bash
git clone https://github.com/mtldatacrab/iforms-json-converter.git
cd iforms-json-converter
```

## Usage

1. Place your input JSON file (from iForms) as `input.json` in the same directory as the script
2. Run the conversion script:

```bash
python convert.py
```

The transformed JSON will be saved to `output.json` in the same directory.

## Input Format Example

Your input JSON from iForms should look like this:

```json
[
  {
    "record": {
      "FirstName": "John",
      "LastName": "Doe",
      "Details": {
        "Age": 30,
        "Email": "john@example.com"
      }
    },
    "location": { "type": "point", "coordinate": [99.999999, 99.999999] }
  }
  // ... more records
]
```

## Output Format Example

The script will transform it to:

```json
[
  {
    "firstname": "John",
    "lastname": "Doe",
    "details": {
      "age": 30,
      "email": "john@example.com"
    }
  }
  // ... more records
]
```
