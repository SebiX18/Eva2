class Usuario:
    def __init__(self, id, nombre_usuario, contraseña, rol):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.rol = rol

    def autenticar(self, username, password):
        return self.nombre_usuario == username and self.contraseña == password

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña

    def asignar_rol(self, nuevo_rol):
        self.rol = nuevo_rol
