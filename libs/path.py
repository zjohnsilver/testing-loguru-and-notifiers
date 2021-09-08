import os


def get_folders_names_from_path(path="."):
    d = path
    root_folders_names = [
        os.path.join(d, o)
        for o in os.listdir(d)
        if os.path.isdir(os.path.join(d, o))
    ]

    return root_folders_names
