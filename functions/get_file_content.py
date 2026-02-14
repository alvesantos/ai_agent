import os

def get_file_content(working_directory, file_path):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(file_path)

    same_dir = os.path.commonpath([base]) == os.path.commonpath([base, target])

    if not same_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    is_file = os.path.isfile(file_path)

    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'