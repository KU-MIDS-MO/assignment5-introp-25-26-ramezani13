def approx_real_root(coeffs, interval):

    a, b = interval
    c0, c1, c2, c3 = coeffs

    #my function
    def p(x):
        return c3*x*x*x+c2*x*x+c1*x+c0

    fa = p(a)
    fb = p(b)

    #bisection method untill the required accuracy i need  ~1e-9 is reached
    while (b - a) > 1e-10:     # smaller interval ⇒ midpoint accurate to 1e-10
        m = (a + b) / 2
        fm = p(m)

        #subinterval where the sign change
        if fa * fm <= 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    #midpoint is my root approximation
    return (a + b) / 2


