from .. import models, utils, schema
from sqlalchemy import func
from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import List, Optional
from .. import outh2
#---------------------sqlalchemy ORM queries-------------------------------------------------

router = APIRouter(
     prefix='/posts',
     tags=['Posts']
)

# @router.get('/')
@router.get('/', response_model= List[schema.PostOut])
def get_post(db: Session = Depends(get_db),user_id :int = Depends(outh2.get_current_user), limit : int = 10, skip:int = 0,
             search : Optional[str] = ""):
    
    
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, 
                 models.Post.id == models.Vote.post_id, 
                    isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # posts = list ( map (lambda x : x._mapping, posts))
    
    
    return posts


@router.post('/',status_code=status.HTTP_201_CREATED, response_model= schema.Post)
def create_post(post : schema.PostCreate,db: Session = Depends(get_db), current_user :int = Depends(outh2.get_current_user)):

    ''' this is length process to fill into table we use dictionary for this'''
    # new_post = models.Post(title=post.title, content = post.content, publisher = post.publisher)
    new_post = models.Post(owner_id = current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}",response_model= schema.PostOut)
def get_post(id: int,db: Session = Depends(get_db), user_id :int = Depends(outh2.get_current_user)):
    post = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, 
                 models.Post.id == models.Vote.post_id, 
                    isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
    else:
        return post



# @router.put("/posts/{id}")
# def update_post(id:int,post:schema.PostCreate):
     
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, publisher = %s WHERE id = %s RETURNING * """,(post.title,post.content,post.publisher,str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post ==None:                    
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     return updated_post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db), current_user :int = Depends(outh2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = post.first()
    print(post.__dict__)

    if deleted_post == None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
    if deleted_post.owner_id != current_user.id:
         raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = "NOT ATHORISHED TO DELETED THIS")  
    post.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)