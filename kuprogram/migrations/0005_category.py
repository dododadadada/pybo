# Generated by Django 4.0.3 on 2022-08-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuprogram', '0004_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
