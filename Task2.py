# Task 2: Write and Append Data to a File

text_to_write = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

print("\nData successfully written to output.txt.\n")

additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("\nData successfully appended.\n")
print("Final content of output.txt:\n")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)