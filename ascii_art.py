import sys
from PIL import Image

# 1. CONSTANTS (Configuration)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# 2. HELPER FUNCTIONS (Small logical steps)
def resize_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width * 0.55)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

# 3. MAIN INTEGRATION FUNCTION
def convert_image_to_ascii(image_path, new_width=100):
    try:
        # Try to open the image
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to find image at {image_path}. Check the filename!")
        return

    # Step-by-step processing
    image = resize_image(image, new_width)
    image = grayify(image)
    
    # Convert pixels to a long string of ASCII chars
    ascii_str = pixels_to_ascii(image)
    
    # Format the string (add line breaks)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    # Loop to cut the string into lines
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    return ascii_img

# 4. EXECUTION BLOCK
if __name__ == "__main__":
    # This block only runs if you run this file directly
    output = convert_image_to_ascii("zlatan.jpg")
    
    if output:
        print(output)
        
        # Save to file
        with open("zlatan_output.txt", "w") as f:
            f.write(output)