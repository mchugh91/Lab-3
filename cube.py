__author__ = 'Ciaran'

def surf_area(width):
    surfarea = 6 * width ** 2
    return surfarea

def volume(width):
    vol = width ** 3
    return vol

def main():

    for width in range(1, 10):
        vol = volume(width)
        surf = surf_area(width)
        if surf == vol:
            print("The width when volume and surface area are equal is:", width)
            break


main()