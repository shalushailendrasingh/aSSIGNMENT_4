# Task 1:Read a File and Handle Errors
try:
    with open("sample.txt", "r") as file:
        # Reading the file line by line
        for line_number, line_content in enumerate(file, start=1):
            print(f"line{line_number}: {line_content.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
    