# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:54:53 2024

@author: rodri
"""

#extraire des données de plusieurs tickers sur yahoo finance

import yfinance as yf

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

import matplotlib.pyplot as plt
data['Close'].plot()
plt.show()