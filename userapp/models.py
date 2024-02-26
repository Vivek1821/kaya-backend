from django.db import models

# Create your models here.


class MigrationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class MigrationCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class UserSignup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    migration_category = models.ForeignKey(MigrationCategory,on_delete=models.SET_NULL,null=True)
    migration_type = models.ForeignKey(MigrationType,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


