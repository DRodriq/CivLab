from PIL import Image, ImageDraw
import random

def generate_random_image(width, height):
    # Create a new image with a random background color
    img = Image.new('RGB', (width, height), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    # Draw some random shapes on the image
    draw = ImageDraw.Draw(img)
    for _ in range(random.randint(10, 50)):
        shape_type = random.choice(['rectangle', 'ellipse'])
        x0 = random.randint(0, width)
        y0 = random.randint(0, height)
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        if shape_type == 'rectangle':
            draw.rectangle([x0, y0, x1, y1], fill=fill_color)
        elif shape_type == 'ellipse':
            draw.ellipse([x0, y0, x1, y1], fill=fill_color)
    
    return img

# Generate and save a random image
img = generate_random_image(20, 20)
img.save('random_image.png')