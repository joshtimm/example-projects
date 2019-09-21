## Author: Joshua Timm
## Purpose: This code takes a folder of images (and only images), and submits the images to the Google Vision API to label the images with 3 parameters: (1) a number of labels describing things contained in the image, (2) the likely emotion on the face of individuals in the image, and (3) performs optical character recognition to put in text form the images that actually contained text. The code outputs 3 CSVs containing the name of the image file annotated/labeled by the vision API and whatever applicable labels the google vision API could come up with. In essence, the code takes one folder full of images and outputs 3 csvs containing the name of those images and the accompanying labels from the API.
import io
import os
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# AUTHENTICATION: authenticate your terminal with Google's Vision API. MUST USE YOUR OWN CREDENTIALS!
# type this code into your actual computer's terminal, NOT in python
# "<" denotes the start of a code chunk and ">" denotes the end of a code chunk
# terminal code: <export GOOGLE_APPLICATION_CREDENTIALS=~/DROPBOX/google_cloud/your-credential.json>

# Instantiates a client
client = vision.ImageAnnotatorClient()
# make the __file__ object so you can call it later with an io.open command
__file__ = "/Users/username/Dropbox/images-to-classify/"
# make the folder object so you can list all the files in the directory that you want to iterate through for the API calls.
folder = os.listdir(__file__) # return back to the folder in line 58 (start of the loop)

############################
# INSTANTIATE CSV FILES
############################

# instantiate the CSV files that you'll be appending to
###### LABELS
LABELS = ['image_id', 'label_description', 'label_score']
LABEL_FILE = open('IMAGE_LABELS.csv', 'w')
with LABEL_FILE:
    writer = csv.writer(LABEL_FILE)
    writer.writerow(LABELS)

###### FACES
FACES = ['image_id', 'face_number', 'anger_likelihood', 'joy_likelihood', 'sorrow_likelihood', 'surprise_likelihood']
FACE_FILE = open('IMAGE_FACES.csv', 'w')
with FACE_FILE:
    writer = csv.writer(FACE_FILE)
    writer.writerow(FACES)

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   'LIKELY', 'VERY_LIKELY')
####### OCR / TEXT
# a work in progress
TEXT = ['image_id', 'text']
TEXT_FILE  = open('IMAGE_OCR.csv', 'w')
with TEXT_FILE:
    writer = csv.writer(TEXT_FILE)
    writer.writerow(TEXT)

##################
# LOOP
##################
for jpg in folder:

    # identify the file to send to the vision API
    file_name = os.path.join(os.path.dirname(__file__), jpg)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)

    ########## LABELS #############

    #extract the labels and add them to the LABELS csv
    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        LABEL_FILE = open('IMAGE_LABELS.csv', 'a')
        with LABEL_FILE:
            writer = csv.writer(LABEL_FILE)
            print('writer: jpg:', jpg)
            writer.writerow([jpg, label.description, label.score])
            ## jpg = image_id
            ## label.description = the human language description of a thing in the public
            ## label.score = the confidence score from google about how sure google is about the label's accuracy

    ########## FACES #################
    response = client.face_detection(image=image)
    faces = response.face_annotations
    counter = 1
    for face in faces:
        FACE_FILE = open('IMAGE_FACES.CSV', 'a')
        with FACE_FILE:
            print('face: jpg:', jpg)
            writer = csv.writer(FACE_FILE)
            # set order of anger > joy > sorrow > surprise
            anger_likelihood = format(likelihood_name[face.anger_likelihood])
            joy_likelihood = format(likelihood_name[face.joy_likelihood])
            sorrow_likelihood = format(likelihood_name[face.sorrow_likelihood])
            surprise_likelihood = format(likelihood_name[face.surprise_likelihood])
            writer.writerow([jpg, counter, anger_likelihood, joy_likelihood, sorrow_likelihood, surprise_likelihood])
            counter += 1

    ############### OCR / TEXT #################
    response = client.text_detection(image=image)
    texts = response.text_annotations
    text_join = []
    # the format for each of the vision API text annotations is to place the entirety of the text at position 0,
    # and then from position 1 onwards it lists each word/token of the entire text
    for text in texts[1:]:
        text_join.append(format(text.description))
    full_text = ' '.join(text_join)


    TEXT_FILE = open('IMAGE_OCR.csv', 'a')
    with TEXT_FILE:
        writer = csv.writer(TEXT_FILE)
        print('text: jpg:', jpg)
        writer.writerow([jpg, full_text])

