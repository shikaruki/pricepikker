from django.shortcuts import render,HttpResponse
from .models import ProductDetails
from bs4 import BeautifulSoup
import requests
import re
from django.contrib import  messages
# Create your views here.
def index(request):
    return render(request,'home/home.html')

    #return HttpResponse("This is home page")


def contact(request):
    return render(request,'home/contactInfo.html')

    #return HttpResponse("this is contact page")

def search(request):
    if request.method == "POST":
        q=request.POST.get('search')
        url = "https://flipkart.com/search?q="
        q = q.replace(" ", "+")
        resp = requests.get(url + q)
        if resp.status_code !=200:
            print("Sorry can't fetch data for this product right now")
        flipSoup=BeautifulSoup(resp.text,'html.parser')
        productObj=[]

        
        val=flipSoup.find_all('a',attrs={'class':'_1fQZEK'})
        if len(val) >0:
            for product in val:
                obj=ProductDetails()
                obj.price=product.find('div',attrs={'class':'_30jeq3 _1_WHN1'}).text
                obj.desc=product.find('div',attrs={'class':'_4rR01T'}).text
                obj.img=product.find('img',attrs={'class':'_396cs4 _3exPp9'}).get('src')
                obj.link="https://www.flipkart.com"+product.get('href')
                productObj.append(obj)
        else:
            val=flipSoup.find_all('div',attrs={'class':'_4ddWXP'})
            for product in val:
                obj=ProductDetails()
                #print(len(product.contents))
                obj.price=product.find('div',attrs={'class':'_30jeq3'}).text
                obj.desc=product.find('a',attrs={'class':'s1Q9rs'}).get('title')
                obj.img=product.find('img',attrs={'class':'_396cs4 _3exPp9'}).get('src')
                obj.link="https://www.flipkart.com"+product.find('a',attrs={'class':'s1Q9rs'}).get('href')
                productObj.append(obj)

        print(len(productObj))
            #print(product.contents[1].contents[1].contents[0].contents[0].contents[0].get('class'))
        return render(request,'home/searchProduct.html',{'lists':productObj})
        #messages.warning(request,name)
    return render(request,'home/searchProduct.html')



def feedback(request):
    #return render(request,'home/searchProduct.html')
    return HttpResponse("This is feedback section")


def login (request):
    return HttpResponse("This is login section")

def result(request):
    return HttpResponse("kjghil")