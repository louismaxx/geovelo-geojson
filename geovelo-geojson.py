#!/usr/bin/python3

import argparse
import json
import sys

def main(input_file, output_file):

    try:
        # Load JSON file
        with open(input_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON. {e}", file=sys.stderr)
        sys.exit(1)

    template = {
        "type": "FeatureCollection",
        "features": []
    }

    value_filter = ['id', 'geometry', 'start_datetime', 'end_datetime']

    for item in data:
        feature = {
            "type": "Feature",
            "geometry": item['geometry'],
            "properties": {
                "id": item['id'],
                "start_datetime": item['start_datetime'],
                "end_datetime": item['end_datetime']
            }
        }
        template['features'].append(feature)

    try:
        with open(output_file, 'w') as file:
            json.dump(template, file, indent=4)
    except IOError as e:
        print(f"Error: Failed to write to output file. {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter and append data to a JSON template.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input JSON file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output JSON file.")

    # Parse arguments
    args = parser.parse_args()

    main(args.input, args.output)