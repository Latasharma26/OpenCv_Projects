import cv2

# Load an image
image = cv2.imread('cats 2.jpg')

# Resize the image
resized_image = cv2.resize(image, (400, 400))

# Crop the image
cropped_image = image[50:200, 100:300]

# Rotate the image
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Flip the image
flipped_image = cv2.flip(image, 1)  # 1 for horizontal, 0 for vertical

# Display the images
cv2.imshow('Resized', resized_image)
cv2.imshow('Cropped', cropped_image)
cv2.imshow('Rotated', rotated_image)
cv2.imshow('Flipped', flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
