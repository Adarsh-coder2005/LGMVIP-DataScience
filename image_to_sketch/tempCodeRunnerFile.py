# Converting Blur Image to Final Sketch
sketch = cv2.divide(gray_image, 255-blur_image, scale=256.0)
cv2.imshow('Sketch', sketch)