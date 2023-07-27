# DATA_AGUMENTATION_FRAMEWORK
Dated :27 June 2023

## ALBUMENTATION:
```
Albumentations is a Python library for fast and flexible image augmentations.
Albumentations efficiently implements a rich variety of image transform operations that are optimized for performance,
and does so while providing a concise, yet powerful image augmentation interface for different computer vision tasks,
including object classification, segmentation, and detection.
```
checkout the link for further information : https://albumentations.ai/


### Getting started
* Albumentations requires Python 3.6 or higher. To install the library from PyPI run
  ```
  pip install -U albumentations
  ```
* Import the libraries
 ```
  import albumentations as ab
  import cv2
  ```
* declare agumentation pipeline
```
transform = ab.Compose([
                        ab.RandomCrop(width=256, height=256),
                        ab.HorizontalFlip(p=0.5),
                        ab.RandomBrightnessContrast(p=0.2), 
                    ])
```
Further more parameters can be used as shown: source - https://albumentations.ai/docs/api_reference/core/composition/    [Do checkout the link for more understanding]
![para_album](https://github.com/MANOJ-S-NEGI/DATA_AGUMENTATION_FRAMEWORK/assets/99602627/3f8e1319-49b1-472e-bd4e-481231b95000)

* Read an image with OpenCV and convert it to the RGB colorspace
* here,RGB image WITH convert into BRG as, we can check, the float values of images simple arrange in reverse.
  ```
  image = plt.imread(image)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  ```
* Augment an image

  ```
  transformed = transform(image=image)
  transformed_image = transformed["image"]
  ```
  * Printing the image:
    ```
    plt.imshow(transformed_image)
    plt.axis(False);
    ```
    ![albumentation_transformed](https://github.com/MANOJ-S-NEGI/DATA_AGUMENTATION_FRAMEWORK/assets/99602627/b08a13e0-0879-4cf1-98a8-178c51ccf8c6)

    * Adding Gaussian Noise:
        ### Parameters
          1. Variance limit - sets the variance range of the noise. The higher the values in the range, the noisier the image will be. The specified numbers must fall between [0.0, 65025.0];
      
          2.Mean - sets the mean of the noise. The higher the mean value, the brighter the image will be. The specified value must fall between [0.0, 255.0];

