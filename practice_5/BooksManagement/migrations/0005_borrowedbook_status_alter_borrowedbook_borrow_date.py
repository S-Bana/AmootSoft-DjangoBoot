# Generated by Django 5.1.1 on 2024-09-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksManagement', '0004_borrowedbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='status',
            field=models.CharField(default='borrowed', max_length=10),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='borrow_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
