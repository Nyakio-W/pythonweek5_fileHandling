# Open the file in write mode ('w')
try:
    with open("my_file.txt", "w") as file:
    # Write three lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")  # Writing a line with numbers
        file.write("This is line 3 with some special characters: !@#$%^&*\n")

    

    with open ('my_file.txt','a') as file:
        file.write("Appeniding to the last one\n")
        file.write("GAS\n")  # Writing a line with numbers
        file.write("pizza\n")

    with open("my_file.txt", "r") as file:
    # Read the contents of the file
        contents = file.read()

   # Display the contents of the file on the console
    print("Contents of my_file.txt:")
    print(contents)
except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied while accessing the file.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("File handling operation completed.")

