from PIL import Image, ImageOps

# using PIL for image processing

# uhhh i'll do this later
def do_image(image, resolution):
    pass

image_path = input("enter path to image: ")

try:
    with Image.open(image_path, "r") as im:

        print(im.size, im.format, im.mode)

        # convert image to grayscale
        im = im.convert("L")
        outfile = image_path[:image_path.rfind(".")] + "_grayscale.png"
        im.save(outfile, "PNG")

        # resize image to cleanly have 3/5 ratio
        # ImageOps.fit(im, size).save("imageops_fit.png")
        xsize = (im.size[0] // 3) * 3
        ysize = (im.size[1] // 5) * 5
        im = ImageOps.fit(im, (xsize, ysize))
        outfile = image_path[:image_path.rfind(".")] + "_resized.png"
        im.save(outfile, "PNG")        

except Exception as err:
    print(err)
    exit()