def remove_4th_char(text):
    index = 3
    if len(text) > index:
       text = text[0 : index : ] + text[index + 1 : :]
    return text
    
print(remove_4th_char("Hack Enosis"))