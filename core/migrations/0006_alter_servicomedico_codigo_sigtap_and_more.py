# Generated migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_cirurgia_tipo_cirurgia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicomedico',
            name='codigo_sigtap',
            field=models.CharField(blank=True, help_text='Ex: 03.01.01.007-5', max_length=20, null=True, verbose_name='Código SIGTAP'),
        ),
        migrations.AlterField(
            model_name='servicomedico',
            name='descricao',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servicomedico',
            name='valor',
            field=models.DecimalField(decimal_places=2, help_text='Valor unitário do serviço em reais', max_digits=10, verbose_name='Valor Unitário (R$)'),
        ),
    ]
