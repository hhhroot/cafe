# Generated by Django 4.0.6 on 2022-07-19 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0003_alter_cafecomplexity_cafe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeflag',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='cafes.cafe'),
        ),
        migrations.AlterField(
            model_name='cafelike',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='cafes.cafe'),
        ),
    ]
