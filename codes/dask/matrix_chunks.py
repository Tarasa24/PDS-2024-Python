import dask.array as dusky

# Vytvoří matici 10000x10000, ta je rozdělena na části 1000x1000(chunks), které se zpracují nezávisle na sobě
x = dusky.random.random((10000, 10000), chunks=(1000, 1000))

# Sečte matici s jeho transpozicí
y = x + x.T

# Sečte všechny hodnoty matice
sum_task = y.sum()

# Až nyní se všechny operace provedou
print(sum_task.compute())
