import collections

def shift_character(char, shift):
    if char.islower():
        base = ord('a')
        num_chars = 26
    elif char.isupper():
        base = ord('A')
        num_chars = 26
    else:
        return char

    shifted_ord = (ord(char) - base + shift) % num_chars + base
    return chr(shifted_ord)


def calculate_letter_frequencies(text):
    frequencies = collections.defaultdict(int)
    total_letters = 0

    for char in text:
        if char.isalpha():
            frequencies[char.lower()] += 1
            total_letters += 1

    for char in frequencies:
        frequencies[char] /= total_letters
    

    return frequencies


def get_highest_frequency_character(letter_frequencies):
    return max(letter_frequencies, key=letter_frequencies.get)


def brute_force_decrypt(ciphertext):
    for shift in range(26):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                decrypted_char = shift_character(char, -shift)
                plaintext += decrypted_char
            else:
                plaintext += char
        print(f'Shift: {shift}\tPlaintext: {plaintext}')


def frequency_analysis_decrypt(ciphertext):
    letter_frequencies = calculate_letter_frequencies(ciphertext)
    most_common_letter = get_highest_frequency_character(letter_frequencies)
    shift = (ord(most_common_letter) - ord('e')) % 26
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = shift_character(char, -shift)
            plaintext += decrypted_char
        else:
            plaintext += char
    print(f'\nletter: e')
    print(f'Shift: {shift}\tPlaintext: {plaintext}')
    shift = (ord(most_common_letter) - ord('t')) % 26
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = shift_character(char, -shift)
            plaintext += decrypted_char
        else:
            plaintext += char
    print(f'\nletter: t')
    print(f'Shift: {shift}\tPlaintext: {plaintext}')
    shift = (ord(most_common_letter) - ord('a')) % 26
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = shift_character(char, -shift)
            plaintext += decrypted_char
        else:
            plaintext += char
    print(f'\nletter: a')
    print(f'Shift: {shift}\tPlaintext: {plaintext}')



def known_plaintext_attack(ciphertext, known_plaintext):
    shift = (ord(ciphertext[0]) - ord(known_plaintext[0])) % 26
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = shift_character(char, -shift)
            plaintext += decrypted_char
        else:
            plaintext += char
    print(f'Shift: {shift}\tPlaintext: {plaintext}')

if __name__ == '__main__':
    ciphertext = 'Ymfy ujwxts nx htrnsl ktw rj! Nk dtz knsi ymnx styj, qttp fwtzsi rd uwtujwyd. Mnsy: N anxnyji ymj fwjf bnym rd ywtqqjd kwtr ymj lfwijs xmji'
    print('Brute Force Decryption')
    brute_force_decrypt(ciphertext)
    print('\nFrequency Analysis Decryption')
    frequency_analysis_decrypt(ciphertext)
    print('\nKnown Plaintext Attack')
    known_plaintext_attack(ciphertext, 'The message has been encrypted with a Caesar cipher.')
