# Generated by Django 4.2.2 on 2024-06-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_internshipresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipresponse',
            name='completion_certificate_submitted',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='internshipresponse',
            name='offer_letter_submitted',
            field=models.TextField(default=None),
        ),
    ]