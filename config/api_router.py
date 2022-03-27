from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from contact_importer.contacts.api.views import FileImportViewSet
from contact_importer.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("files", FileImportViewSet)


app_name = "api"
urlpatterns = router.urls
