from PIL import Image, ImageOps

# using PIL for image processing

# uhhh i'll do this later
def do_image(image, resolution):
    pass

image_path = input("enter path to image: ")

with Image.open(image_path, "r") as im:

    print(im.size, im.format, im.mode)

    # convert image to grayscale
    im = im.convert("L")
    outfile = image_path[:image_path.rfind(".")] + "_grayscale.png"
    im.save(outfile, "PNG")

    # resize image
    RATIO = 1
    xsize = int((im.size[0] / 3) * RATIO)
    ysize = int((im.size[1] / 7) * RATIO)
    im = im.resize((xsize, ysize))

    outfile = image_path[:image_path.rfind(".")] + "_resized.png"
    im.save(outfile, "PNG")

    # convert image to text
    # 255 = white, 0 = black

    # colors from https://paulbourke.net/dataformats/asciiart/
    chars = " .:-=+*#%@"
    output = []
    for y in range(im.size[1]):
        cur_line = ""
        for x in range(im.size[0]):
            index = int(im.getpixel((x, y)) / 255 * len(chars))
            index = min(index, len(chars) - 1)
            cur_line += chars[index]
        output.append(cur_line)
    
    with open("out.txt", "w") as file:
        for line in output:
            file.write(line + "\n")
