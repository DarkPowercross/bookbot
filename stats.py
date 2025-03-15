def main():
    ...

def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(words):
    letters = {}
    for word in words:
        for i in range(len(word)):
            current_letter = word[i].lower()
            if current_letter in letters:
                letters[current_letter] += 1
            else:
                letters[current_letter] = 1
    return letters

def sorted_dict(letters):
    sorted_list = list(letters.items())
    sorted_list.sort(reverse=True, key=lambda item: item[1])
    return dict(sorted_list)

if __name__ == '__main__':
    main()