from pathlib import Path
from PIL import Image
from typer import Typer

app = Typer()

@app.command()
def convert(image_paths: list[Path]):
    """Convert a PNG, JPG, JPEG, GIF, BMP, or TIFF image to a WebP image and delete the original image.

    :param image_paths: A list of paths to the images to convert.
    """
    for path in image_paths:
        if path.suffix.lower() not in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']:
            print(f"Skipping non-image file: {path}")
            continue  # Changed from return to continue to process all images

        try:
            img = Image.open(path)
            webp_path = path.with_suffix('.webp')
            img.save(webp_path, 'WEBP')
            path.unlink()  # Delete the original image
            print(f"Converted and deleted {path}, new file is {webp_path}")
        except Exception as e:
            print(f"Error converting {path}: {e}")
