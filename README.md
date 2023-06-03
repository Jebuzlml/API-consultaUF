# API-consultaUF  
Gracias a esta API construida en  Python podrás consultar de manera sencilla el valor de la UF según el año, mes, día que necesites.

## Instalacion
Para usar la api en tu local, debes realizar los siguientes pasos:

 1. Clonar el repositorio
 2. Ve a la carpeta del proyecto `cd API-consultaUF/`
 3. Crea un nuevo ambiente usando el archivo requeriments.txt
 4. Ejecuta la API usando `uvicorn main:app --reload`


## Endpoint
Para comprobar su ejecución puede acceder a la documentación con la siguiente ruta

> http://127.0.0.1:8000/docs
> nota: la consola entrega la direccion por defecto.

Para acceder a los datos se utiliza la siguiente estructura 
```json
{
  "year": "2022",
  "month": "1",
  "day": "23"
}
   ```
   
   Donde.
 - "year": corresponde al año
 - "month": correspone al mes, este debe ir en números del 1 al 12
 - "day": corresponde al dia

## Demo
Puedes probar la api con el siguiente enlace:
> http://18.228.165.204:666/docs

Tambien puedes usar postman y usar este endpint:
> http://18.228.165.204:666/api/valor-uf

El body debe tener la siguiente estructura: 

```json
{
  "year": "string",
  "month": "string",
  "day": "string"
}
```
