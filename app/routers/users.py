from .. import models, utils, schema
from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post('/',status_code=status.HTTP_201_CREATED, response_model= schema.UserOut)
def create_user(user : schema.UserCreate,db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    ''' this is length process to fill into table we use dictionary for this'''
    # new_post = models.Post(title=post.title, content = post.content, publisher = post.publisher)

    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/{id}",response_model= schema.UserOut)
def get_post(id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
    else:
        return user