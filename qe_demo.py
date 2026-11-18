# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:41:10 2026

@author: egarl
"""

# Simple QE threshold experiment

def classify_qe(score, threshold=85):
    if score < threshold:
        return "Human review"
    return "Accept"

scores = [92, 78, 85, 63, 97]

for score in scores:
    result = classify_qe(score)
    print(f"QE score: {score}, Decision: {result}")

