# Generated by Django 4.0.6 on 2022-07-17 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafelike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cafeimage',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafes.cafe'),
        ),
        migrations.AddField(
            model_name='cafeflag',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafes.cafe'),
        ),
        migrations.AddField(
            model_name='cafeflag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cafecomplexity',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafes.cafe'),
        ),
        migrations.AddField(
            model_name='cafecomplexity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cafe',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafes.addresslevelthree'),
        ),
        migrations.AddField(
            model_name='addressleveltwo',
            name='super_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafes.addresslevelone'),
        ),
        migrations.AddField(
            model_name='addresslevelthree',
            name='super_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafes.addressleveltwo'),
        ),
        migrations.AddConstraint(
            model_name='cafe',
            constraint=models.UniqueConstraint(fields=('name', 'detail_address'), name='unique cafes'),
        ),
    ]
