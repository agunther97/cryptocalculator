import timeit

a=5
b=5

t1 = (timeit.timeit("irreducible_poly(a,b)",number=100,globals=dict(globals(),**locals())))
t2 = (timeit.timeit("irreducible_poly_verbose(a,b,quiet=True)",number=100,globals=dict(globals(),**locals())))

print("aaron time:")
print(t1)
print("grey time:")
print(t2)

print("a results")
print(irreducible_poly(a,b))
print("g results")
print(irreducible_poly_verbose(a,b,quiet=True))
