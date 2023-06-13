from models import Dog
from sqlalchemy import create_engine


def create_table(base, engine):
    base.metadata.create_all(engine)
        


def save(session, dog):
    session.add( dog )
    session.commit()

def get_all(session):
    return session.query(Dog).all()
    

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.like(id)).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(name), Dog.breed.like(breed)).first()

def update_breed(session, dog, breed):
    for dog in session.query(Dog):
        dog.breed = breed