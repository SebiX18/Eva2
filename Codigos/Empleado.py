class Empleado:
    def __init__(self, id, nombre, direccion, telefono, correo, fecha_inicio, salario):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento = None
        self.proyectos = []

    def asignar_departamento(self, departamento):
        self.departamento = departamento

    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
