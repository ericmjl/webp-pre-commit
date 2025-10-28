"""Tests for webp_pre-commit.cli."""

import tempfile
from pathlib import Path

from PIL import Image

from webp_hook.cli import convert


def test_convert_static_gif():
    """Test that static GIFs are converted to static WebP."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a simple static GIF
        img = Image.new("RGB", (10, 10), color="red")
        gif_path = temp_path / "static.gif"
        img.save(gif_path, "GIF")

        # Convert to WebP
        convert([gif_path])

        # Check that WebP file was created and original was deleted
        webp_path = temp_path / "static.webp"
        assert webp_path.exists()
        assert not gif_path.exists()

        # Verify it's a valid static WebP image
        webp_img = Image.open(webp_path)
        assert webp_img.format == "WEBP"
        assert not webp_img.is_animated, "WebP should not be animated for static GIF"
        assert webp_img.n_frames == 1, "WebP should have only one frame for static GIF"


def test_convert_animated_gif():
    """Test that animated GIFs are converted to animated WebP."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a simple animated GIF
        frames = []
        for i in range(3):
            img = Image.new("RGB", (10, 10), color=("red", "green", "blue")[i])
            frames.append(img)

        gif_path = temp_path / "animated.gif"
        frames[0].save(gif_path, "GIF", save_all=True, append_images=frames[1:])

        # Verify it's animated
        gif_img = Image.open(gif_path)
        assert getattr(gif_img, "is_animated", False)

        # Convert to WebP
        convert([gif_path])

        # Check that WebP file was created and original was deleted
        webp_path = temp_path / "animated.webp"
        assert webp_path.exists()
        assert not gif_path.exists()

        # Verify it's a valid animated WebP image
        webp_img = Image.open(webp_path)
        assert webp_img.format == "WEBP"
        # Check that it has multiple frames (indicating animation was preserved)
        assert webp_img.is_animated, "WebP should be animated"
        assert webp_img.n_frames > 1, "WebP should have multiple frames"


def test_convert_other_formats():
    """Test that other image formats continue to work as expected."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Test PNG conversion
        img = Image.new("RGB", (10, 10), color="red")
        png_path = temp_path / "test.png"
        img.save(png_path, "PNG")

        convert([png_path])

        webp_path = temp_path / "test.webp"
        assert webp_path.exists()
        assert not png_path.exists()

        webp_img = Image.open(webp_path)
        assert webp_img.format == "WEBP"


def test_skip_non_image_files():
    """Test that non-image files are skipped."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a text file
        txt_path = temp_path / "test.txt"
        txt_path.write_text("This is not an image")

        # Should not raise an error and should skip the file
        convert([txt_path])

        # File should still exist (not converted)
        assert txt_path.exists()
