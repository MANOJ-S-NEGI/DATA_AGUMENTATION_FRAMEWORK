# DATA_AGUMENTATION_FRAMEWORK
Dated:27 June 2023

## ALBUMENTATION:

Albumentations is a Python library for fast and flexible image augmentations.Albumentations efficiently implements a rich variety of image transform operations that are optimized for performance,
and does so while providing a concise, yet powerful image augmentation interface for different computer vision tasks,
including object classification, segmentation, and detection.

checkout the link for further information: https://albumentations.ai/


### Getting started
* Albumentations require Python 3.6 or higher. To install the library from PyPI run
```
  pip install -U albumentations
 ```
* Import the libraries
 ```
  import albumentations as ab
  import cv2
  ```
* declare argumentation pipeline
```
transform = ab.Compose([
                        ab.RandomCrop(width=256, height=256),
                        ab.HorizontalFlip(p=0.5),
                        ab.RandomBrightnessContrast(p=0.2), 
                    ])
```
Furthermore, parameters can be used as shown: source - https://albumentations.ai/docs/api_reference/core/composition/    [Do check out the link for more understanding]
![para_album](https://github.com/MANOJ-S-NEGI/DATA_AGUMENTATION_FRAMEWORK/assets/99602627/3f8e1319-49b1-472e-bd4e-481231b95000)

* Read an image with OpenCV and convert it to the RGB colorspace
* here, RGB image WITH converts into BRG as we can check, the float values of images simply arrange in reverse.
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
      *  Variance limit - sets the variance range of the noise. The higher the values in the range, the noisier the image will be. The specified numbers must fall between [0.0, 65025.0];
      *  Mean - sets the mean of the noise. The higher the mean value, the brighter the image will be. The specified value must fall between [0.0, 255.0];
    ```
    transform =ab.GaussNoise(var_limit=(0,1000),mean=150,p=0.5)
    ```
* printing image:
  ```
  for i in range(2):
      fig,ax =plt.subplots(nrows=1,figsize=(5,5))
      image = plt.imread(images[0])
      # Now the image is transformed and ready to be accepted by the model
      if i==1:
          im = transform(image=image)['image']
          plt.imshow(im)
          plt.title("noise_img")
      if i==0:
          plt.imshow(image)
          plt.title("original_img")
      plt.axis(False);
  ```
 ![noise](https://github.com/MANOJ-S-NEGI/DATA_AGUMENTATION_FRAMEWORK/assets/99602627/5f66da97-e5ea-4950-b224-f70086d3280b)
_____________________________________________________________________________________________________________________________________________________________________________________________________________________

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

# AGUMENTOR
In principle, Augmentor consists of a number of classes for standard image manipulation functions, such as the Rotate class or the Crop class. You interact and use these classes using a large number of convenience functions, which cover most of the functions you might require when augmenting image datasets for machine learning problems.

Because image augmentation is often a multi-stage procedure, Augmentor uses a pipeline-based approach, where operations are added sequentially in order to generate a pipeline. Images are then passed through this pipeline, where each operation is applied to the image as it passes through.
  * Do check out the source link - https://augmentor.readthedocs.io/en/stable/userguide/mainfeatures.html


```
import Augmentor
a = Augmentor.Pipeline(path)
```
Here,
    * Point to a directory containing ground truth data.
    *Images with the same file names will be added as ground truth data
    * and augmented in parallel to the original data.
    ```
    a.ground_truth("path/to/ground_truth_images/")
    ```

* Add operations to the pipeline as normal:
```
a.rotate(probability=.25, max_left_rotation=5, max_right_rotation=5)
a.flip_left_right(probability=0.5)
a.zoom_random(probability=0.5, percentage_area=0.8)
a.flip_top_bottom(probability=0.5)
a.sample(5)
```
 * for other Parameters: link - https://augmentor.readthedocs.io/en/stable/userguide/mainfeatures.html


![agumentor](https://github.com/MANOJ-S-NEGI/DATA_AGUMENTATION_FRAMEWORK/assets/99602627/d1682deb-6561-4e83-ab7d-49600ac6570e)


 

          
