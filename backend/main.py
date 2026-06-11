from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Base, Coffee
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Coffee Rating API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = SessionLocal()

if db.query(Coffee).count() == 0:

    coffees = [

        Coffee(
            name="Espresso",
            description="Strong Italian Coffee",
            image="https://images.unsplash.com/photo-1511920170033-f8396924c348",
            votes=10
        ),

        Coffee(
            name="Cappuccino",
            description="Creamy Milk Coffee",
            image="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085",
            votes=15
        ),

        Coffee(
            name="Latte",
            description="Smooth and Milky",
            image="https://images.unsplash.com/photo-1509042239860-f550ce710b93",
            votes=20
        )

    ]

    db.add_all(coffees)

    db.commit()

db.close()


@app.get("/coffees")
def get_coffees():

    db = SessionLocal()

    data = crud.get_all_coffees(db)

    db.close()

    return data


@app.post("/vote/{coffee_id}")
def vote(coffee_id: int):

    db = SessionLocal()

    coffee = crud.vote_coffee(db, coffee_id)

    db.close()

    return coffee