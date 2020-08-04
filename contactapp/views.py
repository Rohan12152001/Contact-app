from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from . import models
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# from .forms import PersonForm 
from . import forms

def homepage(request):
    return render(request,'contactapp/homepage.html')


def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'contactapp/contact_list.html', {'persons': persons})

def contact_new(request):
    if request.method == 'POST':
        form = forms.PersonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.PersonForm()
    return render(request, 'contactapp/contact_edit.html', {'form': form})

class contact_detail(DetailView):
    context_object_name = 'contactdetails'
    model = models.Person
    template_name = 'contactapp/contact_detail.html'
    
def contact_edit(request, pk):
    person = get_object_or_404(models.Person, pk=pk)
    if request.method == 'POST':
        form = forms.PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            # return redirect('/person/' + str(person.pk))
            return redirect('/')        ### You have to change this !!!! ##### Take them to contact list !!
    else:
        form = forms.PersonForm(instance=person)
    return render(request, 'contactapp/contact_edit.html', {'form': form})

def contact_delete(request, pk):
    person = get_object_or_404(models.Person, pk=pk)
    person.delete()
    return redirect('/')