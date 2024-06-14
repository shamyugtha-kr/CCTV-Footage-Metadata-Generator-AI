import re
import json
with open('det.txt', 'r') as file1:
    text_data = file1.readlines()

# Regular expression pattern to match the structure of each line
pattern_type = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (\d+): (\d+x\d+) (\d+ persons?, \d+ chairs?, \d+ tvs?, \d+ laptops?), (\d+\.\d+)ms')

# Dictionary to store structured data
structured_data = {}

# Example of how to use the pattern to extract information from each line
for line in text_data:
    match = pattern_type.match(line)
    if match:
        groups = match.groups()
        timestamp, observation_id, _, objects_str, duration = groups
        objects = [obj.strip() for obj in objects_str.split(',')]
        
        if observation_id not in structured_data:
            structured_data[observation_id] = []

        structured_data[observation_id].append({
            'timestamp': timestamp,
            'objects': objects,
            'speed': float(duration)
        })

# Organize data by timestamp
sorted_data = sorted(structured_data.items(), key=lambda x: min(entry['duration'] for entry in x[1]))

# Create a JSON structure
json_data = {'observations': []}
for observation_id, entries in sorted_data:
    for entry in entries:
        json_data['observations'].append({
            'timestamp': entry['timestamp'],
            'observation_id': observation_id,
            'objects': entry['objects'],
            'duration': entry['duration']
        })

# Save the JSON data to a file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print("JSON data has been saved to 'output.json'")
