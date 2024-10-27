import os
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from nlp_text_summary_generator.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read YAML

    Args:
        path_to_yaml (Path): Path

    Raises:
        ValueError: 'YAML Empty'
        e: Error

    Returns:
        ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'YAML File: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('YAML file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories from the list of directories

    Args:
        path_to_directories (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created Directory at: {path}')

@ensure_annotations
def get_size(path: Path) -> str:
    """Return size of file

    Args:
        path (Path): Path

    Returns:
        str: Size in KBs
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'