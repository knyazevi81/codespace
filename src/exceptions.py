from fastapi import HTTPException, status


class UserException(HTTPException):
    status_code: status = status.HTTP_401_UNAUTHORIZED
    detail: str = "Base user exception"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExist(UserException):
    status_code: str = status.HTTP_400_BAD_REQUEST
    detail: str = "User already exist"

class IncorrectLoginOrPasswordException(UserException):
    status_code: status
