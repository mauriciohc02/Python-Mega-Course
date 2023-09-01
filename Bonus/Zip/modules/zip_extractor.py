import zipfile


def extract_archive(zippaths, dest_dir):
    """
    Extract files from given .zip
    """
    for zippath in zippaths:
        with zipfile.ZipFile(zippath, "r") as archive:
            archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive(zippaths=["./compressed.zip"], dest_dir="../")