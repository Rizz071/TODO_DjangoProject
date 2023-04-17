# Generated by Django 4.2 on 2023-04-17 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.TextField()),
                ('order_num', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TODOlist_app.todotitle')),
            ],
        ),
    ]
