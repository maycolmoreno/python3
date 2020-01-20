from django.urls import path, include,re_path


from . import views

urlpatterns = [
    re_path(r'^$', views.mostrar_inicio, name='index'),
    # path(r'login', login, {
    #     'template_name': 'login/login.html'}, name='auth_login'),
]
