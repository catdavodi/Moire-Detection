from PIL import Image, ImageDraw
import math

def generate_concentric_moire_pattern(width, height, radius_step1, radius_step2, max_radius=None):
    """
    Generate a high-resolution moiré pattern image with two sets of concentric circles.

    Parameters:
    width (int): Width of the image.
    height (int): Height of the image.
    radius_step1 (int): Radius step for the first set of concentric circles.
    radius_step2 (int): Radius step for the second set of concentric circles.
    max_radius (int, optional): Maximum radius of the circles. Defaults to half of the smallest dimension of the image.

    Returns:
    Image object: PIL Image object with the moiré pattern.
    """
    if max_radius is None:
        max_radius = min(width, height) // 2

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    center = (width // 2, height // 2)

    # Draw the first set of concentric circles
    for radius in range(0, max_radius, radius_step1):
        draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], outline='black')

    # Draw the second set of concentric circles with a different spacing
    for radius in range(0, max_radius, radius_step2):
        draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], outline='black')

    return image

# Parameters
width, height = 1024, 1024  # Image resolution
radius_step1, radius_step2 = 15, 16  # Slightly different spacings for the circle radii

# Generate and display the moiré pattern
moire_image = generate_concentric_moire_pattern(width, height, radius_step1, radius_step2)
moire_image.show()  # Display the image
# moire_image.save("concentric_moire_pattern.png")  # Optionally, save the image
