from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("staff/", views.staff, name="staff"),
    path("projects/", views.projects, name="projects"),
    path("contact-us/", views.contact, name="contact-us"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
