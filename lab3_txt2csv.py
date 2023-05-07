import re


def clean_data_and_mark_new_pages():
    
    f = open ("lab2_Gawarbati_alphabet_book2.txt", 'r', encoding = 'utf-8')
    txt = f.read()
    f.close ()


    clean_data = ""

    
    #remove "Bismallah al-Rahman al-Raheem" which appeared in txt but was in white color and thus invisible in pdf 
    txt = re.sub('﷽', '', txt)
    
    for line in txt.split("\n"):
        line = re.sub('[A-Za-z0-9@;:.,©-]','', line) #remove english letters, numbers and punctuation
        line = re.sub('()','new_page', line) #a hidden charachter in parentheses


        if line.strip():
            clean_data = clean_data + line.strip() + "\n"

    return clean_data


def remove_the_beginning_and_the_end (clean_data):
    alphabet = ''
    currentLine = 1
    for line in clean_data.split("\n"):
        if currentLine in list(range(68)) + list(range(344,352)) + list(range(387,414)):
            pass
        else:
            alphabet = alphabet + line + "\n"

        currentLine += 1

    return alphabet.strip() #remove the last \n





def make_a_csv (alphabet):
    csv = "letter\tname_of_the_letter\tword1\tword2\tword3\n"
    for page in alphabet.split("new_page\n"):
        for line in page.split("\n"):
            csv = csv + line + "\t"
        csv = csv.strip() + "\n"

    return csv

    

def main ():
    clean_data = clean_data_and_mark_new_pages()
    alphabet = remove_the_beginning_and_the_end (clean_data)
    csv = make_a_csv (alphabet)


    path = 'lab3_alphabet.csv'
    f = open (path, 'w', encoding = 'utf-8')
    f.write (csv)
    f.close



if __name__ == '__main__':
    main ()




