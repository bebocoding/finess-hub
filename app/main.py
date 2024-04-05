from typing import Optional

from fastapi import FastAPI

from .user.user_profile import UserProfile
from .assessments.assessments.assessment import Assessment
from . import schemas

# Create a new user profile
# Create a new user profile
user_1 = UserProfile(
    user_id=1,
    age=25,
    gender='male',
    name='John Doe',
    email='johndoe@example.com',
    password='password123',
    workout_history=['Push-ups', 'Running'],
    fitness_level='Intermediate',
    fitness_goals='Lose Weight',
    preferences={'duration': 30, 'intensity': 'High', 'frequency': 5},
    medical_conditions=['None'],
    weight=70,
    height=180
)

# Create a new assessment using the user profile
# Create a new assessment using the user profile
user_1_assessment = Assessment(user_profile=user_1)


user_trainings, user_parameters = user_1.get_personalized_recommendation()
print(f"A plan of {user_parameters}  \n with excercises are {user_trainings}")


app = FastAPI()


@app.get("/")
async def root():
    return user_1_assessment, user_trainings, user_parameters


@app.post("/")
async def create_workout_plan(user: schemas.UserCreate):

    new_user = UserProfile(**user.model_dump())

    user_1_assessment = Assessment(user_profile=new_user)

    user_trainings, user_parameters = user_1.get_personalized_recommendation()

    return user_1_assessment, user_trainings, user_parameters
