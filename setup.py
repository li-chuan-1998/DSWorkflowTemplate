from setuptools import find_packages, setup

setup(
    name='DSWorkflowTemplateSrc',  # You can name your package anything you like
    version='0.1.0',
    packages=find_packages(),  # This will find all packages under the current directory
    install_requires=[  # Add here any project dependencies like pandas, numpy, etc.
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
    ],
)