import numpy as np
import pandas as pd
import urllib.request
import json
import os
import ssl

# Function to calculate mean score for a trait
def calculate_mean_score(responses):
    trait_score = np.mean(list(responses.values()))
    min_score = 1
    max_score = 5
    normalized_score = (trait_score-min_score)/(max_score-min_score)
    return normalized_score

# Function to give description based on score
def get_trait_description(trait, score):
    descriptions = {
        'Openness': {
            'high': 'You are creative, curious, and open to new experiences!',
            'medium': 'You are moderately open to new ideas and experiences.',
            'low': 'You prefer familiar experiences and tend to be more conventional.'
        },
        'Extraversion': {
            'high': 'You are outgoing, energetic, and enjoy being around people.',
            'medium': 'You are somewhat outgoing but also value your alone time.',
            'low': 'You prefer solitude and tend to be more reserved.'
        },
        'Neuroticism': {
            'high': 'You may experience strong emotions and sometimes feel anxious or sensitive.',
            'medium': 'You are relatively calm but may have occasional emotional ups and downs.',
            'low': 'You are emotionally stable and handle stress well.'
        },
        'Agreeableness': {
            'high': 'You are cooperative, compassionate, and considerate of others.',
            'medium': 'You are generally friendly but can be assertive when needed.',
            'low': 'You are assertive and prefer to prioritize your own needs.'
        },
        'Conscientiousness': {
            'high': 'You are organized, responsible, and reliable.',
            'medium': 'You are somewhat organized but may have moments of spontaneity.',
            'low': 'You tend to be more spontaneous and less focused on details.'
        }
    }

    if score >= 0.7:
        return descriptions[trait]['high']
    elif score >= 0.35:
        return descriptions[trait]['medium']
    else:
        return descriptions[trait]['low']
