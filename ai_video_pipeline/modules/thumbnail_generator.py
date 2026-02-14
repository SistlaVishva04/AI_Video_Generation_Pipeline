from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_thumbnail(image_path, title_text):

    img = Image.open(image_path).convert("RGB")
    img = img.resize((1280, 720))

    draw = ImageDraw.Draw(img)

    # Wrap title text
    wrapped_text = textwrap.fill(title_text.upper(), width=25)

    # Load default font
    font = ImageFont.load_default()

    # Text position
    text_width, text_height = draw.multiline_textsize(wrapped_text, font=font)
    x = (1280 - text_width) / 2
    y = 720 - text_height - 80

    # Draw background rectangle
    draw.rectangle(
        [(x-20, y-20), (x+text_width+20, y+text_height+20)],
        fill=(0, 0, 0)
    )

    # Draw text
    draw.multiline_text(
        (x, y),
        wrapped_text,
        fill=(255, 255, 255),
        font=font,
        align="center"
    )

    output_path = "output/thumbnail.jpg"
    img.save(output_path)

    return output_path