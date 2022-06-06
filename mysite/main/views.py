from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from .forms import FormTest

# Create your views here.
async def index(response):
    return HttpResponse("<h1>index</h1>")

async def home(request):
    return TemplateResponse(request, "home.html",{"name":"10000"})

async def form_test(request):
    if request.method == "POST":
        form = FormTest(request.POST)
        #print(form)
        if form.is_valid():
            name = form.cleaned_data["name"]
            number = form.cleaned_data["number"]
            check = form.cleaned_data["check"]

            print(name,number,check)
            return TemplateResponse(request, "form-check.html",
            {"name":name,"number":number, "check":check}
            )
        else:
            return HttpResponse("<h1>info not valid</h1>")
    else:
        form = FormTest()
        return TemplateResponse(request, "form-test.html",{"form":form})

async def cook(request):

    value = request.COOKIES.get("cook")

    if value:
        response = HttpResponse("get cookie")
        return response
    else:
        response = HttpResponse("set cookie")
        response.set_cookie("cook","cookie seted")
        return response

async def test_static(request):
    return TemplateResponse(request, "test-static.html",{})