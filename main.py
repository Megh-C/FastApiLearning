from fastapi import FastAPI
from typing import Optional

app = FastAPI()
id = 4

@app.get('/')
def index():
    return {'data':{'name':'Megh','Age':'19'}}


#the get is the operation the () value is the path and the decorator is the path opertaino decorator
@app.get('/about')
# function is called path operation function
def about():
    return {'about':'This is the About Page'}

#passing dynamic parameters then need to pass the same in the function also
@app.get('/blog/{id}')
def getOneBlog(id:int):
    return {'Blog': id}

@app.get('/optionalBlog')
def getOptional(limit:int=10,published:bool=True,sorted : Optional[str]=None):
    if(published):
        return{'data':f'published blogs are max {limit}'}
    else:
        return{'data':f'blogs are max {limit}'}
