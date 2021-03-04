text = input("Text: ")


def count_letters(text):
    count = 0
    for symbol in text:
        if (ascii(symbol) > ascii('A') and ascii(symbol) < ascii('z')):
            count += 1
    return count


def count_words(text):
    return len(text.split(' '))


def count_sentences(text):
    count = 0
    for symbol in text:
        if (symbol == '.' or symbol == '!' or symbol == '?'):
            count += 1
    return count


L = count_letters(text) / count_words(text) * 100
S = count_sentences(text) / count_words(text) * 100
grade = 0.0588 * L - 0.296 * S - 15.8

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade " + str(int(grade)))
