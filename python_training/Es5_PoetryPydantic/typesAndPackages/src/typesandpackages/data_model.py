import hashlib
import uuid
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr, model_validator


class Prodotto(BaseModel):
    nome: str
    prezzo: float = Field(description='Prezzo del prodotto', gt=0)
    categoria: Literal['cibo', 'indumenti','casalinghi'] = Field(description='Categoria del prodotto')
    id: UUID = Field(description='Id del prodotto', default_factory=uuid.uuid4)

class Utente(BaseModel):
    nome: str
    cognome: str
    email: EmailStr
    password: str = Field(description='Password hash')

    @model_validator(mode='after')
    def validate_after(self):
        if self.password:
            self.password = hashlib.sha256(self.password.encode()).hexdigest()

        return self

if __name__ == "__main__":
    prodotto = Prodotto(
        nome='Prodotto',
        prezzo=5.00,
        categoria='cibo'    )

    utente = Utente(
        nome='Utente',
        cognome='Utente',
        email='utente@gmoa.co',
        password='ksg',
    )

    print(prodotto)
    print(utente)

