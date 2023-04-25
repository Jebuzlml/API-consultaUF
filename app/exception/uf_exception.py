from fastapi import HTTPException, status


class UfNotFound(HTTPException):
    def __init__(self, detail="El valor de la UF no esta disponible para el dia consultado"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
