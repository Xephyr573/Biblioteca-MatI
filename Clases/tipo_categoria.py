# "Tipo_Categoria" al igual que "Tipo_Usuario", es una sub clase para la BD, para que asi de esta forma podamos identificar de una manera clara el libro en cuestión.

class Tipo_Categoria():
    def __init__(self, id_tipo_categoria, tipo_categoria):
        self.id_tipo_categoria = id_tipo_categoria
        self.tipo_categoria = tipo_categoria