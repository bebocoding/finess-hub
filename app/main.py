from typing import Optional

from fastapi import FastAPI

from .user.user_profile import UserProfile
from .assessments.assessments.assessment import Assessment
from . import schemas
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.post("/")
async def create_workout_plan(user: schemas.UserCreate):

    new_user = UserProfile(**user.model_dump())

    user_1_assessment = Assessment(user_profile=new_user)

    user_trainings, user_parameters = new_user.get_personalized_recommendation()

    return user_1_assessment, user_trainings, user_parameters
