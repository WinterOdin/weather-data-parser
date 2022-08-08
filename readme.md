# AlterData recruitmpremisesk

## the Task premis:

Let user pick two stations from the ones available in the CSV.
Present their monthly statistics side by side The attachedare them.
Attached `data.csv` the contains data for year 2021 from weather stations located in Poland. [Data download](https://drive.google.com/file/d/1BtVwzeTFfKm9KLczKl5VQwfqBw95CQHF/view?usp=sharing)

## Running

To run script activate virtual env and then run python command  

```python
env\Scripts\activate
python script.py cityA cityB
```
where the city can be
- BIALYSTOK,
- GDANSK,
- GORZOW WLKP,
- KATOWICE,
- KIELCE,
- LUBLIN,
- OLSZTYN,
- OPOLE,
- SZCZECIN,
- ZIELONA GORA
### Important
If the city name is a compound (i.e has spaces) wrap the argument in  double quote: "ZIELONA GORA" 

### Running tests
To run tests activate virtual env and run python command 
```python
env\Scripts\activate
pytest tests.py
```
### Requirements
- python version 3.7.9
- attrs
- numpy
- pandas
- pyparsing
- pytest
- typing_extensions

