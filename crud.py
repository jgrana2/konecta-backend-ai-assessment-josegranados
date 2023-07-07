from sqlalchemy.orm import Session
from .models import User, Task
from .auth import get_password_hash

# Create user function was already provided
def create_user(db: Session, user):
    db_user = User(username=user.username, password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ------ User CRUD operations ------
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def update_user(db: Session, user_id: int, new_user_data):
    db.query(User).filter(User.id == user_id).update({
        User.username: new_user_data.username,
        User.password: get_password_hash(new_user_data.password)
    })
    db.commit()
    return get_user(db, user_id)

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

# ------ Task CRUD operations ------
def create_task(db: Session, task, user_id: int):
    db_task = Task(user_id=user_id, title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks_for_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, new_task_data):
    db.query(Task).filter(Task.id == task_id).update({
        Task.title: new_task_data.title,
        Task.description: new_task_data.description,
        Task.completed: new_task_data.completed
    })
    db.commit()
    return get_task_by_id(db, task_id)

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
