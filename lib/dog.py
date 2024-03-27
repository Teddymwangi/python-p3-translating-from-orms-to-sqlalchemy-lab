from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Dog

# Create engine
engine = create_engine('sqlite:///dogs.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

def create_table():
    """Create the table in the database."""
    Base.metadata.create_all(engine)

def save(dog):
    """Save a dog object to the database."""
    session.add(dog)
    session.commit()

def read(id):
    """Read a dog object from the database by ID."""
    return session.query(Dog).filter_by(id=id).first()

def update(id, name=None, breed=None, age=None):
    """Update a dog object in the database."""
    dog = read(id)
    if dog:
        if name:
            dog.name = name
        if breed:
            dog.breed = breed
        if age:
            dog.age = age
        session.commit()
        return True
    else:
        return False

def delete(id):
    """Delete a dog object from the database."""
    dog = read(id)
    if dog:
        session.delete(dog)
        session.commit()
        return True
    else:
        return False
