# Generated by Django 4.2.6 on 2023-10-16 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_alter_vuelo_destino_alter_vuelo_origen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('ciudad', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='llegadas', to='flights.aeropuerto'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='flights.aeropuerto'),
        ),
    ]
