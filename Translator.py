from deep_translator import GoogleTranslator

with open('ENtext.txt' , mode = 'r') as en_file:
    text = str()
    for line in en_file.readlines():
        text += line

    translated_text = GoogleTranslator(target = 'de').translate(text)



with open('DEtext.txt', mode = 'w') as de_file:
    text2 = de_file.write(translated_text)





