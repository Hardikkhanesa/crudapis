from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from core import serializers as core_serializers
from core import models as core_models

# Create your views here.

#Create api
class CrudView(views.APIView):
    def post(self,request):
        data = request.data
        serializer_instance = core_serializers.TestCrudSerializer(
            data=request.data
        )
        if not serializer_instance.is_valid():
            print(
                "serializer_instance.errors {}".format(serializer_instance.errors)
            )
            return Response({
                "error":serializer_instance.errors
            })
            
        name = serializer_instance.validated_data.get("name")
        email = serializer_instance.validated_data.get("email")
        phone = serializer_instance.validated_data.get("phone")
        date_of_birth = serializer_instance.validated_data.get("date_of_birth")
        gender = serializer_instance.validated_data.get("gender")
        
        try:
            instance=core_models.Test.objects.create(
                name=name,
                email=email,
                phone=phone,
                date_of_birth=date_of_birth,
                gender=gender
            )
        except Exception as e:
            print("Error",e)
            return Response({
            "error:  "+str(e)
        })
            
        print(instance.get_details())
        
        return Response({
            "instance created is : "+str(instance.obj_id)
        })
        
    
#update api 
class UpdateView(views.APIView):
    def post(self,request):
        data = request.data
        serializer_instance = core_serializers.UpdateCrudSerializer(
            data=request.data
        )
        if not serializer_instance.is_valid():
            print(
                "serializer_instance.errors {}".format(serializer_instance.errors)
            )
            return Response({
                "error":serializer_instance.errors
            })
            
        
        serializer_instance = core_serializers.TestCrudSerializer(
            data=request.data
        )
        if not serializer_instance.is_valid():
            print(
                "serializer_instance.errors {}".format(serializer_instance.errors)
            )
            return Response({
                "error":serializer_instance.errors
            })
            
        name = serializer_instance.validated_data.get("name")
        email = serializer_instance.validated_data.get("email")
        phone = serializer_instance.validated_data.get("phone")
        date_of_birth = serializer_instance.validated_data.get("date_of_birth")
        gender = serializer_instance.validated_data.get("gender")
        
        
        instance=core_models.Test.objects.filter(
            email=email,
        ).last()
        
        instance.name = name
        instance.phone = phone
        instance.date_of_birth = date_of_birth
        instance.gender = gender
        
        instance.save(update_fields=["name","phone","date_of_birth","gender"])
        
        instance.save()
        print(instance.get_details())
        
        return Response({
            "instance updated"
        })
        
        
 
#delete api 
class DeleteView(views.APIView):
    def post(self,request):
        data = request.data
        serializer_instance = core_serializers.UpdateCrudSerializer(
            data=request.data
        )
        if not serializer_instance.is_valid():
            print(
                "serializer_instance.errors {}".format(serializer_instance.errors)
            )
            return Response({
                "error":serializer_instance.errors
            })
            
        email = serializer_instance.validated_data.get("email")
        
        instance=core_models.Test.objects.filter(
            email=email,
        ).last()
        
       
        
        instance.delete()
        
        return Response({
            "instance deleted"
        })
        
        

#update api 
class GetCrudView(views.APIView):
    def post(self,request):
        data = request.data
        serializer_instance = core_serializers.UpdateCrudSerializer(
            data=request.data
        )
        if not serializer_instance.is_valid():
            print(
                "serializer_instance.errors {}".format(serializer_instance.errors)
            )
            return Response({
                "error":serializer_instance.errors
            })
            
            
      
        email = serializer_instance.validated_data.get("email")
        
        
        
        instance=core_models.Test.objects.filter(
            email=email,
        ).last()
        
        print(instance.get_details())
        data = instance.get_details()
        return Response({
            "data":data 
        })
        
        