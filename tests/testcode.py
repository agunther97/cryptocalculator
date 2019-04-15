import timeit
print("sam:")
print(sam(1234,1234567890,123456))
print("pow:")
print(pow(1234,1234567890,123456))

t1 = (timeit.timeit("sam(12345,67890,12345)",number=1000,globals=dict(globals(),**locals())))
def sam(x,y,z):
    return pow(x,y,z)
t2 = (timeit.timeit("sam(12345,67890,12345)",number=1000,globals=dict(globals(),**locals())))

print("sam time:")
print(t1)
print("pow time:")
print(t2)
