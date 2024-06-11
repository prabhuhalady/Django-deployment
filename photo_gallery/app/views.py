from django.shortcuts import render, redirect
from django.views import View
from .models import Photo, Like
from .forms import PhotoForm

class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html')

class PhotoUploadView(View):
    def get(self, request):
        form = PhotoForm()
        return render(request, 'app/upload_photo.html', {'form': form})

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_photos')
        return render(request, 'app/upload_photo.html', {'form': form})

class PhotoListView(View):
    def get(self, request):
        photos = Photo.objects.all()
        for photo in photos:
            photo.liked_by_user = Like.objects.filter(photo=photo, session_key=request.session.session_key).exists()
        return render(request, 'app/view_photos.html', {'photos': photos})

class ToggleLikeView(View):
    def post(self, request, photo_id):
        photo = Photo.objects.get(id=photo_id)
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        like, created = Like.objects.get_or_create(photo=photo, session_key=session_key)
        if not created:
            like.delete()
            photo.likes -= 1
        else:
            photo.likes += 1
        photo.save()
        return redirect('view_photos')
