from django.contrib import admin

from contact_importer.contacts.models import FileImport, FileImportErrors, Contact

admin.site.register(FileImport)
admin.site.register(FileImportErrors)
admin.site.register(Contact)
