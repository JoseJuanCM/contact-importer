from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "contact_importer.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import contact_importer.users.signals  # noqa F401
        except ImportError:
            pass
