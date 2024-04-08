import sys
from pathlib import Path

from PIL import Image


def convert_to_webp(image_path: Path):
    """Convert a PNG, JPG, JPEG, GIF, BMP, or TIFF image to a WebP image.

    :param image_path: The path to the image to convert.
    :raise ValueError: If the image is not a supported image format.
    """
    path = Path(image_path)
    if path.suffix.lower() not in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']:
        print(f"Skipping non-image file: {image_path}")
        return

    try:
        img = Image.open(image_path)
        webp_path = path.with_suffix('.webp')
        img.save(webp_path, 'WEBP')
        print(f"Converted {image_path} to {webp_path}")
    except Exception as e:
        print(f"Error converting {image_path}: {e}")

if __name__ == "__main__":
    for image_path in sys.argv[1:]:
        convert_to_webp(image_path)
