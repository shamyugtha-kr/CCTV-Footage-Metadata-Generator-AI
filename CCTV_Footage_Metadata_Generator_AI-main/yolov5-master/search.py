import json
   
def search_objects(data, search_term):
    filtered_data = [entry["timestamp"] for entry in data["observations"] if any(search_term in obj for obj in entry["objects"])]
    return filtered_data


if __name__ == "__main__":
    with open('output.json', 'r') as json_file:
        data = json.load(json_file)
# Get search query from the user
search_query = input("Enter the object you want to search for: ")

# Filter data based on the search query
filtered_timestamps = search_objects(data, search_query)

# Display the results
if filtered_timestamps:
    print(f"Timestamps with '{search_query}': {filtered_timestamps}")
else:
    print(f"No observations found with '{search_query}'.")