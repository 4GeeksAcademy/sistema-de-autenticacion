import os
from flask import redirect, url_for
from flask_admin import Admin
from .models import db, User
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    # Redirige al login si no está autenticado
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

    # Opciones para mostrar en el panel de administración
    column_list = ('id', 'email')
    form_excluded_columns = ('password',)

    def on_model_change(self, form, model, is_created):
        """ Hashear la contraseña antes de crear o editar el usuario """
        if is_created:
            model.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        else:
            # Si se está editando, no se debe cambiar la contraseña a menos que se proporcione una nueva
            if form.password.data:
                model.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
    admin.add_view(AuthenticatedModelView(User, db.session))

    # Puedes duplicar esa línea para agregar nuevos modelos
    # admin.add_view(AuthenticatedModelView(YourModelName, db.session))
