import pandas as pd
import os
from IPython.display import display, HTML
from multiprocessing import Pool
from tqdm import tqdm

def display_dfs(dfs_dict):
    output = ""
    for caption, df in dfs_dict.items():
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += "\xa0\xa0\xa0"
    display(HTML(output))

    
def get_dfs_info(df:pd.DataFrame, thres=5):
    # Print the shape of the DataFrame
    print(f"DataFrame shape (rows, columns): {df.shape}")
    
    # Creating a series that contains samples of unique values for each column
    samples_of_unique_values = df.apply(lambda x: x.dropna().unique()[:thres].tolist())
    
    df_info = pd.DataFrame({
        "name": df.columns,
        "unique values": df.nunique().values,
        "non-nulls": len(df) - df.isnull().sum().values,
        "nulls": df.isnull().sum().values,
        "type": df.dtypes.values,
        "samples of unique values": samples_of_unique_values
    })
    
    return df_info

def read_file(file_path: str):
    return pd.read_excel(file_path) if file_path.endswith(".xlsx") else pd.read_csv(file_path)

def read_ex(filename: str):
    if filename.endswith(".xlsx"):
        df = pd.read_excel(os.path.join('./target_data/',filename))
        df['source'] = filename.replace(".xlsx", "")
        df['source'] = pd.to_datetime(df['source'])
        return df
       
def stack_dfs_mul(folder, limit=None):
    files = [file for file in os.listdir(folder) if file.endswith(".xlsx")]
    with Pool(processes=4) as pool:
        dfs = list(tqdm(pool.imap_unordered(read_ex, files), total=len(files)))
        dfs = [df for df in dfs if df is not None]
    
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame()
    
def save(df:pd.DataFrame, filename:str, folder:str="data/interim/"):
    # by default the file will be saved in cwd, and in csv format
    df.to_csv(f"{folder}/{filename}", index=False)
    print(f"Data saved at {folder}.")

if __name__ == '__main__':
    pass