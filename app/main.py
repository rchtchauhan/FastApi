
from . import models
from .database import engine
from sqlmodel import select
from fastapi import Depends, FastAPI
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# models.Base.metadata.create_all(bind=engine)   #this create the table in postgres but we don't need it now 
                                                      #becaause we are using alembic



app.include_router(posts.router)
app.include_router(users.router)           
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return {"hello": "worlds"}


# @app.post('/posts',status_code=status.HTTP_201_CREATED)
# def create_post(post : Post):
#     cursor.execute(""" INSERT INTO posts(title, content, publisher) values (%s, %s, %s) RETURNING * """, (post.title,post.content, post.publisher))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data":new_post}

# @app.get("/post/{id}")
# def get_post(id: int):
#     cursor.execute(""" SELECT * FROM posts WHERE id  = %s """,(str(id),))
#     post = cursor.fetchone()
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     else:
#         return {"post details":post}


# @app.delete("/post/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     cursor.execute(""" DELETE from posts where id = %s RETURNING * """,(str(id))
#                    )
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
    


# @app.put("/posts/{id}")
# def update_post(id:int,post:schema.Post):
     
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, publisher = %s WHERE id = %s RETURNING * """,(post.title,post.content,post.publisher,str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post ==None:                    
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     return {"Updated post":updated_post}









#---------------------sqlalchemy ORM queries-------------------------------------------------
#this is for 
# @app.get('/sqlalchemy')
# def test_post(db: Session = Depends(get_db)):
#      posts = db.query(models.Post).all()
#      return {"post":posts}



# @app.get('/posts')
# def get_data(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts


# @app.post('/posts',status_code=status.HTTP_201_CREATED, response_model= schema.Post)
# def create_post(post : schema.PostCreate,db: Session = Depends(get_db)):

#     ''' this is length process to fill into table we use dictionary for this'''
#     # new_post = models.Post(title=post.title, content = post.content, publisher = post.publisher)

#     new_post = models.Post(**post.model_dump())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post

# @app.get("/post/{id}")
# def get_post(id: int,db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     else:
#         return post



# @app.put("/posts/{id}")
# def update_post(id:int,post:schema.PostCreate):
     
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, publisher = %s WHERE id = %s RETURNING * """,(post.title,post.content,post.publisher,str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post ==None:                    
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     return updated_post



# @app.delete("/post/{id}")
# def delete_post(id:int,db: Session = Depends(get_db)):
#     deleted_post = db.query(models.Post).filter(models.Post.id == id)
#     if deleted_post.first() == None:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     deleted_post.delete(synchronize_session=False)

#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.post('/users',status_code=status.HTTP_201_CREATED, response_model= schema.UserOut)
# def create_user(user : schema.UserCreate,db: Session = Depends(get_db)):
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password

#     ''' this is length process to fill into table we use dictionary for this'''
#     # new_post = models.Post(title=post.title, content = post.content, publisher = post.publisher)

#     new_user = models.User(**user.model_dump())

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user



# @app.get("/user/{id}",response_model= schema.UserOut)
# def get_post(id: int,db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if user == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your post with {id} does not found")
#     else:
#         return user