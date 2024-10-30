class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_fin):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.empleados = []

    def asignar_empleado(self, empleado):
        self.empleados.append(empleado)