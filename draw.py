from display import *
from matrix import *

  # ====================
  # add the points for a rectagular prism whose
  # upper-left corner is (x, y, z) with width,
  # height and depth dimensions.
  # ====================
def add_box( points, x, y, z, width, height, depth ):
    ftl = (x, y, z)
    ftr = (x+width, y, z)
    fbr = (x+width, y-height, z)
    fbl = (x, y-height, z)
    btl = (x, y, z+depth)
    btr = (x+width, y, z+depth)
    bbr = (x+width, y-height, z+depth)
    bbl = (x, y-height, z+depth)

    #Front top left --> Front top right
    add_edge(points, ftl[0], ftl[1], ftl[2], ftr[0], ftr[1], ftr[2])
    #Front top right --> Front bottom right
    add_edge(points, ftr[0], ftr[1], ftr[2], fbr[0], fbr[1], fbr[2])
    #Front bottom right --> Front bottom left
    add_edge(points, fbr[0], fbr[1], fbr[2], fbl[0], fbl[1], fbl[2])
    #Front botton left --> Front top left
    add_edge(points, fbl[0], fbl[1], fbl[2], ftl[0], ftl[1], ftl[2])

    #Back top left --> Back top right
    add_edge(points, btl[0], btl[1], btl[2], btr[0], btr[1], btr[2])
    #Back top right --> Back bottom right
    add_edge(points, btr[0], btr[1], btr[2], bbr[0], bbr[1], bbr[2])
    #Back bottom right --> Back bottom left
    add_edge(points, bbr[0], bbr[1], bbr[2], bbl[0], bbl[1], bbl[2])
    #Back botton left --> Back top left
    add_edge(points, bbl[0], bbl[1], bbl[2], btl[0], btl[1], btl[2])

    #Front top left --> Back top left
    add_edge(points, ftl[0], ftl[1], ftl[2], btl[0], btl[1], btl[2])
    #Front top right --> Back top right
    add_edge(points, ftr[0], ftr[1], ftr[2], btr[0], btr[1], btr[2])
    #Front bottom left --> Back bottom left
    add_edge(points, fbl[0], fbl[1], fbl[2], bbl[0], bbl[1], bbl[2])
    #Front bottom right --> Back bottom right
    add_edge(points, fbr[0], fbr[1], fbr[2], bbr[0], bbr[1], bbr[2])




  # ====================
  # Generates all the points along the surface
  # of a sphere with center (cx, cy, cz) and
  # radius r.
  # Returns a matrix of those points
  # ====================
def generate_sphere( points, cx, cy, cz, r, step ):
    res = []
    phi = 0
    theta = 0
    for phi in range(0, math.pi * 2, step):
        for theta in range(0, math.pi, step):
            x = r * math.cos(theta) + cx
            y = r * math.sin(theta) * math.cos(phi) + cy
            z = r * math.sin(theta) * math.sin(phi) + cz
            res.append([x,y,z])
    return res




  # ====================
  # adds all the points for a sphere with center
  # (cx, cy, cz) and radius r to points
  # should call generate_sphere to create the
  # necessary points
  # ====================
def add_sphere( points, cx, cy, cz, r, step ):
    for pts in generate_sphere(points, cx, cy, cz, r, step):
        add_point(points, pts[0], pts[1], pts[2])


  # ====================
  # Generates all the points along add_edge(matrix, x, y, z, x+width, y, z)the surface
  # of a torus with center (cx, cy, cz) and
  # radii r0 and r1.
  # Returns a matrix of those points
  # ====================
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    pass

  # ====================
  # adds all the points for a torus with center
  # (cx, cy, cz) and radii r0, r1 to points
  # should call generate_torus to create the
  # necessary points
  # ====================
def add_torus( points, cx, cy, cz, r0, r1, step ):
    pass



def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy

    i = 1
    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0add_edge(matrix, x, y, z, x+width, y, z), x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
