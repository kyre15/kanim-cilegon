from django.urls import path
from . import views
from . import dashboard_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("eda884u7g1k7ck75cp0964jqtbcxmu.html", views.facebook_verification, name="facebook_verification"),
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
    # layanan imigrasi
    path('dashboard/', dashboard_views.index, name="dashboard"),
    path('dashboard/paspor-baru', dashboard_views.paspor_baru, name='paspor_baru'),
    path('dashboard/pergantian-paspor', dashboard_views.pergantian_paspor, name='pergantian_paspor'),
    path('dashboard/pergantian-paspor-hilang-atau-rusak', dashboard_views.pergantian_paspor_hilang_atau_rusak, name='pergantian_paspor_hilang_atau_rusak'),
    path('dashboard/perpanjang-visa-kunjungan-saat-kedatangan', dashboard_views.perpanjang_visa_kunjungan_saat_kedatangan, name='perpanjang_visa_kunjungan_saat_kedatangan'),
    path('dashboard/izin-tinggal-kunjungan', dashboard_views.izin_tinggal_kunjungan, name='izin_tinggal_kunjungan'),
    path('dashboard/izin-tinggal-terbatas', dashboard_views.izin_tinggal_terbatas, name='izin_tinggal_terbatas'),
    path('dashboard/izin-masuk-kembali', dashboard_views.izin_masuk_kembali, name='izin_masuk_kembali'),
    path('dashboard/izin-tinggal-tetap', dashboard_views.izin_tinggal_tetap, name='izin_tinggal_tetap'),
    path('dashboard/alih-status-izin-tinggal', dashboard_views.alih_status_izin_tinggal, name='alih_status_izin_tinggal'),
    path('dashboard/perubahan-alamat', dashboard_views.perubahan_alamat, name='perubahan_alamat'),
    path('dashboard/pendaftaran-anak', dashboard_views.pendaftaran_anak, name='pendaftaran_anak'),
    path('dashboard/add-layanan-imigarsi', dashboard_views.add_layanan_imigrasi, name='add_layanan_imigrasi'),
    path('dashboard/update-layanan-imigrasi/<int:pk>', dashboard_views.update_layanan_imigrasi, name='update_layanan_imigrasi'),
    path('dashboard/add-layanan-imigarsi', dashboard_views.add_layanan_imigrasi, name='add_layanan_imigrasi'),
    path('dashboard/update-layanan-imigrasi/<int:pk>', dashboard_views.update_layanan_imigrasi, name='update_layanan_imigrasi'),
    # biaya keimigrasian
    path('dashboard/dokumen-perjalanan-republik-indonesia', dashboard_views.dokumen_perjalanan_republik_indonesia, name='dokumen_perjalanan_republik_indonesia'),
    path('dashboard/visa-kunjungan', dashboard_views.visa_kunjungan, name='visa_kunjungan'),
    path('dashboard/visa-tinggal-terbatas', dashboard_views.visa_tinggal_terbatas, name='visa_tinggal_terbatas'),
    path('dashboard/izin-kunjungan', dashboard_views.izin_kunjungan, name='izin_kunjungan'),
    path('dashboard/izin-tinggal-tetap-keimigrasian', dashboard_views.izin_tinggal_tetap_keimigrasian, name='izin_tinggal_tetap_keimigrasian'),
    path('dashboard/izin-masuk-kembali-keimigrasian', dashboard_views.izin_masuk_kembali_keimigrasian, name='izin_masuk_kembali_keimigrasian'),
    path('dashboard/izin-tinggal-terbatas-keimigrasian', dashboard_views.izin_tinggal_terbatas_keimigrasian, name='izin_tinggal_terbatas_keimigrasian'),
    path('dashboard/biaya-beban', dashboard_views.biaya_beban, name='biaya_beban'),
    path('dashboard/smart-card', dashboard_views.smart_card, name='smart_card'),
    path('dashboard/kartu-perjalanan-bisnis', dashboard_views.kartu_perjalanan_bisnis, name='kartu_perjalanan_bisnis'),
    path('dashboard/fasilitasi-keimigrasian', dashboard_views.fasilitas_keimigrasian, name='fasilitas_keimigrasian'),
    path('dashboard/surat-keterangan-keimigrasian', dashboard_views.surat_keterangan_keimigrasian, name='surat_keterangan_keimigrasian'),
    # zona integritas
    path('dashboard/pengertian', dashboard_views.pengertian, name='pengertian'),
    path('dashboard/area-perubahan', dashboard_views.area_perubahan, name='area_perubahan'),
    path('dashboard/dokumentasi-kegiatan-pzi', dashboard_views.dokumentasi_kegiatan_pzi, name='dokumentasi_kegiatan_pzi'),
    # ppid
    path('dashboard/dasar-hukum-ppid', dashboard_views.dasar_hukum_ppid, name='dasar_hukum_ppid'),
    path('dashboard/sk-penetapan-ppid', dashboard_views.sk_penetapan_ppid, name='sk_penetapan_ppid'),
    path('dashboard/struktur-ppid', dashboard_views.struktur_ppid, name='struktur_ppid'),
    path('dashboard/tugas-dan-fungsi-ppid', dashboard_views.tugas_dan_fungsi_ppid, name='tugas_dan_fungsi_ppid'),
    path('dashboard/standar-pelayanan-informasi', dashboard_views.standar_pelayanan_informasi, name='standar_pelayanan_informasi'),
    path('dashboard/kegiatan-tata-kelola-informasi-publikn', dashboard_views.kegiatan_tata_kelola_informasi_publik, name='kegiatan_tata_kelola_informasi_publik'),
    path('dashboard/sk-informasi-yang-dikecualikan', dashboard_views.sk_informasi_yang_dikecualikan, name='sk_informasi_yang_dikecualikan'),
    path('dashboard/daftar-informasi-publik', dashboard_views.daftar_informasi_publik, name='daftar_informasi_publik'),
    path('dashboard/informasi-berkala', dashboard_views.informasi_berkala, name='informasi_berkala'),
    path('dashboard/informasi-setiap-saat', dashboard_views.informasi_setiap_saat, name='informasi_setiap_saat'),
    path('dashboard/informasi-serta-merta', dashboard_views.informasi_serta_merta, name='informasi_serta_merta'),
    path('dashboard/informasi-dikecualikan', dashboard_views.informasi_dikecualikan, name='informasi_dikecualikan'),
    path('dashboard/profile-ppid', dashboard_views.profile_ppid, name='profile_ppid'),
    path('dashboard/form-permintaan-informasi-dan-pernyataan-kebenaran', dashboard_views.form_permintaan_informasi_dan_pernyataan_kebenaran, name='form_permintaan_informasi_dan_pernyataan_kebenaran'),
    
    path('dashboard/add-content', dashboard_views.add_content, name='add_content'),
    path('dashboard/update-content/<int:pk>', dashboard_views.update_content, name='update_content'),
    path('dashboard/logout/', dashboard_views.logout_dashboard, name="logout_dashboard"),
    
    # arsip dan dokumen
    path('dashboard/daftar-isian-pelaksana-anggaran', dashboard_views.daftar_isian_pelaksana_anggaran, name='daftar_isian_pelaksana_anggaran'),
    path('dashboard/laporan-akuntabilitas-kinerja', dashboard_views.laporan_akuntabilitas_kinerja, name='laporan_akuntabilitas_kinerja'),
    path('dashboard/timpora', dashboard_views.timpora, name='timpora'),
    path('dashboard/file-informasi-berkala', dashboard_views.file_informasi_berkala, name='file_informasi_berkala'),
    path('dashboard/add-file', dashboard_views.add_file, name='add_file'),
    path('dashboard/update-file/<int:pk>', dashboard_views.update_file, name='update_file'),
    path('dashboard/delete-file/<int:pk>', dashboard_views.delete_file, name='delete_file'),
    
    # profile
    path('dashboard/sejarah-imigrasi', dashboard_views.sejarah_imigrasi, name='sejarah_imigrasi'),
    path('dashboard/sejarah-kantor', dashboard_views.sejarah_kantor, name='sejarah_kantor'),
    path('dashboard/tugas-dan-fungsi-profile', dashboard_views.tugas_dan_fungsi_profile, name='tugas_dan_fungsi_profile'),
    
    # galeri
    path('dashboard/foto', dashboard_views.show_foto, name='show_foto'),
    path('dashboard/video', dashboard_views.show_video, name='show_video'),
    path('dashboard/add-foto', dashboard_views.add_foto, name='add_foto'),
    path('dashboard/update-foto/<int:pk>', dashboard_views.update_foto, name='update_foto'),
    path('dashboard/delete-foto/<int:pk>', dashboard_views.delete_foto, name='delete_foto'),
    path('dashboard/add-video', dashboard_views.add_video, name='add_video'),
    path('dashboard/update-video/<int:pk>', dashboard_views.update_video, name='update_video'),
    path('dashboard/delete-video/<int:pk>', dashboard_views.delete_video, name='delete_video'),
    
    #berita
    path('dashboard/kantor-imigrasi', dashboard_views.kantor_imigrasi, name='kantor_imigrasi_cilegon'),
    path('dashboard/kemenkumham-republik-indonesia', dashboard_views.kemenkumham_republik_indonesia, name='kemenkumham_republik_indonesia'),
    path('dashboard/kemenkumham-kanwil-banten', dashboard_views.kemenkumham_kanwil_banten, name='kemenkumham_kanwil_banten'),
    path('dashboard/add-berita', dashboard_views.add_berita, name='add_berita'),
    path('dashboard/update-berita/<int:pk>', dashboard_views.update_berita, name='update_berita'),
    path('dashboard/delete-berita/<int:pk>', dashboard_views.delete_berita, name='delete_berita'),
    path('dashboard/add-berita-image', dashboard_views.add_berita_image, name='add_berita_image'),
    path('dashboard/update-berita-image/<int:pk>', dashboard_views.update_berita_image, name='update_berita_image'),
    path('dashboard/delete-berita-image/<int:pk>', dashboard_views.delete_berita_image, name='delete_berita_image'),
    
    #ipkdanipm
    path('dashboard/ipk-dan-ipm', dashboard_views.ipk_dan_ipm, name='ipk_dan_ipm'),
    path('dashboard/delete-ipk-dan-ipm/<int:pk>', dashboard_views.delete_ipk_dan_ipm, name='delete_ipk_dan_ipm'),
    path('dashboard/update-data-survey-ipk-dan-ipm/<int:pk>', dashboard_views.update_data_survey_ipk_dan_ipm, name='update_data_survey_ipk_dan_ipm'),
    path('dashboard/add-ipk-dan-ipm', dashboard_views.add_ipk_dan_ipm, name='add_ipk_dan_ipm'),
]