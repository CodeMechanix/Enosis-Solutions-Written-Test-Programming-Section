def string_reverse(text):
    output_text = ""
    for i in range(1,len(text)+1):
        output_text += text[len(text)-i]
    return output_text
    
def sentence_reverse(text):
    split_text = text.split(' ')
    len_of_split_text = len(split_text)-1
    reverse_text=[]
    while len_of_split_text >=0:
        str = string_reverse(split_text[len_of_split_text])
        split_text[len_of_split_text] = str
        len_of_split_text = len_of_split_text-1
    
    reverse_text = " ".join(split_text)
    return reverse_text

print(sentence_reverse("Hello Solution"))
