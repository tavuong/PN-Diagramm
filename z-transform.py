import turtle
import math
import cmath
import json
import numpy as np

def main():
 
    print("--------------------")
    print("| Z-Transform      |")
    print("| curve analysis   |")
    print("| Turtle Graphics  |")
    print("--------------------\n")

#   PN-point read - json file
#   Define PN_points array
    POINT_NUMBER = 4
    
    point_zero = [ complex(0, i) for i in range(POINT_NUMBER) ]
    point_pole = [ complex(0, i) for i in range(POINT_NUMBER) ]
    z_jsonRead(point_pole,point_zero, POINT_NUMBER)
    print (point_zero)
    print (point_pole)

    # turtle.delay is 10ms (default).
    turtle.delay(0)

    draw_axes(150)
    draw_Abs_Axes(150)   

# ----PLOT ------------------
    plotz("z(jωT)", 100, 0, 360,point_zero, point_pole,POINT_NUMBER, z_circle)
    draw_PNpoints (point_zero, point_pole, POINT_NUMBER)
    plotz("H(z) funtion", 100, 0, 360,point_zero, point_pole,POINT_NUMBER, z_function)
    plotz("abs H(z)", 150, 0, 360,point_zero, point_pole,POINT_NUMBER, z_abs)
    

    turtle.hideturtle()

    # This stops the window closing after drawing is finished
    turtle.exitonclick()


def draw_axes(radius):

    """
    Draw lines from the origin every
    15 degrees with the angles labelled.
    """

    FONT_SIZE = 8
    FONT = ("Arial", FONT_SIZE, "bold")

    width = radius * 2 +  500
    height = radius * 2 + 500

    turtle.title("Polar Plot")

    turtle.screensize(canvwidth=width, canvheight=height)
    turtle.setup(width=width + 40, height=height + 40)
    turtle.shape("turtle")

    degree_label_radius = radius + 16

    
    turtle.pencolor(0.0, 0.0, 1.0)

    for degrees in range(0, 360, 90):

        radians = math.radians(degrees)

        turtle.penup()
        turtle.home()

        turtle.pendown()
        turtle.goto(math.cos(radians) * radius, math.sin(radians) * radius)

        turtle.penup()
        turtle.goto(math.cos(radians) * degree_label_radius,
                    math.sin(radians) * degree_label_radius)

        turtle.goto(turtle.position()[0], turtle.position()[1] - FONT_SIZE)

        turtle.pendown()
        turtle.write(str(degrees) + u'\u00B0', align='center', font=FONT)

def draw_Abs_Axes(radius):
    FONT_SIZE = 8
    FONT = ("Arial", FONT_SIZE, "bold")
    turtle.penup()
    turtle.home()
    turtle.pencolor(1.0, 0.0, 0.0)
    turtle.goto(-20, radius-350)
    turtle.pendown()
    turtle.write(str('|H(ω)|') , align='left', font=FONT)
    turtle.penup()
    turtle.goto(0, radius-350)
    turtle.pendown()
    turtle.goto(0, radius-450)
    turtle.penup()
    turtle.goto(-10, radius-450)
    turtle.pendown()
    turtle.write(str('1') , align='left', font=FONT)
    turtle.penup()
    turtle.goto(0, radius-450)
    turtle.pendown()
    turtle.goto(0, radius-500)
    #turtle.penup()
    turtle.pendown()
    turtle.write(str('0') + u'\u00B0', align='center', font=FONT)
    turtle.penup()
    turtle.pendown()
    turtle.goto(math.pi*100, radius-500)
    turtle.penup()
    turtle.pendown()
    turtle.write(str('360') + u'\u00B0', align='center', font=FONT)
    turtle.penup()

def draw_PNpoints (point_zero, point_pole,POINT_NUMBER):
    print (point_zero)
    print (point_pole)

#   PN position calculate 
    zpt = complex (0+0*1j)
    for i in range (POINT_NUMBER):
        zpt = point_pole[i]
        if zpt.real < 10: 
          draw_point(100,"x",zpt.real,zpt.imag)
 
    for k in range (POINT_NUMBER):
        zpt = point_zero[k]
        if zpt.real < 10 : 
            draw_point(100,"o",zpt.real,zpt.imag)
    return{}

def draw_point(radius,text,x,y):
    FONT_SIZE = 12
    FONT = ("Arial", FONT_SIZE, "bold")

    turtle.pencolor(1.0, 0.0, 0.0)
    turtle.penup()
    z = complex (x,y)
    print ("point: " + text + str(x) + ", " + str(y))
    distance = abs(z)*radius
    radians = cmath.phase(z)
    turtle.goto (math.cos(radians)*distance,math.sin(radians)*distance - FONT_SIZE)
    turtle.pendown()
    turtle.write(str(text), align='center', font=FONT)
    return {}

def plotz(title, radius, start_degrees, end_degrees,point_zero, point_pole,POINT_NUMBER, function):
# polar plot for z-varaiable and z-funktion
    turtle.title(title)

    turtle.pensize(2)
    turtle.pencolor(0.0, 0.0, 1.0)
    turtle.penup()
    for degrees in range(start_degrees, end_degrees + 1):
        radians = math.radians(degrees)

        pos = function(point_zero, point_pole,POINT_NUMBER,radians, radius)

        turtle.goto(pos["x"], pos["y"])
# titel
# textband = title +": ω= " + str(radians)
        textband = title
        turtle.title(textband)
 
        turtle.pendown()

def z_circle(point_zero, point_pole,POINT_NUMBER,radians, radius):

#    draw unit-circle with z variable moving
    return {"x": math.cos(radians) * radius,
            "y": math.sin(radians) * radius}


def z_jsonRead(point_pole, point_zero,POINT_NUMBER):

    # reading PN-Points from JSON-file

    data = {}
    data['point'] = []
    sname =""
    sname = input ('PN-Points data file:')
    if sname =="":
        json_file = open ('data.txt', "r")
    else: 
        json_file = open (sname, "r")
    data = json.load(json_file)
# pretty dump for Data File
    print(json.dumps(data, sort_keys=True, indent=4))

#   print(json.dumps(data))
#   for p in data['point']:
#        print('type: ' + p['type'])
#        print('re: ' + str(p['re']))
#        print('im: ' + str(p['im']))
#        print('')
# -------- complex array
#   import numpy as np
#   point_zero = [ complex(0, i) for i in range(4) ]
#   print (point_zero)
#   point_pole = [ complex(0, i) for i in range(4) ]
#   print (point_pole)

    i = 0
    for i in range (POINT_NUMBER):
        point_pole [i] = complex (10,0)
        point_zero [i] = complex (10,0)

    i = 0
    k = 0
    for p in data['point']:
        if p['type'] == "":
            continue

        if p['type'] == "p":
            point_pole [i] = complex (float(p['re']),float(p['im'] ))
            i =i + 1

        if p['type'] == "z":
            point_zero [k] = complex (float(p['re']),float(p['im'] ))
            k=k+1
    print (point_pole)
    print (point_zero)
    return {}

def z_function(point_zero, point_pole,POINT_NUMBER, radians, radius):

    """
    H(z) = (z - z00)*(z - z01) / (z - zp0)(z - zp1)
    H(z) == z_h1 / z_h2

    z == e-jωT , T = 1/F , F is samplingrate
    In Programm z = 1.e-jωT 
    z =  complex (radians,radius): from input function
    H(z) = h_z = complex (x + jy): return parameter 
    """ 
    turtle.pencolor(1.0, 0.0, 1.0)


#   PN position calculate 

    z   = complex (math.cos(radians), math.sin(radians))

   # H(z) caluclate
   # H(z) == z_h1 / z_h2
    zpt = complex (0+0*1j)
    z_h1 = complex (1+0*1j)
    z_h2 = complex (1+0*1j)    
    z_abs = 1.
    z_phase = 0
    z_re =1.0
    z_im =1.0
    for i in range (POINT_NUMBER):
        zpt = point_zero[i]
        if zpt.real == 10:
            continue 
        else:
            z_abs  =  abs(z-zpt)
            z_abs  =  abs (z_h1)*z_abs
            z_phase = cmath.phase (z-zpt)
            z_phase = cmath.phase(z_h1) + cmath.phase (z-zpt)
            z_re= z_abs*cmath.cos(z_phase) 
            z_im = z_abs*cmath.sin(z_phase)
            z_h1 = complex(z_re + z_im*1j)
    for k in range (POINT_NUMBER):
        zpt = point_pole[k]
        if zpt.real >= 10:
            continue
        else:
            z_abs  =  abs(z-zpt)
            z_abs  =  abs (z_h2)*z_abs
            z_phase = cmath.phase (z-zpt)
            z_phase = cmath.phase(z_h2) + cmath.phase (z-zpt)
            z_re= z_abs*cmath.cos(z_phase) 
            z_im = z_abs*cmath.sin(z_phase)
            z_h2 = complex(z_re + z_im*1j)
        
    # |H(z)| == distance  
    # dividieren 
    DIS_MAX = 10.0
    if abs(z_h2) != 0:
        distance = abs(z_h1) / abs (z_h2)
    else:
        print ("POLE STELLE is infinitely at w=" + str(radians))
        print ("SET H zu Maximal" + str(DIS_MAX))
        distance = DIS_MAX
    # skalierung für |H(z)| 
    distance = distance * radius
    
    # phase (H(z)) == radians  
    radians  = cmath.phase(z_h1) - cmath.phase (z_h2)
    
    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}

def z_abs(point_zero, point_pole,POINT_NUMBER,radians, radius):

    #   F(z) = z + z0
    #
    
    turtle.pencolor(1.0, 0.0, 0.0)

    z   = complex (math.cos(radians), math.sin(radians))

   # H(z) caluclate
   # H(z) == z_h1 / z_h2
    zpt = complex (0+0*1j)
    z_h1 = complex (1+0*1j)
    z_h2 = complex (1+0*1j)    
    z_abs = 1.
    z_phase = 0
    z_re =1.0
    z_im =1.0
    z_h1_abs = 1.0
    z_h2_abs = 1.0
    for i in range (POINT_NUMBER):
        zpt = point_zero[i]
        if zpt.real == 10:
            break 
        else:
            z_abs  =  abs(z-zpt)
            z_h1_abs  =  z_h1_abs*z_abs

    z_abs = 1.0
    for k in range (POINT_NUMBER):
        zpt = point_pole[k]
        if zpt.real >= 10:
            break 
        else:
            z_abs  =  abs(z-zpt)
            z_h2_abs  =  z_h2_abs *z_abs
        
    
 #   z   = complex (math.cos(radians), math.sin(radians))
 #   z_h1 =  (z - z00)*(z - z01)
 #   z_h2 =  (z - zp0)*(z - zp1)

    # dividieren 
    if z_h2_abs != 0:
        distance = z_h1_abs / z_h2_abs    
    else:
        print ("POLE STELLE is infinitely at w=" + str(radians))
        distance = 10
    # skalierung für |H(w)|
    #   print(radians)
    #   radians is 0-2pi
    #   Scalar radian: 2pi == pi*100
    #   scalar faktor for distance = 50
    #   offset for y  = radius -500
    distance = distance * 50
    return {"x": radians*50,
            "y": distance + radius-500}

main()
