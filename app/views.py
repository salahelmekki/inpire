from os import name
from django.shortcuts import render
from django.urls import reverse
import logging
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, request
from django.forms.models import model_to_dict
from .models import Etudiant
import json
from .forms import EtudiantForm
import csv



def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "index.html", data)
    # if not GET, then proceed
    try:
		

		
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            print('nest pas un fichier csv')
            return HttpResponseRedirect(reverse("upload_csv"))    

        file_data = csv_file.read().decode('utf-8')
        
        
        # print(file_data)
        lines = file_data.split("\n")
        print(lines[0])
        for line in range(1,len(lines)):						
            fields = lines[line].split(",")
            data_dict = {}
            data_dict["prenom"] = fields[0]
            data_dict["nom"] = fields[1]
            data_dict["age"] = fields[2]
            data_dict["moyenne"] = fields[3]
            print(data_dict)
            
            try: 
                Etudiant.objects.create(prenom=data_dict["prenom"],nom=data_dict["nom"] ,
                                    age=data_dict["age"],moyenne=data_dict["moyenne"] )
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))					
                pass
 
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		
    return HttpResponseRedirect(reverse("display"))


def display_csv(request):
    # data = {}
    # if "GET" == request.method:
    #     return render(request, "dispaly.html", data)
    data_json =[]
    datas = Etudiant.objects.order_by("-moyenne")
    
    return render(request,"dispaly.html",{"data":datas})