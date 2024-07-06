from PIL import Image, ImageDraw
import math

def generate_moire_pattern(width, height, line_spacing1, line_spacing2, angle2):
    """
    high-resolution moiré pattern image with two sets of lines.

    Parameters:
    width (int): Width of the image.
    height (int): Height of the image.
    line_spacing1 (int): Spacing between vertical lines in the first set.
    line_spacing2 (int): Spacing between angled lines in the second set.
    angle2 (float): Angle of lines in the second set (in degrees).

    """
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw vertical lines for the first set
    for x in range(0, width, line_spacing1):
        draw.line((x, 0, x, height), fill='black')

    # Draw angled lines for the second set
    angle_rad = angle2 * 3.14159 / 180  # Convert degrees to radians
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    x_start = -height * sin_a
    x_end = width + height * sin_a

    for y in range(-height, height * 2, line_spacing2):
        y_start = y - height * sin_a
        y_end = y + height * sin_a
        draw.line((x_start, y_start, x_end, y_end), fill='black')

    return image

# Parameters
width, height = 1024, 1024  # Image resolution
line_spacing1, line_spacing2 = 10, 10  # Spacing of lines in pixels
angle2 = 5  # Angle for the second set of lines

# Generate and display the moiré pattern
moire_image = generate_moire_pattern(width, height, line_spacing1, line_spacing2, angle2)
moire_image.show()  # Display the image
# moire_image.save("moire_pattern.png")  # Optionally, save the image
