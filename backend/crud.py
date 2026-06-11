from sqlalchemy.orm import Session
from models import Coffee


def get_all_coffees(db: Session):
    return db.query(Coffee).all()


def vote_coffee(db: Session, coffee_id: int):
    coffee = db.query(Coffee).filter(Coffee.id == coffee_id).first()

    if coffee:
        coffee.votes += 1
        db.commit()
        db.refresh(coffee)

    return coffee