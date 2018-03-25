import math

def main():
    a,b,c = [float(x) for x in input("What are the values of a, b and c : ").split(' ')]
    d = float((b**2) - (4 * a * c))
    if d >= 0:
        qs = math.sqrt(d)
        if a == 0:
            r = -c/b
            print("When a = %.3f, b = %.3f and c = %.3f, \n\nSince a = 0, the linear Equation has a single real root & \
                 \n\nThe root is r = %.7f" % (a, b, c, r))
        elif d > 0:
            r1 = (-1*b + qs)/(2*a)
            r2 = (-1*b - qs)/(2*a)
            print("When a = %.3f, b = %.3f and c = %.3f, \n\nthe Quadratic Equation has two real roots & \
                 \n\nThe roots are r1 = %.7f & r2 = %.7f" % (a, b, c, r1, r2))
        else :
            r = (-1 * b) / (2 * a)
            print("When a = %.3f, b = %.3f and c = %.3f, \n\nthe Quadratic Equation has a single real root & \
                 \n\nThe root is r = %.7f" % (a, b, c, r))
    else:
        rRe = (-1*b)/(2*a)
        rIm = (math.sqrt(-d)/(2*a))
        print("When a = %.3f, b = %.3f and c = %.3f, \n\nthe Quadratic Equation has two complex roots & \
        \n\nThe complex roots are r1 = " %(a,b,c) + str(complex(rRe, rIm)) + " & r2 = " + str(complex(rRe, -rIm)))

main()


    # if a == 0:
    #     r = (-1*c)/b
    #     print("When a = %.3f, b = %.3f and c = %.3f, \nSince a=0, the Quadratic Equation has single real root & \
    #     \nThe root is r = %.7f" % (a, b, c, r))
    # elif d > 0:
    #     r1 = (-1*b + qs)/(2*a)
    #     r2 = (-1*b - qs)/(2*a)
    #     print("When a = %.3f, b = %.3f and c = %.3f, \nthe Quadratic Equation has two real roots & \
    #     \nThe roots are r1 = %.7f & r2 = %.7f" % (a, b, c, r1, r2))
    # elif d == 0:
    #     r = (-1 * b) / (2 * a)
    #     print("When a = %.3f, b = %.3f and c = %.3f, \nthe Quadratic Equation has single real root & \
    #     \nThe root is r = %.7f" % (a, b, c, r))
