# Generated by Django 2.2.6 on 2019-11-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='moment',
            name='kind',
            field=models.CharField(choices=[('python技术', 'python技术'), ('数据库技术', '数据库技术'), ('经济学', '经济学'), ('文体资讯', '文体资讯'), ('个人心情', '个人心情'), ('其他', '其他')], default=('python技术', 'python技术'), max_length=20),
        ),
        migrations.AlterField(
            model_name='moment',
            name='user_name',
            field=models.CharField(default='匿名', max_length=20),
        ),
    ]
