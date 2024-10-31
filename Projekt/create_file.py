# Define the name of the file you want to create
file_name = "ip_addresses.txt"

# Open the file in write mode
with open(file_name, 'w') as file:
    # Write some text to the file
    file.write("192.168.0.50\n")

print(f"File '{file_name}' created successfully.")