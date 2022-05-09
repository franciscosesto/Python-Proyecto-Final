from django.urls import path

from .views import  (Creador_Busqueda, HomeVista, Usuario_Vista_Forms, Creador_Vista_Forms_CreateUpdate, 
Espectador_Vista_Forms, Creador_Busqueda, buscar_modelo_creador, LoginView, 
RegisterView, CreadorVista, VistaBorrarCreador, AboutVista, 
PageVista, PageDetailView, PageCreateView, PageUpdateView,
ContactVista, AddAvatarView, ProfileVista, PageDeleteView, 
ProfileUpdateView, UpdateAvatarView, ProfileDataCreateView, ProfileDataUpdateView,
MensajesVista, CrearMensajesVista, AgradecimientosVista )
from django.contrib.auth.views import LogoutView, PasswordChangeView


urlpatterns = [
path("", HomeVista.as_view(), name="inicio"),
path("creador/",CreadorVista.as_view(), name="creador"),
path("usuarioforms/", Usuario_Vista_Forms.as_view(), name="usuarioforms"),
path("creadorforms/", Creador_Vista_Forms_CreateUpdate.as_view(), name="creadorforms"),
path("espectadorforms/", Espectador_Vista_Forms.as_view(), name="espectadorforms"),
path("creadorsearch/", Creador_Busqueda.as_view(), name="creadorsearch"),
path("buscar_creador/", buscar_modelo_creador, name="buscarmodelocreador"),
path("accounts/login/", LoginView.as_view(), name="login"),
path("accounts/signup", RegisterView.as_view(), name="signup"),
path("accounts/profile", ProfileVista.as_view(), name="profile"),
path("accounts/profile/add-profile-data", ProfileDataCreateView.as_view(), name="add-profile-data"),
path("accounts/profile/update-profile-data/<int:pk>/", ProfileDataUpdateView.as_view(), name="profile_data-update"),
path("accounts/profile/update", ProfileUpdateView.as_view(), name="profile-update"),
path("accounts/profile/add-avatar", AddAvatarView.as_view(), name="add-avatar"),
path("accounts/profile/update-avatar/<int:pk>/", UpdateAvatarView.as_view(), name="avatar-update"),
path("logout/", LogoutView.as_view(template_name= "logout/logout.html"), name="logout"),
path("eliminarcreador/<int:creador_id>/", VistaBorrarCreador.as_view(), name="eliminarcreador"),
path("actualizar-creador/<int:creador_id>/", Creador_Vista_Forms_CreateUpdate.as_view(), name="actualizarcreador"),
path("about/", AboutVista.as_view(), name="about"),
path("page/", PageVista.as_view(), name="pages"),
path("page/<int:pk>", PageDetailView.as_view(), name="page"),
path("page/create", PageCreateView.as_view(), name="page-create"),
path("page/update/<int:pk>/", PageUpdateView.as_view(), name="page-update"),
path("page/delete/<int:pk>/", PageDeleteView.as_view(), name="page-delete"),
path("contact", ContactVista.as_view(), name="contact"),
path("password-change", PasswordChangeView.as_view(), name="password-change"),
path("messages/", MensajesVista.as_view(), name="messages"),
path("messages/create", CrearMensajesVista.as_view(), name="messages-create"),
path("agradecimientos", AgradecimientosVista.as_view(), name="agradecimientos"),


]
