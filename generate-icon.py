#!/usr/bin/env python3
"""
Generate icon.png with Chilean flag design in a circular format with UF badge.
Requires Pillow: pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    import math
    
    # Create a 512x512 image with transparent background
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Chilean flag colors
    blue = '#0039A6'  # Official Chilean flag blue
    red = '#D52B1E'   # Official Chilean flag red
    white = '#FFFFFF'
    
    # Draw circular flag (with some padding for border)
    center = (256, 256)
    radius = 240  # Slightly smaller to leave room for border
    
    # Create a mask for the circle
    mask = Image.new('L', (512, 512), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([16, 16, 496, 496], fill=255)
    
    # Draw the flag inside the circle
    # White top half
    draw.ellipse([16, 16, 496, 256], fill=white)
    # Red bottom half
    draw.ellipse([16, 256, 496, 496], fill=red)
    
    # Blue canton (upper left quadrant)
    # Calculate the canton size - it's a square in the upper left
    canton_size = 240  # Half the circle radius
    canton_top_left = (16, 16)
    canton_bottom_right = (16 + canton_size, 16 + canton_size)
    
    # Draw blue canton as a circle segment
    # We'll draw it as a rectangle and then clip it
    canton_mask = Image.new('L', (512, 512), 0)
    canton_mask_draw = ImageDraw.Draw(canton_mask)
    canton_mask_draw.ellipse([16, 16, 16 + canton_size * 2, 16 + canton_size * 2], fill=255)
    canton_mask_draw.rectangle([16 + canton_size, 16, 512, 512], fill=0)
    canton_mask_draw.rectangle([16, 16 + canton_size, 512, 512], fill=0)
    
    # Apply blue color to canton area
    blue_layer = Image.new('RGBA', (512, 512), (0, 57, 166, 255))
    img = Image.composite(blue_layer, img, canton_mask)
    draw = ImageDraw.Draw(img)
    
    # Draw the white star in the blue canton
    star_center = (16 + canton_size // 2, 16 + canton_size // 2)
    star_outer_radius = 60
    star_inner_radius = 25
    
    # Draw 5-pointed star
    points = []
    for i in range(10):
        angle = math.pi / 2 + (i * 2 * math.pi / 10)
        if i % 2 == 0:
            r = star_outer_radius
        else:
            r = star_inner_radius
        x = star_center[0] + r * math.cos(angle)
        y = star_center[1] + r * math.sin(angle)
        points.append((x, y))
    
    draw.polygon(points, fill=white)
    
    # Apply circular mask to make it round
    img.putalpha(mask)
    
    # Add white border
    border_img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    border_draw = ImageDraw.Draw(border_img)
    border_draw.ellipse([8, 8, 504, 504], outline=white, width=16)
    img = Image.alpha_composite(img, border_img)
    draw = ImageDraw.Draw(img)
    
    # Add UF badge in bottom-right corner
    badge_size = 120
    badge_x = 512 - badge_size - 20
    badge_y = 512 - badge_size - 20
    
    # Draw golden yellow badge with gradient effect
    # Create badge background (golden yellow)
    badge_color = '#FFD700'  # Gold
    badge_darker = '#FFA500'  # Darker gold for gradient effect
    
    # Draw badge with rounded corners
    badge_points = [
        (badge_x + 15, badge_y),  # Top left (rounded)
        (badge_x + badge_size - 15, badge_y),  # Top right (rounded)
        (badge_x + badge_size, badge_y + 15),  # Right top (rounded)
        (badge_x + badge_size, badge_y + badge_size - 15),  # Right bottom (rounded)
        (badge_x + badge_size - 15, badge_y + badge_size),  # Bottom right (rounded)
        (badge_x + 15, badge_y + badge_size),  # Bottom left (rounded)
        (badge_x, badge_y + badge_size - 15),  # Left bottom (rounded)
        (badge_x, badge_y + 15),  # Left top (rounded)
    ]
    draw.polygon(badge_points, fill=badge_color)
    
    # Add subtle shadow/depth to badge
    shadow_offset = 3
    shadow_points = [(x + shadow_offset, y + shadow_offset) for x, y in badge_points]
    shadow_img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    shadow_draw.polygon(shadow_points, fill=(0, 0, 0, 50))
    img = Image.alpha_composite(img, shadow_img)
    draw = ImageDraw.Draw(img)
    
    # Draw "UF" text on badge
    try:
        # Try to use a system font
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
        except:
            font = ImageFont.load_default()
    
    text = "UF"
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center text in badge
    text_x = badge_x + (badge_size - text_width) // 2
    text_y = badge_y + (badge_size - text_height) // 2 - bbox[1]
    
    # Draw text with slight shadow for depth
    draw.text((text_x + 2, text_y + 2), text, fill=(0, 0, 0, 100), font=font)
    draw.text((text_x, text_y), text, fill=white, font=font)
    
    # Apply subtle gloss effect (optional - add a white gradient overlay)
    gloss = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    # Draw a subtle white gradient from top
    for i in range(100):
        alpha = int(30 * (1 - i / 100))
        gloss_draw.ellipse([16, 16 + i * 2, 496, 16 + i * 2 + 10], fill=(255, 255, 255, alpha))
    img = Image.alpha_composite(img, gloss)
    
    # Save the image to assets folder
    import os
    os.makedirs('assets', exist_ok=True)
    img.save('assets/icon.png')
    print("✓ assets/icon.png created with circular Chilean flag and UF badge!")
    
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
