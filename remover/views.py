from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .u2net.model import U2NET
from  .u2net.worker import Process

import os
from django.core.files.storage import FileSystemStorage
import torch

p = Process()

def index(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        p.process_single_image('media/'+filename,'media/remover_'+filename)
        processed_image_url = '/media/remover_' + filename
        return render(request, 'remover/result.html', {'processed_image_url': processed_image_url,
                                                                'transaparent':'media/transparent.jpg',
                                                                'original_image':'media/'+filename})
    return render(request, 'remover/index.html')

