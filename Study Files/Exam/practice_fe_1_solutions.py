# Question 1
def get_word_size(word):
    if word == '':
        return 0
    
    return 1 + get_word_size(word[1:])

print(f'{get_word_size("a") = }')
print(f'{get_word_size("car") = }')
print(f'{get_word_size("university") = }')
print(f'{get_word_size("honour") = }')

def process_sentence(sentence, process_word):
    words = sentence.split(' ')
    result = []
    for word in words:
        result.append(process_word(word))
    return result

print(f'{process_sentence("the quick brown fox jumped over the lazy dog", get_word_size)}')

# Question 2
def process_game(filename, handler):
    content = '         '
    with open(filename, 'r') as input_file:
        content = input_file.read()
    handler(content)


def print_game(game_state):
    for i in range(9, 82, 9):
        print(game_state[i-9:i])

process_game('game.txt', print_game)

# Question 3
def has_no_repeated_letter(string):
    if len(string) == 0:
        return True
    
    if string[0] in string[1:]:
        return False
    
    return has_no_repeated_letter(string[1:])

print(f'{has_no_repeated_letter("level") = }')
print(f'{has_no_repeated_letter("car") = }')
print(f'{has_no_repeated_letter("speedometer") = }')
print(f'{has_no_repeated_letter("fairly") = }')

class NoMatchFoundException(Exception):
    pass

def get_longest_matching_substring(string, check_match):
    # this function didn't need to be recursive, but why not?
    if len(string) == 0:
        raise NoMatchFoundException('No substring found that is a match')
    
    # find and check all substrings that begin at index 0
    longest_matching_substring_start = ''
    for i in range(1, len(string)):
        substring = string[:i]
        if check_match(substring) and len(substring) > len(longest_matching_substring_start):
            longest_matching_substring_start = substring
    
    # find and check all of the other substrings (that don't include index 0)
    longest_matching_substring_rest = get_longest_matching_substring(string[1:], check_match)
    
    # identify which substring is longer
    return longest_matching_substring_start if len(longest_matching_substring_start) > len(longest_matching_substring_rest) else longest_matching_substring_rest


print('ablewasiereisawelba:', has_no_repeated_letter('ablewasiereisawelba'))
# expected output: ablewasiereisawelba: False

print('abcd:', has_no_repeated_letter('abcd'))
# expected output: abcd: True

print('longest with no repeated letter:', get_longest_matching_substring('i saw abba, but ablewasiereisawelba by the racecar', has_no_repeated_letter))
# expected output: longest with no repeated letter: ut ablew


