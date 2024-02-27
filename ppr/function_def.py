from PIL import Image

def convert_image(image_path, size):
    with Image.open(image_path, "r") as im:

        im = im.convert("L")

        scaling_factor = -1
        if size == "small":
            scaling_factor = 0.2
        elif size == "medium":
            scaling_factor = 0.5
        elif size == "large":
            scaling_factor = 1
        else:
            raise Exception()

        xsize = int((im.size[0] / 3) * scaling_factor)
        ysize = int((im.size[1] / 7) * scaling_factor)
        im = im.resize((xsize, ysize))

        chars = [c for c in " .:-=+*#%@"]
        output = []

        for y in range(im.size[1]):
            cur_line = ""
            for x in range(im.size[0]):
                index = int(im.getpixel((x, y)) / 255 * len(chars))
                index = min(index, len(chars) - 1)
                cur_line += chars[index]
            output.append(cur_line)

    return output