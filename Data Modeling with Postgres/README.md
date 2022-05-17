## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like to create a Postgres database with tables designed to optimize queries on song play analysis.

## Database Schema Design

Below is a summary of the database schema and ETL pipeline.

Schema for Song Play Analysis

#### Fact Table

fct_songplays - records in log data associated with song plays

#### Dimension Tables

dim_users - the app

dim_songs - music database

dim_artists - music database

dim_time - timestamps of records in songplays broken down into specific units

## Python Scripts


test.ipnb displays the first few rows of each table to let you check your database

create_tables.py drops and created your table

etl.ipynb read and processes a single file from song_data and log_data and loads into your tables in Jupyter notebook

etl.ipynb read and processes a single file from song_data and log_data and loads into your tables in ET

sql_queries.py containg all your sql queries and in imported into the last three files above


