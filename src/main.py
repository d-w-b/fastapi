from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing:str):
    return f"echoing {thing}"

if __name__ == "__main__":
    print("uvicorn 으로 실행합니다.")
    import uvicorn
    uvicorn.run("main:app", reload = True)

