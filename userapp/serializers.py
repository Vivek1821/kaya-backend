from rest_framework import serializers

from userapp.models import MigrationCategory, MigrationType, UserSignup



class MigrationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MigrationType
        fields = '__all__'




class MigrationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MigrationCategory
        fields = '__all__'



class UserSignupSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = '__all__'



class NestedUserSignupSeiralizer(serializers.ModelSerializer):
    migration_category = MigrationCategorySerializer()
    migration_type = MigrationTypeSerializer()
    class Meta:
        model = UserSignup
        fields = '__all__'