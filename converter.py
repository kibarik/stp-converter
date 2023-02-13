import time
import multiprocessing
from functools import partial

import os
from os import listdir
from os.path import isfile, join
import platform
import sys
import glob

if platform.system() == 'Windows': 
    FREECADPATH = glob.glob(r"C:\Program Files\FreeCAD *\bin")
    FREECADPATH = FREECADPATH[0]
    print(FREECADPATH) #in case needed to confirm, uncomment
    
elif platform.system() == 'Darwin': #MacOS
    FREECADPATH = '/Applications/FreeCAD.app/Contents/Resources/lib/'
elif platform.system() == 'Linux': 
    FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.dll file
else:
    print("Error: No recognized system available.")

sys.path.append(FREECADPATH)
import FreeCAD as App
import Part
import Mesh

def converter(filename=""):
    convertedPath = "./converted"
    to_convertPath = "./to_convert"

    to_convert_file =  to_convertPath + "/" + filename
    converted_file = convertedPath + "/"+filename+".stl"

    shape = Part.Shape()
    shape.read(to_convert_file)
    mesh = Mesh.Mesh()
    mesh.addFacets(shape.tessellate(0.01))
    mesh.write(converted_file)

    return converted_file