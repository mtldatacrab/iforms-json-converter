import json
import sys
from typing import Any, Union, Dict, List

def process_object(obj: Any) -> Any:
    """
    Recursively processes an object to handle 'record' keys and nested arrays.
    
    Args:
        obj: The object to process (can be dict, list or other type)
        
    Returns:
        The processed object with 'record' keys handled and all keys lowercased
        
    Raises:
        ValueError: If the input object structure is invalid
    """
    try:
        if isinstance(obj, dict):  # If the object is a dictionary
            if 'record' in obj:  # Process 'record' key if it exists
                record = obj['record']
                if not isinstance(record, dict):
                    raise ValueError("'record' value must be a dictionary")
                # Lowercase keys in the 'record' object
                obj = {key.lower(): value for key, value in record.items()}
            
            # Recursively process all values in the dictionary
            return {key: process_object(value) for key, value in obj.items()}
            
        elif isinstance(obj, list):  # If the object is a list
            # Process each element in the list
            return [process_object(item) for item in obj]
            
        return obj
        
    except Exception as e:
        raise ValueError(f"Error processing object: {str(e)}")


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    try:
        # Load and validate input file
        try:
            with open(input_file, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: Input file '{input_file}' not found")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in input file: {str(e)}")
            sys.exit(1)

        # Process the entire JSON structure
        try:
            transformed_data = process_object(data)
        except ValueError as e:
            print(f"Error processing data: {str(e)}")
            sys.exit(1)

        # Save the transformed JSON
        try:
            with open(output_file, "w") as file:
                json.dump(transformed_data, file, indent=2)
        except IOError as e:
            print(f"Error writing output file: {str(e)}")
            sys.exit(1)

        print(f"Transformed JSON with nested processing saved to {output_file}.")
        
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        sys.exit(1)