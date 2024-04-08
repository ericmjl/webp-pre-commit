from pathlib import Path

from PIL import Image
from typer import Typer

app = Typer()


@app.command()
def convert(image_paths: list[Path]):
    """Convert a PNG, JPG, JPEG, GIF, BMP, or TIFF image to a WebP image.

    :param image_path: The path to the image to convert.
    :raise ValueError: If the image is not a supported image format.
    """
    for path in image_paths:
        if path.suffix.lower() not in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']:
            print(f"Skipping non-image file: {path}")
            return

        try:
            img = Image.open(path)
            webp_path = path.with_suffix('.webp')
            img.save(webp_path, 'WEBP')
            print(f"Converted {path} to {webp_path}")
        except Exception as e:
            print(f"Error converting {path}: {e}")
