from app.exception.uf_exception import UfNotFound


# Funcion encargada de comprobar que el valor de UF entregado existe
def check_final_value(uf_value):
    if len(uf_value) == 0:
        raise UfNotFound()
