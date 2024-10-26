import os
from pathlib import Path
import logging
# from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'nlp-text-summary-generator'

files_list = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for filepath in files_list: 
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    
    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir}')
    
    # Create an empty file if it doesn't exist
    if not file_path.exists():
        file_path.touch()
        logging.info(f'Created file: {file_path}')
    else:
        logging.info(f'File already exists: {file_path}')
