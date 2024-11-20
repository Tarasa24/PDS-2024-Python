import dask


@dask.delayed
def inc(x):
    return x + 1


@dask.delayed
def add(x, y):
    return x + y


# Vyhodnocením se pouze vytváří graf úloh
a = inc(1)  # nevykoná výpočet
b = inc(2)  # nevykoná výpočet
c = add(a, b)  # nevykoná výpočet

# Vykoná všechny výpočty výše
print(c.compute())
