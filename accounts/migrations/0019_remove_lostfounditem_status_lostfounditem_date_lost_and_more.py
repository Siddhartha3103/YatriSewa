# Generated by Django 5.1.1 on 2024-11-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_founditem_lostitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostfounditem',
            name='status',
        ),
        migrations.AddField(
            model_name='lostfounditem',
            name='date_lost',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AddField(
            model_name='lostfounditem',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='lostfounditem',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='founditem',
            name='contact_info',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='founditem',
            name='date_found',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AlterField(
            model_name='founditem',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='founditem',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='founditem',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lostfounditem',
            name='contact_info',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lostfounditem',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='contact_info',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='date_lost',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]