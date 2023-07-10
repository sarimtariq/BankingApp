# BankingApp
Backend code for banking app that handles loading from and writing to csv, and performing basic banking transactions (deposit, withdrawal, transfers).

The code in this Python application was a 1 hour coding interview challenge I took part in some time ago.

The problem statement was as follows:

Given an input file, create a backend application in Python that can handle file input and output, and perform the various banking transactions outlined within the input file. The input file is a ledger that contains various data for multiple different accounts that fall under our bank. The backend system should parse the file, perform the various transactions, and return a transaction log ordered by time and account.

To run the file, simply run the command python3 bank_controller.py

This will read the input file from the csv file and generate an output file in the output folder. The correct output is already included, running the application again will overwrite this existing file.
