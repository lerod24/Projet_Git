# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:38:52 2024

@author: rodri
"""

import yfinance as yf
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

# Fonction pour récupérer les données de Yahoo Finance
def get_data(ticker, start_date, end_date, interval='15m'):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date, interval=interval)
    return data

# Fonction pour stocker les données dans une base de données MySQL
def store_data_to_db(data, ticker, db_config):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Création de la table si elle n'existe pas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_data (
                datetime DATETIME,
                open DOUBLE,
                high DOUBLE,
                low DOUBLE,
                close DOUBLE,
                volume INT,
                ticker VARCHAR(10),
                PRIMARY KEY (datetime, ticker)
            )
        ''')

        for index, row in data.iterrows():
            cursor.execute('''
                INSERT INTO stock_data (datetime, open, high, low, close, volume, ticker)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    open=VALUES(open),
                    high=VALUES(high),
                    low=VALUES(low),
                    close=VALUES(close),
                    volume=VALUES(volume)
            ''', (index.to_pydatetime(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], ticker))

        conn.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur : Les informations d'utilisateur ou de mot de passe sont incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Erreur : La base de données n'existe pas")
        else:
            print(err)
    finally:
        cursor.close()
        conn.close()

# Fonction principale pour récupérer et stocker les données
def main():
    ticker = 'RX=F'  
    start_date = '2024-06-17'
    end_date = '2024-06-21'

    db_config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'trading'
    }

    data = get_data(ticker, start_date, end_date)
    store_data_to_db(data, ticker, db_config)

if __name__ == '__main__':
    main()