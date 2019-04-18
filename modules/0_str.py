def upper(s):
    return s.upper()
def lower(s):
    return s.lower()
def tintTrueFalse(text, succ):
    if succ:
        text=tcolors.OKGREEN+text
    else:
        text=tcolors.FAIL+text
    text+=tcolors.ENDC
    return text

registerFunction("upper", {
    "name" : "Uppercase",
    "arguments_short":["s"],
    "arguments":["input string"],
    "description":"Converts text to uppercase"
})
registerFunction("lower", {
    "name" : "Lowercase",
    "arguments_short":["s"],
    "arguments":["input string"],
    "description":"Converts text to lowercase"
})