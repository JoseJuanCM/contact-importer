from rest_framework import serializers

from contact_importer.contacts.models import FileImport, Contact, FileImportErrors


class FileImportSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FileImport
        fields = ["id", "user", "file", "headers_configuration"]


class FileImportReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileImport
        fields = ["id", "user", "file", "headers_configuration", "status"]
        read_only_fields = fields


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "user", "name", "birth_date", "phone", "address", "franchise", "email", "last4"]


class FileImportErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileImportErrors
        fields = ["id", "file", "record", "error"]
