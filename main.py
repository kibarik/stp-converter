from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import ntpath
import os

from converter import converter

app = FastAPI()
TO_CONVERT = "./to_convert"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload", response_class=FileResponse)
async def convert_file(file: UploadFile):
    fname = f"{file.filename}"
    fpath = TO_CONVERT+f"/{fname}"

    with open(fpath, 'wb') as out_file:
        content = file.file.read()  # async read
        out_file.write(content)  # async write

    converted_file = converter(filename=fname)
    s = os.path.abspath(converted_file)
    fname = s.replace(os.sep,ntpath.sep)
    return FileResponse(fname, media_type="application/octet-stream")

@app.get("/example", response_class=FileResponse)
async def example():
    s = "C:\\Users\\Администратор\\Desktop\\converter\\converted\\example.stp.stl"
    file = "./converted/example.stp.stl"
    s = os.path.abspath(file)
    fname = s.replace(os.sep,ntpath.sep)
    return FileResponse(fname, filename="example.stl", media_type="application/octet-stream")