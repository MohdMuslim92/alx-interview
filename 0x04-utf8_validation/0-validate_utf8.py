#!/usr/bin/python3
""" This module checks if the recieved data is a valid UTF-8 encoding """


def validUTF8(data):
    """ Function to validate recieved data as UTF-8 encoding """
    # Check each byte in the data
    i = 0
    while i < len(data):
        byte = data[i]
        # Number of bytes a character should occupy based on the most
        # significant bits
        if byte >> 7 == 0:  # 1 byte character: 0xxxxxxx
            length = 0
        elif byte >> 5 == 0b110:  # 2 bytes character: 110xxxxx
            length = 1
        elif byte >> 4 == 0b1110:  # 3 bytes character: 1110xxxx
            length = 2
        elif byte >> 3 == 0b11110:  # 4 bytes character: 11110xxx
            length = 3
        else:
            return False

        # Check if there are enough bytes in the data for this character
        if i + length >= len(data):
            return False

        # Check that following bytes start with '10'
        for j in range(i + 1, i + length + 1):
            if not (data[j] >> 6 == 0b10):
                return False

        i += length + 1

    return True
