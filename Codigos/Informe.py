class Informe:
    def __init__(self, id, tipo_informe, fecha_creacion, empleado, departamento, proyecto):
        self.id = id
        self.tipo_informe = tipo_informe
        self.fecha_creacion = fecha_creacion
        self.empleado = empleado
        self.departamento = departamento
        self.proyecto = proyecto

    def generar_informe(self):
        print(f"Informe: Tipo: {self.tipo_informe}, Fecha: {self.fecha_creacion}")

    def generar_informe_excel(self):
        print(f"Informe en Excel: Tipo: {self.tipo_informe}, Fecha: {self.fecha_creacion}")
