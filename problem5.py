# attempt to crack the secret message with a Caesar Cipher:
# we'll try all possible keys (0 to 25) to decrypt the message.
# for each key, we'll shift the letters in the message and check if it looks like English.
# if the decrypted message contains common English words, it's likely the right key.

# a list of common English words
common_words = ["the", "be", "to", "of", "and", "in", "that", "have", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say"]

# the encrypted message
secret_message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

# convert the message to uppercase to be consistent
secret_message = secret_message.upper()

# loop through all possible keys (0 to 25)
for key in range(26):
    decrypted_message = ""
    for char in secret_message:
        if char.isalpha():
            char_code = ord(char)
            decrypted_char_code = ((char_code - 65 - key) % 26) + 65
            decrypted_message += chr(decrypted_char_code)
        else:
            decrypted_message += char

    # split the decrypted message into words
    words_in_decrypted_message = decrypted_message.split()

    # check if any words appear in common English words
    common_english_words = [word for word in words_in_decrypted_message if word in common_words]

    # if we find common English words, display the result
    if common_english_words:
        print(f"possible key {key}: {' '.join(common_english_words)}")
