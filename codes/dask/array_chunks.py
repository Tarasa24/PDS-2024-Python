import dask.array as da

# Rozdělení výpočtu na poli
arr = da.random.random(1000000, chunks=100000)
print("Sum of the array:", arr.sum().compute())
