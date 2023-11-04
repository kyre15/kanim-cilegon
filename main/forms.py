from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from .models import Content, FileArsipDanDokumen, FotoGaleri, YoutubeVideo, Berita, BeritaImage, IndexSurvey, IPKandIKM
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateTimeField

class AddLayananImigrasiForm(forms.ModelForm):
    content_name = forms.CharField()
    tentang_layanan_dan_persyaratan = RichTextUploadingField(null=True, blank=True)
    alur_proses_dan_prosedur= RichTextUploadingField(null=True, blank=True)
    biaya = RichTextUploadingField(null=True, blank=True)
    
    class Meta:
        model = Content
        exclude = ("user","content","category_content")
        
class AddContentForm(forms.ModelForm):
    content_name = forms.CharField()
    content = RichTextUploadingField(null=True, blank=True)
    
    class Meta:
        model = Content
        exclude = ("user","tentang_layanan_dan_persyaratan","category_content", "alur_proses_dan_prosedur", "biaya")
       
class AddFileArsipdanDokumen(forms.ModelForm):
    class Meta:
        model = FileArsipDanDokumen
        exclude = ("file_added_at",)
        
class AddFotoGaleri(forms.ModelForm):
    class Meta:
        model = FotoGaleri
        exclude = ("image_added_at",)
        
class AddVideo(forms.ModelForm):
    class Meta:
        model = YoutubeVideo
        exclude = ("create_at",)
        
class AddBerita(forms.ModelForm):
    class Meta:
        model = Berita
        exclude = ("create_at",)
        
class AddBeritaImage(forms.ModelForm):
    class Meta:
        model = BeritaImage
        exclude = ("image_added_at",)
        
class AddIndexSurvey(forms.ModelForm):
    class Meta:
        model = IndexSurvey
        exclude = ("id",)
        
class IPKdanIPMForm(forms.ModelForm):
    class Meta:
        model = IPKandIKM
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
            'informasi': forms.HiddenInput()
            }
        exclude = ("id",)