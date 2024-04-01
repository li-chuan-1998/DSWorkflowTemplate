import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

def create_project_structure(base_path):
    directories = [
        "data/raw",
        "data/interim",
        "data/processed",
        "data/external",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/notebook",
        "src/visualization",
        "models",
        "reports",
        "reports/figures",
    ]
    
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        # Creates an empty .gitkeep file to ensure the directory is tracked by Git even if empty
        open(os.path.join(dir_path, '.gitkeep'), 'a').close()
    
    # Creates the main Python package
    open(os.path.join(base_path, "src/__init__.py"), 'a').close()
    
    # Additional files
    additional_files = [
        "environment.yml",
        ".gitignore",
        "README.md",
    ]
    for file_name in additional_files:
        open(os.path.join(base_path, file_name), 'a').close()

    # Create placeholder Jupyter notebooks
    notebooks = [
        "01_data_cleaning.ipynb",
        "02_exploratory_data_analysis.ipynb",
        "03_feature_engineering.ipynb",
        "04_model_training.ipynb",
        "05_model_evaluation.ipynb",
    ]
    for notebook_name in notebooks:
        nb_path = os.path.join(base_path, "notebooks", notebook_name)
        nb = new_notebook()
        name = " ".join([i.capitalize().replace(".ipynb","") for i in notebook_name.split('_')[1:]])
        nb.cells.append(new_markdown_cell(f"# {name}"))
        nb.cells.append(new_code_cell("# Add your code here"))
        nbformat.write(nb, nb_path)

project_name = ""  # Or any other name you've chosen
create_project_structure(project_name if project_name else "./")
