# Generated by Django 4.2.1 on 2023-05-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_filearsipdandokumen_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisiDanMisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visi', models.CharField(max_length=200)),
                ('misi', models.CharField(max_length=200)),
                ('moto_1', models.CharField(max_length=50)),
                ('moto_2', models.CharField(max_length=50)),
                ('moto_3', models.CharField(max_length=50)),
                ('tata_nilai_profesional', models.CharField(max_length=300)),
                ('tata_nilai_akuntabel', models.CharField(max_length=300)),
                ('tata_nilai_sinergi', models.CharField(max_length=300)),
                ('tata_nilai_transparan', models.CharField(max_length=300)),
                ('tata_nilai_inovarif', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='filearsipdandokumen',
            name='category',
            field=models.CharField(choices=[('DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN', 'DAFTAR_ISIAN_PELAKSANAAN_ANGGARAN'), ('TIMPORA', 'TIMPORA'), ('LAPORAN_AKUNTABILITAS_KINERJA', 'LAPORAN_AKUNTABILITAS_KINERJA'), ('INFORMASI_BERKALA', 'INFORMASI_BERKALA')], max_length=50),
        ),
    ]
