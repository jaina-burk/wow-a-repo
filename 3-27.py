def reverse_sentence(string):
    sentence = string.split()
    sentence.reverse()
    sentence = " ".join(sentence)
    return sentence

string = input("Enter a sentence you'd like to reverse: ")
result = reverse_sentence(string)
print(result)