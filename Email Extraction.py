import re

# Step 1: Open and read the input file
with open("file.txt", "r") as file:
    content = file.read()

# Step 2: Use regular expressions to extract email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Step 3: Write the emails to a new file
with open("emails.txt", "w") as output_file:
    for email in emails:
        output_file.write(email + "\n")

print(f" {len(emails)} email(s) extracted and saved to 'emails.txt'")