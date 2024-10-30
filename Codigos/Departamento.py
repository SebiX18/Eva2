class Departamento:
    def __init__(self, id, nombre, descripcion, gerente=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.gerente = gerente

    def crear_departamento(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def editar_departamento(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def eliminar_departamento(self):
        self.descripcion = "Departamento eliminado"