from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

CATEGORY_BERITA = (
    ("KANTOR_IMIGRASI_CILEGON", "KANTOR_IMIGRASI_CILEGON"),
    ("KEMENKUMHAM_REPUBLIK_INDONESIA", "KEMENKUMHAM_REPUBLIK_INDONESIA"),
    ("KEMENKUMHAM_KANWIL_BANTEN", "KEMENKUMHAM_KANWIL_BANTEN"),
)

CATEGORY_ARSIP_DOKUMEN = {
    ("DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN", "DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN"),
    ("LAPORAN_AKUNTABILITAS_KINERJA", "LAPORAN_AKUNTABILITAS_KINERJA"),
    ("TIMPORA", "TIMPORA"),
    ("INFORMASI_BERKALA", "INFORMASI_BERKALA"),
}

class FileArsipDanDokumen(models.Model):
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_ARSIP_DOKUMEN
    )
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    file_added_at = models.DateTimeField(auto_now_add=True)

class Berita(models.Model):
    category_berita = models.CharField(
        max_length=30,
        choices=CATEGORY_BERITA
    )
    berita_title = models.CharField(max_length=100)
    berita_descrition = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.berita_title}")

class BeritaImage(models.Model):
    berita_image_file = models.ImageField(upload_to='berita/')
    berita = models.ForeignKey(Berita, on_delete=models.CASCADE, related_name='joni')
    image_added_at = models.DateTimeField(auto_now_add=True)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.berita_image_file.url}" width = "300"/>')
    def __str__(self):
        return (f"{self.berita}")

YOUTUBE_CATEGORY = (
    ('ZONA_INTEGRITAS', 'ZONA_INTEGRITAS'),
    ('JINGLE', 'JINGLE'),
    ('STANDAR', 'STANDAR')
)

class YoutubeVideo(models.Model):
    video_title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    youtube_category = models.CharField(max_length=50, choices=YOUTUBE_CATEGORY)

    def __str__(self):
        return (f"{self.video_title}")

class MainMenu(models.Model):
    main_menu_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.main_menu_name}")

class Menu(models.Model):
    menu_name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.menu_name}")

class SubMenu(models.Model):
    submenu_name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    permalink = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.submenu_name}")

CATEGORY_CONTENT = (
    ('LAYANAN_IMIGRASI', 'LAYANAN_IMIGRASI'),
    ('STANDAR', 'STANDAR')
)

class Content(models.Model):
    content_menu = models.OneToOneField(
        SubMenu,
        on_delete=models.CASCADE,
        primary_key=True
    )
    content_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    category_content = models.CharField(max_length=50, choices=CATEGORY_CONTENT, default='STANDAR')
    content = RichTextUploadingField(null=True, blank=True)
    tentang_layanan_dan_persyaratan = RichTextUploadingField(null=True, blank=True)
    alur_proses_dan_prosedur = RichTextUploadingField(null=True, blank=True)
    biaya = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return (f"{self.content_name}")

FOTO_CATEGORY = (
    ('DOKUMENTASI', 'DOKUMENTASI'),
    ('STANDAR', 'STANDAR')
)

class FotoGaleri(models.Model):
    galeri_image_file = models.ImageField(upload_to='foto/')
    descripion_image = models.CharField(max_length=200)
    image_added_at = models.DateTimeField(auto_now_add=True)
    foto_category = models.CharField(max_length=200, choices=FOTO_CATEGORY)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.galeri_image_file.url}" width = "300"/>')

class Kakanim(models.Model):
    name = models.CharField(max_length=50)
    masa_jabatan = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='kakanim/')

JABATAN = (
    ('KEPALA_KANTOR', 'KEPALA_KANTOR'),
    ('KASUBAG_TATA_USAHA', 'KASUBAG_TATA_USAHA'),
    ('KASI_LALU_LINTAS_DAN_IZIN_TINGGAL_KEIMIGRASIAN', 'KASI_LALU_LINTAS_DAN_IZIN_TINGGAL_KEIMIGRASIAN'),
    ('KASI_TEKNOLOGI_DAN_INFORMASI_KEIMIGRASIAN', 'KASI_TEKNOLOGI_DAN_INFORMASI_KEIMIGRASIAN'),
    ('KASI_INTELEJEN_DAN_PENINDAKAN_KEIMIGRASIAN', 'KASI_INTELEJEN_DAN_PENINDAKAN_KEIMIGRASIAN'),
    ('KAUR_KEPEGAWAIAN', 'KAUR_KEPEGAWAIAN'),
    ('KASUBSI_LALU_LINTAS_KEIMIGRASIAN', 'KASUBI_LALU_LINTAS_KEIMIGRASIAN'),
    ('KASUBSI_IZIN_TINGGAL_KEIMIGRASIAN', 'KASUBSI_IZIN_TINGGAL_KEIMIGRASIAN'),
    ('KASUBSI_TEKNOLOGI_INFORMASI_KEIMIGRASIAN', 'KASUBSI_TEKNOLOGI_INFORMASI_KEIMIGRASIAN'),
    ('KASUBSI_INFORMASI_DAN_KOMUNIKASI_KEIMIGRASIAN', 'KASUBSI_INFORMASI_DAN_KOMUNIKASI_KEIMIGRASIAN'),
    ('KASUBSI_INTELIJEN_KEIMIGRASIAN', 'KASUBSI_INTELIJEN_KEIMIGRASIAN'),
    ('KASUBSI_PENINDAKAN_KEIMIGRASIAN', 'KASUBSI_PENINDAKAN_KEIMIGRASIAN'),
)

class StrukturOrganisasi(models.Model):
    name = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=100, choices=JABATAN)
    TMT = models.DateTimeField()
    foto = models.ImageField(upload_to='photo_pejabat/', default='1')

class VisiDanMisi(models.Model):
    visi = models.CharField(max_length=200)
    misi = RichTextUploadingField()
    moto_1 = models.CharField(max_length=50)
    moto_2 = models.CharField(max_length=50)
    moto_3 = models.CharField(max_length=50)
    tata_nilai_profesional = models.CharField(max_length=300)
    tata_nilai_akuntabel = models.CharField(max_length=300)
    tata_nilai_sinergi = models.CharField(max_length=300)
    tata_nilai_transparan = models.CharField(max_length=300)
    tata_nilai_inovarif = models.CharField(max_length=300)

WILAYAH_KERJA = (
    ('BOJONEGARA', 'BOJONEGARA'),
    ('CIBEBER', 'CIBEBER'),
    ('CILEGON', 'CILEGON'),
    ('CITANGKIL', 'CITANGKIL'),
    ('CIWANDAN', 'CIWANDAN'),
    ('GEROGOL', 'GEROGOL'),
    ('JOMBANG', 'JOMBANG'),
    ('PULOAMPEL', 'PULOAMPEL'),
    ('PULOMERAK', 'PULOMERAK'),
    ('PURWAKARTA', 'PURWAKARTA'),
)

class ListPerusahaanDanPenginapanWilayahKerja(models.Model):
    wilayah_kerja = models.CharField(max_length=20, choices=WILAYAH_KERJA)
    list_of_perusahaan_penginapan = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now_add=True)

class LaporanPelayananWNI(models.Model):
    date = models.DateTimeField()
    total_paspor_baru = models.IntegerField()
    total_pergantian_paspor = models.IntegerField()
    total_pergantian_paspor_hilang_rusak = models.IntegerField()
    total_penyerahan_paspor = models.IntegerField()

class LaporanPelayananWNA(models.Model):
    date = models.DateTimeField()
    total_ijin_tinggal_kunjungan = models.IntegerField()
    total_izin_tinggal_terbatas = models.IntegerField()

class IndexPersepsiKorupsi(models.Model):
    date = models.DateTimeField()
    total_sangat_baik = models.IntegerField()
    total_baik = models.IntegerField()
    total_kurang_baik = models.IntegerField()
    total_tidak_baik = models.IntegerField()
    p = models.CharField(max_length=5)

class IndexKepuasanMasyarakat(models.Model):
    date = models.DateTimeField()
    total_sangat_baik = models.IntegerField()
    total_baik = models.IntegerField()
    total_kurang_baik = models.IntegerField()
    total_tidak_baik = models.IntegerField()
    p = models.CharField(max_length=5)
    
class IndexSurvey(models.Model):
    total_sangat_baik = models.IntegerField(default=1)
    total_baik = models.IntegerField(default=1)
    total_kurang_baik = models.IntegerField(default=1)
    total_tidak_baik = models.IntegerField(default=1)

class IPKandIKM(models.Model):
    date = models.DateTimeField()
    informasi = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='informasi')
    persyaratan = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='persyaratan')
    prosedur_atau_alur = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='prosedur_atau_alur')
    waktu_penyelesaian = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='waktu_penyelesaian')
    tarif_biaya = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='tarif_biaya')
    sarana_prasarana = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='sarana_prasarana')
    respon = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='respon')
    konsultasi_dan_pengaduan = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='konsultasi_dan_pengaduan')
    diskriminasi = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='diskriminasi')
    kecurangan = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='kecurangan')
    gratifikasi = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='gratifikasi')
    pungli = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='pungli')
    calo = models.OneToOneField(IndexSurvey,on_delete=models.CASCADE, related_name='calo')
    
class IPKandIKMSurvey(models.Model):
    date = models.DateTimeField()
    index_survey = models.ForeignKey(
        'IndexSurvey',
        on_delete=models.CASCADE,
    )