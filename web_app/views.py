from django.shortcuts import render, HttpResponse

# Create your views here.
def home (reonest):
    return HttpResponse("Hello,this my project")

def about(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact")