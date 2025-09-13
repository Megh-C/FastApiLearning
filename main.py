from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'Megh','Age':'19'}}

@app.get('/about')
def about():
    return {'about':'This is the About Page'}