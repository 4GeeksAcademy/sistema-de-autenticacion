from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)  # Nuevo usuario activo por defecto

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # No serializar la contraseña por motivos de seguridad
        }

    def set_password(self, password):
        """Generar un hash de la contraseña y guardarlo en la base de datos."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Verificar si la contraseña proporcionada coincide con el hash almacenado."""
        return bcrypt.check_password_hash(self.password, password)
