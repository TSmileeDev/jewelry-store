# Generated by Django 5.0.1 on 2024-01-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201221_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Mới', 'Mới'), ('Chấp nhận', 'Chấp nhận'), ('Đang chuẩn bị', 'Đang chuẩn bị'), ('Đang Ship', 'Đang Ship'), ('Hoàn Thành', 'Hoàn Thành'), ('Đã hủy', 'Đã hủy')], default='Mới', max_length=15),
        ),
    ]
