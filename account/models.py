from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission
from django.conf import settings


class MyAccountManager(BaseUserManager):

    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username address")

        user=self.model(
            email=self.normalize_email(email),
            username=username
            )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


def profile_picture_location(instance, filename):
    file_path = 'pp/{filename}'.format(
            filename = filename
        )
    return file_path
    
class Account(AbstractBaseUser, PermissionsMixin):
    email						= models.EmailField(verbose_name="email",max_length=61,unique=True)
    username					= models.CharField(max_length=31)
    phone_number                = models.CharField(max_length=15, unique=True, null=True, blank=True)
    profile_picture				= models.ImageField(upload_to=profile_picture_location, null=True, blank=True)
    is_owner					= models.BooleanField(default=False)

    date_joined					= models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login					= models.DateTimeField(verbose_name="last_login",auto_now=True)
    is_admin					= models.BooleanField(default=False)
    is_active					= models.BooleanField(default=True)
    is_staff					= models.BooleanField(default=False)
    is_superuser				= models.BooleanField(default=False)

    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =["username",]

    objects = MyAccountManager()


    def __str__(self):
        return self.email +', '+self.username

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_level):
        return True

    # def get_user_permissions(self, obj=None):
    #     return user.user_permissions.all()

    # def get_all_permissions(self, obj=None):
    #     return Permission.objects.all()

    # def get_user_permissions(user):
    #     if user.is_superuser:
    #         return Permission.objects.all()
    #     return user.user_permissions.all() | Permission.objects.filter(group__user=user)

    