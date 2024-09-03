import re

# Read the content of the file
file_path = 'D:\\python_learn\\CDR.txt'  # Update this path if necessary
with open(file_path, 'r') as file:
    cdr_data = file.read()

# Regular expression to match each CDR record without capturing the date and "CDR ELEMENTS FOLLOW"
cdr_pattern = re.compile(r"CDR ELEMENTS FOLLOW(.*?)(?=Tuesday June 29 2021|$)", re.DOTALL)

# Extract all CDR records
cdr_records = cdr_pattern.findall(cdr_data)

# Debugging: Print the raw extracted records
# print("Raw extracted records:")
# for record in cdr_records:
#     print(record)
# print("-----")

# Process each CDR record into a list
cdr_list = []
for record in cdr_records:
    cdr_values = []
    for line in record.strip().split("\n"):
        if line:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                key, value = parts
                cdr_values.append(value.strip())
    cdr_list.append(cdr_values)

# Print the extracted CDR records
print("Processed CDR records:")
for cdr in cdr_list:
    print(cdr)
