from django.db import migrations
from django.core.management.base import BaseCommand
from faker import Faker
from follow_students.models import Student, Major, Scholarship, Rol, User, Donor, Amount
import random
from datetime import datetime, timedelta

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

def create_users(apps, schema_editor):
    User = apps.get_model('follow_students', 'User')
    Rol = apps.get_model('follow_students', 'Rol')

    users_data = [
        {'username': 'diego', 'password': '1234', 'name': 'Diego Mueses', 'rol': 'Filantropía'},
        {'username': 'daniel', 'password': '1234', 'name': 'Daniel Montezuma', 'rol': 'Director de Programa'},
        {'username': 'felipe', 'password': '1234', 'name': 'Juan Felipe', 'rol': 'Bienestar Universitario'},
        {'username': 'darwin', 'password': '1234', 'name': 'Darwin Lenis', 'rol': 'CREA'},
        {'username': 'patiño', 'password': '1234', 'name': 'Juan David', 'rol': 'Apoyo Financiero'},
    ]

    for user_data in users_data:
        rol_name = user_data['rol']
        rol = Rol.objects.get(nombre_rol=rol_name)
        User.objects.create(
            username=user_data['username'],
            password=user_data['password'],
            name=user_data['name'],
            rol=rol
    )

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

   


def create_scholarships(apps, schema_editor):
        
        Donor = apps.get_model('follow_students', 'Donor')
        Amount = apps.get_model('follow_students', 'Amount')
        Scholarship = apps.get_model('follow_students', 'Scholarship')


        donors_data = [
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Fundacion', 'mail': f'tq@gmail.com', 'description': f'Empresa Fundacion valle del lili'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Emcali', 'mail': f'em@gmail.com', 'description': f'Empresa Emcali'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Icetex', 'mail': f'icetex@gmail.com', 'description': f'Empresa Icetex'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Colanta', 'mail': f'ct@gmail.com', 'description': f'Empresa Colanta'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Davivienda', 'mail': f'dv@gmail.com', 'description': f'Empresa Davivienda'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Bancolombia', 'mail': f'bc@gmail.com', 'description': f'Empresa Bancolombia'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'BBVA', 'mail': f'bbva@gmail.com', 'description': f'Empresa BBVA'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Gobierno', 'mail': f'ps@gmail.com', 'description': f'Empresa Gobierno de la Republica'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'JGB', 'mail': f'jgb@gmail.com', 'description': f'Empresa Jorge Garcés Borrero'},
            {'cedula': f'NIT-{random.randint(100000000, 999999999)}', 'name': f'Icesi', 'mail': f'icesi1@gmail.com', 'description': f'Universidad Icesi'}
        ]

        amounts_data = [
            {'code': 1, 'transport': 5000000000, 'alimentation': 1000000000, 'academic': 200000000},
            {'code': 2, 'transport': 7000000000, 'alimentation': 2000000000, 'academic': 500000000},
            {'code': 3, 'transport': 4500000000, 'alimentation': 1500000000, 'academic': 250000000},
            {'code': 4, 'transport': 5750000000, 'alimentation': 3000000000, 'academic': 370000000},
            {'code': 5, 'transport': 9000000000, 'alimentation': 4000000000, 'academic': 800000000},
        ]

        donors = [Donor.objects.create(**donor_data) for donor_data in donors_data]
        amounts = [Amount.objects.create(**amount_data) for amount_data in amounts_data]

        for _ in range(25):
            nombre_nueva_beca = random.choice(donors).name
            image = f'{nombre_nueva_beca}.png'

            scholarship = Scholarship(
                code=random.randint(10000000, 99999999),
                name=f'Beca - {nombre_nueva_beca}',
                assigned_students=random.randint(0, 10),
                academic_percentage=random.randint(50, 100),
                transportation=random.randint(500000, 1000000),
                amount=random.choice(amounts),
                donor=random.choice(donors),
                image=image,  # Agregamos la imagen aquí
            )
            scholarship.save()

def create_students(apps, schema_editor):

    Student = apps.get_model('follow_students', 'Student')
    Major = apps.get_model('follow_students', 'Major')
    Scholarship = apps.get_model('follow_students', 'Scholarship')
    Course = apps.get_model('follow_students', 'Course')
    Grade = apps.get_model('follow_students', 'Grade')

    majors = Major.objects.all()
    scholarships = Scholarship.objects.all()

    fake = Faker('es_CO')

    # Para crear un estudiante especifico para los test

    random_major = random.choice(majors)
    random_scholarships = random.choice(scholarships)
    full_name = "Juan Patiño"
    first_name, last_name = full_name.split(' ', 1)
    email = f"{first_name.lower()}{last_name.lower()}@gmail.com"
    student2 = Student(
            name=full_name,
            phoneNumber=fake.phone_number(),
            date=fake.date_of_birth(minimum_age=18, maximum_age=25),
            icfes=random.randint(280, 500),
            cedula="1107835369",
            code=f'A00381293',
            mail=email,
            aux_transportation= 0,
            aux_academic= 0,
            major=random_major,
            scholarship=random_scholarships
        )
    student2.save()

    course =  Course(
        code = "23",
        name = "Proyecto Papiro"
    )
    course.save()

    grade =  Grade(
        grade = 1.2,
        state =  True,
        course = course,
        student = student2
    )

    grade.save()

    courses_lst = [
        {'code': "1", 'name': "Matematicas Aplicadas II"},
        {'code': "2", 'name': "Proyecto Integrados"},
        {'code': "3", 'name': "Ingenieria de software III"},
        {'code': "4", 'name': "Arquitectura de Computadores"},
        {'code': "5", 'name': "Contabilidad y costos"},
    ]

    courses = [Course.objects.create(**courses_lst) for courses_lst in courses_lst]

    grades_lst = [
        {'grade': 3.8, 'state': True, 'course': courses[0], 'student': student2},
        {'grade': 4.8, 'state': True, 'course': courses[1], 'student': student2},
        {'grade': 4.4, 'state': True, 'course': courses[2], 'student': student2},
        {'grade': 3.5, 'state': True, 'course': courses[3], 'student': student2},
        {'grade': 4.1, 'state': True, 'course': courses[4], 'student': student2},
    ]

    grades = [Grade.objects.create(**grades_lst) for grades_lst in grades_lst]

    for _ in range(25):
        random_major = random.choice(majors)
        random_scholarships = random.choice(scholarships)
    
        full_name = fake.name()
        first_name, last_name = full_name.split(' ', 1)
    
        email = f"{first_name.lower()}{last_name.lower()}@gmail.com"
    
        student = Student(
            name=full_name,
            phoneNumber=fake.phone_number(),
            date=fake.date_of_birth(minimum_age=18, maximum_age=25),
            icfes=random.randint(280, 500),
            cedula=fake.unique.random_number(digits=10),
            code=f'A00{fake.unique.random_number(digits=6)}',
            mail=email,
            aux_transportation= 0,
            aux_academic= 0,
            major=random_major,
            scholarship=random_scholarships
        )
        student.save()

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
        migrations.RunPython(create_non_academic_activities),
        migrations.RunPython(create_users),
        migrations.RunPython(create_scholarships),
        migrations.RunPython(create_students)
    ]

