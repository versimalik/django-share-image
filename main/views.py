from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Image
from django.contrib import messages

# Create your views here.
def index(request):
    all_images = Image.objects.order_by('-created_at')
    context = {
        'images' : all_images,
    }
    return render(request, 'main/index.html', context)

def create(request):
    img = request.FILES['image']
    cap = request.POST['caption']

    if len(cap) < 5:
        error_msg = "Your caption is too short!!!"
        messages.error(request, error_msg)
        return HttpResponseRedirect(reverse('index'))

    new_image = Image.objects.create(image = img, caption = cap)
    messages.success(request, "Success to share image!!")
    return HttpResponseRedirect(reverse('index'))

