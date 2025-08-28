def main():
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            
        print(f"Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()# This program reads a text file, converts its content to uppercase, and writes the modified content to a new file.




# User Input: The program starts by asking the user for the names of the input and output files.

# Input File: The input file is opened in read mode. If the file does not exist, a FileNotFoundError is caught, and an error message is displayed. If there are permission issues, a PermissionError is caught, and an appropriate message is shown. Other I/O errors are handled with a general IOError catch.
def main():
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
        return
    except IOError as e:
        print(f"Error: Could not read file '{input_filename}'. {e}")
        return

    modified_content = content.upper()

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Successfully wrote modified content to '{output_filename}'.")
    except IOError as e:
        print(f"Error: Could not write to file '{output_filename}'. {e}")

if __name__ == "__main__":
    main()