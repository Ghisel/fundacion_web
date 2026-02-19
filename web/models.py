from django.db import models
from django.utils import timezone


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cursos/')
    cupo_maximo = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
        ('proximo', 'Próximamente'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='cerrado'
    )

    fecha_inicio_inscripcion = models.DateField()
    fecha_fin_inscripcion = models.DateField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def cupo_disponible(self):
        aprobadas = self.inscripciones.filter(estado_pago='aprobado').count()
        return self.cupo_maximo - aprobadas

    @property
    def inscripcion_habilitada(self):
        hoy = timezone.localdate()

        return (
            self.estado == "abierto"
            and self.fecha_inicio_inscripcion <= hoy <= self.fecha_fin_inscripcion
        )


class Inscripcion(models.Model):

    ESTADO_PAGO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('comprobante_subido', 'Comprobante Subido'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('lista_espera', 'Lista de Espera'),
    ]

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)

    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    comprobante = models.FileField(
        upload_to='comprobantes/',
        null=True,
        blank=True
    )

    estado_pago = models.CharField(
        max_length=30,
        choices=ESTADO_PAGO_CHOICES,
        default='pendiente'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('curso', 'dni')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso.nombre}"


class Novedad(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(
        upload_to='novedades/',
        blank=True,
        null=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    class meta:
        ordering = ['-fecha_creacion']  # 🔥 más reciente primero
    def __str__(self):
        return self.titulo

# models.py

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"

class Nosotros(models.Model):
    titulo = models.CharField(max_length=200)
    historia = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    imagen = models.ImageField(upload_to='nosotros/', blank=True, null=True)

    def __str__(self):
        return self.titulo


class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='equipo/')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"
