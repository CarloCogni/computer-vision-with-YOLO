import os
from pathlib import Path

# The list of directories to ignore
IGNORE_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'env', 'node_modules', '.idea', '.vscode'}
OUTPUT_FILE = "repo_tree.txt"


def generate_tree(directory, file_obj, prefix=""):
    path = Path(directory)

    try:
        # Get all entries, filter out ignored ones, and sort them
        entries = sorted([e for e in path.iterdir() if e.name not in IGNORE_DIRS])
    except PermissionError:
        print(f"{prefix}[Access Denied]", file=file_obj)
        return

    entries_count = len(entries)

    for i, entry in enumerate(entries):
        is_last = (i == entries_count - 1)
        connector = "└── " if is_last else "├── "

        print(f"{prefix}{connector}{entry.name}", file=file_obj)

        if entry.is_dir():
            # Add proper spacing for the next level
            extension = "    " if is_last else "│   "
            generate_tree(entry, file_obj, prefix + extension)


if __name__ == "__main__":
    target_dir = "."
    root_name = Path(target_dir).resolve().name

    # Open the file and write the tree
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        print(f"--- Repository Tree ---", file=f)
        print(f"{root_name}/\n", file=f)
        generate_tree(target_dir, f)
        print("-----------------------", file=f)

    print(f"Done! The tree has been saved to '{OUTPUT_FILE}'.")