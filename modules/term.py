def clear(h=False):
    print(u"{}[2J{}[;H".format(chr(27), chr(27)))
    if h:
        print(welcomeBanner)

registerFunction("clear", {
    "name" : "Clear",
    "arguments_short":["h"],
    "arguments":["display startup message"],
    "description":"Clear terminal and optionally display message"
})