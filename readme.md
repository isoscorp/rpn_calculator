# RPN CALCULATOR
> Calculator API using Reverse Polish Notation
* Python 3.8
* Flask-RESTPlus
* SQLAlchemy
* PostgresSQL

## Installation
### Setup api
Install dependencies with
```shell
pip install -r ./setup/requirements.txt
```
### Setup database
Install postgres and run the following script
```psql
CREATE DATABASE db;

CREATE SCHEMA IF NOT EXISTS rpn;

CREATE TABLE IF NOT EXISTS rpn.stacks(
    id      SERIAL PRIMARY KEY,
    items   INTEGER array
);
```
You can then configure your database environment variables in `config/config.py`

## Usage
In production, run your application with
```shell
gunicorn main:app --bind "0.0.0.0:8080"
```

## Release History
* 0.0.1
    * Initialized API for RPN calculator