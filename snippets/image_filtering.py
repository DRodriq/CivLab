from PIL import Image

def grayscale_image(input_filename, output_filename):
    """Converts a PNG image to grayscale using the Pillow library.

    Args:
        input_filename (str): The path to the input PNG image.
        output_filename (str): The path to save the grayscale image.
    """

    image = Image.open(input_filename).convert('L')
    image.save(output_filename)

def partial_grayscale(input_filename, output_filename, percent_gray=50):
    """Applies a partial grayscale filter to a PNG image.

    Args:
        input_filename (str): The path to the input PNG image.
        output_filename (str): The path to save the filtered image.
        percent_gray (int): The percentage of grayscale to apply (0-100).
    """

    image = Image.open(input_filename).convert('RGB')  # Ensure RGB mode
    image.getpalette()
    gray_image = image.convert('L') 
    gray_image = gray_image.convert('RGB')


    # Create a blended image with the specified percentage of gray
    result = Image.blend(image, gray_image, percent_gray / 100)

    result.save(output_filename)

def darken_image(input_filename, output_filename, darkening_amount=0.5):
    """Darkens a PNG image uniformly using Pillow.

    Args:
        input_filename (str): The path to the input PNG image.
        output_filename (str): The path to save the modified image.
        darkening_amount (float): A value between 0.0 (no change) 
                                 and 1.0 (completely black). Default is 0.5.
    """

    image = Image.open(input_filename).convert('RGB')
    width, height = image.size

    # Create a black image
    darkening_overlay = Image.new('RGB', (width, height), color=(0, 0, 0))

    # Blend the original and black image based on darkening_amount
    new_image = Image.blend(image, darkening_overlay, darkening_amount)

    new_image.save(output_filename)

# Example usage
input_filename = '/home/drodriq/Source/Python/CivLab_2/assets/civlab_logo.png'
output_filename = 'my_darkened_image.png'
darkening_amount = 0.50  # Darken by 30%
darken_image(input_filename, output_filename, darkening_amount)