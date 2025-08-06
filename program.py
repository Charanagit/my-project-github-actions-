def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b


def write_to_file(filename, content):
    """Writes content to a file."""
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    """Reads content from a file."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

def process_text(text):
    """Converts text to uppercase and counts characters."""
    return text.upper(), len(text)

def calculate_sum(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

if __name__ == "__main__":
    # Writing and reading a file
    filename = "test_file.txt"
    content = "Hello, this is a test file!"
    write_to_file(filename, content)
    
    file_content = read_from_file(filename)
    print("File Content:", file_content)

    # Processing text
    uppercase_text, char_count = process_text(file_content)
    print("Uppercase Text:", uppercase_text)
    print("Character Count:", char_count)

    # Performing calculations
    numbers = [1, 2, 3, 4, 7]
    total = calculate_sum(numbers)
    print("Sum of Numbers:", total)
    