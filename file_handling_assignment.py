# file_handling_assignment.py

# Task 1: File Creation and Writing
try:
    # Creating and opening the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Writing three lines of text to the file
        file.write("Hello, World!\n")
        file.write("Python is fun.\n")
        file.write("The answer to everything is 42.\n")
    print("File 'my_file.txt' created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred while creating or writing to the file: {e}")

# Task 2: File Reading and Display
try:
    # Opening the file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Reading and displaying the content
        content = file.read()
        print("\nFile content after initial writing:")
        print(content)
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Task 3: File Appending
try:
    # Opening the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text
        file.write("Appending some new content.\n")
        file.write("Learning Python is rewarding.\n")
        file.write("Error handling is crucial.\n")
    print("\nAdditional content appended to 'my_file.txt' successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Task 4: Final File Reading and Display
try:
    # Opening the file in read mode ('r') again
    with open("my_file.txt", "r") as file:
        # Reading and displaying the updated content
        updated_content = file.read()
        print("\nFile content after appending:")
        print(updated_content)
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Final block to close resources if needed (though handled by 'with')
finally:
    print("\nFile handling script execution completed.")
