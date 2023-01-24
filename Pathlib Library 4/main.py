from pathlib import Path

root_dir = Path("files")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if(path.is_file()):
        grandparent_foldername = path.parts[-3]
        parent_foldername= path.parts[-2]
        new_filename = grandparent_foldername + "-" + parent_foldername + "-" + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)