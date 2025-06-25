#parse encoded string
def parse_encoded_string(s):
    parts = list(filter(None, s.split('0')))
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }
#Example 
result = parse_encoded_string("Robert000Smith000123")
print(result)


#finding extra characters
def find_extra_char(s1, s2):
    for char in s2:
        if s2.count(char) > s1.count(char):
            return char
#example
print(find_extra_char("eueiieo", "iieoedue"))  # Output: 'd'


#shadow senetence
def is_shadow_sentence(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    if len(words1) != len(words2):
        return False
    for i in range(len(words1)):
        if len(words1[i]) != len(words2[i]):
            return False
        if set(words1[i]) & set(words2[i]):  # check for common letters
            return False
    return True
#example
print(is_shadow_sentence("they are round", "fold two times"))  # True
print(is_shadow_sentence("his friends", "our company"))        # False

#Function to check for duplicate letters in any word
def has_duplicate_letters(sentence):
    words = sentence.split()
    for word in words:
        letters = [char for char in word.lower() if char.isalpha()]
        if len(letters) != len(set(letters)):
            return True
    return False
#example
print(has_duplicate_letters("Every fox jumps"))        # False
print(has_duplicate_letters("Happy cat sings"))        # True (Happy has two p's)


#Function to convert string to space-separated hex values (lowercase)
def ascii_to_hex(s):
    return ' '.join(format(ord(char), '02x') for char in s)
#example
print(ascii_to_hex("Hi!"))  # Output: "48 69 21"


#tic-tae 
def block_win(pos1, pos2):
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in winning_lines:
        if pos1 in line and pos2 in line:
            third = [x for x in line if x != pos1 and x != pos2]
            if third:
                return third[0]
    return None
#Example:
print(block_win(0, 1))  # Output: 2 (completes top row)
print(block_win(2, 4))  # Output: 6 (completes diagonal)
print(block_win(0, 5))  # Output: None (not in same winning line)


#Morse Code Converter Function
def to_morse(text):
    morse_dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---','3': '...--','4': '....-',
        '5': '.....', '6': '-....', '7': '--...','8': '---..','9': '----.',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--',
        ':': '---...', "'": '.----.', '-': '-....-', '/': '-..-.',
        '(': '-.--.',  ')': '-.--.-', '&': '.-...', '=': '-...-', '+': '.-.-.',
        '@': '.--.-.', '"': '.-..-.'
    }
    text = text.upper()
    morse_code = []
    for char in text:
        if char == ' ':
            morse_code.append(' / ')  # Represent space between words
        elif char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            morse_code.append('?')  # Unknown character
    return ' '.join(morse_code)
#example
print(to_morse("Hello, World!"))  
# Output: ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"


#Check for Friday the 13th
import datetime
def has_friday_13(month, year):
    try:
        date = datetime.date(year, month, 13)
        return date.weekday() == 4  # 0=Monday, 4=Friday
    except ValueError:
        return False  # Invalid month/year
#example
print(has_friday_13(9, 2025))   # False
print(has_friday_13(6, 2025))   # True
