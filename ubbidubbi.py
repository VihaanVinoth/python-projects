def ubbidubbi_word(word: str) -> str:
    is_vowel = []
    lower_word = word.lower()

    for i, ch in enumerate(lower_word):
        prev_is_vowel = is_vowel[i - 1] if i > 0 else False
        is_vowel.append(ch in "aeiou" or (ch == "y" and i > 0 and not prev_is_vowel))

    silent_e = (
        len(word) > 2
        and lower_word.endswith("e")
        and not is_vowel[-2]
        and any(is_vowel[:-1])
    )

    result = ""
    for i, ch in enumerate(word):
        if is_vowel[i] and (i == 0 or not is_vowel[i - 1]):
            if not (silent_e and i == len(word) - 1):
                result += "ub"
        result += ch

    return result



def ubbidubbi_translator(sentence):
    out, word = "", ""
    for ch in sentence.lower() + " ": 
        if ch.isalnum():
            word += ch
        else:
            out += ubbidubbi_word(word) + ch
            word = ""
    return out[:-1]


while True:
    sentence = input("Enter the English sentence: ")
    print("Translation:", ubbidubbi_translator(sentence))

    if input("Do another? [y/n] ").lower() != "y":
        print("gubo ubin pubeace! guboodbubye!")
        break
