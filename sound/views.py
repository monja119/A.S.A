import json
import os.path
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from sound.form import FF
from sound.analyse import Analyse
from sound.models import UploadField
import numpy as np

def home(request):
    if request.method == 'POST':
        form = FF(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            type= file.content_type

            #analyse de type
            if 'audio' not in type:
                ErrorMsg = 'Type not supported'
            else :
                form.save()
                db = len(UploadField.objects.all())
                file = ''

                for k in UploadField.objects.all():
                    file = k.file
                file_path = 'sound/media/son/{}'.format(file);
                file_name = str(file)
                analyse = Analyse(file_path,file_name)
                notes = analyse.notes
                nb_notes = len(notes)-1


                directory = Path(__file__).resolve()

                
                notes = json.dumps(notes)

            return render(request, 'sound/analyse.html', locals())

    else:
        form = FF()
        context = {
            'form':form,
        }
    return render(request, 'sound/acceuil.html', locals())

def about(request):
    text = """<h1>about !</h1>
    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def contact(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Conact !</h1>
    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)
