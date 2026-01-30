# Assignment 2c: image purple()

from simpleimage import SimpleImage

def purple_sides(image):

    strip_width = 30
    out = SimpleImage.blank(image.width + 2 * strip_width, image.height)

    for y in range(image.height):
        for x in range(strip_width):
            pixel_out = out.get_pixel(x, y)
            pixel_out.red = 128
            pixel_out.green = 0
            pixel_out.blue = 128

    for y in range(image.height):
        for x in range(strip_width):
            pixel_out = out.get_pixel(out.width - strip_width + x, y)
            pixel_out.red = 128
            pixel_out.green = 0
            pixel_out.blue = 128

    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_out = out.get_pixel(x + strip_width, y)
            pixel_out.red = pixel.red
            pixel_out.green = pixel.green
            pixel_out.blue = pixel.blue

    return out

def main():
    image = SimpleImage("C:/Data/Study/Scaler_study_material/03_Python/Standford/CS_106A_Autumn_2024/Assignment_2/stanford-300.jpg")
    purple_borderimage = purple_sides(image)
    purple_borderimage.show()

if __name__ == "__main__":
    main()
