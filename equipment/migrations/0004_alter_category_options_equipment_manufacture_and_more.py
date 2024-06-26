# Generated by Django 4.2.1 on 2023-12-13 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_servicecenters_alter_equipmentmanufacturer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Тип оборудования', 'verbose_name_plural': 'Тип оборудования'},
        ),
        migrations.AddField(
            model_name='equipment',
            name='manufacture',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipment.equipmentmanufacturer', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='В наличие'),
        ),
        migrations.AlterField(
            model_name='filtervalue',
            name='value',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Параметр фильтра:'),
        ),
        migrations.AlterField(
            model_name='namefilter',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название параметра фильтра:'),
        ),
        migrations.AlterField(
            model_name='servicecenters',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Сервисные центры:'),
        ),
    ]
