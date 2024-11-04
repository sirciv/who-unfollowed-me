import json

def extract_values_from_followers_json(input_file, output_file):

    try:
        # Read the JSON data from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Extract 'value' properties
        values = [
            entry["string_list_data"][0]["value"]
            for entry in data
            if entry["string_list_data"]
        ]

        # Write the values to the output file, each on a new line
        with open(output_file, 'w', encoding='utf-8') as file:
            for value in values:
                file.write(value + '\n')

        print(f"Followers extraction complete. Values saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except json.JSONDecodeError:
        print("Error: The input file is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_values_from_following_json(input_file, output_file):

    try:
        # Read the JSON data from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Extract 'value' properties
        values = [
            entry["string_list_data"][0]["value"]
            for entry in data.get("relationships_following", [])
            if entry["string_list_data"]
        ]

        # Write the values to the output file, each on a new line
        with open(output_file, 'w', encoding='utf-8') as file:
            for value in values:
                file.write(value + '\n')

        print(f"Following extraction complete. Values saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except json.JSONDecodeError:
        print("Error: The input file is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_list_from_file(filename):
    
    # Reads a list from a text file, stripping newline characters.
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def write_list_to_file(filename, data):

    # Writes a list of strings to a text file, each item on a new line.
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def compare_lists(list_a, list_b):

    # Compares two lists and returns unique items in each list.
    exclusive_to_a = set(list_a) - set(list_b)
    exclusive_to_b = set(list_b) - set(list_a)
    return exclusive_to_a, exclusive_to_b

# Process

extract_values_from_followers_json('followers_1.json', 'followers.txt')
extract_values_from_following_json('following.json', 'following.txt')

list_a = read_list_from_file('followers.txt')
list_b = read_list_from_file('following.txt')

if list_a and list_b:

    exclusive_to_a, exclusive_to_b = compare_lists(list_a, list_b)

    write_list_to_file('only_following_you.txt', exclusive_to_a)
    write_list_to_file('only_following_them.txt', exclusive_to_b)

    print("Comparison complete.")
