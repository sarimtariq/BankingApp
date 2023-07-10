from file_interface import FileInterface
from bank_service import BankService



if __name__ == "__main__":
    bank_service = BankService()
    file_int = FileInterface(bank_service)

    data = file_int.load_and_preprocess_data()
    file_int.perform_bank_actions(data)
    file_int.write_bank_statements()