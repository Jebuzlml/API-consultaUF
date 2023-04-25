import requests
import pandas as pandas
from bs4 import BeautifulSoup
from fastapi import HTTPException
from app.utils.check_model import check_year, check_month, check_day
from app.utils.get_uf_utils import check_final_value


class UfValue:
    def __init__(self, year):
        check_year(year)
        self.year = year
        self.url = f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"

    # Metodo encargado de obtener el codigo HTML de la pagina del SII
    def get_data_sii(self):
        self.response = requests.get(self.url)
        self.data_sii = self.response.text

    # Metodo encargado de obtener el codigo HTML de la tabla que almacena los valores de UF segun mes y dia
    def get_data_uf(self):
        self.soup = BeautifulSoup(self.data_sii, 'html.parser')

        uf_data = []
        table_html = self.soup.find('div', {'id': 'mes_all'}).find('table')
        rows_html = table_html.find_all('tr')

        for row in rows_html:
            row_data = []
            cells = row.find_all(['th', 'td'])
            for cell in cells:
                row_data.append(cell.text.strip())
            uf_data.append(row_data)

        # Creacion de grilla para manejar datos con pandas
        self.data_frame = pandas.DataFrame(uf_data[1:], columns=uf_data[0])

    # Metodo encargado de buscar el valor de la UF en la grilla segun mes y dia
    def find_uf_value(self, day, month):
        month = check_month(month)
        day = check_day(day)
        value = self.data_frame.loc[self.data_frame['Día'] == day, month].values

        if len(value) > 0:
            return value[0]
        else:
            return None

    # Metodo encargado de obtener el valor de la UF
    def get_uf_value(self, day, month):
        uf_value = self.find_uf_value(day, month)
        check_final_value(uf_value)

        if uf_value is not None:
            return uf_value
        else:
            raise HTTPException(status_code=404,
                                detail=f"No se encontró un valor de la UF en el dia '{day}' de '{month}'")
