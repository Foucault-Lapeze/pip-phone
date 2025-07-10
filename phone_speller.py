def phone_number_to_words(phone_number):
    digits_mapping = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    result = ""
    for digit in phone_number:
        result += digits_mapping.get(digit, '[Character not mapped]') + ' '
    return result.strip()

# phone_number = input('Veuillez saisir un numéro de téléphone : ')
# print(phone_number_to_words(phone_number))
