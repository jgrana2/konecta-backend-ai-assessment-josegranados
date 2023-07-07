from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .auth import create_access_token, verify_password, get_current_user
from .crud import (
    create_user,
    get_user,
    get_user_by_username,
    update_user,
    delete_user,
    create_task,
    get_tasks_for_user,
    get_task_by_id,
    update_task,
    delete_task,
)
from .database import SessionLocal
from .schemas import UserCreate, Token, TaskCreate, Task, User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# ------ User API Endpoints ------
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=User)
def update_user_endpoint(
    user_id: int, user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return update_user(db, user_id, user)

@app.delete("/users/{user_id}")
def delete_user_endpoint(
    user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    if delete_user(db, user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# ------ Task API Endpoints ------
@app.post("/tasks", response_model=Task)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task, current_user.id)

@app.get("/tasks", response_model=list[Task])
def read_tasks_for_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_tasks_for_user(db, current_user.id)

@app.get("/tasks/{task_id}", response_model=Task)
def read_task_by_id(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_endpoint(
    task_id: int, task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return update_task(db, task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if delete_task(db, task_id):
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
