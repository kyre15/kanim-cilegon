from django.contrib import admin
from django import forms

from main.models import MainMenu, SubMenu, Content, Menu, YoutubeVideo, Berita, BeritaImage, FotoGaleri, FileArsipDanDokumen, Kakanim, StrukturOrganisasi, VisiDanMisi, ListPerusahaanDanPenginapanWilayahKerja

# class MainMenuField(admin.ModelAdmin):
#     list_display = ('main_menu_name', 'create_at')
#     search_fields = ['main_menu_name']
# admin.site.register(MainMenu, MainMenuField)
#
# class MenuField(admin.ModelAdmin):
#     list_display = ('menu_name', 'create_at', 'main_menu')
#     search_fields = ['menu_name']
# admin.site.register(Menu, MenuField)

# class SubMenuField(admin.ModelAdmin):
#     list_display = ('submenu_name', 'create_at', 'permalink', 'menu')
#     search_fields = ['submenu_name']
# admin.site.register(SubMenu, SubMenuField)


class ContentForm(forms.ModelForm):
    pass

class ContentField(admin.ModelAdmin):
    list_display = ('content_name', 'create_at', 'content', 'content_menu')
    search_fields = ['content_name']
    form = ContentForm
admin.site.register(Content, ContentField)

class YoutubeVideoField(admin.ModelAdmin):
    list_display = ('video_title', 'url', 'youtube_category')
    search_fields = ['video_title', 'url']
admin.site.register(YoutubeVideo, YoutubeVideoField)

class BeritaImageField(admin.ModelAdmin):
    list_display = ('category_berita', 'berita_title', 'berita_descrition', 'create_at')
    search_fields = ['category_berita', 'berita_title']
admin.site.register(Berita, BeritaImageField)

class BeritaImageField(admin.ModelAdmin):
    list_display = ('berita', 'img_preview', 'image_added_at')
    search_fields = ['berita']
admin.site.register(BeritaImage, BeritaImageField)

class FotoGaleriField(admin.ModelAdmin):
    list_display = ('galeri_image_file', 'descripion_image', 'image_added_at', 'img_preview', 'foto_category')
    search_fields = ['descripion_image']
admin.site.register(FotoGaleri, FotoGaleriField)

class FileArsipDanDockumentField(admin.ModelAdmin):
    list_display = ('file_name', 'file', 'category', 'file_added_at')
    search_fields = ['file_name', 'category']
admin.site.register(FileArsipDanDokumen, FileArsipDanDockumentField)

class KanimField(admin.ModelAdmin):
    list_display = ('name', 'masa_jabatan', 'foto')
    search_fields = ['name', 'masa_jabatan']
admin.site.register(Kakanim, KanimField)

class StrukturOrganisasiField(admin.ModelAdmin):
    list_display = ('name', 'jabatan', 'TMT')
    search_fields = ['name', 'jabatan']
admin.site.register(StrukturOrganisasi, StrukturOrganisasiField)

class VisiMisiField(admin.ModelAdmin):
    list_display = ('visi', 'misi', 'moto_1', 'moto_2', 'moto_3', 'tata_nilai_profesional', 'tata_nilai_akuntabel',
                    'tata_nilai_sinergi', 'tata_nilai_transparan', 'tata_nilai_inovarif')
admin.site.register(VisiDanMisi, VisiMisiField)

class ListPerusahaanDanPenginapanWilayahKerjaField(admin.ModelAdmin):
    list_display = ('wilayah_kerja', 'list_of_perusahaan_penginapan', 'create_at')
admin.site.register(ListPerusahaanDanPenginapanWilayahKerja, ListPerusahaanDanPenginapanWilayahKerjaField)