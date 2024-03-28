import matplotlib.pyplot as plt
import pandas as pd
import os
from IPython.display import display, HTML
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from multiprocessing import Pool
from tqdm import tqdm

def display_dfs(dfs:list, captions:list):
    """
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table captions
    """
    output = ""
    combined = dict(zip(captions, dfs))
    for caption, df in combined.items():
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += "\xa0\xa0\xa0"
    display(HTML(output))

def draw_cm(y_test, y_pred, classes):
    cm = confusion_matrix(y_test, y_pred, labels=classes)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
    disp.plot()
    plt.show()
    
def get_eval_res(y_test, y_pred, classes):
    draw_cm(y_test, y_pred, classes)
    print("Overall Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
def get_info(df, thres=5):
    num_nulls = df.isnull().sum().values
    uval = df.nunique().values
    uval = uval[:thres] if len(uval) > thres else uval
    return pd.DataFrame({"name": df.columns, "unique values": df.nunique().values, 
                         "non-nulls": len(df)-num_nulls, "nulls": num_nulls,
                         "type": df.dtypes.values})

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

if __name__ == '__main__':
    pass