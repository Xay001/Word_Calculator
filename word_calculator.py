word = 1

text = input("Enter the text :")

for i in text:
    if(i == " "):
        word = word + 1

print(word)