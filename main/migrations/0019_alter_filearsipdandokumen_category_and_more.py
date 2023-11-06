# Generated by Django 4.2.5 on 2023-11-04 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_filearsipdandokumen_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filearsipdandokumen',
            name='category',
            field=models.CharField(choices=[('DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN', 'DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN'), ('LAPORAN_AKUNTABILITAS_KINERJA', 'LAPORAN_AKUNTABILITAS_KINERJA'), ('TIMPORA', 'TIMPORA'), ('INFORMASI_BERKALA', 'INFORMASI_BERKALA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='indexsurvey',
            name='variable',
            field=models.CharField(choices=[('INFORMASI', 'informasi'), ('PERSYARATAN', 'persyaratan'), ('PROSEDUR_ATAU_ALUR', 'prosedur atau alur'), ('WAKTU_PENYELESAIAN', 'waktu penyelesaian'), ('TARIF_BIAYA', 'tarif biaya'), ('SARANA_PRASARANA', 'sarana prasarana'), ('RESPON', 'respon'), ('KONSULTASI_DAN_PENGADUAN', 'konsultasi dan pengaduan'), ('DISKRIMINASI', 'diskriminasi'), ('KECURANGAN', 'kecurangan'), ('GRATIFIKASI', 'gratifikasi'), ('PUNGLI', 'pungli'), ('CALO', 'calo')], max_length=30),
        ),
    ]
