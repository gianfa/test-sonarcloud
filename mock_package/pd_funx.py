# %%
import pd
import np

df = pd.DataFrame(
    {'A': [1, 2, 3],
     'B': [4, 5, 6],
     'C': [7, 8, 9]})


def new_fun():
    return True

def pd_funx():
    
    # CSmell_1: Loop in DF 
    for x in df:
        print(x)

    # Bug?
    pandas.read_csv("my_csv.csv")

    return True