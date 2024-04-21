from django.urls import path
from .views import HomeView, MusicView, video, audio, obtener_informacion

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', MusicView.as_view(), name='music'),
    path('obtener_informacion/', obtener_informacion, name='obtener_informacion'),
    path('video/', video, name='video'),
    path('audio/', audio, name='audio'),
]