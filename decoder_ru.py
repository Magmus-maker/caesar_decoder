def decrypt_cesar_cipher(text, shift):
    # Дешифрование текста методом Цезаря для русского языка.
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - ord('а') - shift) % 32) + ord('а'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def count_words_in_dictionary(text, dictionary):
    # Подсчет количества слов из текста, которые есть в словаре.
    words = text.split()
    count = 0
    for word in words:
        if word.lower() in dictionary:
            count += 1
    return count

def load_dictionary(file_name):
    # Загрузка словаря из файла для русского языка.
    dictionary = set()
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            dictionary.add(word.lower())
    return dictionary

def main():
    # Загрузка словаря
    ru_dictionary = load_dictionary('ru_RU.txt')

    # Ввод зашифрованного текста
    encrypted_text = input("Введите зашифрованный текст: ")

    # Преобразование текста к нижнему регистру
    encrypted_text = encrypted_text.lower()

    print("Зашифрованный текст:", encrypted_text)

    # Подсчет общего количества слов в тексте
    words_total = len(encrypted_text.split())

    # Определение необходимого количества совпадающих слов для достижения порога в 80%
    words_required = int(words_total * 0.4)

    # Перебор всех возможных сдвигов и дешифрование текста
    shift = 0
    while shift < 32:  # для русского алфавита 32 буквы
        decrypted_text = decrypt_cesar_cipher(encrypted_text, shift)
        count_matching_words = count_words_in_dictionary(decrypted_text, ru_dictionary)
        if count_matching_words >= words_required:
            print("Предполагаемый оригинал текста:", decrypted_text)
            print("Для расшифровки было сделано", shift, "сдвигов.")
            break
        shift += 1
    else:
        print("Не удалось найти расшифровку.")

if __name__ == "__main__":
    main()
