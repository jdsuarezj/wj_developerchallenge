from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import ScanForm
import json
import sys

# Library for aylien textapi
from aylienapiclient import textapi
# Credentials API
client = textapi.Client('ID', 'KEY') #CHANGE THIS with your Aylien's credentials

# Return the Scan view 
@login_required(login_url="/login/")
def scan_view(request):
    return render(request, "index.html")

# Load the others pages in the template with the path pages/
@login_required(login_url="/login/")
def pages(request):
    context = {}
    load_template = request.path.split('/')[-1]
    template = loader.get_template('pages/' + load_template)
    return HttpResponse(template.render(context, request))

# IndexView 
# Render the index with the responses from the API
@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        form = ScanForm(request.POST)
        if form.is_valid():
            # URL from the TextArea in the index view
            urlInput = form.cleaned_data.get('urlInput')      
            # Params for request the API    
            paramInput = {'url': urlInput}
            # Sentiment endpoint
            sentiment = client.Sentiment(paramInput)     
            # Entities endpoint       
            entities = client.Entities(paramInput)
            # Concepts endpoint
            concepts = client.Concepts(paramInput)
            conceptsResult = [ v for v in concepts['concepts'].values() ]
            # Summarize endpoint
            summarize = client.Summarize(paramInput)

            # Return the data to the view
            return render(
                request, 'pages/scan.html',
                {
                    'form': form,
                    'text': sentiment['text'],
                    'polarity': sentiment['polarity'],
                    'subjectivity': sentiment['subjectivity'],
                    'polarity_confidence': (sentiment['polarity_confidence'])*100,
                    'subjectivity_confidence': (sentiment['subjectivity_confidence'])*100,                    
                    'entities': entities['entities'],
                    'concepts': conceptsResult,
                    'summarize': summarize['sentences']
                }
            )
    else:
        form = ScanForm()
    return render(request, 'index.html', {'form': form})
