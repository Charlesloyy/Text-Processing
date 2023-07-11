import string
def text_process(mess):
    nopunc = [char.lower() for char in mess if char not in string.punctuation]
    nopunc = "".join(nopunc)
    
    return nopunc

mess = input("Enter: ")
print(text_process(mess))
