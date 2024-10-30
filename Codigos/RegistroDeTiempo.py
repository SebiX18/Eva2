class RegistroDeTiempo:
    def __init__(self, id, fecha, horas_trabajadas, descripcion, empleado, proyecto):
        self.id = id
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        self.empleado = empleado
        self.proyecto = proyecto

    def registrar_horas(self, horas, descripcion):
        self.horas_trabajadas = horas
        self.descripcion = descripcion