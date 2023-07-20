from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.db.models import Sum, F

from .models import FotoGaleri, Berita, BeritaImage, YoutubeVideo, FileArsipDanDokumen, SubMenu, Content, Menu, \
    VisiDanMisi, Kakanim, StrukturOrganisasi, ListPerusahaanDanPenginapanWilayahKerja, LaporanPelayananWNI, \
    LaporanPelayananWNA, IndexPersepsiKorupsi, IndexKepuasanMasyarakat
from datetime import datetime, timedelta

import subprocess
import os
import threading

def home(response):
    one_week_ago = datetime.today() - timedelta(days=7)
    wni_menus = SubMenu.objects.filter(menu__menu_name__contains="Warga Negara Indonesia")
    wna_menus = SubMenu.objects.filter(menu__menu_name__contains="Warga Negara Asing")
    highlight_foto = get_foto_galeri()
    fotos = FotoGaleri.objects.order_by("-image_added_at")[:8]
    headline_berita = get_single_berita()
    headline_berita_image = get_berita_image_single()
    beritas = Berita.objects.order_by("-create_at")[1:5]
    youtube_videos = YoutubeVideo.objects.order_by("-create_at")[:4]
    subprocess.run(["rm", "-rf", "images/imigrasi_cilegon"])
    subprocess.run(["cp", "-R", "imigrasi_cilegon", "images/"])
    fetch_image = threading.Thread(target=fetch_instagram, args=[])
    fetch_image.start()
    total_laporan_pelayanan_wni = LaporanPelayananWNI.objects.all().aggregate(total=Coalesce(Sum(
        F('total_paspor_baru') +
        F('total_pergantian_paspor') +
        F('total_pergantian_paspor_hilang_rusak') +
        F('total_penyerahan_paspor')
    ), 0))['total']
    total_laporan_pelayanan_wna = LaporanPelayananWNA.objects.all().aggregate(total=Coalesce(Sum(
        F('total_ijin_tinggal_kunjungan') +
        F('total_izin_tinggal_terbatas')
    ), 0))['total']
    this_week_laporan_pelayanan_wni = LaporanPelayananWNI.objects.filter(date__gte=one_week_ago)
    this_month_laporan_pelayanan_wni = LaporanPelayananWNI.objects.filter(date__month=str(datetime.today().month))
    this_year_laporan_pelayanan_wni = LaporanPelayananWNI.objects.filter(date__year=str(datetime.today().year))
    this_week_laporan_pelayanan_wna = LaporanPelayananWNA.objects.filter(date__gte=one_week_ago)
    this_month_laporan_pelayanan_wna = LaporanPelayananWNA.objects.filter(date__month=str(datetime.today().month))
    this_year_laporan_pelayanan_wna = LaporanPelayananWNA.objects.filter(date__year=str(datetime.today().year))

    return render(response, "main/beranda.html",{
          'wni_menus': wni_menus,
          'wna_menus': wna_menus,
          'highlight_foto': highlight_foto,
          'fotos': fotos,
          'headline_berita': headline_berita,
          'headline_berita_image': headline_berita_image,
          'berita_with_image': zip(beritas, get_berita_image(beritas)),
          'youtube_videos': youtube_videos,
          'instagram_image': get_list_of_instagram(),
        'total_all_pelayanan': total_laporan_pelayanan_wni + total_laporan_pelayanan_wna,
        'total_all_this_week_pelayanan':
            this_week_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'] +
            this_week_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_all_this_month_pelayanan':
            this_month_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'] +
            this_month_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_all_this_year_pelayanan':
            this_year_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'] +
            this_year_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_this_month_wni': this_month_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
            F('total_paspor_baru') +
            F('total_pergantian_paspor') +
            F('total_pergantian_paspor_hilang_rusak') +
            F('total_penyerahan_paspor')
        ), 0))['total']
        })

def get_foto_galeri():
    querySet = FotoGaleri.objects.order_by("-image_added_at")
    if querySet.exists():
        return FotoGaleri.objects.order_by("-image_added_at")[0]
    else:
        return ""
def get_single_berita():
    querySet = Berita.objects.all()

    if querySet.exists():
        return Berita.objects.order_by("-create_at")[0]
    else:
        return ""

def get_berita_image_single():
    query_set = Berita.objects.all()

    if query_set.exists():
        headline_berita = Berita.objects.order_by("-create_at")[0]
        query_set2 = BeritaImage.objects.order_by("image_added_at").filter(berita=headline_berita.id)
        if query_set2.exists():
            return query_set2[0]
        else:
            return ""
    else:
        return ""



def fetch_instagram():
    subprocess.run(["python3", "fetch_image_script.py"])
    subprocess.run(["python3", "delete_unnecessary_instagram_file.py"])

def layanan_imigrasi(response):
    return render(response, "main/layanan-imigrasi.html", {
        'list_of_submenu_wni': get_submenu("Warga Negara Indonesia"),
        'list_of_submenu_wna': get_submenu("Warga Negara Asing"),
        'content_paspor_baru': get_content("Paspor Baru"),
        'content_penyerahan_paspor': get_content("Penyerahan Paspor"),
        'content_pergantian_paspor': get_content("Pergantian Paspor"),
        'content_pergantian_paspor_hilang_rusak': get_content("Pergantian Paspor Hilang/Rusak"),
        'content_perpanjang_visa_kunjugnan_saat_kedatangan': get_content("Perpanjang Visa Kunjungan Saat Kedatangan"),
        'content_izin_tingga_kunjungan': get_content("Izin Tinggal Kunjungan"),
        'content_izin_tinggal_terbatas': get_content("Izin Tinggal Terbatas"),
        'content_izin_masuk_kembali': get_content("Izin Masuk Kembali"),
        'content_izin_tinggal_kembali': get_content("Izin Tinggal Tetap"),
        'content_alih_status_izin_tinggal': get_content("Alih Status Izin Tinggal"),
        'content_perubahan_alamat': get_content("Perubahan Alamat"),
        'content_pendaftaran_anak_berkewarganegaraan_ganda':
            get_content("Pendaftaran Anak Berkewarganegaraan Ganda dan Fasilitas Keimigrasian (Ganda Terbatas)"),
    })

def ppid(response):
    return render(response, "main/ppid.html", {
        'list_of_submenu_ppid': get_submenu('PPID'),
        'content_dasar_hukum_ppid': get_content("Dasar Hukum PPID"),
        'content_sk_penetapan_ppid': get_content("SK Penetapan PPID"),
        'content_struktur_ppid': get_content("Struktur PPID"),
        'content_tugas_dan_fungsi_ppid': get_content("Tugas dan Fungsi PPID"),
        'content_standar_pelayanan_informasi': get_content("Standar Pelayanan Informasi"),
        'content_kegiatan_tata_kelola_informasi_publik': get_content("Kegiatan Tata kelola Informasi Publik"),
        'content_sk_informasi_yang_dikecualikan': get_content("SK Informasi yang Dikecualikan"),
        'content_daftar_informasi_publik': get_content("Daftar Informasi Publik"),
        'content_informasi_berkala':
            FileArsipDanDokumen.objects.filter(category='INFORMASI_BERKALA').order_by("-file_added_at")[:5],
        'content_informasi_setiap_saat': get_content("Informasi Setiap Saat"),
        'content_informasi_serta_merta': get_content("Informasi Serta Merta"),
        'content_informasi_dikecualikan': get_content("Informasi Dikecualikan"),
        'content_profile_ppid': get_content("Profile PPID"),
        'content_form_permintaan_informasi_dan_Pernyataan_kebenaran':
            get_content("Form Permintaan Informasi & Pernyataan Kebenaran")
    })

def profile(response):
    return render(response, "main/profile.html", {
        'list_of_submenu_profile': get_submenu('Profile'),
        'content_sejarah_imigrasi': get_content('Sejarah Imigrasi'),
        'content_sejarah_kantor': get_content('Sejarah Kantor'),
        'content_visi_dan_misi': VisiDanMisi.objects.all().first(),
        'content_struktur_organisasi': get_content('Struktur Organisasi'),
        'content_tugas_dan_fungsi': get_content('Tugas dan Fungsi'),
        'content_jabatan_kepala_kantor': get_struktur_organisasi("KEPALA_KANTOR"),
        'content_jabatan_kasubag_tata_usaha': get_struktur_organisasi("KASUBAG_TATA_USAHA"),
        'content_jabatan_kasi_lalu_lintas': get_struktur_organisasi("KASI_LALU_LINTAS_DAN_IZIN_TINGGAL_KEIMIGRASIAN"),
        'content_jabatan_kasi_teknologi': get_struktur_organisasi("KASI_TEKNOLOGI_DAN_INFORMASI_KEIMIGRASIAN"),
        'content_jabatan_kasi_intelijen': get_struktur_organisasi("KASI_INTELEJEN_DAN_PENINDAKAN_KEIMIGRASIAN"),
        'content_jabatan_kaur_kepegawaian': get_struktur_organisasi("KAUR_KEPEGAWAIAN"),
        'content_jabatan_kasubi_lalu_lintas': get_struktur_organisasi("KASUBSI_LALU_LINTAS_KEIMIGRASIAN"),
        'content_jabatan_kasubi_izin': get_struktur_organisasi("KASUBSI_IZIN_TINGGAL_KEIMIGRASIAN"),
        'content_jabatan_kasubi_teknologi': get_struktur_organisasi("KASUBSI_TEKNOLOGI_INFORMASI_KEIMIGRASIAN"),
        'content_jabatan_kasubi_informasi': get_struktur_organisasi("KASUBSI_INFORMASI_DAN_KOMUNIKASI_KEIMIGRASIAN"),
        'content_jabatan_kasubi_intelijen': get_struktur_organisasi("KASUBSI_INTELIJEN_KEIMIGRASIAN"),
        'content_jabatan_kasubi_penindakan': get_struktur_organisasi("KASUBSI_PENINDAKAN_KEIMIGRASIAN"),
        'content_kakanim_dari_waktu': get_all_kakanim,
        'list_of_perusahaan_penginapan_bojonegara': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='BOJONEGARA'),
        'list_of_perusahaan_penginapan_cibeber': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='CIBEBER'),
        'list_of_perusahaan_penginapan_cilegon': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='CILEGON'),
        'list_of_perusahaan_penginapan_citangkil': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='CITANGKIL'),
        'list_of_perusahaan_penginapan_ciwandan': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='CIWANDAN'),
        'list_of_perusahaan_penginapan_gerogol': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='GEROGOL'),
        'list_of_perusahaan_penginapan_jombang': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='JOMBANG'),
        'list_of_perusahaan_penginapan_puloampel': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='PULOAMPEL'),
        'list_of_perusahaan_penginapan_pulomerak': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='PULOMERAK'),
        'list_of_perusahaan_penginapan_purwakarta': ListPerusahaanDanPenginapanWilayahKerja.objects.get(
            wilayah_kerja='PURWAKARTA'),
    })

def biaya_keimigrasian(response):
    return render(response, "main/biaya-imigrasi.html", {
        'list_of_submenu_dokumen_perjalanan': get_submenu("Dokumen Perjalanan"),
        'list_of_submenu_visa': get_submenu("Visa"),
        'list_of_submenu_izin_keimigrasian': get_submenu("Izin Keimigrasian"),
        'list_of_submenu_pnbp_keimigrasian_lainnya': get_submenu("PNBP Keimigrasian Lainnya"),
        'content_dokumen_perjalanan_republik_indonesia': get_content("Dokumen Perjalanan Republik Indonesia"),
        'content_visa_kunjungan': get_content("Visa Kunjungan"),
        'content_visa_tinggal_terbatas': get_content("Visa Tinggal Terbatas"),
        'content_izin_kunjugan': get_content("Izin Kunjungan"),
        'content_izin_tinggal_terbatas': get_content("Izin Tinggal Terbatas"),
        'content_izin_tinggal_tetap': get_content("Izin Tinggal Tetap"),
        'content_izin_masuk_kembali': get_content("Izin Masuk Kembali (Re-Entry Permit)"),
        'content_biaya_beban': get_content("Biaya Beban"),
        'content_smart_card': get_content("Smart Card"),
        'content_kartu_perjalan_Pebisnis':
            get_content("Kartu Perjalanan Pebisnis Asia Pacific Economic Cooperation (KPP APEC)/APEC Business Travel Card (ABTC)"),
        'content_failitas_keimigrasian':
            get_content("Fasilitas Keimigrasian (Afidavit) Bagi Anak Berkewarganegaraan Ganda"),
        'content_surat_keterangan_keimigrasian': get_content("Surat Keterangan Keimigrasian"),
    })

def arsip_dan_dokumen(response):
    daftar_isian_pelaksanaan_anggaran = \
        FileArsipDanDokumen.objects.filter(category='DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN').order_by("-file_added_at")[:5]
    laporan_akuntabilitas_kinerja = \
        FileArsipDanDokumen.objects.filter(category='LAPORAN_AKUNTABILITAS_KINERJA').order_by("-file_added_at")[:5]

    return render(response, "main/arsip-dan-dokumen.html", {
        'daftar_isian_pelaksanaan_anggaran': daftar_isian_pelaksanaan_anggaran,
        'laporan_akuntabilitas_kinerja': laporan_akuntabilitas_kinerja,
        'list_of_submenu_arsip_dan_dokumen': get_submenu("Arsip dan Dokumen")
    })

def zona_integritas(response):
    return render(response, "main/zona-integritas.html", {
        'list_of_submenu_zona_integritas': get_submenu('Zona Integritasi'),
        'content_pengertian': get_content("Pengertian"),
        'content_6_area_perbahan': get_content("6 Area Perubahan"),
        'content_dokumentasi_kegiatan_pzi': get_image("DOKUMENTASI"),
        'content_jingle_kantor_imigrasi_kelas_ii_tpi_cilegon': get_youtube_video("JINGLE"),
        'content_paparan_wbk_2023': get_youtube_video("ZONA_INTEGRITAS")
    })

def timpora(response):
    return render(response, "main/timpora.html", {
        'list_of_submenu_timpora': get_submenu('Timpora'),
        'file_timpora': FileArsipDanDokumen.objects.filter(category='TIMPORA').order_by("-file_added_at")[:5]
    })

def berita(response):
    berita_header_from_kemenkumham_kanwil_banten = get_header_berita('KEMENKUMHAM_KANWIL_BANTEN')
    berita_header_from_kemenkumham_republik_indonesia = get_header_berita('KEMENKUMHAM_REPUBLIK_INDONESIA')
    berita_header_from_kantor_imigrasi_cilegon = get_header_berita('KANTOR_IMIGRASI_CILEGON')
    berita_from_kemenkumham_kanwil_banten = \
        Berita.objects.order_by('-create_at').filter(category_berita='KEMENKUMHAM_KANWIL_BANTEN')[1:10]
    total_berita_from_kemenkumham_kanwil_banten = \
        Berita.objects.order_by('-create_at').filter(category_berita='KEMENKUMHAM_KANWIL_BANTEN').count()
    berita_from_kemenkumham_republik_indonesia = \
        Berita.objects.order_by('-create_at').filter(category_berita='KEMENKUMHAM_REPUBLIK_INDONESIA')[1:10]
    total_berita_from_kemenkumham_republik_indonesia = \
        Berita.objects.order_by('-create_at').filter(category_berita='KEMENKUMHAM_REPUBLIK_INDONESIA').count()
    berita_from_kantor_imigrasi_cilegon = \
        Berita.objects.order_by('-create_at').filter(category_berita='KANTOR_IMIGRASI_CILEGON')[1:10]
    total_berita_from_kantor_imigrasi_cilegon = \
        Berita.objects.order_by('-create_at').filter(category_berita='KANTOR_IMIGRASI_CILEGON').count()

    return render(response, "main/berita.html", {
        'berita_header_from_kemenkumham_kanwil_banten': berita_header_from_kemenkumham_kanwil_banten,
        'berita_header_from_kemenkumham_republik_indonesia': berita_header_from_kemenkumham_republik_indonesia,
        'berita_header_from_kantor_imigrasi_cilegon': berita_header_from_kantor_imigrasi_cilegon,
        'berita_header_image_from_kantor_imigrasi_cilegon': get_berita_detail_image(
            'KANTOR_IMIGRASI_CILEGON', berita_header_from_kantor_imigrasi_cilegon),
        'berita_header_image_from_kemenkumham_republik_indonesia': get_berita_detail_image(
            'KEMENKUMHAM_REPUBLIK_INDONESIA', berita_header_from_kemenkumham_republik_indonesia),
        'berita_header_image_from_kemenkumham_kanwil_banten': get_berita_detail_image(
            'KEMENKUMHAM_KANWIL_BANTEN', berita_header_from_kemenkumham_kanwil_banten),
        'berita_image_from_kantor_imigrasi_cilegon': zip(berita_from_kantor_imigrasi_cilegon,
                                                         get_berita_image(berita_from_kantor_imigrasi_cilegon)),
        'berita_image_from_kemenkumham_republik_indonesia': zip(    berita_from_kemenkumham_republik_indonesia,
                                                                get_berita_image(berita_from_kemenkumham_republik_indonesia)),
        'berita_image_from_kemenkumham_kanwil_banten': zip(berita_from_kemenkumham_kanwil_banten,
                                                                get_berita_image(berita_from_kemenkumham_kanwil_banten))
    })

def get_header_berita(category_berita):
    querySet = Berita.objects.order_by('-create_at').filter(category_berita=category_berita)

    if querySet.exists():
        return querySet[0]
    else:
        return Berita.objects.none()

def get_berita_detail_image(berita_header_from, header):
    query_set = Berita.objects.order_by('-create_at').filter(category_berita=berita_header_from)
    query_set_image = BeritaImage.objects.all()

    if query_set.exists():
        if query_set_image.exists():
            return BeritaImage.objects.filter(berita__berita_title=header.berita_title).first()
        else:
            return BeritaImage.objects.none()
    else:
        pass

def galeri(response):
    return render(response, "main/galeri.html", {
        'fotos': get_all_image(),
        'videos': get_all_youtube_video()
    })

def berita_detail(request, pk):
    berita = Berita.objects.get(id=pk)
    berita_image_header = get_berita_image_header(berita)
    berita_image_content = BeritaImage.objects.filter(berita=berita.id)
    berita_terkini = Berita.objects.order_by('-create_at').all()[:4]
    berita_terkini_image = get_berita_image(berita_terkini)

    return render(request, "main/berita-detail.html", {
        'berita': berita,
        'berita_image_header': berita_image_header,
        'berita_image_content': berita_image_content,
        'berita_terkini': zip(berita_terkini, berita_terkini_image)
    })

def get_berita_image_header(berita):
    query_set = BeritaImage.objects.filter(berita=berita.id)

    if query_set.exists():
        return BeritaImage.objects.filter(berita=berita.id).first()
    else:
        BeritaImage.objects.none()

def dasbor_publik(response):
    one_week_ago = datetime.today() - timedelta(days=7)

    total_laporan_pelayanan_wni = LaporanPelayananWNI.objects.all().aggregate(total=Coalesce(Sum(
        F('total_paspor_baru') +
        F('total_pergantian_paspor') +
        F('total_pergantian_paspor_hilang_rusak') +
        F('total_penyerahan_paspor')
    ), 0))['total']
    total_laporan_pelayanan_wna = LaporanPelayananWNA.objects.all().aggregate(total=Coalesce(Sum(
        F('total_ijin_tinggal_kunjungan') +
        F('total_izin_tinggal_terbatas')
    ), 0))['total']
    this_week_laporan_pelayanan_wni = LaporanPelayananWNI.objects.filter(date__gte=one_week_ago)
    this_month_laporan_pelayanan_wni = LaporanPelayananWNI.objects.filter(date__month=str(datetime.today().month))
    this_year_laporan_pelayanan_wni = LaporanPelayananWNI.objects.filter(date__year=str(datetime.today().year))
    this_week_laporan_pelayanan_wna = LaporanPelayananWNA.objects.filter(date__gte=one_week_ago)
    this_month_laporan_pelayanan_wna = LaporanPelayananWNA.objects.filter(date__month=str(datetime.today().month))
    this_year_laporan_pelayanan_wna = LaporanPelayananWNA.objects.filter(date__year=str(datetime.today().year))
    this_month_ipk = IndexPersepsiKorupsi.objects.filter(date__month=str(datetime.today().month))
    this_year_ipk = IndexPersepsiKorupsi.objects.filter(date__year=str(datetime.today().year))
    this_month_ikm = IndexKepuasanMasyarakat.objects.filter(date__month=str(datetime.today().month))
    this_year_ikm = IndexKepuasanMasyarakat.objects.filter(date__year=str(datetime.today().year))

    return render(response, "main/dasbor-publik.html", {
        'total_all_pelayanan': total_laporan_pelayanan_wni + total_laporan_pelayanan_wna,
        'total_all_this_week_pelayanan':
            this_week_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'] +
            this_week_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_all_this_month_pelayanan':
            this_month_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'] +
            this_month_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_all_this_year_pelayanan':
            this_year_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'] +
            this_year_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_this_month_wni': this_month_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
                F('total_paspor_baru') +
                F('total_pergantian_paspor') +
                F('total_pergantian_paspor_hilang_rusak') +
                F('total_penyerahan_paspor')
            ), 0))['total'],
        'total_this_month_paspor_baru_wni': aggregateSpecificField(
            this_month_laporan_pelayanan_wni, 'total_paspor_baru'),
        'total_this_month_total_pergantian_paspor_wni': aggregateSpecificField(
            this_month_laporan_pelayanan_wni, 'total_pergantian_paspor'),
        'total_this_month_total_pergantian_paspor_hilang_rusak_wni': aggregateSpecificField(
            this_month_laporan_pelayanan_wni, 'total_pergantian_paspor_hilang_rusak'),
        'total_this_month_total_penyerahan_paspor_wni': aggregateSpecificField(
            this_month_laporan_pelayanan_wni, 'total_penyerahan_paspor'),
        'total_this_month_wna': this_month_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
                F('total_ijin_tinggal_kunjungan') +
                F('total_izin_tinggal_terbatas')
            ), 0))['total'],
        'total_this_month_total_ijin_tinggal_kunjungan_wna': aggregateSpecificField(
            this_month_laporan_pelayanan_wna, 'total_ijin_tinggal_kunjungan'),
        'total_this_month_total_izin_tinggal_terbatas_paspor_wna': aggregateSpecificField(
            this_month_laporan_pelayanan_wna, 'total_izin_tinggal_terbatas'),
        'total_this_week_wni': this_week_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
            F('total_paspor_baru') +
            F('total_pergantian_paspor') +
            F('total_pergantian_paspor_hilang_rusak') +
            F('total_penyerahan_paspor')
        ), 0))['total'],
        'total_this_week_paspor_baru_wni': aggregateSpecificField(
            this_week_laporan_pelayanan_wni, 'total_paspor_baru'),
        'total_this_week_total_pergantian_paspor_wni': aggregateSpecificField(
            this_week_laporan_pelayanan_wni, 'total_pergantian_paspor'),
        'total_this_week_total_pergantian_paspor_hilang_rusak_wni': aggregateSpecificField(
            this_week_laporan_pelayanan_wni, 'total_pergantian_paspor_hilang_rusak'),
        'total_this_week_total_penyerahan_paspor_wni': aggregateSpecificField(
            this_week_laporan_pelayanan_wni, 'total_penyerahan_paspor'),
        'total_this_week_wna': this_week_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
            F('total_ijin_tinggal_kunjungan') +
            F('total_izin_tinggal_terbatas')
        ), 0))['total'],
        'total_this_week_total_ijin_tinggal_kunjungan_wna': aggregateSpecificField(
            this_week_laporan_pelayanan_wna, 'total_ijin_tinggal_kunjungan'),
        'total_this_week_total_izin_tinggal_terbatas_paspor_wna': aggregateSpecificField(
            this_week_laporan_pelayanan_wna, 'total_izin_tinggal_terbatas'),
        'total_this_year_wni': this_year_laporan_pelayanan_wni.aggregate(total=Coalesce(Sum(
            F('total_paspor_baru') +
            F('total_pergantian_paspor') +
            F('total_pergantian_paspor_hilang_rusak') +
            F('total_penyerahan_paspor')
        ), 0))['total'],
        'total_this_year_paspor_baru_wni': aggregateSpecificField(
            this_year_laporan_pelayanan_wni, 'total_paspor_baru'),
        'total_this_year_total_pergantian_paspor_wni': aggregateSpecificField(
            this_year_laporan_pelayanan_wni, 'total_pergantian_paspor'),
        'total_this_year_total_pergantian_paspor_hilang_rusak_wni': aggregateSpecificField(
            this_year_laporan_pelayanan_wni, 'total_pergantian_paspor_hilang_rusak'),
        'total_this_year_total_penyerahan_paspor_wni': aggregateSpecificField(
            this_year_laporan_pelayanan_wni, 'total_penyerahan_paspor'),
        'total_this_year_wna': this_year_laporan_pelayanan_wna.aggregate(total=Coalesce(Sum(
            F('total_ijin_tinggal_kunjungan') +
            F('total_izin_tinggal_terbatas')
        ), 0))['total'],
        'total_this_year_total_ijin_tinggal_kunjungan_wna': aggregateSpecificField(
            this_year_laporan_pelayanan_wna, 'total_ijin_tinggal_kunjungan'),
        'total_this_year_total_izin_tinggal_terbatas_paspor_wna': aggregateSpecificField(
            this_year_laporan_pelayanan_wna, 'total_izin_tinggal_terbatas'),
        'this_year_ipk': this_year_ipk,
        'this_year_ikm': this_year_ikm
    })

def aggregateSpecificField(table, field):
    total = 0
    for i in table:
        if field == 'total_paspor_baru':
            total = total + i.total_paspor_baru
        elif field == 'total_pergantian_paspor':
            total = total + i.total_pergantian_paspor
        elif field == 'total_pergantian_paspor_hilang_rusak':
            total = total + i.total_pergantian_paspor_hilang_rusak
        elif field == 'total_penyerahan_paspor':
            total = total + i.total_penyerahan_paspor
        elif field == 'total_ijin_tinggal_kunjungan':
            total = total + i.total_ijin_tinggal_kunjungan
        elif field == 'total_izin_tinggal_terbatas':
            total = total + i.total_izin_tinggal_terbatas

    return total

def get_berita_image(beritas):
    list_of_berita_image = []
    querySet = BeritaImage.objects.all()

    if querySet.exists():
        for berita in beritas:
            list_of_berita_image.append(BeritaImage.objects.filter(berita=berita.id).first())
    else:
        pass

    return list_of_berita_image

def get_menu(main_menu):
    return Menu.objects.filter(main_menu__main_menu_name=main_menu)

def get_submenu(menu):
    return SubMenu.objects.filter(menu__menu_name__contains=menu)

def get_content(submenu):
    querySet = Content.objects.filter(content_menu__submenu_name=submenu).order_by("-create_at").exists()
    if querySet:
        return Content.objects.filter(content_menu__submenu_name=submenu).order_by("-create_at")[0]
    else:
        Content.objects.none()

def get_berita(category):
    return Berita.objects.filter(category_berita=category)

def get_berita_header(category):
    return Berita.objects.filter(category_berita=category)[0]

def get_all_image():
    return FotoGaleri.objects.all().order_by('-image_added_at')[:20]

def get_image(category):
    return FotoGaleri.objects.filter(foto_category=category).order_by('-image_added_at')

def get_all_youtube_video():
    return YoutubeVideo.objects.all().order_by('-create_at')[:20]

def get_youtube_video(category):
    return YoutubeVideo.objects.filter(youtube_category=category).order_by('-create_at')

def get_all_kakanim():
    queryset = Kakanim.objects.all().exists()
    if queryset:
        return Kakanim.objects.all()
    else:
        return Kakanim.objects.none()

def get_struktur_organisasi(jabatan):
    queryset = StrukturOrganisasi.objects.filter(jabatan=jabatan).exists()
    if queryset:
        return StrukturOrganisasi.objects.filter(jabatan=jabatan).order_by('-id')[0]
    else:
        return StrukturOrganisasi.objects.none()

def get_list_of_instagram():
    current_path = os.getcwd() + "/images/imigrasi_cilegon/"
    list_of_item = os.listdir(current_path)

    return ["/images/imigrasi_cilegon/" + x for x in list_of_item]