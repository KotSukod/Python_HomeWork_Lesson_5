# Напишите программу удаляющую из текста слов, содержащие "абв"               

data = 'Я люблю Джавуабв абви Питон '
help = "абв"
   
text = []

while data != '':
    space_pos = data.index(' ') 
    text.append(data[:space_pos].lower())
    data = data[space_pos + 1:]
i = 0
txt_str = ''
while i < len(text):
    if help in  text[i]:
        text.remove(text[i])
        i -= 1   
    i += 1    
for i in text:
    txt_str = txt_str + i + ' ' 

print(txt_str)



  
