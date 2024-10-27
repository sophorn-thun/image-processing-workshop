from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
img = Image.open("camera-image.jpg")
img.show()

# To display image's size and mode
print("image size: ", img.size)
print("image mmode: ", img.mode)

# To resize the image
low_res_img = img.resize((1000, 500))
low_res_img.show()
print(low_res_img.size)

# To crop the image
cropped_img = img.crop((300, 150, 700, 1000))
cropped_img.show()

# To rotate the image
rotated_img = img.rotate(45)
rotated_img.show()

# To quantify the image
quantized_img = img.quantize(8)
quantized_img.show()

# To split the image
r,g,b = img.split()
grb_img = Image.merge("RGB", (g, r, b))
grb_img.show()

# To increase saturation of the image
hsv_image = img.convert('HSV')
h, s, v = hsv_image.split()
channel_array = np.array(s)
channel_array[:,:] = channel_array[:,:]*10
s = Image.fromarray(channel_array)
edited_hsv_image = Image.merge('HSV', (h,s,v))
edited_hsv_image.show()
sharp_img=filter(ImageFilter.SHARPEN)
sharp_img.show()
blur_img = img.filter(ImageFilter.BLUR)
blur_img.show()
