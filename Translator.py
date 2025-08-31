from deep_translator import GoogleTranslator

with open('ENtext.txt' , mode = 'r') as en_file:
    text = GoogleTranslator(target = 'de').translate(str(en_file.readlines()))

with open('DEtext.txt', mode = 'w') as de_file:
    text2 = de_file.write(text)
    print(text2)




