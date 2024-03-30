# Caesar Cipher Decryptor

## Project Description:

This project is a Python-based tool for decrypting Caesar cipher-encrypted text. Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This tool allows decryption for both English and Russian languages.

## Features:

- **Language Support:** Supports decryption for both English and Russian languages. The user can specify the language of the encrypted text.
  
- **Dictionary Matching:** Utilizes dictionaries of common words for English and Russian to assess the likelihood of correct decryption. This aids in distinguishing between multiple potential decryption outcomes.

- **Threshold Functionality:** Allows users to set a threshold for the minimum percentage of recognized words required for successful decryption.

## Usage:

1. **Language Selection:** Users choose the language of the encrypted text (English or Russian) for accurate decryption.
   
2. **Dictionary Loading:** Loads dictionaries for the selected language to compare decrypted text against.
   
3. **Text Input:** Users input the encrypted text they wish to decrypt.
   
4. **Decryption:** The tool iterates through possible shifts to decrypt the text and identifies the most probable original text based on dictionary word matches and the specified threshold.

## How to Use:

1. Clone this repository to your local machine.

2. Ensure Python is installed on your system.

3. Run the `decoder.py` script. Also you can check `decoder_ru.py` and `decoder_en.py` files.

4. Follow the prompts to select the language, input the encrypted text, and set the threshold (if desired).

## Dependencies:

- Python 3.x 
- Text files containing dictionaries for English and Russian languages (`en_US.txt`, `ru_RU.txt`) 

## Contributing:

Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
