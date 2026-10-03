import os
from PIL import Image, ImageDraw, ImageFont
class MemeEngine:
    """ A class to generate Memes and save them to a specified directory"""
    def __init__(self, output_dir):
        """ Initialise a MemeEngine object with an output directory to save memes """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """ Create a meme with the given image path, text, and author, and save it to the output directory """
        img = Image.open(img_path)
        original_width, original_height = img.size
        aspect_ratio = original_height / original_width
        new_height = int(width * aspect_ratio)
        img = img.resize((width, new_height))

        draw = ImageDraw.Draw(img)


        text_position = (10, new_height-50)
        draw.text(text_position, f"{text} - {author}",  fill='white', font=ImageFont.load_default(), fontsize=40)

        output_path = os.path.join(self.output_dir, f"meme_{os.path.basename(img_path)}")
        img.save(output_path)
        return output_path
    