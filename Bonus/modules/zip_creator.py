import zipfile
import pathlib


def compress2zip(filepaths, dest_dir):
    """
    Compress given files to a .zip
    """
    # Use Path for create paths in differents OS
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    compress2zip(filepaths=["./__init__.py"], dest_dir="./")