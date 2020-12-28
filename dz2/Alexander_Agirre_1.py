ten_types = [10, 11.0, "doc", True, None, {10, "doc"},
             b'doc', ("doc", 10, True), ["doc", 22], {"name": "Серёжа"}]
for ten in ten_types:
    print(f"{str(ten):20}: type={type(ten)}")
