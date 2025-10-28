"""CLI module for webp-pre-commit hook."""

from pathlib import Path

from PIL import Image
from typer import Typer

app = Typer()


@app.command()
def convert(image_paths: list[Path]):
    """Convert PNG, JPG, JPEG, GIF, BMP, or TIFF images to WebP and delete originals.

    :param image_paths: A list of paths to the images to convert.
    """
    for path in image_paths:
        if path.suffix.lower() not in [
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".bmp",
            ".tiff",
        ]:
            print(f"Skipping non-image file: {path}")
            continue  # Changed from return to continue to process all images

        try:
            img = Image.open(path)
            webp_path = path.with_suffix(".webp")

            # Check if it's an animated GIF
            if path.suffix.lower() == ".gif":
                is_animated = getattr(img, "is_animated", False)
                if is_animated:
                    img.save(webp_path, "WEBP", save_all=True)
                    print(f"Converted animated GIF {path} to animated WebP {webp_path}")
                else:
                    img.save(webp_path, "WEBP")
                    print(f"Converted static GIF {path} to WebP {webp_path}")
            else:
                # Regular conversion for other formats
                img.save(webp_path, "WEBP")
                print(f"Converted {path} to WebP {webp_path}")

            path.unlink()  # Delete the original image
        except Exception as e:
            print(f"Error converting {path}: {e}")
