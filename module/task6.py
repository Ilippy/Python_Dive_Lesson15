# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
from pathlib import Path
from collections import namedtuple

Path('log').mkdir(exist_ok=True)
FORMAT = "%(levelname)s: %(asctime)s - %(message)s"
LOG_FILE_NAME = "log/file.log"
# logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

handler = logging.FileHandler(LOG_FILE_NAME, encoding="UTF-8")
handler.setFormatter(logging.Formatter(FORMAT))
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def out_parser():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-p', '--path', metavar='path', default=str(Path.cwd()))
    result = parser.parse_args()
    return result.path


def task6(path: str):
    path = Path(path)
    if not path.is_dir():
        error_text = f"Папки с путем '{path}' не найдено"
        logger.error(error_text)
        raise ValueError(error_text)
    PathElement = namedtuple("PathElement", ['name', 'extension', 'directory', 'parent_dir'])
    path_element_list = []
    for file in path.iterdir():
        temp_path = path / file
        name = temp_path.stem
        suffix = temp_path.suffix or 'directory does not have extension'
        directory = temp_path.is_dir()
        parent_dir = temp_path.parent.stem
        logger.info(f"file/dir name: {name}, suffix: {suffix}, directory: {directory}, parent_dir: {parent_dir}")
        path_element_list.append(PathElement(name, suffix, directory, parent_dir))
    return path_element_list
