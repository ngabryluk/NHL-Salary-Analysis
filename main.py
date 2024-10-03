import pandas as pd
import os

def main():

    filename = os.listdir(os.path.join(os.getcwd(), "data"))[0]
    filepath = os.path.join(os.getcwd(), "data", filename)

    df = pd.read_excel(filepath)

    print(df)

if __name__ == "__main__":
    main()