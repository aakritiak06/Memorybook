# Generated by Django 3.1.7 on 2021-03-24 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Generaldetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepicurl', models.TextField(default='-')),
                ('profilepicname', models.TextField(default='-')),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Problem_reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('details', models.TextField(default='-')),
            ],
        ),
        migrations.CreateModel(
            name='Wallmessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('color', models.TextField(default='orange', null=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField(blank=True)),
                ('Branch', models.CharField(max_length=100, null=True)),
                ('Summary', models.TextField(blank=True, default='-')),
                ('Mobile', models.CharField(blank=True, max_length=16, null=True)),
                ('Website', models.CharField(blank=True, max_length=100, null=True)),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('general', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.generaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_format', models.BooleanField(null=True)),
                ('thought', models.TextField(default='-')),
                ('picurl', models.TextField(default='-')),
                ('picname', models.TextField(default='-')),
                ('videourl', models.TextField(default='-')),
                ('videoname', models.TextField(default='-')),
                ('comment_num', models.IntegerField(default=0)),
                ('love_num', models.IntegerField(default=0)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likeusr', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likedpost', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.TextField(default='-')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cmntusr', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cmntpost', to='main.post')),
                ('usr_det', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='det', to='main.generaldetails')),
            ],
        ),
    ]
