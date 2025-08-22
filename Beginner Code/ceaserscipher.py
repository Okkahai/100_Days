alphabet = ["a", "b", "c", "d", "e", "f", "g", 
            "h", "i", "j", "k", "l", "m", "n", 
            "o", "p", "q", "r", "s", "t", "u", 
            "v", "w", "x", "y", "z"]

def caesar(text, shift, direction):
    result = ""
    for char in text:
        if char.lower() in alphabet:
            pos = alphabet.index(char.lower())
            if direction == "encode":
                new_pos = (pos + shift) % 26
            elif direction == "decode":
                new_pos = (pos - shift) % 26
            else:
                return "Invalid direction"
            
            # Preserve case
            if char.isupper():
                result += alphabet[new_pos].upper()
            else:
                result += alphabet[new_pos]
        else:
            result += char  # Non-alphabet chars stay the same
    return result

# Example usage:
message = "Hello World"
shift_amount = 5

encoded = caesar(message, shift_amount, "encode")
print(f"Encoded: {encoded}")

decoded = caesar(encoded, shift_amount, "decode")
print(f"Decoded: {decoded}")
