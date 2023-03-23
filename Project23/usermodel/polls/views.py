from django.shortcuts import render
from models import User
from rest_framework.views import APIView
from rest_framework.response import Response
 


# Create your views here.

class UserApiView(APIView):
    def get(self,request):
        allUsers=User.objects.all().values()
        return Response({"Message":"List of Users","User List":allUsers})
    
    def post(self,request):

        User.objects.create(id=request.data["id"],
                            phone=request.data["phone"],
                            name=request.data["name"],
                            email=request.data["email"]
                            )
        
        allUsers=User.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New user added","User":allUsers})
    

