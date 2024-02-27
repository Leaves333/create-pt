def convert_image(image_path, size):
    pass
image_path, output_size = 0, 0

result = convert_image(image_path, output_size)
output_file = image_path[:image_path.rfind('.')] + ".txt";
with open(output_file, "w") as file:
    for row in result:
        file.write(row + "\n")