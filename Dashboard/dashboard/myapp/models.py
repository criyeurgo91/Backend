from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Account(models.Model):
    id_account = models.AutoField(primary_key=True)
    email_account = models.CharField(max_length=45, unique=True)
    password_account = models.CharField(max_length=255)
    dateregister_account = models.DateTimeField(auto_now_add=True)
    dateupdate_account = models.DateTimeField(auto_now=True)
    isadmin_account = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Antes de guardar el objeto, cifra la contraseña si no está cifrada
        if not self.password_account.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2$')):
            self.password_account = make_password(self.password_account)
        super().save(*args, **kwargs)
   
    def __str__(self):
        return self.email_account



class UserProfile(models.Model):
    id_userProfile = models.AutoField(primary_key=True)
    account_id_account = models.ForeignKey('Account', on_delete=models.CASCADE)
    image_userProfile = models.ImageField(upload_to='imgProfiles', null=True, blank=True)
    name_userProfile = models.CharField(max_length=45)
    lastname_userProfile = models.CharField(max_length=45)
    phone_userProfile = models.CharField(max_length=10)
    dateregister_userProfile = models.DateTimeField(auto_now_add=True)
    dateupdate_userProfile = models.DateTimeField(auto_now=True)
    ismander_userProfile = models.BooleanField(default=False)

    def __str__(self):
        return self.name_userProfile


class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    user_id_userProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    image_document = models.ImageField(upload_to='imgDocs',max_length=255)
    isdocument_vehicle = models.BooleanField()
    isverified_document = models.BooleanField()

    DOCUMENT_TYPES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('SOAT', 'SOAT'),
        ('LICENCIA', 'Licencia'),
        ('OPERACION', 'Operación'),
        ('TECNOMECANICA', 'Tecnomecánica'),
        ('RECIBO', 'Recibo'),
    ]

    type_document = models.CharField(max_length=15, choices=DOCUMENT_TYPES)

    dateregister_document = models.DateTimeField(auto_now_add=True)
    dateupdate_document = models.DateTimeField(auto_now=True)
    dateverified_document = models.DateTimeField(null=True)


class Mander(models.Model):
    id_mander = models.AutoField(primary_key=True)
    user_id_userProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    image_mander = models.ImageField (upload_to='imgMander',max_length=255, null=False)
    ishavecar_mander = models.BooleanField()
    ishavemoto_mander = models.BooleanField()
    isactive_mander = models.BooleanField()
    isvalidate_mander = models.BooleanField(default=False)
    dateregister_mander = models.DateTimeField(auto_now_add=True)
    dateupdate_mander = models.DateTimeField(auto_now=True)
    address_mander = models.CharField(max_length=100)
    cc_mander = models.CharField(max_length=13)

class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    name_service = models.CharField(max_length=45)
    detail_service = models.CharField(max_length=255)
    image_service = models.ImageField(upload_to='imgService',max_length=255)

    def __str__(self):
        return self.name_service

class Request(models.Model):
    id_request = models.AutoField(primary_key=True)
    service_id_service = models.ForeignKey('Service', on_delete=models.CASCADE)
    user_id_userProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    detail_request = models.CharField(max_length=255)

    STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Proceso', 'Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    status_request = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendiente')

    dateregister_request = models.DateTimeField(auto_now_add=True)
    dateupdate_request = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Request {self.id_request}: {self.detail_request}'

class Requestmanager(models.Model):
    id_requestmanager = models.AutoField(primary_key=True)
    request_id_request = models.ForeignKey('Request', on_delete=models.CASCADE)
    image_requestmanager = models.ImageField(upload_to='imgRequestmanager',max_length=255,null=True,blank=True)
    mander_id_mander = models.ForeignKey('Mander', on_delete=models.CASCADE, null=True)

    STATUS_CHOICES = [
        ('espera', 'En espera'),
        ('proceso', 'En proceso'),
        ('terminado', 'Terminado'),
    ]
    status_requestmanager = models.CharField(max_length=10, choices=STATUS_CHOICES)

    detail_requestmanager = models.CharField(max_length=45)
    dateregister_requestmanager = models.DateTimeField(auto_now_add=True)
    dateupdate_requestmanager = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    id_vehicle = models.AutoField(primary_key=True)
    user_id_userProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    image_vehicle = models.ImageField(upload_to='imgVehicles', max_length=255, null=False)
    brand_vehicle = models.CharField(max_length=20)
    plate_vehicle = models.CharField(max_length=10)
    model_vehicle = models.SmallIntegerField()
    color_vehicle = models.CharField(max_length=45)

    VEHICLE_TYPE_CHOICES = [
        ('ninguno', 'Ninguno'),
        ('bicicle', 'Bicicleta'),
        ('bike', 'Motocicleta'),
        ('car', 'Automóvil'),
    ]
    type_vehicle = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)

    isverified_vehicle = models.BooleanField(default=False)
    dateregister_vehicle = models.DateTimeField(auto_now_add=True)
    dateupdate_vehicle = models.DateTimeField(auto_now=True)
    dateverified_vehicle = models.DateTimeField(auto_now=True)
