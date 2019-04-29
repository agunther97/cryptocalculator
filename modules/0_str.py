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
def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result
def subscript(strv):
    if type(strv)!=str:
        strv=str(strv)
    return strv.translate(SUBSCRIPT)
def superscript(strv):
    if type(strv)!=str:
        strv=str(strv)
    return strv.translate(SUPERSCRIPT)
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
