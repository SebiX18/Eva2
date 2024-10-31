CREATE TABLE Rol (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Permiso (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Empleado (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(15),
    correo VARCHAR(100),
    fecha_inicio DATE,
    salario DECIMAL(10, 2),
    departamento_id INT
);

CREATE TABLE Departamento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    gerente_id INT,
    FOREIGN KEY (gerente_id) REFERENCES Empleado(id)
);

CREATE TABLE Usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES Rol(id)
);

CREATE TABLE Proyecto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE
);

CREATE TABLE RegistroDeTiempo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    horas_trabajadas DECIMAL(5, 2),
    descripcion TEXT,
    empleado_id INT,
    proyecto_id INT,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id),
    FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id)
);

CREATE TABLE Informe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_informe VARCHAR(100) NOT NULL,
    fecha_creacion DATE,
    empleado_id INT,
    departamento_id INT,
    proyecto_id INT,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id),
    FOREIGN KEY (departamento_id) REFERENCES Departamento(id),
    FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id)
);

CREATE TABLE Rol_Permiso (
    rol_id INT,
    permiso_id INT,
    PRIMARY KEY (rol_id, permiso_id),
    FOREIGN KEY (rol_id) REFERENCES Rol(id),
    FOREIGN KEY (permiso_id) REFERENCES Permiso(id)
);

CREATE TABLE Empleado_Proyecto (
    empleado_id INT,
    proyecto_id INT,
    PRIMARY KEY (empleado_id, proyecto_id),
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id),
    FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id)
);
