from PIL import Image, ImageOps, ImageDraw, ImageFont
import numpy
import random

# create = 'text';
# create = 'image';


def add_border(input_image, output_image, border):
    img = Image.open(input_image)
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill='black')
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    bimg.save(output_image)


def createSingleText(color_sequence, kat, image):
    name = kat + str(image)
    fielContent = kat + str(image) + ' '+ color_sequence + ' '
    filename = name + '.txt'
    f = open(filename, 'w+')
    moreOrLess = numpy.random.randint(2)
    if moreOrLess == 1:
        f.write(fielContent*13)
        pass
    else:
        f.write(fielContent*10)
        pass
    pass


def createSingleImage(color, kat, image, font, W, H):
    orientation = numpy.random.randint(2)
    msg = kat + str(image)
    print(msg)
    filename = msg + '.png'
    print(filename)
    if orientation == 1:
        blank_image_landscape = Image.new('RGBA', (W, H), color)
        img_draw = ImageDraw.Draw(blank_image_landscape)
        w, h = font.getsize(msg)
        img_draw.text(((W-w)/2, (H-h)/2), msg, font=font, fill="black")
        blank_image_landscape.save(filename)

        add_border(filename, output_image=filename, border=20)
        pass
    else:
        blank_image_portrait = Image.new('RGBA', (H, W), color)
        img_draw = ImageDraw.Draw(blank_image_portrait)
        w, h = font.getsize(msg)
        img_draw.text(((H-w)/2, (W-h)/2), msg, font=font, fill="black")
        blank_image_portrait.save(filename)

        add_border(filename, output_image=filename, border=20)
        pass
    pass


def createImages():
    ImageFont.load_default()
    font = ImageFont.load_default()
    image_name = 'pil_color.png'
    W, H = (800, 500)
    color_sequence = ['red', 'green', 'blue', 'plum']
    for kat in ('emotion', 'nah', 'weit'):
        for image in range(10):
            color = random.choice(color_sequence)
            # createSingleImage(color, kat, image, font, W, H)
            createSingleText(color, kat, image)

        pass


# img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
# arial = ImageFont.truetype("arial.ttf", 9)
createImages()
