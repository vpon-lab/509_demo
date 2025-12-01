
import argparse
from pathlib import Path

def clean_files(folder, ext, delete=False):
    folder = Path(folder)
    count = 0

    # Search recursively for matching files
    for file in folder.rglob(f"*.{ext}"):
        print("Found:", file)
        count += 1

        if delete:
            file.unlink()      # deletes the file
            print("Deleted:", file)

    print("Total files found:", count)
    if delete:
        print("All matching files deleted.")

def main():
    # ---- CLI setup ----
    parser = argparse.ArgumentParser(description="File cleaner CLI tool")

    parser.add_argument(
        "--folder",
        required=True,
        help="Folder to search (e.g., . or /path/to/folder)"
    )

    parser.add_argument(
        "--ext",
        required=True,
        help="File extension to search for (e.g., txt, log, jpg)"
    )

    parser.add_argument(
        "--delete",
        action="store_true",
        help="If provided, delete the matching files"
    )

    args = parser.parse_args()

    # run the tool
    clean_files(args.folder, args.ext, args.delete)

if __name__ == "__main__":
    main()
