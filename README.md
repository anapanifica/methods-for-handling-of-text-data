# Lab reports

_Anastasia Panova, April 2023_


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

## Lab 4

The data file 'lab4_corpus.flextext' is part of the corpus of Gawarbati (an underdescribed Indo-Aryan language) that I use in my PhD project. The corpus is tokenized and annotated in the program FLEx and stored in an xml-like format. The code `lab4_code.py` finds collocations which occur 10 times in the coorpus and makes a frequency list. Here is an output of the code:

```
[('kaɽi', 'tabaː'), ('alhamdu', 'lillah'), ('do', 'hazaːr'), ('hazaːr', 'bais'), ('ɕe', 'ʥausãː'), ('ʥaː', 'baten'), ('nun', 'sobaːra'), ('amai', 'ʥaua'), ('niɕisan', 'tʰanek'), ('ɕi', 'ʥausãː'), ('tʰanem', 'naːsir'), ('aːindaː', 'ʂaʦi'), ('haranua', 'niɕisan'), ('ɕila', 'ʨal'), ('ite', 'hadikaː')]
[['ki', 1009], ['bi', 709], ['au', 530], ['tʰana', 514], ['ama', 419], ['giri', 401], ['ba', 382], ['tine', 375], ['woi', 373], ['laka', 359], ['ʨi', 349], ['e', 338], ['lau', 322], ['na', 314], ['asa', 303]]
```




