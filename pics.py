import random

WIDTH = 500
HEIGHT = 500


def write(f):
    f.write("P3\n")

    dimensions = "{} {}\n".format(WIDTH, HEIGHT)
    f.write(dimensions)

    f.write("255")

    for i in range(WIDTH):
        for j in range(HEIGHT):
            r = random.randint(0, 255)

        
    return;

def main():
    myfile = open("image", "a")
    write(myfile)
    myfile.close()
    return;

if __name__ == "__main__":
    main()
