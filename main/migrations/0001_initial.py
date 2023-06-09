# Generated by Django 4.2.1 on 2023-05-28 23:39

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_berita', models.CharField(choices=[('KANTOR_IMIGRASI_CILEGON', 'KANTOR_IMIGRASI_CILEGON'), ('KEMENKUMHAM_REPUBLIK_INDONESIA', 'KEMENKUMHAM_REPUBLIK_INDONESIA'), ('KEMENKUMHAM_KANWIL_BANTEN', 'KEMENKUMHAM_KANWIL_BANTEN')], max_length=30)),
                ('berita_title', models.CharField(max_length=100)),
                ('berita_descrition', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileArsipDanDokumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN', 'DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN'), ('LAPORAN_AKUNTABILITAS_KINERJA', 'LAPORAN_AKUNTABILITAS_KINERJA')], max_length=50)),
                ('file_name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='files/')),
                ('file_added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FotoGaleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galeri_image_file', models.ImageField(upload_to='foto/')),
                ('descripion_image', models.CharField(max_length=200)),
                ('image_added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_menu_name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('main_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mainmenu')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.menu')),
                ('content_name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category_content', models.CharField(choices=[('LAYANAN_IMIGRASI', 'LAYANAN_IMIGRASI'), ('STANDAR', 'STANDAR')], max_length=50)),
                ('tentang_layanan_dan_persyaratan', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('alur_proses_dan_prosedur', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('biaya', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submenu_name', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('permalink', models.CharField(max_length=50)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menu')),
            ],
        ),
        migrations.CreateModel(
            name='BeritaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('berita_image_file', models.ImageField(upload_to='berita/')),
                ('image_added_at', models.DateTimeField(auto_now_add=True)),
                ('berita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joni', to='main.berita')),
            ],
        ),
    ]
