# Generated by Django 3.2.3 on 2022-12-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0006_addsturesult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addsturesult',
            name='student_id',
            field=models.CharField(max_length=255),
        ),
    ]
