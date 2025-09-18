import zipfile as zf
import pathlib

def make_zip(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,'compressed1.zip')
    with zf.ZipFile(dest_path, 'w') as zip:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath, filepath.name)