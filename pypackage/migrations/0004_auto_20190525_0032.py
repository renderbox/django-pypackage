# Generated by Django 2.1.8 on 2019-05-25 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pypackage', '0003_auto_20190524_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='requires_python',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='version',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='pypackage.Package'),
        ),
    ]
