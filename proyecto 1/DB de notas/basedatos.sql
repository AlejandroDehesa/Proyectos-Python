CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuario (
    id int(25) auto_increment not null,
    nombre varchar(100),
    apellidos varchar(100),
    email varchar(100) not null,    
    password varchar(100) not null,
    fecha date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDB;




CREATE TABLE notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)ENGINE=InnoDb;
