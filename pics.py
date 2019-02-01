import random
import math

WIDTH = 500
HEIGHT = 500
PART = 20

def write(f):
    x = WIDTH / PART
    y = HEIGHT / PART
    
    f.write("P3\n")

    dimensions = "{} {}\n".format(WIDTH, HEIGHT)
    f.write(dimensions)

    f.write("255\n")

    plot = []

    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append([])
        plot.append(row)

    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            #r = 255 * j / WIDTH
            #g = 255 * i / HEIGHT
            #b = 255

            if i % 2 == 0:
                g = 255 * j / WIDTH
                b = 255 * (i % y) / y
                r = 255
            else:
                g = 255 * (j % x) / x
                b = 255 * i / HEIGHT
                r = 255
            
            colors = "{} {} {} ".format(r, g, b)

            plot[i][j] = colors

    # circle making stuff
    xcor = 200
    ycor = 200
    radius = 100

    x1 = 0
    y1 = radius

    """
    while y1 > - radius:
        # set colors equal to black
        plot[xcor + x1][ycor + y1] = "{} {} {} ".format(0, 0, 0)
        plot[xcor - x1][ycor + y1] = "{} {} {} ".format(0, 0, 0)

        # move down
        y1 -= 1

        x1 = int( ( radius ** 2 - y1 ** 2 ) ** .5 )
    """ 
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            f.write(plot[i][j])
        f.write("\n")  


        """
        for i in range(HEIGHT):
        for j in range(WIDTH):
        
        
        
        colors = "{} {} {} ".format(r, g, b)
        f.write(colors)

        f.write("\n")
        """
    return;

def main():
    myfile = open("image.ppm", "a")
    write(myfile)
    myfile.close()
    return;

if __name__ == "__main__":
    main()
