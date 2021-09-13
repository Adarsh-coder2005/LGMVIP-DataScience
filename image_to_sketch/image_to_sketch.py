# Importing the Library
import cv2

# Taking the Imput Option
print('Coose the option: ')
print('1. Capture the Image')
print('2. Choose the pre-defined image')

choice = int(input())

# Capturing the Image from Webcam
if choice == 1:
    camera = cv2.VideoCapture(0)

    while(True):
        ret, frame = camera.read()
        if not ret:
            print('Failed to grab the Frame')
            break
        cv2.imshow('Frame', frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            print('Closing...')
            break
        elif k%256 == 32:
            cv2.imwrite('Original_Image.jpg', frame)
    image = cv2.imread('Original_Image.jpg')
    camera.release()
    cv2.destroyAllWindows()

# Taking the pre-defined Image
elif choice == 2:
    image = cv2.imread('Original_Image.jpg')

# Original Input Image
original_image = cv2.resize(image, (480,480))
cv2.imshow('Original Image', original_image)

# Converting Original Image to Gray Image
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)

# Converting Gray Image to Inverted Image
inverted_image = cv2.bitwise_not(gray_image)
cv2.imshow('Inverted Image', inverted_image)

# Converting Inverted Image to Blur Image
blur_image = cv2.GaussianBlur(inverted_image, (21,21), 0)
cv2.imshow('Blur Image', blur_image)

# Converting Blur Image to Final Sketch
sketch = cv2.divide(gray_image, 255-blur_image, scale=256.0)
cv2.imshow('Sketch', sketch)

cv2.waitKey(0)