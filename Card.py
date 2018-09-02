# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 14:51:53 2018

@author: Moon
"""

"Moon"
import sys
import numpy as np
sys.path.insert(0, "/usr/local/lib/python2.7/site-packages/") 
import cv2

def rectify(h):
  h = h.reshape((4,2))
  hnew = np.zeros((4,2),dtype = np.float32)

  add = h.sum(1)
  hnew[0] = h[np.argmin(add)]
  hnew[2] = h[np.argmax(add)]
   
  diff = np.diff(h,axis = 1)
  hnew[1] = h[np.argmin(diff)]
  hnew[3] = h[np.argmax(diff)]

  return hnew

###############################################################################
#IMAGE MATCHING
###############################################################################
def preprocess(img):
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray,(5,5), 5 )
#  thresh = cv2.adaptiveThreshold(blur,255,1,1,11,1)
  retval, thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
#  cv2.imshow('thresh', thresh)  
#  cv2.waitKey(0) 
  return thresh
 
  
def imgdiff(img1,img2):
  img1 = cv2.GaussianBlur(img1,(5,5),5)
  img2 = cv2.GaussianBlur(img2,(5,5),5)    
  diff = cv2.absdiff(img1,img2)  
  diff = cv2.GaussianBlur(diff,(5,5),5)    
  flag, diff = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY) 
#  cv2.imshow('Diff', diff)  
#  cv2.waitKey(0) 
  return np.sum(diff)  

def find_closest_card(training,img):
  features = preprocess(img)
  return sorted(training.values(), key=lambda x:imgdiff(x[1],features))[0][0]

  
   
###############################################################################
#CARD EXTRACTION
###############################################################################  
def getCards(im, numcards=4):
  gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray,(1,1),1000)
  flag, thresh = cv2.threshold(blur, 140, 255, cv2.THRESH_BINARY) 
#  cv2.imshow('thresh', thresh)  
#  cv2.waitKey(0) 
  _, contours, _= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  contours = sorted(contours, key=cv2.contourArea,reverse=True)[:numcards]  

  for card in contours:
    peri = cv2.arcLength(card,True)
    approx = rectify(cv2.approxPolyDP(card,0.02*peri,True))
#
#    box = np.int0(approx)
#    cv2.drawContours(im,[box],0,(255,255,0),6)
#    imx = cv2.resize(im,(1000,600))
#    cv2.imshow('a',imx)  
#    cv2.waitKey(0)     
#    
    h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)

    transform = cv2.getPerspectiveTransform(approx,h)
    warp = cv2.warpPerspective(im,transform,(450,450))
    
    yield warp

###############################################################################
#GET VALUE
############################################################################### 
def get_training(training_labels_filename,training_image_filename,num_training_cards,avoid_cards=None):
  training = {}

  labels = {}
  for line in file(training_labels_filename): 
    key, num, suit = line.strip().split()
    labels[int(key)] = (num,suit)
    
    
  im = cv2.imread(training_image_filename)
  for i,c in enumerate(getCards(im,num_training_cards)):
    if avoid_cards is None or (labels[i][0] not in avoid_cards[0] and labels[i][1] not in avoid_cards[1]):
      training[i] = (labels[i], preprocess(c))

  return training

  

def get_suits(training_labels_filename,training_image_filename,num_training_cards,avoid_cards=None):
  suits = {}
  
  labels = {}
  for line in file(training_labels_filename): 
    key, num, suit = line.strip().split()
    labels[int(key)] = (suit)
    
    
  im = cv2.imread(training_image_filename)
  for i,c in enumerate(getCards(im,num_training_cards)):
    if avoid_cards is None or (labels[i][0] not in avoid_cards[0] and labels[i][1] not in avoid_cards[1]):
      suits[i] = (labels[i], preprocess(c))
      
  return suits

    
#   Number of Diamonds = 2 Number of Spades = 1 Number of Clubs = 2 Number of Hearts = 1 Total Cards = 6  