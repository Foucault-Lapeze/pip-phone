from phone_speller import phone_number_to_words

def test_digits_only():
    assert phone_number_to_words("123") == "one two three"

def test_digits_with_spaces():
    assert phone_number_to_words("1 2 3") == "one [Character not mapped] two [Character not mapped] three"

def test_empty_string():
    assert phone_number_to_words("") == ""

def test_non_digit_characters():
    assert phone_number_to_words("12a3") == "one two [Character not mapped] three"

def test_all_digits():
    assert phone_number_to_words("0123456789") == "zero one two three four five six seven eight nine"
