# Generated by Django 4.0.10 on 2023-11-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_review_alter_vacancy_model_pic_alter_vacancy_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='body',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='accommodation',
            field=models.TextField(blank=True, null=True, verbose_name='Проживание'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='additional_text',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='nutrition',
            field=models.TextField(blank=True, null=True, verbose_name='Питание'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='requirement_text',
            field=models.TextField(blank=True, null=True, verbose_name='Требования'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='responsibility_text',
            field=models.TextField(blank=True, null=True, verbose_name='Обязанности'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='schedule',
            field=models.TextField(blank=True, null=True, verbose_name='График работы'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='working_condition_text',
            field=models.TextField(blank=True, null=True, verbose_name='Условия работы'),
        ),
    ]