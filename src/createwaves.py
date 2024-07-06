from PIL import Image, ImageDraw
import numpy as np

def generate_moire_pattern_sine_waves(width, height, frequency, amplitude, line_spacing, phase_shift1, phase_shift2):
    """
    high-resolution moiré pattern image with multiple sets of repeating and overlapping horizontal sine waves.

    Parameters:
    width (int): Width of the image.
    height (int): Height of the image.
    frequency (float): Frequency of the sine waves (waves per image width).
    amplitude (int): Amplitude of the sine waves (pixel offset from center line).
    line_spacing (int): Vertical spacing between each sine wave.
    phase_shift1 (float): Phase shift of the first set of sine waves in radians.
    phase_shift2 (float): Phase shift of the second set of sine waves in radians.

    Returns:
    Image object: PIL Image object with the pattern.
    """
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw multiple sine waves for each set
    for y in range(0, height, line_spacing):
        for x in range(width):
            # Calculate the y position of the first set of waves
            y1 = y + amplitude * np.sin(frequency * 2 * np.pi * x / width + phase_shift1)
            # Calculate the y position of the second set of waves
            y2 = y + amplitude * np.sin(frequency * 2 * np.pi * x / width + phase_shift2)
            # Draw the sine waves
            draw.point((x, int(y1)), 'black')
            draw.point((x, int(y2)), 'black')

    return image

# Parameters
width, height = 1024, 1024  # Image resolution
frequency = 10  # Frequency of sine waves, waves per image width
amplitude = 50  # Amplitude of the sine waves
line_spacing = 20  # Vertical spacing between each sine wave
phase_shift1, phase_shift2 = 0, np.pi / 4  # Phase shifts for moiré effect

# Generate and display the moiré pattern
moire_image = generate_moire_pattern_sine_waves(width, height, frequency, amplitude, line_spacing, phase_shift1, phase_shift2)
moire_image.show()  # Display the image
# moire_image.save("sine_wave_moire_pattern.png")  # Optionally, save the image
