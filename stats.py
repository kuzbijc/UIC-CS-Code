
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
       
def histo(file):
    df = pd.read_csv(file)  
    y = df["score"]
    plt.hist(y)
    plt.xlabel("ACT Score")
    plt.ylabel("ACT Score Frequency")
    plt.show()
    print(np.mean(y))
    print(np.std(y))
    print(max(y))
    print(min(y))
    print(len(y))
   
def main():
    histo("act.csv")

main()


