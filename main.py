from fastapi import FastAPI
from app.model.uf_model import Uf
from app.utils.get_uf_value_util import UfValue

app = FastAPI(
    title='API para consultar valor de UF',
    description='Gracias a esta API podras consultar de manera sencilla el valor de la uf segun el año, mes, '
                'dia que necesites',
    version='1'
)

""""
Para consultar la documentacion de la API 
ingresar a -> http://127.0.0.1:8000/docs
"""


# Evento al iniciar el servidor
@app.on_event('startup')
async def startup():
    print("Iniciando el servidor")


# Evento al apagar el servidor
@app.on_event('shutdown')
def shutdown():
    print("Apagando el servidor")


# Funcion encargada de entregar un valor de UF segun año, mes y dia
@app.post("/api/valor-uf")
def check_uf(check: Uf):
    uf = UfValue(check.year)
    uf.get_data_sii()
    uf.get_data_uf()
    uf_value = uf.get_uf_value(check.day, check.month)

    return {
        "dia": check.day,
        "mes": check.month,
        "año": check.year,
        "valor_uf": uf_value
    }
