def english_to_piglatin(word):
    '''english_to_piglatin(word) -> string
    Translates word into Pig Latin.'''
    # check if first character capitalized
    capitalWord = word[0].isupper()
    # make first character lower case
    word = word[0].lower() + word[1:]

    if word[0] in 'aeiouAEIOU':  # check if the first letter is a vowel
        outword = word + 'way'
    else:
        # word begins with a consonant
        consonants = ''  # keep track of consonants at start of word
        while len(word) > 0 and word[0] not in 'aeiou':
            consonants += word[0]  # add the consonant
            word = word[1:]  # remove the first letter from word
        outword = word + consonants + 'ay'

    # check if we need to capitalize the output
    if capitalWord:
        outword = outword[0].upper() + outword[1:]
    return outword


pig = str(input("What word do you want to translate? "))
print(english_to_piglatin(pig))
