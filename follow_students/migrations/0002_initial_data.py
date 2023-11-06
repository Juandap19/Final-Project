# Generated by Django 4.2.5 on 2023-10-16 21:26

from django.db import migrations

def create_permisos(apps, schema_editor):
    Permiso = apps.get_model('follow_students', 'Permiso')
    permisos = ['Panel de control', 'Registrar estudiante', 'Gestionar estudiante', 'Generar reporte', 'Cargar informacion DP', 'Cargar informacion BU', 'Cargar informacion CREA', 'Pedir Actualizacion de Informacion', 'Pagos']
    for permiso in permisos:
        Permiso.objects.create(nombre_permiso=permiso)
        
def create_rol(apps, schema_editor):
    Permiso = apps.get_model('follow_students', 'Rol')
    roles = ['Filantropía', 'Director de Programa', 'Bienestar Universitario', 'CREA', 'Apoyo Financiero']
    for rol in roles:
        Permiso.objects.create(nombre_rol=rol)
        
def create_rol_permiso(apps, schema_editor):
    RolPermiso = apps.get_model('follow_students', 'RolPermiso')
    Rol = apps.get_model('follow_students', 'Rol')
    Permiso = apps.get_model('follow_students', 'Permiso')

    rol_permisos = [
        {'rol': 'Filantropía', 'permisos': ['Panel de control', 'Registrar estudiante', 'Gestionar estudiante', 'Generar reporte', 'Pedir Actualizacion de Informacion']},
        {'rol': 'Director de Programa', 'permisos': ['Cargar informacion DP']},
        {'rol': 'Bienestar Universitario', 'permisos': ['Cargar informacion BU']},
        {'rol': 'CREA', 'permisos': ['Cargar informacion CREA']},
        {'rol': 'Apoyo Financiero', 'permisos': ['Pagos']}
    ]

    for rol_permiso in rol_permisos:
        rol = Rol.objects.get(nombre_rol=rol_permiso['rol'])
        for permiso_nombre in rol_permiso['permisos']:
            permiso = Permiso.objects.get(nombre_permiso=permiso_nombre)
            RolPermiso.objects.create(rol=rol, permiso=permiso)

def create_actividades_no_academicas(apps, schema_editor):
    ActividadNoAcademica = apps.get_model('follow_students', 'ActividadNoAcademica')
    actividades = ['Fútbol', 'Futbol Femenino', 'Futsal', 'Baloncesto', 'Voleibol', 'Atletismo', 'Natación', 'Ajedrez', 'Ultimate']

    for actividad in actividades:
        ActividadNoAcademica.objects.create(nombre=actividad)
        
def create_majors(apps, schema_editor):
    Major = apps.get_model('follow_students', 'Major')

    # Aquí puedes definir las carreras que quieras crear
    majors = [
        {'nombre': 'Administración de Empresas con énfasis en Negocios Internacionales', 'precio': 13340000},
        {'nombre': 'Economía y Negocios Internacionales', 'precio': 13340000},
        {'nombre': 'Mercadeo Internacional y Publicidad', 'precio': 13340000},
        {'nombre': 'Finanzas', 'precio': 13340000},
        {'nombre': 'Ingeniería Bioquímica', 'precio': 12730000},
        {'nombre': 'Ingeniería Industrial', 'precio': 13340000},
        {'nombre': 'Ingeniería de Sistemas', 'precio': 12730000},
        {'nombre': 'Ingeniería Telemática', 'precio': 12730000},
        {'nombre': 'Diseño de Medios Interactivos', 'precio': 12730000},
        {'nombre': 'Diseño Industrial', 'precio': 13340000},
        {'nombre': 'Biología con concentraciones en Conservación y Biología Molecular/Biotecnología', 'precio': 11250000},
        {'nombre': 'Química con énfasis en Bioquímica', 'precio': 11250000},
        {'nombre': 'Química Farmacéutica', 'precio': 12260000},
        {'nombre': 'Derecho', 'precio': 12730000},
        {'nombre': 'Antropología', 'precio': 10110000},
        {'nombre': 'Psicología', 'precio': 11250000},
        {'nombre': 'Sociología', 'precio': 10110000},
        {'nombre': 'Ciencia Política con énfasis en Relaciones Internacionales', 'precio': 10110000},
        {'nombre': 'Música', 'precio': 12730000},
        {'nombre': 'Comunicación', 'precio': 11250000},
        {'nombre': "Licenciatura en Educación Básica Primaria", "precio":9380000 },
        {"nombre": "Licenciatura en Lenguas Extranjeras con énfasis Inglés", "precio":9380000 },
        {"nombre": "Licenciatura en Artes", "precio":9380000 },
        {"nombre": "Licenciatura en Literatura y Lengua Castellana", "precio":9380000 },
        {"nombre": "Licenciatura en Ciencias Sociales", "precio":9380000 },
        {"nombre": "Licenciatura en Ciencias Naturales", "precio":9380000 }
    ]

    for major in majors:
        Major.objects.create(nombre=major['nombre'], precio=major['precio'])


class Migration(migrations.Migration):

    dependencies = [
        ('follow_students', '0001_initial'),  # replace with your dependency
    ]

    operations = [
        # migrations.RunPython(create_permisos),
        # migrations.RunPython(create_rol),
        # migrations.RunPython(create_rol_permiso),
        # migrations.RunPython(create_actividades_no_academicas),
        # migrations.RunPython(create_majors)
    ]
