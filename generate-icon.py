#!/usr/bin/env python3
"""
Simple script to generate icon.png for the Raycast extension.
Requires Pillow: pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    
    # Create a 512x512 image with Raycast blue background
    img = Image.new('RGB', (512, 512), color='#007AFF')
    draw = ImageDraw.Draw(img)
    
    # Draw a white circle
    draw.ellipse([50, 50, 462, 462], fill='#FFFFFF', outline='#0051D5', width=8)
    
    # Try to use a nice font, fallback to default if not available
    try:
        # Try to use a system font
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw UF text
    draw.text((256, 200), 'UF', fill='#007AFF', anchor='mm', font=font_large)
    
    # Draw CLP text
    draw.text((256, 320), 'CLP', fill='#007AFF', anchor='mm', font=font_small)
    
    # Save the image
    img.save('icon.png')
    print("✓ icon.png created successfully!")
    
except ImportError:
    print("Error: Pillow is not installed.")
    print("Install it with: pip3 install Pillow")
    print("Then run this script again.")
    exit(1)
except Exception as e:
    print(f"Error creating icon: {e}")
    exit(1)

