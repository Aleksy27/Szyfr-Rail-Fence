def encrypt(input_text, encryption_key, fill_char='\n'):
    input_text = input_text.replace(" ", "").upper()
    
    direction = -1
    current_row, current_col = 0,0 

    num_rows = encryption_key
    num_cols = len(input_text)
    rail_fence_cipher = [[fill_char for i in range(num_cols)] for j in range(num_rows)]

    for i in range(num_cols):
        rail_fence_cipher[current_row][current_col] = input_text[i]

        if current_row == 0:
            direction = -direction
        elif current_row == num_rows - 1:
            direction = -direction

        current_row, current_col = current_row + direction, current_col + 1

    rail_fence_text = ""

    for i in range(num_rows):
        for j in range(num_cols):
            if rail_fence_cipher[i][j] != fill_char:
                rail_fence_text += rail_fence_cipher[i][j]

    return rail_fence_text


def decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()

    num_rows = key
    num_cols = len(cipher_text)
    rail_fence_cipher = [[' ' for i in range(num_cols)] for j in range(num_rows)]

    direction = -1
    current_row, current_col = 0, 0

    for i in range(num_cols):
        if current_row == 0:
            direction = -direction
        elif current_row == num_rows - 1:
            direction = -direction

        rail_fence_cipher[current_row][current_col] = '*'
        current_row, current_col = current_row + direction, current_col + 1

    index = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if rail_fence_cipher[i][j] == '*' and index < len(cipher_text):
                rail_fence_cipher[i][j] = cipher_text[index]
                index += 1

    text = ""
    current_row, current_col = 0, 0
    direction = -1

    for i in range(num_cols):
        if current_row == 0:
            direction = -direction
        elif current_row == num_rows - 1:
            direction = -direction

        text += rail_fence_cipher[current_row][current_col]
        current_row, current_col = current_row + direction, current_col + 1

    return text

# enc_text = encrypt("milego sprawdzania", 3)
# dec_text = decrypt(enc_text, 3)
# print("Encrypted:", enc_text)
# print("Decrypted:", dec_text)