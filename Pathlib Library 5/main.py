from pathlib import Path
from datetime import datetime

root_dir = Path("files")

for path in root_dir.glob("**/*"):
    if path.is_file():
        date_created = datetime.fromtimestamp(path.stat().st_ctime)
        date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
        print(type(date_created))
        new_filename = "a" + date_created_str + '_' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)


