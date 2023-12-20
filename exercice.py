import json  # Import the JSON module

# Read the original JSON file
with open("data.json", "r") as file:
    data = json.load(file)  # Load JSON content into a dictionary
    print(data)  # Print the original content of the file

# Modify the dictionary by adding a new key-value pair
data["langage"] = "Python"

# Write the modified dictionary back to the JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)  # Save the modified data with an indentation of 2 spaces

# Read the modified JSON file
with open("data.json", "r") as file:
    data = json.load(file)  # Load the modified JSON content into a dictionary
    print("\nContenu du fichier après modification :")
    print(data)  # Print the content of the file after the modification