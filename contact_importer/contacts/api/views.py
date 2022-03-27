import csv

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from config.settings.base import MEDIA_ROOT
from contact_importer.contacts.api.serializers import FileImportSerializer, FileImportReadOnlySerializer
from contact_importer.contacts.models import FileImport, Contact
from contact_importer.contacts.validations import name_validation, phone_validation


class FileImportViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = FileImportSerializer
    queryset = FileImport.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return FileImportReadOnlySerializer
        return FileImportSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
