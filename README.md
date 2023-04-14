# Lab reports
_Anastasia Panova, 14 April 2023_


## Lab 1


The code `glossa.py` extracts the text content of the linguistic articles available athttps://www.glossa-journal.org/articles/ (only the first page). The results are stored in the file `data.json`.

How to run `glossa.py`:

```
python3 -m venv env
source env/bin/activate
pip install scrapy
scrapy runspider glossa.py -o data.json
deactivate
```

