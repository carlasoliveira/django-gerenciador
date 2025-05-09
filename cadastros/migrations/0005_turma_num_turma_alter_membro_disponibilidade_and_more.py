# Generated by Django 4.2.20 on 2025-04-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_atualizacaomembro_options_membro_observacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='num_turma',
            field=models.IntegerField(default=0, unique=True, verbose_name='número da turma'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='disponibilidade',
            field=models.ManyToManyField(to='cadastros.disponibilidade', verbose_name='disponibilidade'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=100, verbose_name='nome da mãe'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=100, verbose_name='nome do pai'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='resumo',
            field=models.TextField(blank=True, max_length=300, verbose_name='resumo'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='sacramentos',
            field=models.CharField(choices=[('B', 'Somente o Batismo'), ('E', 'Somente a Eucaristia'), ('BE', 'Batismo e Eucaristia'), ('T', 'Todos concluídos')], default='T', max_length=2, verbose_name='Sacramentos de Iniciação Cristã'),
        ),
    ]
