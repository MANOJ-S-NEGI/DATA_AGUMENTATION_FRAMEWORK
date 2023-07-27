import albumentations as ab
import cv2
import matplotlib.pyplot as plt


# declare agumentation pipeline
def albumentations_function(image="images/"):
    transform = ab.Compose([
        ab.RandomCrop(width=256, height=256),
        ab.HorizontalFlip(p=0.5),
        ab.RandomBrightnessContrast(p=0.2),
    ])

    # Read an image with OpenCV and convert it to the RGB colorspace
    image = plt.imread(image[2])
    # print(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # print(image)
    # Augment an image
    transformed = transform(image=image)
    transformed_image = transformed["image"]
    plt.imshow(transformed_image)
    plt.axis(False);
    # print(transformed_image)


# gaussian function:
def gaussian_func(image=""):
    transform = ab.GaussNoise(var_limit=(0, 1000), mean=150, p=0.5)
    for i in range(2):
        fig, ax = plt.subplots(nrows=1, figsize=(5, 5))
        image = plt.imread(image)
        # Now the image is transformed and ready to be accepted by the model
        if i == 1:
            im = transform(image=image)['image']
            plt.imshow(im)
            plt.title("noise_img")
        if i == 0:
            plt.imshow(image)
            plt.title("original_img")
    plt.axis(False);
