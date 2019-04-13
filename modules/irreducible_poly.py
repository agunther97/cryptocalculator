import itertools

def irreducible_poly(degree, field_size):
    polys = [1]
    product_list = [i for i in range(field_size)]
    for i in range(degree):
        polys = list(itertools.product(polys, product_list))
    flat_polys = []
    for entry in polys:
        entry_str = str(entry)
        poly_pieces= []
        for letter in entry_str:
            if str.isdigit(letter):
                poly_pieces.append(int(letter))
        flat_polys.append(poly_pieces)
    reduceable_count = 0
    for poly in flat_polys:
        for i in range(0, field_size):
            if (pow(i,degree) + poly[1]*i + poly[2]) % field_size == 0:
                reduceable_count += 1
                break
    print((len(polys) - reduceable_count) * (field_size - 1))

registerFunction("irreducible_poly", {
    "name" : "Find the number of irreducible polynomials for a field size",
    "arguments_short":["degree","field_size"],
    "arguments":["the degree of the polynominal", "the field size (i.e. Z mod #)"],
    "description":"Returns the number of irreducible polynomials for a given field size"
})