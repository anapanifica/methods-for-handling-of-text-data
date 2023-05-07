import fasttext
import re

clean_txt = ''

file = open("lab6_war_and_peace.txt", "r", encoding="utf8")
txt = file.read()
file.close()

txt_lower = txt.lower()

re_word = re.compile(r'\w+')
for word in re_word.findall(txt_lower):
    clean_txt += word + " "


f = open ('lab6_war_and_peace_tokenized.txt', 'w', encoding = 'utf-8')
f.write (clean_txt)
f.close

# train the model
war_and_peace = fasttext.train_unsupervised('lab6_war_and_peace_tokenized.txt', model = 'skipgram')
war_and_peace.save_model("lab6_war_and_peace.bin")

