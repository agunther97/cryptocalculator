def test1():
    return 1
def test2(x):
    return x
def test3(x,y):
    return x*y
registerFunction("test1",{
    "name":"Test Function 1",
    "arguments_short":[],
    "arguments":[],
    "description":"Test func that returns 1"
})
registerFunction("test2",{
    "name":"Test Function 2",
    "arguments_short":["x"],
    "arguments":["num1"],
    "description":"Literally does nothing"
})
registerFunction("test3",{
    "name":"Test Function 3",
    "arguments_short":["x","y"],
    "arguments":["num1","num2"],
    "description":"Multiplies numbers"
})


