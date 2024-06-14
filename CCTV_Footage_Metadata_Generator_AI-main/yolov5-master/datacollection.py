import json
import subprocess
import re
import time

# Replace 'your_command' with the actual command that generates the machine data
command = 'python detect.py --source 0'

# Initialize an empty list to store live data
live_data = []

# Define a regular expression pattern to match lines of the specified format
pattern = re.compile(r'^\d+: \d+x\d+ \d+ persons, \d+\.\d+ms$')

try:
    # Open a subprocess to run the command and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    while True:
        # Read one line of output from the subprocess
        line = process.stdout.readline().strip()

        if not line and process.poll() is not None:
            # If the subprocess has finished producing output, break from the loop
            break

        # Check if the line matches the specified format
        if pattern.match(line):
            # Process and store the live data
            data_entry = {
                "live_data": line,
                "timestamp": time.time(),  # Use the current timestamp
            }

            live_data.append(data_entry)

        # Add a delay if needed to control the rate of data capture
        time.sleep(1)  # Sleep for 1 second (adjust as needed)

except KeyboardInterrupt:
    # Handle keyboard interrupt (e.g., user presses Ctrl+C to exit the loop)

    # Convert the list of dictionaries to JSON
    json_output = json.dumps(live_data, indent=2)

    # Save the JSON data to a file
    with open('live_data_output.json', 'w') as json_file:
        json_file.write(json_output)

    print("Live data capture completed. JSON data saved to 'live_data_output.json'.")
