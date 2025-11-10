import gint as g
import time as t

def text(x:int,y:int,ctx:str):
    g.dtext(x,y,g.C_BLACK,ctx)
    g.dupdate()

async def intro():
    text(1,1,"-----------Physium Formulae---------")
    text(130,20, "v1.0.0")
    text(1,40,"Physics Solver for Classpad II")
    text(1,60,"By @SciMath-Solvers")
    g.pollevent()



t.sleep(2)