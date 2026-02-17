from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import InscripcionForm
from .models import Curso, Novedad
from .forms import ContactoForm

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "web/contacto_exito.html")
    else:
        form = ContactoForm()

    return render(request, "web/contacto.html", {"form": form})



def inscribirse(request, curso_id):

    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = InscripcionForm(request.POST, request.FILES)

        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.curso = curso
            inscripcion.save()

            return render(request, 'web/inscripcion_exitosa.html', {
                'curso': curso
            })
    else:
        form = InscripcionForm()

    return render(request, 'web/inscribirse.html', {
        'form': form,
        'curso': curso
    })

def inicio(request):
    print("ENTRÉ A INICIO")
    return render(request, 'web/inicio.html')


def nosotros(request):
    return render(request, 'web/nosotros.html')

def lista_cursos(request):
    print("ENTRÉ A LISTA_CURSOS")
    cursos = Curso.objects.all()
    print("CURSOS:", cursos)
    return render(request, 'web/cursos.html', {'cursos': cursos})

def novedades(request):
    print("ENTRÉ A NOVEDADES")
    novedades = Novedad.objects.all().order_by('-fecha_creacion')
    print("NOVEDADES:", novedades)
    return render(request, 'web/novedades.html', {'novedades': novedades})



