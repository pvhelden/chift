from fastapi import APIRouter
from sqlmodel import Session, create_engine, select
from starlette.responses import JSONResponse

from models import Contact

DATABASE_URL = "postgresql://postgres:admin@localhost/chift-db"

engine = create_engine(DATABASE_URL)

router = APIRouter()


@router.get("/contacts/", response_model=Contact)
async def get_all_contacts():
    """
    Retrieve a list of all contacts from the database.

    :return: A JSON response containing a list of contact objects.
    """
    with Session(engine) as session:
        statement = select(Contact)
        contacts = session.exec(statement).fetchall()
        serialized = [contact.dict() for contact in contacts]
    return JSONResponse(serialized)


@router.get("/contacts/{contact_id}", response_model=Contact)
async def get_contact_by_id(contact_id: int):
    """
    Retrieve a contact by its ID from the database.

    :param contact_id: The unique ID of the contact to retrieve.
    :return: A JSON response containing the contact object with the specified ID.
    """
    with Session(engine) as session:
        statement = select(Contact).where(Contact.id == contact_id)
        contact = session.exec(statement).first()
        serialized = contact.dict()
    return JSONResponse(serialized)
