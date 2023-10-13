from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("layanan-imigrasi/", views.layanan_imigrasi, name="layanan-imigrasi"),
    path("galeri/", views.galeri, name="galeri"),
    path("ppid/", views.ppid, name="ppid"),
    path("profile/", views.profile, name="profile"),
    path("biaya-keimigrasian/", views.biaya_keimigrasian, name="biaya-keimigrasian"),
    path("arsip-dan-dokumen/", views.arsip_dan_dokumen, name="arsip-dan-dokumen"),
    path("zona-integritas/", views.zona_integritas, name="zona-integritas"),
    path("timpora/", views.timpora, name="timpora"),
    path("berita/", views.berita, name="berita"),
    path("berita/<int:pk>", views.berita_detail, name="berita-detail"),
    path("dasbor-publik/", views.dasbor_publik, name="dasbor-publik"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]