from django.conf.urls import url
from.import views

urlpatterns = [ 
			url(r'^$' , views.login, name='login'),
			url(r'index' , views.index, name='index'),
			url(r'index2' , views.index2, name='index2'),
			url(r'index3' , views.index3, name='index3'),
			url(r'tables' , views.tables, name='tables.html'),
			url(r'tables_dynamic' , views.tables_dynamic, name='tables_dynamic.html'),
			url(r'form' , views.form, name='form.html'),
			url(r'form_upload' , views.form_upload, name='form_upload.html'),
			url(r'form_validation' , views.form_validation, name='form_validation.html'),
			url(r'contacts' , views.contacts, name='contacts.html'),
			url(r'chartjs' , views.chartjs, name='chartjs.html'),
			url(r'calendar' , views.calendar, name='calendar.html'),
]
