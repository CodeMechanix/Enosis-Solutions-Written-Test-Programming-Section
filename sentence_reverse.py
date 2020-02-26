
def sentence_reverse(text):
    split_text = text.split(' ')
    len_of_split_text = len(split_text)-1
    reverse_text=[]
    while len_of_split_text >=0:
        reverse_text.append(split_text[len_of_split_text])
        len_of_split_text = len_of_split_text-1
    
    reverse_text = " ".join(reverse_text)
    return reverse_text

print(sentence_reverse("Hello Enosis Solution"))