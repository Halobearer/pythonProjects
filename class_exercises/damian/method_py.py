hello = "hello world!!!"
print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.capitalize())
print(hello.casefold())
print(hello.swapcase())
print(hello.count("1"))
print(hello.center(20, "*"))
print(hello.ljust(20, "*"))
print(hello.rjust(20, "*"))
print(hello.endswith("!!!"))
print(hello.replace("!", "q", 1))
print(hello.strip())
print(hello.zfill(20))
print(hello.split("e"))
print("*".join(["a", "b", "c"]))
print(hello.index())

bin = "101100011001011110456"
print(bin.replace("1", "x").replace("0", "1").replace("x", "0"))
print(bin.translate(str.maketrans("01", "10", "456")))

for i in range()
