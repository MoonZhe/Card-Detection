"Moon"
import os
import sys
import numpy as np
path = os.path.dirname(os.path.abspath(__file__))
import cv2
import Card
###############################################################################
#README
############################################################################### 
#filename = Image source
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 14:55:10 2018

@author: Moon
"""

"Moon"
import os
import sys
import numpy as np
path = os.path.dirname(os.path.abspath(__file__))
import cv2
import Card
###############################################################################
#README
############################################################################### 
#filename = Image source

#num_cards = Number of cards inside the picture

#If using images from assignment, training_image_filename = train_img_2,
#training_labels_filename = train_file_2

#If using images similar to real playing card, training_image_filename = train_img_1,
#training_labels_filename = train_file_1

#num_training_cards = 19 if using train_file_2 and 56 if train_file_1

############################################################################### 
#CONSTANTS
############################################################################### 
img_path = path + '/Card_Imgs/testtest.jpg.'
numofcards = 19
train_file_1 = path + '/Training/train.tsv'
train_file_2 = path + '/Training/train1.tsv'
train_img_1 = path + '/Training/train.png'
train_img_2 = path + '/Training/training.bmp'
numoftrainingcards = 56

total = 0
heart = 0
spades = 0
diamond = 0
club = 0
quit = 0 

############################################################################### 
if quit == 0:

#Image file: test.JPG Number of cards in the image: 4 Training Image file: train.png Training Label: train.tsv 56
    filename = img_path
    num_cards = numofcards
    training_image_filename = train_img_1
    training_labels_filename = train_file_1    
    num_training_cards = numoftrainingcards
    
    training = Card.get_training(training_labels_filename,training_image_filename,num_training_cards)
    suits = Card.get_suits(training_labels_filename,training_image_filename,num_training_cards)
    im = cv2.imread(filename)
    

#    #Debug: uncomment to see registered images
#    for i,c in enumerate(Card.getCards(im,num_cards)):
#      card = Card.find_closest_card(training,c,)
#      cv2.imshow(str(card),c)
#    cv2.waitKey(0) 
    
#    width = im.shape[0]
#    height = im.shape[1]
#    if width < height:
#     im = cv2.transpose(im)
#     im = cv2.flip(im,1)

   
    cards = [Card.find_closest_card(training,c) for c in Card.getCards(im,num_cards)]
    suits = [Card.find_closest_card(suits,c) for c in Card.getCards(im,num_cards)]

    print cards
#    print suits
    
    for index, x in enumerate(suits):
        if x == 'Spades': 
            spades += 1
            total += 1
            
        elif x == 'Club':
            club += 1
            total += 1
            
        elif x == 'Heart':
            heart += 1
            total += 1   
            
        elif x== 'Diamond':
            diamond+= 1
            total += 1
        
        else:
            total += 1
            
            
    print "Number of Spades = " , spades, "\n" "Number of Hearts = ",  heart, "\n" "Number of Clubs = " , club , " \n" "Number of Diamonds = " , diamond, "\n" "Total Cards = ", total

# Number of Diamonds = 2 Number of Spades = 1 Number of Clubs = 2 Number of Hearts = 1 Total Cards = 6       
             
quit = 1



#num_cards = Number of cards inside the picture

#If using images from assignment, training_image_filename = train_img_2,
#training_labels_filename = train_file_2

#If using images similar to real playing card, training_image_filename = train_img_1,
#training_labels_filename = train_file_1

#num_training_cards = 19 if using train_file_2 and 56 if train_file_1

############################################################################### 
#CONSTANTS
############################################################################### 
img_path = path + '/Card_Imgs/testtest.jpg.'
numofcards = 19
train_file_1 = path + '/Training/train.tsv'
train_file_2 = path + '/Training/train1.tsv'
train_img_1 = path + '/Training/train.png'
train_img_2 = path + '/Training/training.bmp'
numoftrainingcards = 56

total = 0
heart = 0
spades = 0
diamond = 0
club = 0
quit = 0 

############################################################################### 
if quit == 0:

#Image file: test.JPG Number of cards in the image: 4 Training Image file: train.png Training Label: train.tsv 56
    filename = img_path
    num_cards = numofcards
    training_image_filename = train_img_1
    training_labels_filename = train_file_1    
    num_training_cards = numoftrainingcards
    
    training = Card.get_training(training_labels_filename,training_image_filename,num_training_cards)
    suits = Card.get_suits(training_labels_filename,training_image_filename,num_training_cards)
    im = cv2.imread(filename)
    

#    #Debug: uncomment to see registered images
#    for i,c in enumerate(Card.getCards(im,num_cards)):
#      card = Card.find_closest_card(training,c,)
#      cv2.imshow(str(card),c)
#    cv2.waitKey(0) 
    
#    width = im.shape[0]
#    height = im.shape[1]
#    if width < height:
#     im = cv2.transpose(im)
#     im = cv2.flip(im,1)

   
    cards = [Card.find_closest_card(training,c) for c in Card.getCards(im,num_cards)]
    suits = [Card.find_closest_card(suits,c) for c in Card.getCards(im,num_cards)]

    print cards
#    print suits
    
    for index, x in enumerate(suits):
        if x == 'Spades': 
            spades += 1
            total += 1
            
        elif x == 'Club':
            club += 1
            total += 1
            
        elif x == 'Heart':
            heart += 1
            total += 1
            
        elif x== 'Diamond':
            diamond+= 1
            total += 1
        
        else:
            total += 1
            
            
    print "Number of Spades = " , spades, "\n" "Number of Hearts = ",  heart, "\n" "Number of Clubs = " , club , " \n" "Number of Diamonds = " , diamond, "\n" "Total Cards = ", total

# Number of Diamonds = 2 Number of Spades = 1 Number of Clubs = 2 Number of Hearts = 1 Total Cards = 6       
             
quit = 1


