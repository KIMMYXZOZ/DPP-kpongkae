table = 0

while table <= 12:
    print(f"Table de  {table}: ", end="")

    i = 0
    while i <= 12:
        print(f" {table*i}", end="")
        i += 1

    print()
    table += 1