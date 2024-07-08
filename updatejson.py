import json

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to save JSON data to a file
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a new topic to the JSON data
def add_topic(data, topic_name, topic_content):
    # Check if 'Assistable' and 'topics' exist in the data
    if 'Assistable' in data and 'topics' in data['Assistable']:
        # Create the new topic structure
        new_topic = {
            topic_name: topic_content
        }
        # Append the new topic to the list of topics
        data['Assistable']['topics'].append(new_topic)
    else:
        print("Invalid data structure")
    return data

# Example usage
file_path = 'assistable_docs_partial_array.json'  # Update this path to the location of your JSON file
data = load_json(file_path)

# Define new topic content
new_topic_name = "New Topic"  # Replace with the actual name of the new topic
new_topic_content = [
    {
        "title": "Introduction",
        "content": "This is an introduction to the new topic."
    },
    {
        "title": "Details",
        "content": "These are the details of the new topic."
    }
]

# Add the new topic
data = add_topic(data, new_topic_name, new_topic_content)

# Save the updated JSON
save_json(data, file_path)