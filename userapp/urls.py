from django.urls import path,include
from rest_framework.routers import SimpleRouter

from userapp.views import MigrationCategoryViewSet, MigrationTypeViewSet, UserSignupViewSet


router = SimpleRouter()
router.register(r'migration-category', MigrationCategoryViewSet)
router.register(r'migration-type', MigrationTypeViewSet)
router.register(r'user-signup', UserSignupViewSet)

urlpatterns = [
    path('migration',include(router.urls))
]