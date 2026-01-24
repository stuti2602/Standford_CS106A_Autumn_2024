# Assignment 2b: image hat()
from simpleimage import SimpleImage

def hat(image):
    width = image.width
    height = image.height

    for y in range(height):
        for x in range(width):
            if y < height * 0.25:
                pixel = image.get_pixel(x, y)
                pixel.red = 255
                pixel.green = 255
                pixel.blue = 0
    return image 

def main():
    image = SimpleImage('C:/Data/Study/Scaler_study_material/03_Python/Standford/CS_106A_Autumn_2024/Assignment_2/stanford-300.jpg')  
    yellow_hatimage = hat(image)
    yellow_hatimage.show()                     

if __name__ == '__main__':
    main()
