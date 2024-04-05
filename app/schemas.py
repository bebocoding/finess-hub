from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: int
    age: int
    gender: str
    name: str
    email: str
    password: str
    workout_history: list[str] = []
    fitness_level: str
    fitness_goals: str
    preferences: dict
    medical_conditions: list[str] = [],
    weight: int
    height: int
