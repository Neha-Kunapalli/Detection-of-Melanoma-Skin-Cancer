# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:05:25 2021

@author: User
"""
import cv2

def main(file):
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img1 = cv2.GaussianBlur(gray, (5, 5), 0)
    img2 = cv2.medianBlur(gray, 3)
    img3 = cv2.bilateralFilter(gray,9,75,75)
    cv2.imshow('Original image',image)
    cv2.imshow('Gray image', gray)
    cv2.imshow('guassian image',img1)
    cv2.imshow('median blur image', img2)
    cv2.imshow('bilateral image', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()