# Generated by Django 4.2.1 on 2023-12-13 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FilterValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NameFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='equipment.category', verbose_name='Категория: '),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Image: '),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='tar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts_p', to='equipment.target', verbose_name='Назначение: '),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Модель оборудования: '),
        ),
    ]