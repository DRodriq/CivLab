from PIL import Image
import random
import json
from datetime import datetime
import unittest


def convert_grayscale_img(input_filename, output_filename):
    """Applies a full grayscale filter to a PNG image."""
    image = Image.open(input_filename).convert('L')
    image.save(output_filename)


def convert_grayscale_partial_img(input_filename, output_filename, percent_gray=50):
    """Applies a partial grayscale filter to a PNG image."""

    image = Image.open(input_filename).convert('RGB')  # Ensure RGB mode
    image.getpalette()
    gray_image = image.convert('L') 
    gray_image = gray_image.convert('RGB')

    # Create a blended image with the specified percentage of gray
    result = Image.blend(image, gray_image, percent_gray / 100)
    result.save(output_filename)


def darken_image(input_filename, output_filename, darkening_amount=0.5):
    """Darkens a PNG image uniformly using Pillow."""

    image = Image.open(input_filename).convert('RGB')
    width, height = image.size

    # Create a black image
    darkening_overlay = Image.new('RGB', (width, height), color=(0, 0, 0))

    # Blend the original and black image based on darkening_amount
    new_image = Image.blend(image, darkening_overlay, darkening_amount)

    new_image.save(output_filename)


def generate_random_palette(p_size):
    palette = []
    for _ in range(p_size):
        color = [random.randint(0, 255) for _ in range(3)]
        palette.append(color)
    return palette

 
def convert_img_to_palette(img, palette):
    """
    Converts a PNG image to a the colors of the palette
    Uses least distance algorithm between images in the source image
    and converts to closest color in the palette
    """
    img = img.convert('RGB')
    data = img.getdata()
 
    new_data = []
    for pixel in data:
        r, g, b = pixel
        # Find the closest color in the palette using Euclidean distance
        min_distance = float('Inf')
        for color in palette:
            cr, cg, cb = color
            distance = (r-cr)**2 + (g-cg)**2 + (b-cb)**2
            if distance < min_distance:
                min_distance = distance
                closest_color = color
 
        new_data.append(closest_color)
  
    img.putdata(new_data)
    return img


def save_palette(palette, filename="palettes.json"):
    """Saves a color palette to palettes.json with a timestamp."""

    timestamp = datetime.now().isoformat()  # Get current time in ISO format
    data = {"timestamp": timestamp, "palette": palette}

    with open(filename, "a") as f:  # Append to file
        json.dump(data, f)
        f.write("\n")  # Add newline for readability


def load_palette(val, filename="palettes.json"):
    """Loads a color palette from the JSON file by its timestamp."""

    with open(filename, "r") as f:
        for line in f:
            data = json.loads(line)
            for key, value in data.items():
                if(value.count(val) != -1):
                    return data["palette"]

    return None


def extract_palette(img):
    """Extracts a palette of unique colors from a PNG image."""
    colors = img.getcolors()
    palette = colors
    return palette


def save_palette_from_image(image_path, filename="palettes.json"):
    """Extracts a palette from an image and saves it with source image information."""
    with Image.open(image_path) as img:
        palette = extract_palette(img)
    timestamp = datetime.now().isoformat()
    data = {
        "timestamp": timestamp,
        "palette": palette,
        "source_image": image_path
    }

    with open(filename, "a") as f:
        json.dump(data, f)
        f.write("\n")

convert_grayscale_partial_img("assets/images/civlab_logo.png", "assets/images/civlab_logo_grayscale_25.png", 25)
