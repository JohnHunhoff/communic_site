from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import IndexView, SingleView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>', SingleView.as_view(), name='single_page')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


