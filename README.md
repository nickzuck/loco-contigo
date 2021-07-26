# loco-contigo

## Installation:
- Python 3.7
- Postgres
- Other Requirements using (`pip install requirements.txt`)

## How to Run
- Change the settings of the database using settings.py as per your database setting
- Migrate using `python manage.py migrate`
- Start application by `python manage.py runserver`

## URLS :
- Create Transaction  : /transactionservice/transaction (POST) 
- Get Transaction : /transactionservice/transaction/<txn_id> (GET)
- Get Transaction Ids by Type : /transactionservice/transaction/types/<type> (GET)
- Get Transaction Heirarchical Sum - /transactionservice/transaction/sum/<txn_id> (GET)
