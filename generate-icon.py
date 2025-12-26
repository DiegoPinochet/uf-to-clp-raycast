#!/usr/bin/env python3
"""
Generate icon.png with Chilean flag design for the Raycast extension.
Requires Pillow: pip install Pillow
"""

try:
    from PIL import Image, ImageDraw
    
    # Create a 512x512 image
    img = Image.new('RGB', (512, 512), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    # Chilean flag colors
    # Blue: #0039A6 (official Chilean flag blue)
    # Red: #D52B1E (official Chilean flag red)
    # White: #FFFFFF
    
    # Draw the red bottom half
    draw.rectangle([0, 256, 512, 512], fill='#D52B1E')
    
    # Draw the blue canton (upper left square)
    # The canton is half the height, so 256x256
    draw.rectangle([0, 0, 256, 256], fill='#0039A6')
    
    # Draw the white star in the blue canton
    # Star center at (128, 128) - center of the canton
    star_center = (128, 128)
    star_outer_radius = 80
    star_inner_radius = 35
    
    # Draw a 5-pointed star
    import math
    points = []
    for i in range(10):
        angle = math.pi / 2 + (i * 2 * math.pi / 10)
        if i % 2 == 0:
            radius = star_outer_radius
        else:
            radius = star_inner_radius
        x = star_center[0] + radius * math.cos(angle)
        y = star_center[1] + radius * math.sin(angle)
        points.append((x, y))
    
    draw.polygon(points, fill='#FFFFFF')
    
    # Save the image to assets folder
    import os
    os.makedirs('assets', exist_ok=True)
    img.save('assets/icon.png')
    print("✓ assets/icon.png created with Chilean flag design!")
    
except ImportError:
    print("Error: Pillow is not installed.")
    print("Install it with: pip3 install Pillow")
    print("Or use: pip3 install --user Pillow")
    exit(1)
except Exception as e:
    print(f"Error creating icon: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
