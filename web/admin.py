from django.contrib import admin
from .models import Curso, Novedad, Inscripcion
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha_creacion', 'leido')
    list_filter = ('leido', 'fecha_creacion')
    search_fields = ('nombre', 'email', 'asunto')




@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nombre', 'apellido', 'dni', 'estado_pago', 'fecha_creacion')
    list_filter = ('estado_pago', 'curso')
    search_fields = ('nombre', 'apellido', 'dni')

    def save_model(self, request, obj, form, change):
        if obj.estado_pago == 'aprobado':
            if obj.curso.cupo_disponible() <= 0:
                obj.estado_pago = 'lista_espera'
        super().save_model(request, obj, form, change)



@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'cupo_maximo', 'mostrar_cupo_disponible')

    def mostrar_cupo_disponible(self, obj):
        return obj.cupo_disponible()

    mostrar_cupo_disponible.short_description = 'Cupo Disponible'


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')