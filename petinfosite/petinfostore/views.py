import os
from xml.dom import minidom

from django.shortcuts import render
from petinfostore.models import Person, Pet


def petview(request, owner_id = -1):
    people = Person.objects.all()
    if (owner_id != -1):
        owner = Person.objects.get(id=owner_id)
        pets = Pet.objects.filter(owner=owner_id)
        return render(request, 'petinfo.html', {'people': people, 'pets': pets, 'owner': owner})
    return render(request, 'petinfo.html', {'people': people})

def parse(request):
    xmldoc = minidom.parse(os.path.join(os.getcwd(), 'petinfostore/synchro.xml'))
    readbitlist = xmldoc.getElementsByTagName('readbit')
    elements = []
    for s in readbitlist :
        x = s.attributes['score'].value
        elements.append(x)
    return render(request, 'parse.html', {'elements': elements})