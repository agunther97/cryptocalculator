import itertools

def irreducible_poly(degree, field_size):
    polys = [1]
    for i in range(degree):
        polys = list(itertools.product(polys, [0,1,2,3,4]))
    polys = [(entry[0][0], entry[0][1], entry[1]) for entry in polys]
    reduceable_count = 0
    for poly in polys:
        for i in range(1, field_size):
            if (pow(i,degree) + poly[1] * i + poly[2]) % field_size == 0:
                print(poly)
                print(i)
                reduceable_count += 1
    print(reduceable_count)