from fastapi import HTTPException, status


class YearOutOfRangeException(HTTPException):
    def __init__(self, detail="El año ingresado no está disponible"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class DayOutOfRangeException(HTTPException):
    def __init__(self, detail="El dia ingresado no está disponible"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class MonthOutOfRangeException(HTTPException):
    def __init__(self, detail="El mes ingresado no está disponible"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
