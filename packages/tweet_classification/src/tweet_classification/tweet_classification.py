# -*- coding: utf-8 -*-
""" tweet_classification.py """
__author__ = 'abdullahbozdag'
__creation_date__ = '17.02.2023'

from typing import List

from transformers import pipeline


class TweetClassification:
    def __init__(self):
        self.classifier = pipeline(
            "zero-shot-classification", model="facebook/bart-large-mnli"
        )

    def classify(self, sentence: str, labels: List[str], multi_label: int = 0):
        if multi_label == 0:
            return self.classifier(sentence, labels, multi_label=False)
        else:
            return self.classifier(sentence, labels, multi_label=True)
