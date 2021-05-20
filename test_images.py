import re
from collections import defaultdict
from os import walk
from pathlib import Path


def get_files_by_suffix(suffix: str):
    root_folder = Path(__file__).parent
    for root, _, files in walk(root_folder):
        for file in files:
            file = Path(root) / file
            if file.suffix == suffix:
                yield file


def find_links_in_md_file(filepath: Path):
    file_content = filepath.read_text(encoding="utf8")
    pattern = re.compile(r"!\[\w+\]\(([\w./\-_]+)\)")
    matches = pattern.finditer(file_content)
    for match in matches:
        image = filepath.parent / match.group(1)
        image = image.resolve()
        assert image.is_file()
        yield image


def get_image_mapping():
    image_files = list(get_files_by_suffix(".png"))
    md_files = list(get_files_by_suffix(".md"))

    images_to_files = defaultdict(list)
    for file in md_files:
        images = list(find_links_in_md_file(file))
        for image in images:
            images_to_files[image].append(file)

    for image, files in images_to_files.items():
        if len(files) != 1:
            print(image, f"has {len(files)} files")

    print(f"{len(images_to_files.keys())}-{len(image_files)}")
    non_included_images = set(images_to_files.keys()) - set(image_files)
    print(non_included_images)


get_image_mapping()
