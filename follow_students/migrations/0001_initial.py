# Generated by Django 4.2.5 on 2023-10-08 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadNoAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Beca',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('estudiantes_asignados', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('icfes', models.IntegerField()),
                ('cedula', models.CharField(max_length=20)),
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('correo', models.EmailField(max_length=254)),
                ('aux_transportation', models.CharField(default=0, max_length=100)),
                ('aux_academic', models.CharField(default=0, max_length=100)),
                ('beca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='follow_students.beca')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Montos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transporte', models.IntegerField()),
                ('alimentacion', models.IntegerField()),
                ('academico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroActividadEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_asistencia', models.CharField(max_length=100)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.actividadnoacademica')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Gasto_beca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_dinero', models.FloatField()),
                ('tiempo_acumulado', models.IntegerField()),
                ('tiempo_seleccionado', models.CharField(choices=[('1', 'Dias'), ('2', 'Mes'), ('3', 'Año')], default='1', max_length=2)),
                ('tipo', models.CharField(max_length=20)),
                ('beca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follow_students.beca')),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follow_students.estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.major'),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('motivo', models.TextField()),
                ('resultado', models.TextField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='beca',
            name='donante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.donante'),
        ),
        migrations.AddField(
            model_name='beca',
            name='montos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.montos'),
        ),
    ]
