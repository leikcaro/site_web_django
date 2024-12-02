from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BoardsModel
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexPageView(TemplateView): #clase que nos permite renderizar una pagina sencilla sin lógica
    template_name = "index.html"
    
def fecha_actual(request, name):
    import datetime
    if not name:
        name = "Mundo"
    fecha_actual = datetime.datetime.now()
    context = {"fecha_actual": fecha_actual,
                "name": name
    }
    return render(request, "fecha_actual.html", context)

def menu_view(request):
    return render(request, "menu.html")

def home(request):
    return render(request, "home.html")

def datosform_view(request):
    if request.method == "GET":
        print(request.GET)  # Muestra los datos enviados por el formulario
        valor_tu_nombre = request.GET.get("tu_nombre")  # Captura un campo específico
        print(f"Valor de tu_nombre: {valor_tu_nombre}")
    # elif request.method == "POST":
    #     print(request.POST)  # Muestra los datos enviados por el formulario
    #     valor_tu_nombre = request.POST.get("tu_nombre")  # Captura un campo específico
    #     print(f"Valor de tu_nombre: {valor_tu_nombre}")
    # return render(request, "datosform.html")
    
def datosform_view2(request):
    context = {}
    context["form"] = InputForm()
    print(request.POST)
    return render(request, "datosform2.html", context)

def widget_view(request):
    context = {}
    form = WidgetForm()
    print(request)
    print(form.fields.keys())
    context["form"] = WidgetForm()
    print(request.POST)
    return render(request, "widget_home.html", context)

def boardsform_view(request):
    context = {}
    # Inicializamos el formulario con datos del POST o vacío.
    form = BoardsForm(request.POST or None, request.FILES or None) 

    if form.is_valid():
        form.save()  # Guardamos los datos si son válidos.
        return render(request, "home.html", context)  # Redirigimos después de guardar.

    # Si no es válido, o es una solicitud GET, renderizamos la página con el formulario.
    context["form"] = form
    return render(request, "datosform.html", context)

#crear las plantillas para el login y logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Listar todos los Boards
# class BoardListView(ListView):
#     model = BoardsModel
#     template_name = 'boards_list.html'  # Ruta del template
#     context_object_name = 'boards'  # Nombre del contexto en la plantilla
class BoardsListView(LoginRequiredMixin, ListView):
    model = BoardsModel
    template_name = 'boards_list.html'
    context_object_name = 'boards'
    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Parámetro de redirección

# Ver el detalle de un Board
class BoardDetailView(DetailView):
    model = BoardsModel
    template_name = 'boards/board_detail.html'  # Asegúrate de que el nombre es correcto
    context_object_name = 'board'

# Crear un nuevo Board
class BoardCreateView(CreateView):
    model = BoardsModel
    template_name = 'boards/boards_form.html'  # Ruta del template
    fields = ['titulo', 'descripcion']  # Campos que quieres incluir en el formulario
    success_url = reverse_lazy('boards_list')  # Redirigir al listado tras crear

# Actualizar un Board existente
class BoardUpdateView(UpdateView):
    model = BoardsModel
    template_name = 'boards/boards_form.html'  # Reutilizamos el formulario
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('boards_list')

# Eliminar un Board
class BoardDeleteView(DeleteView):
    model = BoardsModel
    template_name = 'boards/boards_confirm_delete.html'  # Ruta del template
    success_url = reverse_lazy('boards_list')  # Redirigir tras eliminar
    
class CustomLoginView(LoginView):
    #template_name = 'registration/login.html'  # Plantilla que usarás # Si creaste un formulario personalizado
    redirect_authenticated_user = True  # Redirige si el usuario ya está autenticado
    success_url = reverse_lazy('home')  # URL a la que redirige después del login

    def get_success_url(self):
        return self.success_url

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # URL a la que redirige después del logout
