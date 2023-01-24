from pathlib import Path

root_dir = Path("files")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if(path.is_file()):
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '-' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)