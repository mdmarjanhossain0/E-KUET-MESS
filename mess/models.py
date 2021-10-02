from django.db import models

from account.models import Account

def mess_picture_location(instance, filename):
    file_path = 'mess/{mess_name}/{filename}'.format(
            filename = filename,
            mess_name = instance.name
        )
    return file_path

def mess_space_picture_location(instance, filename):
    file_path = 'mess/{mess_name}/{space_name}/{filename}'.format(
            filename = filename,
            mess_name = instance.name,
            space_name = instance.name
        )
    return file_path

class Category(models.Model):
    name                     = models.CharField(max_length=15, unique=True)


    def __str__(self):
        return self.name
    



class Mess(models.Model):
    name                    = models.CharField(max_length=31, unique=True)
    category                = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner                   = models.ForeignKey(Account, on_delete=models.CASCADE)
    distance                = models.IntegerField()
    price_range             = models.CharField(max_length=15)
    image_1                 = models.ImageField(upload_to=mess_picture_location, null=True, blank=True)
    details                 = models.TextField(max_length=501)

    def __str__(self):
        return self.name




class Space(models.Model):
    image_1                 = models.ImageField(upload_to=mess_picture_location, null=True, blank=True)
    image_2                 = models.ImageField(upload_to=mess_picture_location, null=True, blank=True)
    image_3                 = models.ImageField(upload_to=mess_picture_location, null=True, blank=True)
    image_4                 = models.ImageField(upload_to=mess_picture_location, null=True, blank=True)
    image_5                 = models.ImageField(upload_to=mess_picture_location, null=True, blank=True)

    mess                    = models.ForeignKey(Mess, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=31, unique=True)
    details                 = models.TextField(max_length=501)
    price                   = models.IntegerField()
    mess_type               = models.CharField(max_length=15)
    square_fit              = models.IntegerField()

    
    total_room              = models.IntegerField(default=1)
    washroom                = models.IntegerField(default=1)
    is_attach_washroom      = models.BooleanField(default=False)
    kitchen                 = models.BooleanField(default=False)
    corridor                = models.BooleanField(default=False)
    total_windows           = models.IntegerField(default=1)
    

    room_capability         = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    



