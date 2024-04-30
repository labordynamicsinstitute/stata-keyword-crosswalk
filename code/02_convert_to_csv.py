#!/usr/bin/env python3

import pandas as pd
import argparse

def convert_stata_to_csv(stata_file_path, csv_file_path):
    # Read the STATA file using pandas
    data = pd.read_stata(stata_file_path)

    # Write the data to a CSV file
    data.to_csv(csv_file_path, index=False)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Convert STATA file to CSV")

    # Add the arguments
    parser.add_argument('--input', metavar='input', type=str, default='keyword-package-crosswalk.dta',
                        help='The input STATA file path')
    parser.add_argument('--output', metavar='output', type=str, default='keyword-package-crosswalk.csv',
                        help='The output CSV file path')

    # Parse the arguments
    args = parser.parse_args()

    # Convert the STATA file to CSV
    convert_stata_to_csv(args.input, args.output)

if __name__ == "__main__":
    main()
