from django.shortcuts import render

from bokeh.plotting import figure
from bokeh.embed import components

# Create your views here.
def login(request):
			return render(request, 'login.html')
			
def index(request):
			return render(request, 'index.html')

def index2(request):
			return render(request, 'index2.html')
		
def index3(request):
			return render(request, 'index3.html')

def tables(request):
			return render(request, 'tables.html')
			
def tables_dynamic(request):
			return render(request, 'tables_dynamic.html')

def form_upload(request):
			return render(request, 'form_upload.html')
		
def form_validation(request):
			return render(request, 'form_validation.html')
			
def form(request):
			return render(request, 'form.html')
			
def contacts(request):
			return render(request, 'contacts.html')

def chartjs(request):
			return render(request, 'chartjs.html')
		
def calendar(request):
			return render(request, 'calendar.html')