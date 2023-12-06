def get_word_size(word):
    if word == "":
        return 0
    else:
        return 1 + get_word_size(word[1:])


def process_sentence(sentence, process_word):
    if sentence == "":
        return []
    else:
        return [process_word(sentence.split()[0])] + process_sentence(
            " ".join(sentence.split()[1:]), process_word
        )


print(process_sentence("the quick brown fox jumped over the lazy dog", get_word_size))
