from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.contrib import messages
from .models import Usuarios, Libro,Genero,Prestamo,Detalle_Libro
# Create your views here.
def login(request):
    return render(request, 'login.html')
def admin(request):
    usuario = Usuarios.objects.values()
    libro= Libro.objects.all()
    genero= Genero.objects.all()
    prestamo= Prestamo.objects.all()
 
    context = {
        'usuario': usuario,
        'libro': libro,
        'genero': genero,
        'prestamo': prestamo,
    }
    return render(request, 'Crud.html', context)
def Inicio(request):
    usuario = Usuarios.objects.values()
    libro = Libro.objects.values()
    return render(request,'inicio.html',{'usuario': usuario, 'libro':libro})


def Inicio_sesion(request):

    if request.method == 'GET':
            return render(request, 'login.html', {})
    else:
        username = request.POST.get("user")
        clave = request.POST.get("password")
        try:
            usuario = Usuarios.objects.filter(username= username, password= clave).first()
           
            if not usuario   :
               return render(request,'login.html', {'error':  'Usuario o Contraseña no Existe!' })                
            
            else:
                return redirect('home')
        except Usuarios.DoesNotExist:
               return render(request,'login.html', {'error':  'Usuario o Contraseña no Existe!' })
        

#codigo de CRUD
def Crear_Libro(request):
    libro= request.POST.get('libro')
    decrip= request.POST.get('descripción')
    edito= request.POST.get('editorial')
    page= request.POST.get('paginas')
    fecha= request.POST.get('anio_publi')

    crear = Libro.objects.create(
    nombre =libro,
    descripcion = decrip,
    editorial=edito,
    paginas=page,
    anio_publicacion=fecha,
    )
    messages.success(request, 'Libro Creado!')
    return redirect('crud')
 

#Album

def Crear_Genero(request):
    genero= request.POST.get('genero')

    crear = Genero.objects.create(
        nombre=genero
    )
    messages.success(request, 'Genero del Libro Creado!')
    return redirect('crud')

#cancion
def Crear_Prestamo(request):
    fecha1= request.POST.get('fecha_prestamos')
    fecha2= request.POST.get('fecha_entrega')

    crear = Prestamo.objects.create(
        fecha_prestamo = fecha1,
        fecha_devolucion = fecha2
    )
    messages.success(request, 'Prestamo  Creado!')
  
    return redirect('crud')

def Actualizar_Libro_mostrar(request,id):
    
    actualizar = Libro.objects.get(id=id)
    info={
        'libro': actualizar
    }

    return render(request, 'crud/Actualizar_Libro.html ',info)


def Actualizar_Genero_mostrar(request,id):
    
    actualizar = Genero.objects.get(id=id)
    info={
        'genero': actualizar
    }

    return render(request, 'crud/Actualizar_Genero.html ',info)


def Actualizar_Prestamo_mostrar(request,id):
    
    actualizar = Prestamo.objects.get(id=id)
    info={
        'prestamo': actualizar
    }

    return render(request, 'crud/Actualizar_Prestamo.html ',info)


def Actualizar_Libro(request):
    id= request.POST.get('idA')
    libro= request.POST.get('libroA')
    decrip= request.POST.get('descripciónA')
    edito= request.POST.get('editorialA')
    page= request.POST.get('paginasA')
    fecha= request.POST.get('anio_publiA')

    libros = Libro.objects.get(id=id)
    libros.nombre = libro
    libros.descripcion = decrip
    libros.editorial = edito
    libros.paginas = page
    libros.anio_publicacion = fecha
    libros.save()
    messages.success(request, 'Libro Actualizado!')
    return redirect('crud')
    
def Actualizar_Genero(request):
    
    id= request.POST.get('id')
    nombre= request.POST.get('generoA')

    genero = Genero.objects.get(id=id)
    genero.nombre = nombre

    genero.save()
    messages.success(request, 'Genero del Libro Creado!')
    return redirect('crud')
    
def Actualizar_Prestamo(request):
    id= request.POST.get('id')

    fecha1= request.POST.get('fecha_prestamos')
    fecha2= request.POST.get('fecha_entrega')

    prestamo = Prestamo.objects.get(id=id)
    prestamo.fecha_prestamo = fecha1
    prestamo.fecha_devolucion = fecha2
 
    prestamo.save()
    messages.success(request, 'Prestamo del Libro Creado!')
    return redirect('crud')
    


def Delete_Libro(request,id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    messages.success(request, 'Cancion Eliminado!')
    return redirect('crud')

def Delete_Genero(request,id):
    genero = Genero.objects.get(id=id)
    genero.delete()
    messages.success(request, 'Cancion Eliminado!')
    return redirect('crud')

def Delete_Prestamo(request,id):
    prestamo = Prestamo.objects.get(id=id)
    prestamo.delete()
    messages.success(request, 'Cancion Eliminado!')
    return redirect('crud')





def Informacion(request,id):
 
    info = Detalle_Libro.objects.get(id=id)
    libro= info.id_libro 
    genero= info.id_genero
    prestamo= info.id_prestamo 
    # # artista= info.i
    context={
         'info':info,
         'libro':libro,
         'genero':genero,
         'prestamo':prestamo,
    }
    info.save()
    return render(request, 'info.html ',context)