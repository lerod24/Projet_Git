# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:54:53 2024

@author: rodri
"""

#extraire des données de plusieurs tickers sur yahoo finance


import yfinance as yf
import mysql.connector
from mysql.connector import Error
import pandas as pd

#definir le ticker
SG= 'GLE.PA'
Apple="AAPL"
MS="MSFT"
Google="GOOGL"
Cac40="^FCHI"
Facebook="META"
Toyota="TM.BA"
SAP_erp="SAP"
TotalEnergies="TTE.PA"
tickers = [SG, Apple, MS, Google, Cac40, Facebook, Toyota, SAP_erp, TotalEnergies]

# Télécharger les données historiques pour ce ticker
data = yf.download(tickers, start="2024-05-01", end="2024-05-31")

# Afficher les premières lignes des données
print(data.head())


# Télécharger les données pour une action spécifique (par exemple, Apple)
google="GOOGL"

ticker = "GOOGL"
data = yf.download(ticker, start='2024-05-01', end='2024-05-31')

# Configuration de la connexion MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',  
        database='yahoo_finance'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        create_table_query = 
        CREATE TABLE IF NOT EXISTS stock_data (
            Date DATE PRIMARY KEY,
            Open FLOAT,
            High FLOAT,
            Low FLOAT,
            Close FLOAT,
            Adj_Close FLOAT,
            Volume BIGINT
        )
        '''

        cursor.execute(create_table_query)
        connection.commit()

        # Insérez les données dans la table
        for i, row in data.iterrows():
            insert_query = '''
            REPLACE INTO stock_data (Date, Open, High, Low, Close, Adj_Close, Volume) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (i, row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']))

        connection.commit()
        print("Données insérées avec succès")

except Error as e:
    print("Erreur lors de la connexion à MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion MySQL fermée")