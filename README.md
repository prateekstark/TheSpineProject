# The Spine Project

## Dataset Description:
The dataset consists of radiological images, X rays, from over 1000 thousand patients who visited the
Indian Spinal Injuries Centre seeking for their treatment. The X-ray images of the patients focus or
highlight the thoracic and lumbar regions of the vertebral column. For each patient in the dataset,
there are two X-Ray images highlighting two different views namely AP and Lateral, that help in
identifying the underlying abnormality vividly. This gives us a total of 2000 X-ray images, equally
divided among the two views.

Here we have performed two tasks **A) Classification** and **B) Segmentation**

## A) Classification :

For classification task, we had to identify patients with damaged or normal spinal cord according
to the characteristics of their AP and LAT images. In this case we take the original RGB image for
both LAT and AP views and down sample them to 224x224x1. Then augment AP and LAT images
together and input it to the neural network. The output of the network will be a label (Damaged or
Normal).

### Our Result :
We adjusted the validation split in data to 0.1 ratio. Accuracy was used as metric and the validation
acc was 85%.

### Our Architecture :

Conv2d_1_input:InputLayer
___
conv2d_1:Conv2D
___
batch_normalization_1()
___
activation_1()
___
max_pooling_2d_1
___
conv2d_2:Conv2D()
___
batch_normalization_2()
___
activation_2()
___
max_pooling_2d_2()
___
conv2d_3:Conv2D()
___
batch_normalization_3()
___
activation_3()
___
max_pooling_2d_3
___
dropout_1()
___
flatten_1()
___
dense_1()
___
batch_normalization_4()
___
activation_4()
___
dense_2

## B) Segmentation

For the segmentation task, we had to create 3 masks for the AP image and 5 masks for the LAT
image. In this case we take the original RGB image for the two cases separately, down sample it to
224x224x3 and then input it to the neural network. The output of the network will be 224x224 masks
(single-channel). Hence we trained eight different models. Some test masks are shown below:  

### Our Architecture :

We use the UNET Architecture. The architecture is one of the state of the art architectures for
bio-medical image segmentation. Our U-Net implementation has 4 downblocks, 1 bottleneck layer
and 4 upblocks.
