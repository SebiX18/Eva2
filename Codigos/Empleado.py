import mysql.connector
from mysql.connector import Error
from tkinter import Tk, Label, Entry, Button, END, messagebox
from tkinter import ttk
import bcrypt

class Empleado:
    def __init__(self, id, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id=None, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento_id = departamento_id
        self.contrasena = contrasena 

    @staticmethod
    def conectar_bd():
        try:
            conexion = mysql.connector.connect(
                user='root',        
                host='localhost',   
                database='prueba',  
                password='',           
                port='3306'            
            )
            return conexion
        except Error as e:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos: {e}")
            return None

    def guardar(self):
        conn = Empleado.conectar_bd()
        if conn is None:
            return
        cursor = conn.cursor()
        if self.contrasena:
            salt = bcrypt.gensalt()
            hashed_contrasena = bcrypt.hashpw(self.contrasena.encode('utf-8'), salt)
        else:
            hashed_contrasena = None

        query = '''
            INSERT INTO empleado (id, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id, contrasena)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        data = (
            self.id, self.nombre, self.direccion, self.telefono, self.correo,
            self.fecha_inicio, self.salario, self.departamento_id, hashed_contrasena
        )
        try:
            cursor.execute(query, data)
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado guardado exitosamente.")
        except Error as e:
            messagebox.showerror("Error", f"Error al guardar el empleado: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def obtener_empleados():
        conn = Empleado.conectar_bd()
        if conn is None:
            return []
        cursor = conn.cursor()
        query = "SELECT id, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id FROM empleado"
        try:
            cursor.execute(query)
            empleados = cursor.fetchall()
            return empleados
        except Error as e:
            messagebox.showerror("Error", f"Error al obtener empleados: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def actualizar(self):
        conn = Empleado.conectar_bd()
        if conn is None:
            return
        cursor = conn.cursor()
        if self.contrasena:
            salt = bcrypt.gensalt()
            hashed_contrasena = bcrypt.hashpw(self.contrasena.encode('utf-8'), salt)
            query = '''
                UPDATE empleado SET nombre=%s, direccion=%s, telefono=%s, correo=%s,
                fecha_inicio=%s, salario=%s, departamento_id=%s, contrasena=%s WHERE id=%s
            '''
            data = (
                self.nombre, self.direccion, self.telefono, self.correo,
                self.fecha_inicio, self.salario, self.departamento_id,
                hashed_contrasena, self.id
            )
        else:
            query = '''
                UPDATE empleado SET nombre=%s, direccion=%s, telefono=%s, correo=%s,
                fecha_inicio=%s, salario=%s, departamento_id=%s WHERE id=%s
            '''
            data = (
                self.nombre, self.direccion, self.telefono, self.correo,
                self.fecha_inicio, self.salario, self.departamento_id,
                self.id
            )
        try:
            cursor.execute(query, data)
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado actualizado exitosamente.")
        except Error as e:
            messagebox.showerror("Error", f"Error al actualizar el empleado: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def eliminar(id_empleado):
        conn = Empleado.conectar_bd()
        if conn is None:
            return
        cursor = conn.cursor()
        query = "DELETE FROM empleado WHERE id = %s"
        try:
            cursor.execute(query, (id_empleado,))
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado eliminado exitosamente.")
        except Error as e:
            messagebox.showerror("Error", f"Error al eliminar el empleado: {e}")
        finally:
            cursor.close()
            conn.close()
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados")

        labels = [
            "ID Empleado", "Nombre Empleado", "Dirección", "Teléfono",
            "Correo", "Fecha Inicio (YYYY-MM-DD)", "Salario", "Departamento ID",
            "Contraseña"
        ]
        self.entries = {}
        for i, label in enumerate(labels):
            Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='w')
            entry = Entry(root)
            if label == "Contraseña":
                entry.config(show="*")  
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry

        Button(root, text="Agregar Empleado", command=self.agregar_empleado).grid(row=9, column=0, padx=10, pady=10)
        Button(root, text="Mostrar Empleados", command=self.mostrar_empleados).grid(row=9, column=1, padx=10, pady=10)
        Button(root, text="Actualizar Empleado", command=self.actualizar_empleado).grid(row=10, column=0, padx=10, pady=10)
        Button(root, text="Eliminar Empleado", command=self.eliminar_empleado).grid(row=10, column=1, padx=10, pady=10)

        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Dirección", "Teléfono", "Correo",
                                                "Fecha Inicio", "Salario", "Departamento"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_empleado)

    def agregar_empleado(self):
        try:
            id = int(self.entries["ID Empleado"].get())
            nombre = self.entries["Nombre Empleado"].get()
            direccion = self.entries["Dirección"].get()
            telefono = self.entries["Teléfono"].get()
            correo = self.entries["Correo"].get()
            fecha_inicio = self.entries["Fecha Inicio (YYYY-MM-DD)"].get()
            salario = float(self.entries["Salario"].get())
            departamento_id = int(self.entries["Departamento ID"].get()) if self.entries["Departamento ID"].get() else None
            contrasena = self.entries["Contraseña"].get()

            empleado = Empleado(id, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id, contrasena)
            empleado.guardar()
            self.mostrar_empleados()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa datos válidos.")

    def mostrar_empleados(self):
        empleados = Empleado.obtener_empleados()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for emp in empleados:
            self.tree.insert("", END, values=emp)

    def actualizar_empleado(self):
        try:
            id = int(self.entries["ID Empleado"].get())
            nombre = self.entries["Nombre Empleado"].get()
            direccion = self.entries["Dirección"].get()
            telefono = self.entries["Teléfono"].get()
            correo = self.entries["Correo"].get()
            fecha_inicio = self.entries["Fecha Inicio (YYYY-MM-DD)"].get()
            salario = float(self.entries["Salario"].get())
            departamento_id = int(self.entries["Departamento ID"].get()) if self.entries["Departamento ID"].get() else None
            contrasena = self.entries["Contraseña"].get()

            empleado = Empleado(id, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id, contrasena)
            empleado.actualizar()
            self.mostrar_empleados()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa datos válidos.")

    def eliminar_empleado(self):
        try:
            id = int(self.entries["ID Empleado"].get())
            Empleado.eliminar(id)
            self.mostrar_empleados()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    def seleccionar_empleado(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            keys = ["ID Empleado", "Nombre Empleado", "Dirección", "Teléfono",
                    "Correo", "Fecha Inicio (YYYY-MM-DD)", "Salario", "Departamento ID"]
            for i, key in enumerate(keys):
                self.entries[key].delete(0, END)
                self.entries[key].insert(0, values[i])

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
