
def string_reverse(text):
    output_text = ""
    for i in range(1,len(text)+1):
        output_text += text[len(text)-i]
    return output_text

text = input()
print(string_reverse(text))