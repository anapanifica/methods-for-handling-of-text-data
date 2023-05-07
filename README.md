# Lab reports

_Anastasia Panova, April-May 2023_


All files mentioned in the reports can be found here: https://github.com/anapanifica/methods-for-handling-of-text-data.


## Lab 1


The code `lab1_spider.py` extracts the text content of the linguistic articles available at https://www.glossa-journal.org/articles/ (only the first page). The results are stored in the file `lab1_data.json`.

To run `lab1_spider.py` on my own computer, I installed `scrapy` in the virtual environment:

```
python3 -m venv env
source env/bin/activate
pip install scrapy
scrapy runspider lab1_spider.py -o lab1_data.json
deactivate
```

## Lab 2

The data for this lab is the alphabet book of Gawarbati, an underdescribed Indo-Aryan language. It is a searchable pdf file which contains letters, words and several sentences in Gawarbati (written in the Urdu-based script) and some information about the publisher in English.

First, I converted the pdf file to txt on the university server.
```
pdftotext lab2_Gawarbati_alphabet_book.pdf
```
However, the resulting `lab2_Gawarbati_alphabet_book.txt` file contained a lot of hidden, unprintable charachters, and it was very difficult to remove all of them (at least, I couldn't). So, I exported the pdf file to txt using the implemented function in the Adobe Acrobat Reader, and saved it as `lab2_Gawarbati_alphabet_book2.txt`. Then I used the code `lab2_clean_data.py` to remove unprintable charachetrs (in this file it was easy to detect them), English words, numerals and punctuation. The raw UTF-8 text in Gawarbati is saved in `lab2_res.txt`.


## Lab 3

The code `lab3_txt2csv.py` reads the file `lab2_Gawarbati_alphabet_book2.txt` (also used in Lab 2), removes the beginning and the end of the book and saves it  in the tabular format to `lab3_alphabet.csv`. The csv-table follows the structure of the alphabet book and has the following columns: `letter`, `name_of_the_letter`, `word1`, `word2`, `word3`. Normally in `word1` the target letter is in the beginning of the word, in `word2` the target letter is in the middle of the word, and in `word3` the target letter is in the end of the world. For some letters not all types of words are present in the book.



## Lab 4

The data file `lab4_corpus.flextext` is part of the corpus of Gawarbati that I use in my PhD project. The corpus is transcribed in IPA, tokenized and annotated in the program FLEx and stored in an xml-like format. The code `lab4_code.py` finds collocations which occur 10 times in the corpus and makes a frequency list. Here is an output of the code:

```
[('kaɽi', 'tabaː'), ('alhamdu', 'lillah'), ('do', 'hazaːr'), ('hazaːr', 'bais'), ('ɕe', 'ʥausãː'), ('ʥaː', 'baten'), ('nun', 'sobaːra'), ('amai', 'ʥaua'), ('niɕisan', 'tʰanek'), ('ɕi', 'ʥausãː'), ('tʰanem', 'naːsir'), ('aːindaː', 'ʂaʦi'), ('haranua', 'niɕisan'), ('ɕila', 'ʨal'), ('ite', 'hadikaː')]
[['ki', 1009], ['bi', 709], ['au', 530], ['tʰana', 514], ['ama', 419], ['giri', 401], ['ba', 382], ['tine', 375], ['woi', 373], ['laka', 359], ['ʨi', 349], ['e', 338], ['lau', 322], ['na', 314], ['asa', 303]]
```

## Lab 5

In this lab, I trained tokenization and lemmatization models for Abaza, a Northwest Caucasian language. Following [this](https://github.com/stanfordnlp/stanza-train) and [this](https://stanfordnlp.github.io/stanza/training_and_evaluation.html) instructions, I cloned repositories `stanza` and `stanza-train`, removed the toy English data and replaced it by the Abaza data. I used [the UD treebank of Abaza](https://github.com/UniversalDependencies/UD_Abaza-ATB/tree/dev) which contains about 100 sentences. I divided them into training data and test data, added required .txt files with plain sentences and trained models for tokenization and lemmatization. I did not manage to train models for pos-tagging and syntactic annotation because they require pretrained embedding vectors, and there are no pretrained embedding vectors for Abaza.

After that, I created the folder `abq_stanza_resources` and several files inside that folder, following the instruction on adding a new language [here](https://stanfordnlp.github.io/stanza/new_language.html). I wrote the script `try.py` to check how the model tokenizes and lemmatizes sentences from the test data.

As expected, the results for tokenization do not make much sense because the plain sentences in the Abaza treebank were already tokenized. The results for lemmatization are very bad. This is also expected because Abaza has a very complicated morphology, and the Abaza treebank is very small.

The output of `try.py`:

```
2023-04-28 01:29:04 INFO: Loading these models for language: abq (Abaza):
=======================================
| Processor | Package                 |
---------------------------------------
| tokenize  | stanza/sav...kenizer.pt |
| lemma     | stanza/sav...matizer.pt |
=======================================

2023-04-28 01:29:04 INFO: Using device: cpu
2023-04-28 01:29:04 INFO: Loading: tokenize
2023-04-28 01:29:05 INFO: Loading: lemma
2023-04-28 01:29:05 INFO: Done loading processors!
[
  [
    {
      "id": 1,
      "text": "сара",
      "lemma": "сара",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "сыхьиз",
      "lemma": "х",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "фатимапI",
      "lemma": "а",
      "start_char": 12,
      "end_char": 20
    }
  ]
]

```


# Lab6

The data for this lab is the novel "War and Peace" by Leo Tolstoy (in the English translation). I downloaded the txt version of the novel from here: https://www.gutenberg.org/ebooks/2600. I tokenized the text and used `fasttext` to train a model, see `lab6_fasttext_train.py`. Then I checked the nearest neighbors of several words, see `lab6_fasttext_check.py`. This is the output for the nearest neighbors of the word _black_:

```
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
[(0.9686030745506287, 'blue'), (0.9515423774719238, 'thick'), (0.949993908405304, 'bluish'), (0.9420170783996582, 'cloth'), (0.9416075348854065, 'swift'), (0.9343125224113464, 'shaggy'), (0.9326506853103638, 'hairy'), (0.9326242804527283, 'breeches'), (0.9290524125099182, 'pillows'), (0.9290413856506348, 'yellow')]
```






