from rest_framework import serializers
from myapp.models import *



class account_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ('id_account', 'email_account', 'password_account', 'dateregister_account', 'dateupdate_account', 'isadmin_account')


class user_profile_serializer(serializers.ModelSerializer):
    account_id_account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), allow_null=True)
    class Meta:
        model  = UserProfile
        fields = ('id_userProfile', 'account_id_account', 'image_userProfile', 'name_userProfile', 'lastname_userProfile', 'phone_userProfile', 'dateregister_userProfile', 'dateupdate_userProfile', 'ismander_userProfile')
        depth = 2
        
class document_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Document
        fields = ('id_document', 'user_id_userProfile', 'image_document', 'isdocument_vehicle', 'isverified_document', 'type_document', 'dateregister_document', 'dateupdate_document', 'dateverified_document')

class mander_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Mander
        fields = ('id_mander', 'user_id_userProfile', 'image_mander', 'ishavecar_mander', 'ishavemoto_mander', 'isactive_mander', 'isvalidate_mander', 'dateregister_mander', 'dateupdate_mander', 'address_mander', 'cc_mander')

class service_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Service
        fields = ('id_service', 'name_service', 'detail_service', 'image_service')

class request_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Request
        fields = ('id_request', 'service_id_service', 'user_id_userProfile', 'detail_request', 'status_request', 'dateregister_request', 'dateupdate_request')

class request_manager_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Requestmanager
        fields = ('id_requestmanager', 'request_id_request', 'image_requestmanager', 'mander_id_mander', 'status_requestmanager', 'detail_requestmanager', 'dateregister_requestmanager', 'dateupdate_requestmanager')

class vehicle_serializer(serializers.ModelSerializer):
    class Meta:
        model  = Vehicle
        fields = ('id_vehicle', 'user_id_userProfile', 'image_vehicle', 'brand_vehicle', 'plate_vehicle', 'model_vehicle', 'color_vehicle', 'type_vehicle', 'isverified_vehicle', 'dateregister_vehicle', 'dateupdate_vehicle', 'dateverified_vehicle')

