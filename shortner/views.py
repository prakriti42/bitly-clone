from django.shortcuts import render , redirect

#importing uuid
import uuid 

from django.http import HttpResponse
#importing models

from .models import Url 

# Create your views here.

#Uses function based views 

#index view for rendering the homepage
def index(request):
    return render(request, 'index.html')

#generate view for generating the urlid on form submission 
def generate(request):
    if request.method == 'POST':    #if the form is submitted
        url = request.POST['link'] #get the url from the form
        urlid = str(uuid.uuid4())[:5]  #generate a random urlid and store it as an instance 
        result_url = Url(inputUrl=url, urlid=urlid) #create a new url object
        result_url.save() #save the url object to the database
        return HttpResponse(urlid) #return the urlid to the form and print it on the page

#lead view for redirecting the url to the original url
def lead(request, key):
    url_details = Url.objects.get(urlid=key) #get the url object from the database
    return redirect("https://"+ url_details.inputUrl) #redirect to the original url