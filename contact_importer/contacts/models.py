import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FileImport(TimeStampedModel):
    class FileStatus(models.TextChoices):
        HOLD = "HOLD", "On Hold"
        PROCESSING = "PROCESSING", "Processing"
        FAILED = "FAILED", "Failed"
        TERMINATED = "TERMINATED", "Terminated"

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_user")
    file = models.FileField(upload_to="files/")
    headers_configuration = models.JSONField()
    status = models.CharField(max_length=20, choices=FileStatus.choices, default=FileStatus.HOLD)

    class Meta:
        verbose_name = "File Import"
        verbose_name_plural = "Files Import"

    def __str__(self):
        return f'{self.id}'


class FileImportErrors(TimeStampedModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    file = models.ForeignKey(FileImport, on_delete=models.CASCADE, related_name="file_error")
    record = models.CharField(max_length=250)
    error = models.CharField(max_length=250)

    class Meta:
        verbose_name = "File Import Error"
        verbose_name_plural = "Files Import Errors"

    def __str__(self):
        return f'{self.file}'


class Contact(TimeStampedModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contact_user")
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    card = models.CharField(max_length=20)
    franchise = models.CharField(max_length=25)
    email = models.EmailField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        constraints = [UniqueConstraint(fields=['user', 'email'], name='unique_user_contact')]

    def __str__(self):
        return f'Name: {self.name} | Email: {self.email}'

