def find_longest_word(document, longest_word=""):
    if len(document) == 0:
        return longest_word

    else:
        new_list = document.split(" ", 1)
        if len(new_list[0]) > len(longest_word):
            longest_word = new_list[0]

        if len(new_list) > 1:
            return find_longest_word(new_list[1], longest_word)

    return longest_word
