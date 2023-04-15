import re

clean_data = ""

with open ("lab2_Gawarbati_alphabet_book2.txt") as f:
   for line in f:

        line = re.sub('[A-Za-z0-9@;:.,©-]',"", line) #remove english letters, numbers and punctuation
        line = re.sub('(<0x\w*>)',"", line) #remove hidden charachters

        if line.strip():
            clean_data = clean_data + line.strip() + "\n"
            
            
f = open("lab2_res.txt", "w", encoding = 'utf-8')
f.write(clean_data)
f.close()
