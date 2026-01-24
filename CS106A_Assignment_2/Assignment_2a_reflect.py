# Assignment 2a: image reflect()
# "C:/Data/Study/Scaler_study_material/03_Python/Standford/CS_106A_Autumn_2024/Assignment_2/stanford-300.jpg"

from simpleimage import SimpleImage

def reflect_top_bottom(image):
    out = SimpleImage.blank(image.width, image.height * 2)

    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)

            top = out.get_pixel(x, y)
            top.red = pixel.red
            top.green = pixel.green
            top.blue = pixel.blue

            bottom = out.get_pixel(x, out.height - 1 - y)
            bottom.red = pixel.red
            bottom.green = pixel.green
            bottom.blue = pixel.blue
    return out


def main():
    image = SimpleImage('C:/Data/Study/Scaler_study_material/03_Python/Standford/CS_106A_Autumn_2024/Assignment_2/stanford-300.jpg')  
    reflected = reflect_top_bottom(image)
    reflected.show()                     


if __name__ == '__main__':
    main()


