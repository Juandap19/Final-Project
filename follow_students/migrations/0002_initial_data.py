from django.db import migrations

def create_permisos(apps, schema_editor):
    Permiso = apps.get_model('follow_students', 'Permiso')
    permisos = ['Panel de control', 'Registrar estudiante', 'Gestionar estudiante', 'Generar reporte', 'Cargar informacion DP', 'Cargar informacion BU', 'Cargar informacion CREA', 'Pedir Actualizacion de Informacion', 'Pago Alimentacion' ,'Pago Academico' , 'Pago Transporte']
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
        {'rol': 'Apoyo Financiero', 'permisos': ['Pago Alimentacion' ,'Pago Academico' , 'Pago Transporte' ]}
    ]

    for rol_permiso in rol_permisos:
        rol = Rol.objects.get(nombre_rol=rol_permiso['rol'])
        for permiso_nombre in rol_permiso['permisos']:
            permiso = Permiso.objects.get(nombre_permiso=permiso_nombre)
            RolPermiso.objects.create(rol=rol, permiso=permiso)

def create_non_academic_activities(apps, schema_editor):
    NonAcademicActivity = apps.get_model('follow_students', 'NonAcademicActivity')
    activities = ['Fútbol', 'Futbol Femenino', 'Futsal', 'Baloncesto', 'Voleibol', 'Atletismo', 'Natación', 'Ajedrez', 'Ultimate']

    for activity in activities:
            NonAcademicActivity.objects.create(name=activity)
            
def create_supportCenter(apps, schema_editor):
    SupportCenter = apps.get_model('follow_students', 'SupportCenter')
    
    centers = [
        {'name': 'Cambas'},
        {'name': 'EL Center'},
        {'name': 'Centreo Leo'}
    ]
    
    for center in centers:
        SupportCenter.objects.create(name=center['name'])
    

def create_majors(apps, schema_editor):
    Major = apps.get_model('follow_students', 'Major')

    majors = [
        {'name': 'Administración de Empresas con énfasis en Negocios Internacionales', 'price': 13340000},
        {'name': 'Economía y Negocios Internacionales', 'price': 13340000},
        {'name': 'Mercadeo Internacional y Publicidad', 'price': 13340000},
        {'name': 'Finanzas', 'price': 13340000},
        {'name': 'Ingeniería Bioquímica', 'price': 12730000},
        {'name': 'Ingeniería Industrial', 'price': 13340000},
        {'name': 'Ingeniería de Sistemas', 'price': 12730000},
        {'name': 'Ingeniería Telemática', 'price': 12730000},
        {'name': 'Diseño de Medios Interactivos', 'price': 12730000},
        {'name': 'Diseño Industrial', 'price': 13340000},
        {'name': 'Biología con concentraciones en Conservación y Biología Molecular/Biotecnología', 'price': 11250000},
        {'name': 'Química con énfasis en Bioquímica', 'price': 11250000},
        {'name': 'Química Farmacéutica', 'price': 12260000},
        {'name': 'Derecho', 'price': 12730000},
        {'name': 'Antropología', 'price': 10110000},
        {'name': 'Psicología', 'price': 11250000},
        {'name': 'Sociología', 'price': 10110000},
        {'name': 'Ciencia Política con énfasis en Relaciones Internacionales', 'price': 10110000},
        {'name': 'Música', 'price': 12730000},
        {'name': 'Comunicación', 'price': 11250000},
        {"name": "Licenciatura en Educación Básica Primaria", "price": 9380000},
        {"name": "Licenciatura en Lenguas Extranjeras con énfasis Inglés", "price": 9380000},
        {"name": "Licenciatura en Artes", "price": 9380000},
        {"name": "Licenciatura en Literatura y Lengua Castellana", "price": 9380000},
        {"name": "Licenciatura en Ciencias Sociales", "price": 9380000},
        {"name": "Licenciatura en Ciencias Naturales", "price": 9380000}
    ]


    for major in majors:
        Major.objects.create(name=major['name'], price=major['price'])


class Migration(migrations.Migration):

    dependencies = [
        ('follow_students', '0001_initial'),  # replace with your dependency
    ]

    operations = [
        migrations.RunPython(create_permisos),
        migrations.RunPython(create_rol),
        migrations.RunPython(create_rol_permiso),
        migrations.RunPython(create_majors),
        migrations.RunPython(create_supportCenter),
        migrations.RunPython(create_non_academic_activities)
    ]

