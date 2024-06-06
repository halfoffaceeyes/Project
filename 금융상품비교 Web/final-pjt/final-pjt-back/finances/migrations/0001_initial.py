# Generated by Django 4.2.13 on 2024-05-20 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdt_category', models.CharField(max_length=10)),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('finance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.finance')),
            ],
        ),
    ]
