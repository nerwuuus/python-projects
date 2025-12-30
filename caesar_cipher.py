# =========================================================
#                     Simple solution
# =========================================================
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encode(plain_text, shift_amount):
    result = ''
    for letter in plain_text:
        shifted_index = ((alphabet.index(letter) + shift_amount) % 26) # 26 letters in the alphabet
        shifted_letter = alphabet[shifted_index]
        result += shifted_letter
    print(result)

encode(plain_text='hello', shift_amount=1)
# returns 'ifmmp'
