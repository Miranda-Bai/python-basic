import execjs

with open("example.js", "r") as f:
    js_func = execjs.compile(f.read())

result = js_func.call("<function name>", "<parameters the function needs>")

print(result)