from PIL import Image

#opens the image
try:
    img = Image.open("C:/Users/Ahmed/Downloads/keanu.png")
except Exception as e:
    print("Error",e)
#converts image to grayscale
img_gray = img.convert('L')
img_gray.save("C:/Users/Ahmed/Downloads/grayscale.png")

#defining ascii characters in a list for image intensity values after converting to grayscale
ascii_chars= ['@', '#', '*', '.', ' ']

#setting intervals for grayscale
intervals=4
intensity = 255 #assigning intensity to a variable

#dividing grayscale intensities into intervals
interval_size = intensity / intervals 

#calculating thresholds (calculating thresholds helps to know where one intervals ends and the other one starts)
threshold_1 = interval_size * 1
threshold_2 = interval_size * 2
threshold_3 = interval_size * 3
threshold_4 = interval_size * 4

#to access pixel data and make changes
try:
    pixel_values = img_gray.load()
except Exception as e:
    print("Error",e)
    
#getting width and height of the image using size tuple
width, height = img_gray.size
ascii_art=""
for x in range(height):
    for y in range(width):
        img_intensity=pixel_values[x,y]
        if img_intensity<threshold_1:
            ascii_char=ascii_chars[0]
        elif threshold_1<img_intensity<threshold_2:
            ascii_char=ascii_chars[1]
        elif threshold_2<img_intensity<threshold_3:
            ascii_char=ascii_chars[2]
        elif threshold_3<img_intensity<threshold_4:
            ascii_char=ascii_chars[3]

        ascii_art +=ascii_char
        
    ascii_art += "\n"
    
with open("ascii_art.txt", "w") as text_file:
    text_file.write(ascii_art)

print("ASCII art saved to ascii_art.txt")