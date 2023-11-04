from .models import Content, FileArsipDanDokumen, FotoGaleri, YoutubeVideo, Berita, BeritaImage, IPKandIKM, IndexSurvey
from .forms import AddLayananImigrasiForm, AddContentForm, AddFileArsipdanDokumen, AddFotoGaleri, AddVideo, AddBerita, AddBeritaImage, AddIndexSurvey, IPKdanIPMForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max
from django.db.models.functions import TruncMonth

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, 
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return render(request, 'dashboard/index.html', {})

def logout_dashboard(request):
    logout(request)
    return redirect('dashboard')

# layanan imigrasi

def paspor_baru(request):
    return render(request, 'dashboard/layanan_imigrasi/paspor-baru.html', {
        'content_paspor_baru': get_content('Paspor Baru')
    })

def pergantian_paspor(request):
    return render(request, 'dashboard/layanan_imigrasi/pergantian-paspor.html', {
        'content_pergantian_paspor': get_content('Pergantian Paspor')
    })

def pergantian_paspor_hilang_atau_rusak(request):
    return render(request, 'dashboard/layanan_imigrasi/pergantian-paspor-hilang-atau-rusak.html', {
        'content_pergantian_paspor_hilang_atau_rusak': get_content('Pergantian Paspor Hilang/Rusak')
    })

def perpanjang_visa_kunjungan_saat_kedatangan(request):
    return render(request, 'dashboard/layanan_imigrasi/perpanjang-visa-kunjungan-saat-kedatangan.html', {
        'perpanjang_visa_kunjungan_saat_kedatangan': get_content('Perpanjang Visa Kunjungan Saat Kedatangan')
    })

def izin_tinggal_kunjungan(request):
    return render(request, 'dashboard/layanan_imigrasi/izin-tinggal-kunjungan.html', {
        'izin_tinggal_kunjungan': get_content('Izin Tinggal Kunjungan')
    })

def izin_tinggal_terbatas(request):
    return render(request, 'dashboard/layanan_imigrasi/izin-tinggal-terbatas.html', {
        'izin_tinggal_terbatas': get_content('Izin Tinggal Terbatas')
    })

def izin_masuk_kembali(request):
    return render(request, 'dashboard/layanan_imigrasi/izin-masuk-kembali.html', {
        'izin_masuk_kembali': get_content('Izin Masuk Kembali')
    })

def izin_tinggal_tetap(request):
    return render(request, 'dashboard/layanan_imigrasi/izin-tinggal-tetap.html', {
        'izin_tinggal_tetap': get_content('Izin Tinggal Tetap')
    })

def alih_status_izin_tinggal(request):
    return render(request, 'dashboard/layanan_imigrasi/alih-status-izin-tinggal.html', {
        'alih_status_izin_tinggal': get_content('Alih Status Izin Tinggal')
    })

def perubahan_alamat(request):
    return render(request, 'dashboard/layanan_imigrasi/perubahan-alamat.html', {
        'perubahan_alamat': get_content('Perubahan Alamat')
    })

def pendaftaran_anak(request):
    return render(request, 'dashboard/layanan_imigrasi/pendaftaran-anak.html', {
        'pendaftaran_anak': get_content('Pendaftaran Anak Berkewarganegaraan Ganda dan Fasilitas Keimigrasian (Ganda Terbatas)')
    })
    
# biaya keimigrasian
    
def dokumen_perjalanan_republik_indonesia(request):
    return render(request, 'dashboard/biaya_keimigrasian/dokumen-perjalanan-republik-indonesia.html', {
        'content_dokumen_perjalanan_republik_indonesia': get_content('Dokumen Perjalanan Republik Indonesia')
    })

def visa_kunjungan(request):
    return render(request, 'dashboard/biaya_keimigrasian/visa-kunjungan.html', {
        'visa_kunjungan': get_content('Visa Kunjungan')
    })

def visa_tinggal_terbatas(request):
    return render(request, 'dashboard/biaya_keimigrasian/visa-tinggal-terbatas.html', {
        'visa_tinggal_terbatas': get_content('Visa Tinggal Terbatas')
    })

def izin_kunjungan(request):
    return render(request, 'dashboard/biaya_keimigrasian/izin-kunjungan.html', {
        'izin_kunjungan': get_content('Izin Kunjungan')
    })

def izin_tinggal_tetap_keimigrasian(request):
    return render(request, 'dashboard/biaya_keimigrasian/izin-tinggal-tetap-keimigrasian.html', {
        'izin_tinggal_tetap_keimigrasian': get_content('Izin Tinggal Tetap')
    })

def izin_masuk_kembali_keimigrasian(request):
    return render(request, 'dashboard/biaya_keimigrasian/izin-masuk-kembali-keimigrasian.html', {
        'izin_masuk_kembali_keimigrasian': get_content('Izin Masuk Kembali (Re-Entry Permit)')
    })
    
def izin_tinggal_terbatas_keimigrasian(request):
    return render(request, 'dashboard/biaya_keimigrasian/izin-tinggal-terbatas-keimigrasian.html', {
        'izin_tinggal_terbatas_keimigrasian': get_content('Izin Tinggal Terbatas')
    })

def biaya_beban(request):
    return render(request, 'dashboard/biaya_keimigrasian/biaya-beban.html', {
        'biaya_beban': get_content('Biaya Beban')
    })

def smart_card(request):
    return render(request, 'dashboard/biaya_keimigrasian/smart-card.html', {
        'smart_card': get_content('Smart Card')
    })

def kartu_perjalanan_bisnis(request):
    return render(request, 'dashboard/biaya_keimigrasian/kartu-perjalanan-bisnis.html', {
        'kartu_perjalanan_bisnis': get_content('Kartu Perjalanan Pebisnis Asia Pacific Economic Cooperation (KPP APEC)/APEC Business Travel Card (ABTC)')
    })

def fasilitas_keimigrasian(request):
    return render(request, 'dashboard/biaya_keimigrasian/fasilitasi-keimigrasian.html', {
        'fasilitas_keimigrasian': get_content('Fasilitas Keimigrasian (Afidavit) Bagi Anak Berkewarganegaraan Ganda')
    })

def surat_keterangan_keimigrasian(request):
    return render(request, 'dashboard/biaya_keimigrasian/surat-keterangan-keimigrasian.html', {
        'surat_keterangan_keimigrasian': get_content('Surat Keterangan Keimigrasian')
    })
    
# zona integritas

def pengertian(request):
    return render(request, 'dashboard/zona_integritas/pengertian.html', {
        'pengertian': get_content('Pengertian')
    })

def area_perubahan(request):
    return render(request, 'dashboard/zona_integritas/area-perubahan.html', {
        'area_perubahan': get_content('6 Area Perubahan')
    })

def dokumentasi_kegiatan_pzi(request):
    return render(request, 'dashboard/zona_integritas/dokumentasi-kegiatan-pzi.html', {
        'dokumentasi_kegiatan_pzi': get_content('Dokumentasi Kegiatan PZI')
    })
    
# ppid
      
def dasar_hukum_ppid(request):
    return render(request, 'dashboard/ppid/dasar-hukum-ppid.html', {
        'dasar_hukum_ppid': get_content('Dasar Hukum PPID')
    })

def sk_penetapan_ppid(request):
    return render(request, 'dashboard/ppid/sk-penetapan-ppid.html', {
        'sk_penetapan_ppid': get_content('SK Penetapan PPID')
    })

def struktur_ppid(request):
    return render(request, 'dashboard/ppid/struktur-ppid.html', {
        'struktur_ppid': get_content('Struktur PPID')
    })

def tugas_dan_fungsi_ppid(request):
    return render(request, 'dashboard/ppid/tugas-dan-fungsi-ppid.html', {
        'tugas_dan_fungsi_ppid': get_content('Tugas dan Fungsi PPID')
    })

def standar_pelayanan_informasi(request):
    return render(request, 'dashboard/ppid/standar-pelayanan-informasi.html', {
        'standar_pelayanan_informasi': get_content('Standar Pelayanan Informasi')
    })

def kegiatan_tata_kelola_informasi_publik(request):
    return render(request, 'dashboard/ppid/kegiatan-tata-kelola-informasi-publik.html', {
        'kegiatan_tata_kelola_informasi_publik': get_content('Kegiatan Tata kelola Informasi Publik')
    })

def sk_informasi_yang_dikecualikan(request):
    return render(request, 'dashboard/ppid/sk-informasi-yang-dikecualikan.html', {
        'sk_informasi_yang_dikecualikan': get_content('SK Informasi yang Dikecualikan')
    })
    
def daftar_informasi_publik(request):
    return render(request, 'dashboard/ppid/daftar-informasi-publik.html', {
        'daftar_informasi_publik': get_content('Daftar Informasi Publik')
    })

def informasi_berkala(request):
    return render(request, 'dashboard/ppid/informasi-berkala.html', {
        'informasi_berkala': get_content('Informasi Berkala')
    })

def informasi_setiap_saat(request):
    return render(request, 'dashboard/ppid/informasi-setiap-saat.html', {
        'informasi_setiap_saat': get_content('Informasi Setiap Saat')
    })

def informasi_serta_merta(request):
    return render(request, 'dashboard/ppid/informasi-serta-merta.html', {
        'informasi_serta_merta': get_content('Informasi Serta Merta')
    })

def informasi_dikecualikan(request):
    return render(request, 'dashboard/ppid/informasi-dikecualikan.html', {
        'informasi_dikecualikan': get_content('Informasi Dikecualikan')
    })
    
def profile_ppid(request):
    return render(request, 'dashboard/ppid/profile-ppid.html', {
        'profile_ppid': get_content('Profile PPID')
    })

def form_permintaan_informasi_dan_pernyataan_kebenaran(request):
    return render(request, 'dashboard/ppid/form-permintaan-informasi-dan-pernyataan-kebenaran.html', {
        'form_permintaan_informasi_dan_pernyataan_kebenaran': get_content('Form Permintaan Informasi & Pernyataan Kebenaran')
    })
    
# profile

def sejarah_imigrasi(request):
    return render(request, 'dashboard/profile/sejarah-imigrasi.html', {
        'sejarah_imigrasi': get_content('Sejarah Imigrasi')
    })
    
def sejarah_kantor(request):
    return render(request, 'dashboard/profile/sejarah-kantor.html', {
        'sejarah_kantor': get_content('Sejarah Kantor')
    })

def tugas_dan_fungsi_profile(request):
    return render(request, 'dashboard/profile/tugas-dan-fungsi-profile.html', {
        'tugas_dan_fungsi_profile': get_content('Tugas dan Fungsi')
    })
    
def add_layanan_imigrasi(request):
    form = AddLayananImigrasiForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_layanan_Imigrasi = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/layanan_imigrasi/add_layanan_imigrasi.html', {'form':form})
    else:
        return redirect('dashboard')
    
def update_layanan_imigrasi(request, pk):
    if request.user.is_authenticated:
        current_layanan_imigrasi = Content.objects.get(content_menu_id=pk)
        form = AddLayananImigrasiForm(request.POST or None, instance=current_layanan_imigrasi)
        if form.is_valid():
                add_layanan_Imigrasi = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/layanan_imigrasi/update-layanan-imigrasi.html', {
            'form':form,
            'content_paspor_baru': get_content('Paspor Baru'),
            'content_pergantian_paspor': get_content('Pergantian Paspor'),
            'content_pergantian_paspor_hilang_atau_rusak': get_content('Pergantian Paspor Hilang/Rusak'),
            'perpanjang_visa_kunjungan_saat_kedatangan': get_content('Perpanjang Visa Kunjungan Saat Kedatangan'),
            'izin_tinggal_kunjungan': get_content('Izin Tinggal Kunjungan'),
            'izin_tinggal_terbatas': get_content('Izin Tinggal Terbatas'),
            'izin_masuk_kembali': get_content('Izin Masuk Kembali'),
            'izin_tinggal_tetap': get_content('Izin Tinggal Tetap'),
            'alih_status_izin_tinggal': get_content('Alih Status Izin Tinggal'),
            'perubahan_alamat': get_content('Perubahan Alamat'),
            'pendaftaran_anak': get_content('Pendaftaran Anak Berkewarganegaraan Ganda dan Fasilitas Keimigrasian (Ganda Terbatas)')
            })
    else:
        return redirect('update_layanan_imigrasi', pk=pk)
    
def delete_layanan_imigrasi(request):
    pass
    
def get_content(content_menu):
    return Content.objects.order_by('-create_at').filter(content_menu__submenu_name=content_menu).first()
    
def add_content(request):
    form = AddContentForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_content = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/add_content.html', {'form':form})
    else:
        return redirect('dashboard')
    
def update_content(request, pk):
    if request.user.is_authenticated:
        current_content = Content.objects.get(content_menu_id=pk)
        form = AddContentForm(request.POST or None, instance=current_content)
        if form.is_valid():
                add_content = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/update-content.html', {
            'form':form,
            })
    else:
        return redirect('dashboard')
    
# file
    
def add_file(request):
    form = AddFileArsipdanDokumen(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_file = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/add_file.html', {'form':form})
    else:
        return redirect('dashboard')
    
def update_file(request, pk):
    if request.user.is_authenticated:
        current_file = FileArsipDanDokumen.objects.get(id=pk)
        form = AddFileArsipdanDokumen(request.POST or None, request.FILES or None, instance=current_file)
        if form.is_valid():
                add_file = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/update_file.html', {
            'form':form,
            })
    else:
        return redirect('dashboard')
    
def delete_file(request, pk):
    file = FileArsipDanDokumen.objects.get(id=pk)
    file.delete()
    return redirect(request.META.get('HTTP_REFERER'))
    
def daftar_isian_pelaksana_anggaran(request):
    return render(request, 'dashboard/arsip_dan_dokumen/daftar-isian-pelaksana-anggaran.html', {
        'daftar_isian_pelaksana_anggaran': get_file('DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN')
    })
    
def laporan_akuntabilitas_kinerja(request):
    return render(request, 'dashboard/arsip_dan_dokumen/laporan-akuntabilitas-kinerja.html', {
        'laporan_akuntabilitas_kinerja': get_file('LAPORAN_AKUNTABILITAS_KINERJA')
    })

def timpora(request):
    return render(request, 'dashboard/arsip_dan_dokumen/timpora.html', {
        'timpora': get_file('TIMPORA')
    })
    
def file_informasi_berkala(request):
    return render(request, 'dashboard/arsip_dan_dokumen/file-informasi-berkala.html', {
        'file_informasi_berkala': get_file('INFORMASI_BERKALA')
    })
    
def get_file(file_category):
   return FileArsipDanDokumen.objects.filter(category=file_category).order_by('-file_added_at')

def show_foto(request):
    return render(request, 'dashboard/galeri/foto.html', {
        'foto': get_foto()
    })
    
def show_video(request):
    return render(request, 'dashboard/galeri/video.html', {
        'video': get_video()
    })

def get_foto():
    return FotoGaleri.objects.all().order_by('-image_added_at')

def add_foto(request):
    form = AddFotoGaleri(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_foto = form.save()
                return redirect('show_foto')
        return render(request, 'dashboard/galeri/add_foto.html', {'form':form})
    else:
        return redirect('dashboard')

def update_foto(request, pk):
    if request.user.is_authenticated:
        current_foto = FotoGaleri.objects.get(id=pk)
        form = AddFotoGaleri(request.POST or None, request.FILES or None, instance=current_foto)
        if form.is_valid():
            add_foto = form.save()
            return redirect('show_foto')
        return render(request, 'dashboard/galeri/update_foto.html', {
            'form':form,
            })
    else:
        return redirect('update_foto', pk=pk)

def delete_foto(request, pk):
    foto = FotoGaleri.objects.get(id=pk)
    foto.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def add_video(request):
    form = AddVideo(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_video = form.save()
                return redirect('show_video')
        return render(request, 'dashboard/galeri/add_video.html', {'form':form})
    else:
        return redirect('dashboard')

def update_video(request, pk):
    if request.user.is_authenticated:
        current_video = YoutubeVideo.objects.get(id=pk)
        form = AddVideo(request.POST or None, request.FILES or None, instance=current_video)
        if form.is_valid():
                add_video = form.save()
                return redirect('show_video')
        return render(request, 'dashboard/galeri/update_video.html', {
            'form':form,
            })
    else:
        return redirect('dashboard')

def delete_video(request, pk):
    foto = YoutubeVideo.objects.get(id=pk)
    foto.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def get_video():
    return YoutubeVideo.objects.all().order_by('-create_at')

#berita

def kantor_imigrasi(request):
    kantor_imigrasi_cilegon = get_berita("KANTOR_IMIGRASI_CILEGON")
    kantor_imigrasi_cilegon_image = get_berita_image(kantor_imigrasi_cilegon, "KANTOR_IMIGRASI_CILEGON")
    
    return render(request, 'dashboard/berita/kantor-imigrasi.html', {
        'kantor_imigrasi': zip(kantor_imigrasi_cilegon, kantor_imigrasi_cilegon_image),
        'kantor_imigrasi_image': kantor_imigrasi_cilegon_image
    })
    
def kemenkumham_republik_indonesia(request):
    kemenkumham_republik_indonesia = get_berita("KEMENKUMHAM_REPUBLIK_INDONESIA")
    kemenkumham_republik_indonesia_image = get_berita_image(kemenkumham_republik_indonesia, "KEMENKUMHAM_REPUBLIK_INDONESIA")
    
    return render(request, 'dashboard/berita/kemenkumham-republik-indonesia.html', {
        'kemenkumham_republik_indonesia': zip(kemenkumham_republik_indonesia, kemenkumham_republik_indonesia_image)
    })

def kemenkumham_kanwil_banten(request):
    kemenkumham_kanwil_banten = get_berita("KEMENKUMHAM_KANWIL_BANTEN")
    kemenkumham_kanwil_banten_image = get_berita_image(kemenkumham_kanwil_banten, "KEMENKUMHAM_KANWIL_BANTEN")
    
    return render(request, 'dashboard/berita/kemenkumham-kanwil-banten.html', {
        'kemenkumham_kanwil_banten': zip(kemenkumham_kanwil_banten, kemenkumham_kanwil_banten_image)
    })
    
def add_berita(request):
    form = AddBerita(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_berita = form.save()
                return redirect(request.POST.get('category_berita').lower())
        return render(request, 'dashboard/berita/add-berita.html', {'form':form})
    else:
        return redirect('dashboard')

def update_berita(request, pk):
    if request.user.is_authenticated:
        current_berita = Berita.objects.get(id=pk)
        form = AddBerita(request.POST or None, request.FILES or None, instance=current_berita)
        if form.is_valid():
                add_berita = form.save()
                return redirect(request.POST.get('category_berita').lower())
        return render(request, 'dashboard/berita/update-berita.html', {
            'form':form,
            })
    else:
        return redirect('update_berita', pk=pk)

def delete_berita(request, pk):
    foto = Berita.objects.get(id=pk)
    foto.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def get_berita(category):
    return Berita.objects.filter(category_berita=category).order_by('-create_at')

def get_berita_image(beritas, category_berita):
    # check kalo title berita iamge sama dengan title berita dan save semua yang sama
    # kalo nggak sama di buat array/tuple baru
    list_of_image = []
    
    berita_images = BeritaImage.objects.filter(berita__category_berita=category_berita).order_by('-image_added_at')
    
    for berita in beritas:
        list_of_image.append(BeritaImage.objects.filter(berita__berita_title=berita.berita_title))
        
    return list_of_image

def add_berita_image(request):
    form = AddBeritaImage(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_berita_image = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/berita/add-berita-image.html', {'form':form})
    else:
        return redirect('dashboard')

def update_berita_image(request, pk):
    if request.user.is_authenticated:
        current_berita_image = BeritaImage.objects.get(id=pk)
        form = AddBeritaImage(request.POST or None, request.FILES or None, instance=current_berita_image)
        if form.is_valid():
                add_berita_image = form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/berita/update-berita-image.html', {'form':form})
    else:
        return redirect('update_image_berita', pk=pk)

def delete_berita_image(request, pk):
    berita_image = BeritaImage.objects.get(id=pk)
    berita_image.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def ipk_dan_ipm(request):
    last_entries = (IPKandIKM.objects
    .annotate(tx_month=TruncMonth('date'))
    .values('tx_month')
    .annotate(last_entry=Max('date'))
    .values_list('last_entry', flat=True))
    
    return render(request, 'dashboard/ipk-dan-ipm.html', {
        'ipk_dan_ipm': IPKandIKM.objects.filter(date__in=last_entries).order_by('-date')
    })
    
def delete_ipk_dan_ipm(request, pk):
    ipk_dan_ipm = IPKandIKM.objects.get(id=pk)
    ipk_dan_ipm.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def update_data_survey_ipk_dan_ipm(request, pk):
    if request.user.is_authenticated:
        current_survey_data = IndexSurvey.objects.get(id=pk)
        form = AddIndexSurvey(request.POST or None, request.FILES or None, instance=current_survey_data)
        if form.is_valid():
                add_index_survet = form.save()
                return redirect('ipk_dan_ipm')
        return render(request, 'dashboard/update-data-survey-ipk-dan-ipm.html', {'form':form})
    else:
        return redirect('update_data_survey_ipk_dan_ipm', pk=pk)
    
def add_ipk_dan_ipm(request):
    ipk_dan_ipm_form = IPKdanIPMForm(request.POST or None, request.FILES or None)
    index_survey_form = AddIndexSurvey(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if ipk_dan_ipm_form.is_valid():
                add_ipk_dan_ipm = ipk_dan_ipm_form.save()
                return redirect('ipk_dan_ipm')
        return render(request, 'dashboard/add-ipk-dan-ipm.html', {
            'ipk_dan_ipm_form': ipk_dan_ipm_form,
            'index_survey_form': index_survey_form
            })
    else:
        return redirect('dashboard')