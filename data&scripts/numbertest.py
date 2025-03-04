def count_terms(input_string):
    # Split the string by commas and count the resulting items
    terms = input_string.split(',')
    return len(terms)

# Read the input from a text file
file_path = 'AKI files.txt'  # Replace with your file path
try:
    with open(file_path, 'r') as file:
        input_string = file.read().strip()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit(1)

# Remove the parentheses from the input string if present
input_string = input_string.strip('()')

# Count the terms
term_count = count_terms(input_string)

print(f"The number of terms in the file is: {term_count}")
