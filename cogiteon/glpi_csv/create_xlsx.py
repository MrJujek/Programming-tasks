import pandas as pd

# Load the existing file
existing_df = pd.read_excel("pandas_to_excel.xlsx", sheet_name="new_sheet_one")

new_data = {
    "Fruits": ["Banana", "Grapes"],
    "Sales": [150, 250]
}

new_df = pd.DataFrame(new_data)

updated_df = existing_df.append(new_df, ignore_index=True)

updated_df.to_excel("pandas_example.xlsx", index=False, sheet_name="Sheet_one")


######### nie dziala