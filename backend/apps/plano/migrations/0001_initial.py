# Generated by Django 2.2.1 on 2019-05-08 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def carga(apps, schema_editor):
    
    plans = [
        {
            'title': 'Mensal',
            'price': 15.00,
        },
        {
            'title': 'Bimestral',
            'price': 35.00,
        },
        {
            'title': 'Trimestral',
            'price': 45.00,
        }
    ]

    for plan in plans:
        TypePlans = apps.get_model('plano', 'Plano')()
        TypePlans.title = plan['title']
        TypePlans.price = plan['price']
        TypePlans.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('type_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.Plano')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(carga),
    ]