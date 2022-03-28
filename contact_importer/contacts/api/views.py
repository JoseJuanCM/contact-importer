from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from contact_importer.contacts.api.serializers import FileImportSerializer, FileImportReadOnlySerializer, \
    ContactSerializer, FileImportErrorsSerializer
from contact_importer.contacts.models import FileImport, Contact, FileImportErrors


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class FileImportViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = FileImportSerializer
    queryset = FileImport.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return FileImportReadOnlySerializer
        return FileImportSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ContactViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class FileImportErrorsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = FileImportErrorsSerializer
    queryset = FileImportErrors.objects.all()
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['file']

    def get_queryset(self):
        return self.queryset.filter(file__user=self.request.user)
