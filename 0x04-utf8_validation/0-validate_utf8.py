def validUTF8(data):
    # Number of bytes expected for the next character
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte (starts with "10")
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b0:
                continue  # Single-byte character, move to the next byte
            else:
                return False  # Invalid sequence
        else:
            # Check if the byte is a continuation byte (starts with "10")
            if byte >> 6 != 0b10:
                return False  # Invalid sequence
            num_bytes -= 1

    return num_bytes == 0  

