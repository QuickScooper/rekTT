from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def hello(name: str = None, message: str = None):
    return f'Hello {name}! {message}!'
