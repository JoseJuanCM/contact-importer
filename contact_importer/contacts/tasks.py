import csv

from config import celery_app
from config.settings.base import MEDIA_ROOT
from contact_importer.contacts.models import FileImport, Contact, FileImportErrors
from contact_importer.contacts.validations import name_validation, phone_validation, birth_date_validation, \
    credit_card_franchise, tokenize_credit_card


@celery_app.task()
def process_files():
    files = FileImport.objects.filter(status="HOLD")
    for file in files:
        file.status = "PROCESSING"
        file.save()
        with open(MEDIA_ROOT + "/" + str(file.file), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            row_count = 0
            total_errors = 0
            for row in reader:
                errors = {}
                credit_card_brand = None
                credit_card_last4 = None
                credit_card_token = None
                """Column for name field"""
                try:
                    contact_name = row.get(file.headers_configuration['name'])
                    if not name_validation(contact_name):
                        errors[file.headers_configuration['name']] = "Invalid symbol in name"
                except:
                    errors[file.headers_configuration['name']] = "Column not found"

                """Column for address field"""
                try:
                    contact_address = row.get(file.headers_configuration['address'])
                    if not contact_address:
                        errors[file.headers_configuration['address']] = "Empty address"
                except:
                    errors[file.headers_configuration['address']] = "Column not found"

                """Column for email filed"""
                try:
                    contact_email = row.get(file.headers_configuration['email'])
                    if Contact.objects.filter(email=contact_email, user=file.user).exists():
                        errors[file.headers_configuration['email']] = "Email already registered"
                except:
                    errors[file.headers_configuration['email']] = "Column not found"

                """Column for phone filed"""
                try:
                    contact_phone = row.get(file.headers_configuration['phone'])
                    if not phone_validation(contact_phone):
                        errors[file.headers_configuration['phone']] = "Phone wrong format"
                except:
                    errors[file.headers_configuration['phone']] = "Column not found"

                """Column for birth date filed"""
                try:
                    contact_birth_date = row.get(file.headers_configuration['birth_date'])
                    if not birth_date_validation(contact_birth_date):
                        errors[file.headers_configuration['birth_date']] = "Birthday wrong format"
                except:
                    errors[file.headers_configuration['birth_date']] = "Column not found"

                """Column for credit card filed"""
                try:
                    contact_card = row.get(file.headers_configuration['card'])
                    credit_card_validation = credit_card_franchise(contact_card)
                    if not credit_card_validation:
                        errors[file.headers_configuration['card']] = "Franchise not found or length invalid"
                    else:
                        credit_card_brand = credit_card_validation
                        credit_card_last4 = contact_card[-4:]
                        credit_card_token = tokenize_credit_card(contact_card)
                except:
                    errors[file.headers_configuration['card']] = "Column not found"

                row_count += 1
                if errors:
                    FileImportErrors.objects.create(file=file, record=row, error=errors)
                    total_errors += 1
                else:
                    Contact.objects.create(user=file.user, name=contact_name, email=contact_email,
                                           birth_date=contact_birth_date, phone=contact_phone,
                                           address=contact_address, card=credit_card_token,
                                           franchise=credit_card_brand, last4=credit_card_last4)

            if row_count == total_errors:
                file.status = "FAILED"
                file.save()
            else:
                file.status = "TERMINATED"
                file.save()
    return True
