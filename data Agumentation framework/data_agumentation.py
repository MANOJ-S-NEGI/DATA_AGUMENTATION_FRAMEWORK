import os
import matplotlib.pyplot as plt
import Augmentor


def Agumentor_function(folder_path="images"):
    AP = Augmentor.Pipeline(folder_path)
    AP.ground_truth("path/to/ground_truth_images/")
    # Add operations to the pipeline as normal:
    AP.rotate(probability=.25, max_left_rotation=5, max_right_rotation=5)
    AP.flip_left_right(probability=0.5)
    AP.zoom_random(probability=0.5, percentage_area=0.8)
    AP.flip_top_bottom(probability=0.5)
    AP.sample(5)

    # for printing the sample
    agumentor_image_path = f"{folder_path}/output/"
    # checking output directory
    agumentor_image_files = os.listdir(agumentor_image_path)
    print(len(agumentor_image_files))
    # storing output directory data to list
    argmentor_images = []
    for i in agumentor_image_files:
        argmentor_images.append(f"{agumentor_image_path}{i}")

    # plotting the agumentor images:
    fig = plt.figure(figsize=(15, 15))
    for i in range(len(agumentor_image_files)):
        img = plt.imread(argmentor_images[i])
        ax = fig.add_subplot(6, 5, i + 1, xticks=[], yticks=[])
        ax.imshow(img)






