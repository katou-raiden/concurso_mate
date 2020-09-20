# Generated by Django 2.2 on 2020-09-20 15:26

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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', null=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_mod', models.DateTimeField(auto_now=True)),
                ('votes_plus', models.IntegerField(default=0)),
                ('votes_minus', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_mod', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(default='', null=True)),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='forum.Tag')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', null=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_mod', models.DateTimeField(auto_now=True)),
                ('votes_plus', models.IntegerField(default=0)),
                ('votes_minus', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.Answer')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.Post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forum.Post'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
