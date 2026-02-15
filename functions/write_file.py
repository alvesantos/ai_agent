import os

def write_file(working_directory, file_path, content):
    try:
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        same_dir = os.path.commonpath([base]) == os.path.commonpath([base, target])

        if not same_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        is_dir = os.path.isdir(target)

        if is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(name=os.path.dirname(target), exist_ok=True)

        with open(target, 'w') as file:
            file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as error:
        return f"Error: {error}"
