# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:48:00 2026

@author: egarl
"""

# QE experiment: classify scores by severity

def classify_qe(score):
    if score < 70:
        return "High priority review"
    elif score < 85:
        return "Normal review"
    else:
        return "Accept"

scores = [92, 78, 85, 63, 97]

for score in scores:
    result = classify_qe(score)
    print(f"QE score: {score}, Decision: {result}")

