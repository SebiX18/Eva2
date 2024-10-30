class Permiso:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def definir_permisos(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion