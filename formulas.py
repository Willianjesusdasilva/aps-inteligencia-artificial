class formulas:
    def trimf (self, x, a, b, c):
        if x<=a:
            return 0
        if a<=x and x<=b:
            return (x-a)/(b-a)
        if b<=x and x<=c:
            return (c-x)/(c-b)
        if c<=x:
            return 0

    def tramf(self, x, a, b, c, d):
        if x<=a:
            return 0
        if a<=x and x<=b:
            return (x-a)/(b-a)
        if b<=x and x<=c:
            return 1
        if c<=x and x<=d:
            return (d-x)/(d-c)
        if d<=x:
            return 0