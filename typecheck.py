dataTypes=["str", "int", "float", "bool", "NoneType", "range", "list", "tuple", "set", "dict", "frozenset", "complex", "bytes", "bytearray", "memoryview"]

def check(arg):
    typer = str(type(arg)).split("'")[1]
    if typer in dataTypes:
        return dataTypes[dataTypes.index(typer)]