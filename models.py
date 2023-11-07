from sqlmodel import Field, SQLModel


class Contact(SQLModel, table=True):
    """
    A model representing a contact in the database.

    Attributes:
        id (int): The unique identifier for the contact (primary key).
        name (str): The name of the contact.
    """
    id: int = Field(default=None, primary_key=True)
    name: str
