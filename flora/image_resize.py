from PIL import Image
import os


def calc_size(size):
    w, h = size[0], size[1]
    if w > h:
        x = int((250/h)*w)
        return (x, 250),  (0, (x-250)//2, 0, 250+((x-250)//2))
    elif h > w:
        x = int((250/w)*h)
        return (250, x), ((x-250)//2, 0, 250+((250-x)//2), 0)
    else:
        return (250, 250), (0, 0, 0, 0)


def resizing(image_path):
    img = Image.open(image_path)
    n_img = Image.new('RGB', (250,250), (255,255,255))

    new_size, crop_val = calc_size(img.size)[0], calc_size(img.size)[1]
    new_img = img.resize(new_size, Image.ANTIALIAS)
    n_img.paste(new_img)

    os.remove(image_path)
    n_img.save(image_path)


