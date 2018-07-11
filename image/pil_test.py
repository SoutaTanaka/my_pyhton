from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGB", (512, 512), (128, 128, 128))


draw = ImageDraw.Draw(im)

draw.multiline_text((0, 0), 'Pillow sample', fill=(0, 0, 0))




