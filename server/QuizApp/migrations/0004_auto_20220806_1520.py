# Generated by Django 3.2.6 on 2022-08-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0003_remove_answer_updated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='updated_date',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='answer',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Answer Text'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('B', 'BEGINNER'), ('I', 'INTERMADIATE'), ('A', 'ADVANCED')], max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Quiz Title'),
        ),
    ]
