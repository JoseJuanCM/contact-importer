import csv

from rest_framework import serializers

from config.settings.base import MEDIA_URL, MEDIA_ROOT
from contact_importer.contacts.models import FileImport


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
