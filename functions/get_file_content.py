import os

def get_file_content(working_directory, file_path):
    try:
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        same_dir = os.path.commonpath([base]) == os.path.commonpath([base, target])

        if not same_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(target)

        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_LENGTH_TO_READ = 10000

        with open(target) as file:
            content = file.read(MAX_LENGTH_TO_READ)
        
            if file.read(1): 
                content += f'[...File "{file_path}" truncated at {MAX_LENGTH_TO_READ} characters]'

        return content
    except Exception as e:
        return f"Error: {e}"