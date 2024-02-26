from rest_framework.viewsets import ModelViewSet
from userapp.models import MigrationCategory, MigrationType, UserSignup

from rest_framework.views import APIView

from userapp.serializers import MigrationCategorySerializer, MigrationTypeSerializer, NestedUserSignupSeiralizer, UserSignupSeiralizer
from drf_spectacular.utils import extend_schema
# Create your views here.


@extend_schema(tags=["Migration Category"])
class MigrationCategoryViewSet(ModelViewSet):
    serializer_class = MigrationCategorySerializer
    queryset = MigrationCategory.objects.all()



@extend_schema(tags=["Migration Type"])
class MigrationTypeViewSet(ModelViewSet):
    serializer_class = MigrationTypeSerializer
    queryset = MigrationType.objects.all()



@extend_schema(tags=["User Sign up"])
class UserSignupViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return NestedUserSignupSeiralizer
        else:
            return UserSignupSeiralizer
    queryset = UserSignup.objects.all()


                