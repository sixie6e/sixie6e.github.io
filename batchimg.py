from PIL import Image, ImageDraw, ImageFont
import os
import random
import logging

def get_image_datetime(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()
    if exif_data is not None:
        datetime_tag = 36867
        if datetime_tag in exif_data:
            return exif_data[datetime_tag]

def add_datetime_box(image_path, datetime_str):
	img = Image.open(image_path)
	width, height = img.size
	box_height = int(height * 0.1) 
	box_img = Image.new('RGB', (width, box_height), 
						(random.randint(144, 255), random.randint(238, 255), 
						 random.randint(144, 255)))
	draw = ImageDraw.Draw(box_img)
	font_size = int(width * 0.2 / 10)
	font = ImageFont.truetype("Monoid-Regular.ttf", font_size)
	text_width, text_height = draw.textsize(datetime_str, font=font)
	text_x = (text_width) // 2
	text_y = (box_height - text_height) // 2
	draw.text((text_x, text_y), datetime_str+' @sixie6e Brent Elisens', font=font, fill=(0, 0, 0))
	new_img = Image.new('RGB', (width, height + box_height))
	new_img.paste(img, (0, 0))
	new_img.paste(box_img, (0, height))
	new_image_path = os.path.splitext(image_path)[0] + "--.jpg"
	new_img.save(new_image_path)
	return new_image_path


if __name__ == "__main__":
    image_dir = "/home/*****/*****/"
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.jpg')):
            image_path = os.path.join(image_dir, filename)
            datetime_str = get_image_datetime(image_path)
            if datetime_str:
                new_image_path = add_datetime_box(image_path, datetime_str)
                print(f"{new_image_path}")
            else:
                print(logging.warning("error"))


