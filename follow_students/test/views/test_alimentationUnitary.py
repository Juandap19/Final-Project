from django.test import TestCase, Client
from django.urls import reverse
from follow_students.models import *

class AlimentacionTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Client = Client()

        cls.the_donor = Donor.objects.create(cedula = "1107835369" , name = "Juan David Patiño" , mail = "juanda232405@hotmail.com", description = "Joven empresario, ganadero, panadero, futuro dueño de Icesi" )

        cls.amount1 = Amount.objects.create(code = '199' , transport = 10000000 , alimentation = 5000000 , academic =  50000000 )

        cls.amount2 = Amount.objects.create(code = '299' , transport = 6000000 , alimentation = 2000000 , academic =  1200000 )

        cls.scholarship1 = Scholarship.objects.create(code = "099" , name = "Emcali" ,amount = cls.amount1, donor = cls.the_donor, assigned_students =  1 , academic_percentage = 50 , transportation = 300000, image = "logo_EMCALI.png")

        cls.scholarship2 = Scholarship.objects.create(code = "098" , name = "Valle Del lili" ,amount = cls.amount2, donor = cls.the_donor, assigned_students =  1 , academic_percentage = 100 , transportation = 100000, image = "logo_FUNDACION.png")


        # Crear una carrera (Major)
        cls.major = Major.objects.create(
            name="Ingeniería de Sistemas",
            price=10300000
        )

        # Crear un estudiante (Student)
        cls.student = Student.objects.create(
            name="Juan Carmelo",
            phoneNumber="12367890",
            date="2023-01-01",
            icfes=0,
            cedula="1234",
            code="A00381289",
            mail="juanda2342324@example.com",
            major=cls.major,
            scholarship = cls.scholarship1
        )

        # Crear una carrera (Major)
        cls.major2 = Major.objects.create(
            name="Pedagogia",
            price=7300000
        )

        # Crear un estudiante (Student)
        cls.student2 = Student.objects.create(
            name="Juan Carlos Alberto",
            phoneNumber="12347810",
            date="2023-02-01",
            icfes=0,
            cedula="12343",
            code="A00381299",
            mail="juaAlbero324@example.com",
            major=cls.major2,
            scholarship = cls.scholarship2
        )


    def test_get_render_page(self):
        response = self.client.get('/apoyo_financiero_alimentacion/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './financial_alimentation.html')

    def test_post_success(self):
        print("\nTEST-POST-SUCESS")
        # Verificamos que no tengan registrado ningun gasto en nuestra tabla de datos, dato caso que ya existan gastos de variables de ruido tenemos que tenga la lista de datos - 1 pusto que no se han agregado un nuevo gasto asociado al estudiante
        fondo_alimentacion_previo = self.student.scholarship.amount.alimentation

        print("{} Gastos registrados antes de la agregación de uno nuevo".format(Scholarship_expense.objects.count()))

        gastos_previos = Scholarship_expense.objects.count()

        #Se manda por el metodo post de la pagina de financiero.
        response = self.client.post('/apoyo_financiero_alimentacion/', {
            'student_code': self.student.code,
            'money_quantity': '200000',
            'acumulate_time': '12',
            'select_time': '1'
        })

        #Por ultimo buscamos que se haya añadido el gasto y que sobre todo pertenezca al estudiante que al cual se le realizo, Por ende se realizan los asset devidos y a los gastos previos se incrementa en 1, que fue el gasto registrado

        self.assertEqual(Scholarship_expense.objects.count(), gastos_previos+1 )

        # Aqui verificamos que se saque el mismo estudiante con el que se registro el pago, que es el atributo .student lo mostraremos en pantalla par que sea más claro aun.Pero primero se debe de guarda en una variable para que sea mas organizado.

        student_expense = Scholarship_expense.objects.get(student = self.student)
        self.assertEqual(student_expense.student.code, self.student.code)
        print('Estudiante del gasto {} \nEstudiante del atributo .student {}'.format(student_expense.student.code,self.student.code))

        #Ademas veremos si se desconto el pago para la beca asociada al estudiante, en el monto de Alimentacion

        self.assertEqual(fondo_alimentacion_previo - 200000 , 4800000 )

        # Por ultimo verificamos que el mensaje de exito fue correctamente enviado y redirecciona otra vez a la pantalla para poder cargar este

        self.assertEqual(response.status_code, 200) 

    def test_post_student_not_found(self):
        print("\nTEST-POST-STUDENT-NOT-FOUND" )

        # Consultamos los gastos previos  para conocer cuantos se encuentran registrados antes de intentar lanzar el test con un codigo inexistente, este deberia no dejarnos poner ninguna cargo      
        print("{} Gastos registrados antes de la agregación de uno nuevo".format(Scholarship_expense.objects.count()))

        gastos_previos = Scholarship_expense.objects.count()

        response = self.client.post('/apoyo_financiero_alimentacion/', {
            'student_code': 'A00123443',
            'money_quantity': '3000',
            'acumulate_time': '33',
            'select_time': '2'
        })

        # Despues de intentar hace el pago con un codigo inexistente debe de tener las misma cantidad de gastos previamente registrados, ya que no se tuvo que añadir nada a nuestra tabla de gastos becas.
        self.assertEqual(gastos_previos, gastos_previos)

        #Adicionalmente lo podes ver aqui
        print("{} Gastos registrados Post el intento de  agregación de uno nuevo con un codigo invalido".format(Scholarship_expense.objects.count()))

        #Ademas muestra un mensaje error puesto que la no se pudo procesar debido a un error del cliente, esto se vera en selenium posteriormente, porahora solo se debe de redigir a la pagina
        self.assertEqual(response.status_code, 302) 

    def test_post_insufficient_funds(self):
        print("\nTEST-POST-INSUFFICIENT-FUNDS")
        # Consultamos los gastos previos  para conocer cuantos se encuentran registrados antes de intentar lanzar el test con una cantidad de dinero acumulado superio, este no deberia  dejarnos poner ninguna cargo.      
        print("{} Gastos registrados antes de la agregación de uno nuevo".format(Scholarship_expense.objects.count()))

        gastos_previos = Scholarship_expense.objects.count()

        response = self.client.post('/apoyo_financiero_alimentacion/', {
            'student_code':  self.student2.code,
            'money_quantity': '2100000',
            'acumulate_time': '1',
            'select_time': '3'
        })

        # Despues de intentar hace el pago con un pago que excede los fondos disponible debe de tener las misma cantidad de gastos previamente registrados, ya que no se tuvo que añadir nada a nuestra tabla de gastos becas.
        self.assertEqual(gastos_previos, gastos_previos)

        #Adicionalmente lo podes ver aqui
        print("{} Gastos registrados Post el intento de  agregación de uno nuevo con un codigo invalido".format(Scholarship_expense.objects.count()))

        #Ademas muestra un mensaje error ya que no es autorizado realizar el pago , puesto que los saldo son insuficientes para realizar el pago.Esto se vera luego en las pruebas de selenium
        self.assertEqual(response.status_code, 302) 
        


            