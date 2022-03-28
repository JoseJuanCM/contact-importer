import hashlib
import re

from django.utils.datetime_safe import datetime


def name_validation(name):
    for letter in name:
        if letter not in [" ", "-"]:
            if not letter.isalpha():
                return False
    return True


def phone_validation(phone):
    phone_regex_1 = re.compile(r'(\(\+\d\d\)) (\d\d\d-\d\d\d-\d\d-\d\d)')
    phone_regex_2 = re.compile(r'(\(\+\d\d\)) (\d\d\d \d\d\d \d\d \d\d)')
    match_1 = phone_regex_1.fullmatch(phone)
    match_2 = phone_regex_2.fullmatch(phone)
    if match_1:
        return True
    elif match_2:
        return True
    return False


def birth_date_validation(birth_date):
    birth_date_regex = re.compile(r'(\d\d\d\d-\d\d-\d\d)')
    match = birth_date_regex.fullmatch(birth_date)
    if match:
        return True
    return False


def credit_card_franchise(credit_card):
    if credit_card.startswith(('51', '52', '53', '54', '55')) and len(credit_card) == 16:
        return "Mastercard"
    elif credit_card.startswith(('34', '37')) and len(credit_card) == 15:
        return "American Express"
    elif credit_card.startswith('36') and len(credit_card) in [14, 15, 16, 17, 18, 19]:
        return "Diners Club International"
    elif credit_card.startswith(('6011', '644', '645', '646', '647', '648', '649', '65')) and len(credit_card) in \
            [16, 17, 18, 19]:
        return "Discover Card"
    elif credit_card.startswith(('3528', '3529', '3530', '3531', '3532', '3533', '3534', '3535', '3536', '3537', '3538',
                                 '3539', '3540', '3541', '3542', '3543', '3544', '3545', '3546', '3547', '3548', '3549',
                                 '3550', '3551', '3552', '3553', '3554', '3555', '3556', '3557', '3558', '3559', '3560',
                                 '3561', '3562', '3563', '3564', '3565', '3566', '3567', '3568', '3569', '3570', '3571',
                                 '3572', '3573', '3574', '3575', '3576', '3577', '3578', '3579', '3580', '3581', '3582',
                                 '3583', '3584', '3585', '3586', '3587', '3588', '3589')) and len(credit_card) in \
            [16, 17, 18, 19]:
        return "JCB"
    elif credit_card.startswith('4') and len(credit_card) in [13, 16]:
        return "Visa"
    elif credit_card.startswith(('4026', '417500', '4508', '4844', '4913', '4917')) and len(credit_card) == 16:
        return "Visa Electron"
    else:
        return False


def tokenize_credit_card(credit_card):
    salt = str(datetime.utcnow().microsecond)
    return hashlib.sha256(salt.encode() + credit_card.encode()).hexdigest()
