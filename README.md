# example projects
 
This is a simple collection of projects to demonstrate skills. The files should be somewhat self-explanatory, but here's a description of what each file contains.

# google_vision_classification.py
This code takes a folder of images (and only images), and submits the images to the Google Vision API to label the images with 3 parameters: (1) a number of labels describing things contained in the image, (2) the likely emotion on the face of individuals in the image, and (3) performs optical character recognition to put in text form the images that actually contained text. The code outputs 3 CSVs containing the name of the image file annotated/labeled by the vision API and whatever applicable labels the google vision API could come up with. In essence, the code takes one folder full of images and outputs 3 csvs containing the name of those images and the accompanying labels from the API.

# Experiment Design
