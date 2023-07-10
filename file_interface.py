import csv
from datetime import datetime

class FileInterface:

    """
    Class containing code to load and preprocess data from csv file, perform the associated
    action based on the csv file, and write the output to a csv file.
    """

    def __init__(self, bank_service):
        self.bank_service = bank_service

    def load_and_preprocess_data(self):
        with open('csv/input-file.csv', newline='') as f:
            reader = csv.DictReader(f, fieldnames=["time","account","counterparty account","action","amount"])
            next(reader) # skip header

            data_dict = [row for row in reader]

        for data in data_dict:
            data['time'] = datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S')
            if data['amount']:
                data['amount'] = float(data['amount'].replace('$', ''))
            
        return data_dict
    
    def perform_bank_actions(self, data):
        action_map = {
        "create account": self.bank_service.add_account,
        "deposit": self.bank_service.deposit_cash,
        "withdraw": self.bank_service.withdraw_cash,
        "instant transfer": self.bank_service.transfer_funds
        }

        for row in data:
            if row['action'] in action_map:
                action_map[row['action']](row)

    def write_bank_statements(self):
        data_dict = self.bank_service.get_current_transaction_history()
        sorted_data = sorted(data_dict, key=lambda x: (x['time'], x['account']))
        
        with open('output/output-file.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=sorted_data[0].keys())
            writer.writeheader()
            for row in sorted_data:
                writer.writerow(row)

