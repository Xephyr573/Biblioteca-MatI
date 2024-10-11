# "Tipo_usuario" al igual que "Tipo_categoria", es una sub clase para la BD, para que asi de esta forma podamos identificar de una manera clara al usuario.

class Tipo_Usuario():
    def __init__(self, id_tipo_usuario, tipo_usuario, descripcion_tipo_usuario):
        self.id_tipo_usuario = id_tipo_usuario
        self.tipo_usuario = tipo_usuario
        self.descripcion_tipo_usuario = descripcion_tipo_usuario