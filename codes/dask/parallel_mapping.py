import dask.bag as db

# Cesty ke zpracovávaným souborům
files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]


# Funkce, které se zpracuje soubor a vrátí nějaký výsledek
def process_file(file_name):
    with open(file_name, "r") as f:
        return len(f.read())


if __name__ == "__main__":
    # Namapování funkce, který se má paralelně aplikovat na každý soubor
    bag = db.from_sequence(files)
    mapping = bag.map(process_file)

    # ... dojde vytvoření "grafu úloh" - aplikace funkce
    sum_tasks = mapping.sum()

    # K veškerému výpočtu dojde až zavoláním .compute()
    print("Total number of characters:", sum_tasks.compute())
