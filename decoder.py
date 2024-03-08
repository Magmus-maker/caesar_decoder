def decrypt_caesar_cipher(text, shift, language):
    # Decrypt text using Caesar cipher for the specified language.
    decrypted_text = ''
    if language == 'eng':
        alphabet_size = 26
        base_char = 'a'
    elif language == 'rus':
        alphabet_size = 32
        base_char = 'а'
    else:
        raise ValueError("Invalid language specified.")
    
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - ord(base_char) - shift) % alphabet_size) + ord(base_char))
            if char.isupper():
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def count_words_in_dictionary(text, dictionary):
    # Count the number of words from the text that are in the dictionary.
    words = text.split()
    count = 0
    for word in words:
        if word.lower() in dictionary:
            count += 1
    return count

def load_dictionary(file_name):
    # Load dictionary from file for the specified language.
    dictionary = set()
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            dictionary.add(word.lower())
    return dictionary

def main():
    # Define threshold variable
    threshold = None
    
    # Language selection
    language = input("Choose a language (eng/rus): ").lower()
    if language not in ['eng', 'rus']:
        print("Invalid language selection.")
        return

    # Load dictionary
    if language == 'eng':
        dictionary = load_dictionary('en_US.txt')
        threshold = 0.8
    elif language == 'rus':
        dictionary = load_dictionary('ru_RU.txt')
        threshold = 0.4

    # Input encrypted text
    encrypted_text = input("Enter encrypted text: ")

    # Convert text to lowercase
    encrypted_text = encrypted_text.lower()

    print("Encrypted text:", encrypted_text)

    # Count total words in the text
    words_total = len(encrypted_text.split())

    # Determine the required number of matching words to achieve the threshold
    if threshold is not None:
        words_required = int(words_total * threshold)
    else:
        print("Error: Threshold not defined.")
        return

    # Iterate over all possible shifts and decrypt the text
    shift = 0
    if language == 'eng':
        alphabet_size = 26
    elif language == 'rus':
        alphabet_size = 32
    
    while shift < alphabet_size:
        decrypted_text = decrypt_caesar_cipher(encrypted_text, shift, language)
        count_matching_words = count_words_in_dictionary(decrypted_text, dictionary)
        if count_matching_words >= words_required:
            print("Probable original text:", decrypted_text)
            print("Shifts made for decryption:", shift)
            break
        shift += 1
    else:
        print("Decryption unsuccessful.")

if __name__ == "__main__":
    main()