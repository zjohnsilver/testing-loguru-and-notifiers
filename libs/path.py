import os


def get_folders_names_from_path(path="."):
    d = path
    root_folders_names = [
        os.path.join(d, o)
        for o in os.listdir(d)
        if os.path.isdir(os.path.join(d, o))
    ]

    return root_folders_names

def create_folders_if_not_exists(folder_names = [], path=""):
    for folder_name in folder_names:
        folder_name = folder_name.split("/")[1]
        folder_path = os.path.join(path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  