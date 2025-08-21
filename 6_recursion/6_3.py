def encode_char(char, rotor_position):
    if not rotor_position:
        return char
    if char.isupper():
        char = chr((ord(char) - 64) % 26 + 65)
    else:
        char = chr((ord(char) - 96) % 26 + 97)
    return encode_char(char, rotor_position-1)

def decode_char(char, rotor_position):
    if not rotor_position:
        return char
    if char.isupper():
        char = chr((ord(char) - 66) % 26 + 65)
    else:
        char = chr((ord(char) - 98) % 26 + 97)
    return decode_char(char, rotor_position-1)

def encode_message(message, rotor_position, index=0):
    message = list(message)
    if index == len(message):
        return "".join(message)
        
    if message[index].isalpha():
        if (rotor_position+index) % 26 == 0:
            rotor_position+=1
            message[index] = encode_char(message[index], rotor_position+index)
        else:
            message[index] = encode_char(message[index], rotor_position+index)
    return encode_message(message, rotor_position, index+1)
    
def decode_message(encoded_message, rotor_position, index=0):
    encoded_message = list(encoded_message)
    if index == len(encoded_message):
        return "".join(encoded_message)
    if encoded_message[index].isalpha():
        if (rotor_position+index) % 26 == 0:
            rotor_position+=1
            encoded_message[index] = decode_char(encoded_message[index], rotor_position+index)
        else:
            encoded_message[index] = decode_char(encoded_message[index], rotor_position+index)
    return decode_message(encoded_message, rotor_position, index+1)
    

# char, i = input().split()
# decode_char(char, int(i))
print("This is Caesar cipher")
message ,initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:",encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)