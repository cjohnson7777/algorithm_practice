# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
# NOT SOLVED

def encode(word):
    newWord = ""
    i = 0

    while i < len(word):
        j = i
        while j < len(word) and word[j] == word[i]:
            j += 1

        length = str(len(word[i:j]))
        newWord += length
        newWord += word[i]
        i = j
    
    return newWord

# 4A3B2C1D2A

  

#print(encode("AAAABBBCCDAA"))
#print(decode("4A3B2C1D2A"))




    