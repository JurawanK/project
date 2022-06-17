from fastapi import FastAPI
import uvicorn

from action import Action
a = Action

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add_hw")
async def add_hw(name, hw_name):
    data = a.addHW(name, hw_name)
    
@app.get("/delete_hw")
async def update_status_hw(ID):
    data = a.DeleteHW(ID)
    return data

@app.get("/get_hw")
async def get_hw(ID):
    data = a.getHWByID(ID)
    return data

#'CLOSE', 'OPEN'
@app.get("/update_status_hw")
async def update_status_hw(ID, status):
    data = a.updateStatusHW(ID, status)
    return data


@app.get("/update_value")
async def update_value_hw(ID, value):
    data = a.updateValueHW(ID, value)
    return data

@app.get("/get_all_hw")
async def get_all_hw():
    data = a.getAllHW()
    return data

@app.get("/get_value_hw")
async def get_value_hw(ID):
    data = a.getValueHWByID(ID)
    return data

@app.get("/get_status_hw")
async def get_status_hw(ID):
    data = a.getStatusHWByID(ID)
    return data

@app.get("/update_status_value")
async def updateStatusValueHW(ID, status, value):
    data = a.updateStatusValueHW(ID, status, value)
    return data

#'ON','OFF'
@app.get("/get_auto_hw")
async def get_auto_hw(ID):
    data = a.getAutoHWByID(ID)
    return data

@app.get("/update_auto_hw")
async def update_auto_hw(ID, auto):
    data = a.updateAutoHW(ID, auto)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.128.48", port=80) 
           