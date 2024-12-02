from django.apps import AppConfig


class BoardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "boards"

# class CustomLoginView(LoginRequiredMixin, View):
#     login_url = '/custom-login/'
#     redirect_field_name = 'next_page'
#     # Tu código aquí

