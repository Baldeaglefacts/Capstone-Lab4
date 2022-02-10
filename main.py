def camel_case(sentence):
    # Converts sentence to titlecase. Splits the sentence into a list of words, then makes the first entry in the list
    # lowercase. Finally, it reattaches the sentence without spaces in between.
    if sentence != "":
        titleSentence = sentence.title()
        splitSentence = titleSentence.split()
        splitSentence[0] = splitSentence[0].lower()
        camalCaseSentence = "".join(splitSentence)
        return camalCaseSentence
    else:
        return ""

def main():
    sentence = input('Enter your sentence: ')
    camalcased = camel_case(sentence.strip())
    print(camalcased)

if __name__ == '__main__':
    main()
