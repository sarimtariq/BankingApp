class BankService:

    """
    Class containing business logic to track bank accounts, current balances,
    transaction history, and allow deposits, withdrawals, and transfers.
    """

    def __init__(self):
        self.accounts_db = {}
        self.transaction_history = []

    def get_current_transaction_history(self):
        return self.transaction_history
    
    def get_curr_account_state(self):
        return [{key:value} for key, value in self.accounts_db.items()]

    def add_account(self, trans_row):
        # Use acc_num:curr_bal dict to track added accounts.
        self.accounts_db[trans_row['account']] = 0.0

    def deposit_cash(self, trans_row):
        if not self.__isValidAccount(trans_row['account']):
            print("Invalid account number")

        else:
            acc_id = trans_row['account']
            amount = trans_row['amount']
            transaction = {'time': trans_row['time'],
                        'account': trans_row['account'],
                        'credit': trans_row['amount'],
                        'debit': None,
                        'status': 'Success',
                        'type': 'ATM',
                        'balance': self.accounts_db[acc_id]}

            self.accounts_db[acc_id] += amount
            transaction['balance'] = self.accounts_db[acc_id]
            self.transaction_history.append(transaction)

    def withdraw_cash(self, trans_row):

        if not self.__isValidAccount(trans_row['account']):
            print("Invalid account number")

        else:
            acc_id = trans_row['account']
            amount = trans_row['amount']
            curr_bal = self.accounts_db[acc_id]

            transaction = {'time': trans_row['time'],
                            'account': acc_id,
                            'credit': None,
                            'debit': amount,
                            'status': None,
                            'type': 'ATM',
                            'balance': curr_bal}

            if amount <= curr_bal:
                curr_bal -= amount

                self.accounts_db[acc_id] = curr_bal
                transaction['status'] = 'Success'
                transaction['balance'] = curr_bal
            else:
                transaction['status'] = 'Failed'

            self.transaction_history.append(transaction)

    def transfer_funds(self, trans_row):
        if not self.__isValidAccount(trans_row['account']):
            print("Sending account number invalid")
        else:
            self.__internal_transfer(trans_row)

    def __internal_transfer(self, trans_row):
        sending_acc = trans_row['account']
        receiving_acc = trans_row['counterparty account']
        amount = trans_row['amount']
        sender_curr_bal = self.accounts_db[sending_acc]
        rec_curr_bal = self.accounts_db[receiving_acc]

        sender_transaction = {'time': trans_row['time'],
                        'account': sending_acc,
                        'credit': None,
                        'debit': amount,
                        'status': None,
                        'type': 'Internal Transfer',
                        'balance': sender_curr_bal}
        
        rec_transaction = {'time': trans_row['time'],
                        'account': receiving_acc,
                        'credit': amount,
                        'debit': None,
                        'status': None,
                        'type': 'Internal Transfer',
                        'balance': rec_curr_bal}

        if amount <= sender_curr_bal:
            # decrement senders account
            sender_curr_bal -= amount
            # update status and balance
            sender_transaction['status'] = 'Success'
            sender_transaction['balance'] = sender_curr_bal
            # append transaction to transaction history
            self.transaction_history.append(sender_transaction)
            # update curr bal
            self.accounts_db[sending_acc] = sender_curr_bal

            # increment receivers account
            rec_curr_bal += amount
            # update status and balance
            rec_transaction['status'] = 'Success'
            rec_transaction['balance'] = rec_curr_bal
            # append transaction to transaction history
            self.transaction_history.append(rec_transaction)
            # update curr bal
            self.accounts_db[receiving_acc] = rec_curr_bal
        else:
            # update status to failed for both transactions
            sender_transaction['status'] = 'Failed'
            rec_transaction['status'] = 'Failed'
            # append sender transaction
            self.transaction_history.append(sender_transaction)
            self.transaction_history.append(rec_transaction)

    def __isValidAccount(self, account_id):
        return account_id in self.accounts_db
