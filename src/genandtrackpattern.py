import numpy as np
from PIL import Image, ImageDraw
from googleapiclient.discovery import build
import os
from google.oauth2 import service_account
from datetime import datetime

# Setup Google Sheets for logging
def setup_google_sheets():
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    return sheet

# Function to generate and save images with varying parameters and log to Google Sheets
def generate_images_and_log(num_images, width, height, output_folder, spreadsheet_id, line_thickness, center_displacement):
    sheet = setup_google_sheets()
    range_name = 'Sheet1!A2'  # Adjust based on your sheet's needs
    value_input_option = 'USER_ENTERED'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(num_images):
        # Randomize parameters within a range for variability
        radius_step1 = np.random.randint(10, 30)
        radius_step2 = radius_step1 + np.random.randint(1, 5)  # Ensure step2 is always different from step1
        displacement = np.random.randint(-center_displacement, center_displacement, size=2)  # Random displacement for the center
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Generates a timestamp
        image_name = f"concentric_pattern_{i+1}_{timestamp}.png"  # Appends the timestamp to the filename
        image_path = os.path.join(output_folder, image_name)

        image = generate_concentric_moire_pattern(width, height, radius_step1, radius_step2, line_thickness, displacement)
        image.save(image_path)
        
        # Log to Google Sheet
        values = [
            [image_name, radius_step1, radius_step2, str(displacement.tolist())]
        ]
        body = {
            'values': values
        }
        result = sheet.values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body
        ).execute()

def generate_concentric_moire_pattern(width, height, radius_step1, radius_step2, line_thickness, center_displacement):
    max_radius = min(width, height) // 2  # Define max_radius based on the dimensions of the image

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Adjust center for first set of concentric circles
    center_x, center_y = width // 2 + center_displacement[0], height // 2 + center_displacement[1]
    for radius in range(0, max_radius, radius_step1):
        draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], outline='black', width=line_thickness)

    # Second set of concentric circles remains centered
    center = (width // 2, height // 2)
    for radius in range(0, max_radius, radius_step2):
        draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], outline='black', width=line_thickness)

    return image

# Parameters
num_images = 100  # Number of images to generate
width, height = 1024, 1024  # Image resolution
output_folder = './output_images'  # Folder to save images
spreadsheet_id = '15ZEW19mth9T3RTclaB9GftCDTydADdlSqQvHTl2KcsA'  # Google Spreadsheet ID
line_thickness = 4
center_displacement = 100  # Maximum range for random displacement

generate_images_and_log(num_images, width, height, output_folder, spreadsheet_id, line_thickness, center_displacement)

# Generate and display an example moiré pattern with no displacement
moire_image = generate_concentric_moire_pattern(width, height, 15, 16, 4, [0, 0])
moire_image.show()  # Display the image
