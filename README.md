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
scrapy runspider glossa.py -o data.json
deactivate
```

