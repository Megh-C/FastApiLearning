from fastapi import FastAPI,status , Depends,Response,HTTPException
from . import models,schemas
from .database import engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def welcomeUser():
    return('Hello User')

#will pass the title and the body as the function parameters and its of type Blog pydantic
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog , db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/getAll')
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs 

@app.get('/blog/{id}')
def getBlogById(id:int,response:Response,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return  {'detail':f"The blog with id {id} Does not Exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The blog with id {id} Does not Exist")
                            
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Response':f'The Blog with id {id} is deleted'}

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter()
