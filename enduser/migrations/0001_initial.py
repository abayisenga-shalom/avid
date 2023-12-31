# Generated by Django 4.2.5 on 2023-09-14 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('agent_photo', models.ImageField(upload_to='agent_profile/')),
            ],
            options={
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(upload_to='properties/vehicles/')),
                ('image2', models.ImageField(upload_to='properties/vehicles/')),
                ('image3', models.ImageField(upload_to='properties/vehicles/')),
                ('image4', models.ImageField(upload_to='properties/vehicles/')),
                ('image5', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('image6', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('image8', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('image9', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('image10', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('image11', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('image12', models.ImageField(blank=True, upload_to='properties/vehicles/')),
                ('video_Url', models.CharField(blank=True, max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enduser.agent')),
            ],
            options={
                'verbose_name_plural': 'Vehicles',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('beds', models.CharField(max_length=20)),
                ('baths', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(upload_to='properties/rooms/')),
                ('image2', models.ImageField(upload_to='properties/rooms/')),
                ('image3', models.ImageField(upload_to='properties/rooms/')),
                ('image4', models.ImageField(upload_to='properties/rooms/')),
                ('image5', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('image6', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('image8', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('image9', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('image10', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('image11', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('image12', models.ImageField(blank=True, upload_to='properties/rooms/')),
                ('video_Url', models.CharField(blank=True, max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enduser.agent')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(upload_to='properties/lands/')),
                ('image2', models.ImageField(upload_to='properties/lands/')),
                ('image3', models.ImageField(upload_to='properties/lands/')),
                ('image4', models.ImageField(upload_to='properties/lands/')),
                ('image5', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('image6', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('image8', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('image9', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('image10', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('image11', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('image12', models.ImageField(blank=True, upload_to='properties/lands/')),
                ('video_Url', models.CharField(blank=True, max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enduser.agent')),
            ],
            options={
                'verbose_name_plural': 'Lands',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('beds', models.CharField(max_length=20)),
                ('baths', models.CharField(max_length=20)),
                ('garage', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(upload_to='properties/apartments/')),
                ('image2', models.ImageField(upload_to='properties/apartments/')),
                ('image3', models.ImageField(upload_to='properties/apartments/')),
                ('image4', models.ImageField(upload_to='properties/apartments/')),
                ('image5', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image6', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image8', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image9', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image10', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image11', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image12', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('video_Url', models.CharField(blank=True, max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enduser.agent')),
            ],
            options={
                'verbose_name_plural': 'Houses',
            },
        ),
        migrations.CreateModel(
            name='Commerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(upload_to='properties/commerces/')),
                ('image2', models.ImageField(upload_to='properties/commerces/')),
                ('image3', models.ImageField(upload_to='properties/commerces/')),
                ('image4', models.ImageField(upload_to='properties/commerces/')),
                ('image5', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('image6', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('image8', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('image9', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('image10', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('image11', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('image12', models.ImageField(blank=True, upload_to='properties/commerces/')),
                ('video_Url', models.CharField(blank=True, max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enduser.agent')),
            ],
            options={
                'verbose_name_plural': 'Commerces',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('beds', models.CharField(max_length=20)),
                ('baths', models.CharField(max_length=20)),
                ('garage', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(upload_to='properties/apartments/')),
                ('image2', models.ImageField(upload_to='properties/apartments/')),
                ('image3', models.ImageField(upload_to='properties/apartments/')),
                ('image4', models.ImageField(upload_to='properties/apartments/')),
                ('image5', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image6', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image8', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image9', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image10', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image11', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('image12', models.ImageField(blank=True, upload_to='properties/apartments/')),
                ('video_Url', models.CharField(blank=True, max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enduser.agent')),
            ],
            options={
                'verbose_name_plural': 'Apartments',
            },
        ),
    ]
