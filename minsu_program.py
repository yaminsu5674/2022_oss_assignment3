from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
app = FastAPI()

numbers = []


@app.exception_handler(RequestValidationError)
async def handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"result": "Error"}),
    )


@app.post("/numbers")
async def addNumber(new: int):
    if type(new) == int:
        numbers.append(new)
        return {"result": "OK"}


@app.get("/numbers/average")
async def getAverage():
    if len(numbers) == 0:
        return{"result": "No numbers in the array"}
    else:
        average = 0
        for num in numbers:
            average += num
        average = average/len(numbers)
        average = str(average)
        return {"result": average}


@app.get("/numbers/sum")
async def getSum():
    if len(numbers) == 0:
        return{"result": "No numbers in the array"}
    else:
        sum = 0
        for num in numbers:
            sum += num
        sum = str(sum)
        return{"result": sum}

#not nothing


@app.get("/numbers/stddev")
async def getStddev():
    if len(numbers) == 0:
        return{"result": "No numbers in the array"}
    else:
        average = 0
        for num in numbers:
            average += num
        average = average/len(numbers)
        stddev = 0
        for num in numbers:
            temp = abs(average - num)
            temp = temp**2
            stddev += temp
        stddev = stddev**(1/2)
        stddev = str(stddev)
        return{"result": stddev}
