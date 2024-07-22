from fastapi import HTTPException, status


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует.",
)


IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверено введены почта или пароль.",
)


TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Срок годности токена истёк.",
)


TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует.",
)


IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена.",
    )


IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена.",
    )


UserNotExistsHiddenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неизвестная ошибка.",
    )


UserIsNotAdminHiddenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неизвестная ошибка.",
)