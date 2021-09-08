import os
import argparse
import importlib
from pathlib import Path
from libs.path import get_folders_names_from_path
from core.logger import logger

BASE_DIR = Path(__file__).resolve().parent


if __name__ == "__main__":
    folder_path = os.path.join(BASE_DIR, "logs")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    root_folders_names = get_folders_names_from_path(".")

    process_folders_names = [
        folder_name for folder_name in root_folders_names if "P" in folder_name
    ]

    for process_folder_name in process_folders_names:
        process_folder_name = process_folder_name.split("/")[1]
        folder_path = os.path.join(BASE_DIR, "logs", process_folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--process",
        required=False,
        help="Number of process you want execute",
    )
    parser.add_argument(
        "-f",
        "--folder",
        required=False,
        help="relative folder of your process",
    )
    parser.add_argument("-s", "--script", help="filename of script")
    parser.add_argument(
        "-ptf", "--path_to_file", help="path to the file you wants to execute"
    )

    args = parser.parse_args()

    if args.path_to_file:
        module = importlib.import_module("%s" % (args.path_to_file))

    elif args.process:
        process_number = int(args.process)

        logger.add(
            os.path.join(
                BASE_DIR,
                "logs/P%03d/{time:YYYY-MM-DD}.log" % (process_number),
            ),
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            enqueue=True,
        )
        module = importlib.import_module("P%03d.main" % (process_number))

    elif args.folder and args.script:
        module = importlib.import_module(
            "%3s.%3s" % (args.folder, args.script)
        )

    else:
        raise Exception(
            "Invalid Arguments... Check main.py for list of possible arguments"
            "for program execution"
        )
