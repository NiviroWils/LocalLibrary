# Generated by Django 4.2.7 on 2023-11-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_bookinstance_options_bookinstance_borrower_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(help_text='Enter a language of the book', max_length=200)),
            ],
        ),
    ]
