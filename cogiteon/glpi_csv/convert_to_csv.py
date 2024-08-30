import pandas as pd
import os

def fix_df(df: pd.DataFrame) -> pd.DataFrame:
    to_delete = [x for x in list(df.columns) if x in ["lp", "LP", "lp.", "LP.", "Lp", "Lp."]]
    return df.drop(columns=to_delete)

def convert_to_csv(filename: str) -> None:
    xls = pd.ExcelFile(filename)
    worksheets = xls.sheet_names

    if len(worksheets) == 1:
        df = pd.read_excel(xls)
        name = filename.split(".")[:-1]
        csv_file = "./csv/" + '.'.join(name) + ".csv"
        
        df = fix_df(df)

        df.to_csv(csv_file, index=False, sep=";", encoding="utf-8")
        
        print(f"'{filename}' was successfully converted to '{csv_file}'.")

    else:
        for worksheet in worksheets:
            if any(to_check in worksheet for to_check in ["Arkusz", "arkusz", "Worksheet", "worksheet", "Sheet", "sheet", "Wykres", "wykres", "Chart", "chart", "Graph", "graph"]):
                continue
            
            else:
                df = pd.read_excel(xls, sheet_name=worksheet)
                csv_file = f"./csv/{worksheet}.csv"

                df = fix_df(df)

                df.to_csv(csv_file, index=False, sep=";", encoding="utf-8")
                
                print(f"Sheet '{worksheet}' from '{filename}' was successfully converted to '{csv_file}'.")


if __name__ == "__main__":
    os.makedirs("csv", exist_ok=True)

    for filename in os.listdir("."):
        if filename.endswith(("xls", "xlsx")):
            try:
                convert_to_csv(filename)
            except Exception as e:
                print(f"Error: {e}")
