"""
Batch Process B: Second transformation

Read from a file, transform, write to a new file.
In this case, covert degree C to degree K.

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

INPUT_FILE_NAME = "batchfile_1_celcius.csv"
OUTPUT_FILE_NAME = "batchfile_2_kelvin.csv"

# Define program functions (bits of reusable code)


def convert_c_to_k(temp_c):
    """Convert to Celsius to Kelvin.
    Use the built-in round() function to round to 2 decimal places
    Use the built-in float() function to convert the string to a float (a floating point number)
    All CSV values are read as strings.
    """
    logging.debug(f"Calling convert_c_to_k() with {temp_c}.")
    kelvin = round(float(temp_c) + 273.15, 2)
    logging.debug(f"Converted {temp_c}C to {kelvin}K.")
    return kelvin


def process_rows(input_file_name, output_file_name):
    """Read from input file, convert temperature, and write to output file."""
    logging.info(f"Calling process_rows(): {input_file_name} to {output_file_name}.")

    # Create a file object for input (r = read access)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")

        header = next(reader)
        logging.info(f"Skipped header row: {header}")

        # Create a file object for output (w = write access)
        # Set the newline parameter to an empty string to avoid extra newlines in the output file
        with open(output_file_name, "w", newline="") as output_file:
            logging.info(f"Opened for writing: {output_file_name}.")

            # Create a CSV writer object
            writer = csv.writer(output_file, delimiter=",")

            # Write the header row to the output file
            writer.writerow(["Year", "Month", "Day", "Time", "TempK"])

            # For each data row in the reader
            for row in reader:
                # Extract the values from the input row into named variables
                Year, Month, Day, Time, TempC = row

                # Call the conversion function, passing in the TempC argument
                # Assign the return value to a new variable named TempK
                TempK = convert_c_to_k(TempC)

                # Write the transformed data to the output file
                writer.writerow([Year, Month, Day, Time, TempK])


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process B.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
