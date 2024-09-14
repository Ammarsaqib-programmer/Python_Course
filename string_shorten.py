def shorten_string(string):
    if len(string) > 10:
        # Truncate the string after the 8th character and append '...'
        return string[:8] + "..."
    else:
        # If the string length is 10 or less, return the string as it is
        return string

# Example usage
input_string = input("Enter a string: ")
result = shorten_string(input_string)
print(result)
