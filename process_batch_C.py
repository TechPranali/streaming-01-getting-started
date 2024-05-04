"""
Batch Process C: Third transformation

Read from a file, transform, write to a new file.
In this case, covert degree K to degree F.

Note: 
This is a batch process, but the file objects we use are 
often called 'file-like objects' or 'streams'.
Streaming differs in that the input data is unbounded.

Use logging, very helpful when working with batch and streaming processes. 

"""

# Import from Python Standard Library

import csv
import logging

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Declare program constants

INPUT_FILE_NAME = "batchfile_2_kelvin.csv"
OUTPUT_FILE_NAME = "batchfile_3_farenheit.csv"

# Define program functions (bits of reusable code)
# Use docstrings - and indentation matters!


def convert_k_to_f(temp_k):
    """Convert Kelvin to Fahrenheit."""
    logging.debug(f"Calling convert_k_to_f() with {temp_k}.")
    fahrenheit = round((float(temp_k) - 273.15) * 9 / 5 + 32, 2)
    logging.debug(f"Converted {temp_k}K to {fahrenheit}F.")
    return fahrenheit


def process_rows(input_file_name, output_file_name):
    """Read from input file, convert temperature, and write to output file."""
    logging.info(f"Starting conversion from {input_file_name} to {output_file_name}.")
    with open(input_file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter=",")
        header = next(reader)  # Skip the header
        logging.info(f"Header read and skipped: {header}")

        with open(output_file_name, "w", newline="") as output_file:
            writer = csv.writer(output_file, delimiter=",")
            writer.writerow(["Year", "Month", "Day", "Time", "TempF"])  # Write the output header

            for row in reader:
                Year, Month, Day, Time, TempK = row
                TempF = convert_k_to_f(TempK)
                writer.writerow([Year, Month, Day, Time, TempF])
                logging.debug(f"Processed row from {TempK}K to {TempF}F")
    logging.info("Conversion process completed successfully.")


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process C.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
