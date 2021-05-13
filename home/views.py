from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *



# Create your views here.
def inicio_view(request):
    return render(request,'inicio.html')

def about_view(request):
    return render(request,'about.html')

def contacto_view(request):
    c = ""
    a = ""
    t = ""
    enviado = False
    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            enviado = True
            c = formulario.cleaned_data['correo']
            a = formulario.cleaned_data['titulo']
            t = formulario.cleaned_data['texto']
    else: #GET
              formulario = contacto_form()          

    formulario = contacto_form()

    return render(request,'contacto.html', locals())    

def listar_videos_view(request):

    videos = Video.objects.filter()

    return render(request,'videos.html',locals())

def listar_equipos_view(request):
    
    equipos = Equipo.objects.filter()

    return render(request,'equipos.html',locals())    

def listar_jugadores_view(request):
    jugadores = Jugador.objects.filter()
    return render(request,'jugadores.html',locals())

def listar_categorias_view(request):
    categorias = Categoria.objects.filter()
    return render(request,'categorias.html',locals())    

def agregar_video_view(request):
    if request.method == 'POST':
        formulario = agregar_video_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/videos/')
    else:#GET
        formulario = agregar_video_form()


    return render (request, 'agregar_video.html',locals())

def agregar_equipo_view(request):
    if request.method == 'POST':
        formulario = agregar_equipo_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/equipos/')
    else:#GET
        formulario = agregar_equipo_form()


    return render (request, 'agregar_equipo.html',locals())

def agregar_jugador_view(request):
    if request.method == 'POST':
        formulario = agregar_jugador_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/jugadores/')
    else:#GET
        formulario = agregar_jugador_form()


    return render (request, 'agregar_jugador.html',locals())

def agregar_categoria_view(request):
    if request.method == 'POST':
        formulario = agregar_categoria_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias/')
    else:#GET
        formulario = agregar_categoria_form()


    return render (request, 'agregar_categoria.html',locals())            

def ver_video_view(request,id_video):
    detalle = Video.objects.get(id=id_video)
    return render(request,'ver_video.html',locals())    

def eliminar_video_view(request,id_video):
    objeto = Video.objects.get(id=id_video)
    objeto.delete()
    return redirect('/videos/') 

def editar_video_view(request,id_video):
    objeto = Video.objects.get(id=id_video)
    if request.method == 'POST':
        formulario = agregar_video_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/videos/')
    else:        
        formulario = agregar_video_form(instance=objeto)

    return render(request,'agregar_video.html',locals()) 

def ver_equipo_view(request,id_equipo):
    detalle = Equipo.objects.get(id=id_equipo)
    return render(request,'ver_equipo.html',locals())    

def eliminar_equipo_view(request,id_equipo):
    objeto = Equipo.objects.get(id=id_equipo)
    objeto.delete()
    return redirect('/equipos/') 

def editar_equipo_view(request,id_equipo):
    objeto = Equipo.objects.get(id=id_equipo)
    if request.method == 'POST':
        formulario = agregar_equipo_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/equipos/')
    else:        
        formulario = agregar_equipo_form(instance=objeto)

    return render(request,'agregar_equipo.html',locals()) 

def ver_jugador_view(request,id_jugador):
    detalle = Jugador.objects.get(id=id_jugador)
    return render(request,'ver_jugador.html',locals())    

def eliminar_jugador_view(request,id_jugador):
    objeto = Jugador.objects.get(id=id_jugador)
    objeto.delete()
    return redirect('/jugadores/') 

def editar_jugador_view(request,id_jugador):
    objeto = Jugador.objects.get(id=id_jugador)
    if request.method == 'POST':
        formulario = agregar_jugador_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/jugadores/')
    else:        
        formulario = agregar_jugador_form(instance=objeto)

    return render(request,'agregar_jugador.html',locals()) 

def ver_categoria_view(request,id_categoria):
    detalle = Categoria.objects.get(id=id_categoria)
    return render(request,'ver_categoria.html',locals())    

def eliminar_categoria_view(request,id_categoria):
    objeto = Categoria.objects.get(id=id_categoria)
    objeto.delete()
    return redirect('/categorias/') 

def editar_categoria_view(request,id_categoria):
    objeto = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        formulario = agregar_categoria_form(request.POST,request.FILES,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias/')
    else:        
        formulario = agregar_categoria_form(instance=objeto)

    return render(request,'agregar_categoria.html',locals())     

def login_view(request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario'] 
            cla = formulario.cleaned_data['clave'] 
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request,usuario)
                return redirect('/')
            else:
                msj = 'usuario o clave incorrectos'  
    else:#GET
        formulario = login_form()
    return render(request,'login.html',locals())        

def logout_view(request):
    logout(request)
    return redirect('/login/') 

def register_view(request):
    formulario = register_form()
    if request.method == 'POST':
        formulario = register_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email'] 
            password_1 = formulario.cleaned_data['password_1']
            password_2 = formulario.cleaned_data['password_2']
            u =  User.objects.create_user(username=usuario,email=correo,password=password_1)
            u.save()
            return render(request, 'tanks_for_register.html',locals())
        else:
            return render(request, 'register.html',locals())
    return render(request, 'register.html',locals())                
                   