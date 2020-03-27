def is_valid_bank_account(account_number):
    if int(account_number)/4 != 0:
        validation_error("Toto není validní číslo účtu")
    return True
