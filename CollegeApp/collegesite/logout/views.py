import django
from django.shortcuts import render

# Create your views here.
def logoutfunction(request):
     return render(request,'login_page.html')