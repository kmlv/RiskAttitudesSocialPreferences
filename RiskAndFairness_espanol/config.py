'''
Please use lowercase for dictionary keys in the future // Rachel

# default probability in Security mode is prob_a: 0, prob_b: 100

# positive -> sec_1bl_1ch;
# negative -> sec_2bl_1ch;
# independent -> sec_1bl_2ch;
# single -> sec_ownrisk

Kristian Lopez Vargas <kristianlvargas@gmail.com>
Eli Pandolfo <epandolf@ucsc.edu>

'''
from .models import BasePlayer as Player
import random
import copy
from turtle import xcor
import pandas as pd
import math



# if you want to turn off shuffling, change this to False
shuffle = True
 # randomiza numero de tareas por bloque
shuffle2 = False
# shuffle_treatments = True

# this will be a list, each element of which is the paying round for a group.
# With the default of 16 participants, there will be 8 groups, so chosen_rounds
# should never have more than 8 elements.
# If chosen rounds is empty, models.py will randomly assign the chosen round for each group.
# indexing starts at 1, not 0
chosen_rounds = []

data = [
# [
# {'mode': 'sec_ownrisk', 'm': 33.32, 'p_x': .33, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 34.2, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 35.16, 'p_x': .41, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 36.23, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 37.41, 'p_x': .5, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 38.72, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 40.16, 'p_x': .61, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 41.76, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 43.52, 'p_x': .74, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 45.47, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 46.52, 'p_x': .86, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 47.62, 'p_x': .9, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 48.78, 'p_x': .9500000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 50, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 51.28, 'p_x': 1.05, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 52.63, 'p_x': 1.11, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 54.05, 'p_x': 1.16, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 55.54, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 58.75, 'p_x': 1.35, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 62.3, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 66.22, 'p_x': 1.65, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 70.55, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 75.34, 'p_x': 2.01, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 80.64, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 86.49, 'p_x': 2.46, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 92.96000000000001, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100.1, 'p_x': 3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 3.32, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 4.060000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 100, 'p_x': 4.95, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 20.19, 'p_x': .2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 24.66, 'p_x': .25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 30.12, 'p_x': .3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 36.79, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 44.93, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 54.88, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 67.03, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 81.87000000000001, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 54.21, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 58.46, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 63.66, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 70, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 77.75, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 87.21000000000001, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
# {'mode': 'sec_ownrisk', 'm': 98.77, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}}
# ],
[
{'mode': 'sec_1bl_1ch', 'm': 33.32, 'p_x': .33, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 34.2, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 35.16, 'p_x': .41, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 36.23, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 37.41, 'p_x': .5, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 38.72, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 40.16, 'p_x': .61, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 41.76, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 43.52, 'p_x': .74, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 45.47, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 46.52, 'p_x': .86, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 47.62, 'p_x': .9, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 48.78, 'p_x': .9500000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 50, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 51.28, 'p_x': 1.05, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 52.63, 'p_x': 1.11, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 54.05, 'p_x': 1.16, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 55.54, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 58.75, 'p_x': 1.35, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 62.3, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 66.22, 'p_x': 1.65, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 70.55, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 75.34, 'p_x': 2.01, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 80.64, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 86.49, 'p_x': 2.46, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 92.96000000000001, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100.1, 'p_x': 3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 3.32, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 4.060000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 100, 'p_x': 4.95, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 20.19, 'p_x': .2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 24.66, 'p_x': .25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 30.12, 'p_x': .3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 36.79, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 44.93, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 54.88, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 67.03, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 81.87000000000001, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 54.21, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 58.46, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 63.66, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 70, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 77.75, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 87.21000000000001, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_1bl_1ch', 'm': 98.77, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}}
],
[
{'mode': 'sec_2bl_1ch', 'm': 33.32, 'p_x': .33, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 34.2, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 35.16, 'p_x': .41, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 36.23, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 37.41, 'p_x': .5, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 38.72, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 40.16, 'p_x': .61, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 41.76, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 43.52, 'p_x': .74, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 45.47, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 46.52, 'p_x': .86, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 47.62, 'p_x': .9, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 48.78, 'p_x': .9500000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 50, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 51.28, 'p_x': 1.05, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 52.63, 'p_x': 1.11, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 54.05, 'p_x': 1.16, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 55.54, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 58.75, 'p_x': 1.35, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 62.3, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 66.22, 'p_x': 1.65, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 70.55, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 75.34, 'p_x': 2.01, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 80.64, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 86.49, 'p_x': 2.46, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 92.96000000000001, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100.1, 'p_x': 3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 3.32, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 4.060000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 100, 'p_x': 4.95, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 20.19, 'p_x': .2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 24.66, 'p_x': .25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 30.12, 'p_x': .3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 36.79, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 44.93, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 54.88, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 67.03, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 81.87000000000001, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 54.21, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 58.46, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 63.66, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 70, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 77.75, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 87.21000000000001, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_2bl_1ch', 'm': 98.77, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}}
],
[
{'mode': 'probability', 'a_x': 91, 'a_y': 5, 'b_x': 5, 'b_y': 31, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 79, 'a_y': 5, 'b_x': 5, 'b_y': 32, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 70, 'a_y': 5, 'b_x': 5, 'b_y': 34, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 61, 'a_y': 5, 'b_x': 5, 'b_y': 36, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 55, 'a_y': 5, 'b_x': 5, 'b_y': 38, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 49, 'a_y': 5, 'b_x': 5, 'b_y': 41, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 45, 'a_y': 5, 'b_x': 5, 'b_y': 45, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 41, 'a_y': 5, 'b_x': 5, 'b_y': 49, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 38, 'a_y': 5, 'b_x': 5, 'b_y': 55, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 36, 'a_y': 5, 'b_x': 5, 'b_y': 61, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 34, 'a_y': 5, 'b_x': 5, 'b_y': 70, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 32, 'a_y': 5, 'b_x': 5, 'b_y': 79, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 31, 'a_y': 5, 'b_x': 5, 'b_y': 91, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 25, 'a_y': 25, 'b_x': 5, 'b_y': 31, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 25, 'a_y': 25, 'b_x': 5, 'b_y': 45, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 25, 'a_y': 25, 'b_x': 5, 'b_y': 91, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 91, 'a_y': 5, 'b_x': 25, 'b_y': 25, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 45, 'a_y': 5, 'b_x': 25, 'b_y': 25, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 31, 'a_y': 5, 'b_x': 25, 'b_y': 25, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 85, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 70, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 59, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 49, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 41, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 34, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 29, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 25, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'probability', 'a_x': 21, 'a_y': 5, 'b_x': 5, 'b_y': 85, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}}
],
[
{'mode': 'det_giv', 'm': 33.32, 'p_x': .33, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 34.2, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 35.16, 'p_x': .41, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 36.23, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 37.41, 'p_x': .5, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 38.72, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 40.16, 'p_x': .61, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 41.76, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 43.52, 'p_x': .74, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 45.47, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 46.52, 'p_x': .86, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 47.62, 'p_x': .9, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 48.78, 'p_x': .9500000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 51.28, 'p_x': 1.05, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 52.63, 'p_x': 1.11, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 54.05, 'p_x': 1.16, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 55.54, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 58.75, 'p_x': 1.35, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 62.3, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 66.22, 'p_x': 1.65, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 70.55, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 75.34, 'p_x': 2.01, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 80.64, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 86.49, 'p_x': 2.46, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 92.96000000000001, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100.1, 'p_x': 3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 2.23, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 2.72, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 3.32, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 4.060000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 100, 'p_x': 4.95, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 20.19, 'p_x': .2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 24.66, 'p_x': .25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 30.12, 'p_x': .3, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 36.79, 'p_x': .37, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 44.93, 'p_x': .45, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 54.88, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 67.03, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 81.87000000000001, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 54.21, 'p_x': .55, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 58.46, 'p_x': .67, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 63.66, 'p_x': .8200000000000001, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 70, 'p_x': 1, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 77.75, 'p_x': 1.22, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 87.21000000000001, 'p_x': 1.49, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}},
{'mode': 'det_giv', 'm': 98.77, 'p_x': 1.82, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}}
],
[
{'mode': 'sec_ownrisk_fixedother', 'm': 33.32, 'p_x': .33, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 34.2, 'p_x': .37, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 35.16, 'p_x': .41, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 36.23, 'p_x': .45, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 37.41, 'p_x': .5, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 38.72, 'p_x': .55, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 40.16, 'p_x': .61, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 41.76, 'p_x': .67, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 43.52, 'p_x': .74, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 45.47, 'p_x': .8200000000000001, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 46.52, 'p_x': .86, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 47.62, 'p_x': .9, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 48.78, 'p_x': .9500000000000001, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 50, 'p_x': 1, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 51.28, 'p_x': 1.05, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 52.63, 'p_x': 1.11, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 54.05, 'p_x': 1.16, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 55.54, 'p_x': 1.22, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 58.75, 'p_x': 1.35, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 62.3, 'p_x': 1.49, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 66.22, 'p_x': 1.65, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 70.55, 'p_x': 1.82, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 75.34, 'p_x': 2.01, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 80.64, 'p_x': 2.23, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 86.49, 'p_x': 2.46, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 92.96000000000001, 'p_x': 2.72, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100.1, 'p_x': 3, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 1.22, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 1.49, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 1.82, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2.23, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2.72, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 3.32, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 4.060000000000001, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 4.95, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 20.19, 'p_x': .2, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 24.66, 'p_x': .25, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 30.12, 'p_x': .3, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 36.79, 'p_x': .37, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 44.93, 'p_x': .45, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 54.88, 'p_x': .55, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 67.03, 'p_x': .67, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 81.87000000000001, 'p_x': .8200000000000001, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 54.21, 'p_x': .55, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 58.46, 'p_x': .67, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 63.66, 'p_x': .8200000000000001, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 70, 'p_x': 1, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 77.75, 'p_x': 1.22, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 87.21000000000001, 'p_x': 1.49, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}},
{'mode': 'sec_ownrisk_fixedother', 'm': 98.77, 'p_x': 1.82, 'a': 0, 'b': 0, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 0, 'p_x': 1, 'p_y': 1, 'a': 0}, 'label': {'x': 'Fichas en Estado A (50%)', 'y': 'Fichas en Estado B (50%)'}}
]
]

#aleatorizar numero de tareas por bloque
if shuffle2 == True:
    
    data2 = []

    #sin randomizar 
    tasks_por_bloque = [10,12,10,15]
    
    #randomizando // habilitar cuando se desee aleatorizar el nro de tareas por bloque
    #tasks_por_bloque_rand = [random.randint(1,len(block)) for block in data ] 
    
    #cambiar tasks_por_bloque por tasks_por_bloque_rand si se desea aleatorizar el nro de tareas por bloque
    for block, tasks in zip(data,tasks_por_bloque):  
     
        data2.append(random.sample(block,k=tasks)) 

    data = data2 #setear la nueva data

# data = [
#     # [
#     #    
#     # ],
#     # [
#     #     {'mode': 'sec_1bl_1ch', 'm': 50, 'p_x': 0.60},
#     # ],
#     # [
#     #     {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2},
#     # ],
#     [
#         {'mode': 'sec_2bl_1ch', 'm': 50, 'p_x': 0.60},
#     ],
#     # [
#     #     {'mode': 'sec_ownrisk', 'm': 50, 'p_x': 0.60},
#     # ],
#     # [
#     #     {'mode': 'sec_ownrisk_fixedother', 'm': 50, 'p_x': 0.60, 'a': 30, 'b': 13.3},
#     # ],
#     # [
#     #     {'mode': 'sec_otherrisk_ownfixed', 'm': 50, 'p_x': 0.60, 'a': 30, 'b': 13.3},
#     # ],
#     # [
#     #     {'mode': 'probability', 'a_x': 70, 'a_y': 10, 'b_x': 10, 'b_y': 80}
#     # ]
# ]

def shuffle(data):

    if shuffle == False:
        return data

    shuffled_data = []

    # shuffle each block
    session_1=[2,3,5,4,1]
    session_2=[3,2,5,4,1]
    session_3=[2,3,4,5,1]
    session_4=[3,2,4,5,1]
    session_5=[4,3,1,2,5]
    #session_6=[4,3,2,1,5]
    session_7=[3,4,1,2,5]
    session_8=[3,4,2,1,5]

    list_sessions=[session_1, session_2, session_3, session_4, session_5, session_7, session_8]
    random_session= random.choice(list_sessions)
    print('random_session: ',random_session)
    sorted_data = [i for _,i in sorted(zip(random_session,data))]

    for block in sorted_data:
        shuffled_data.append(random.sample(block, k=len(block))) ##randomiza el orden de las tareas por bloque
    return shuffled_data


def flatten(shuffled_data):
    return [period for block in shuffled_data for period in block]

# converts config data into a pandas dataframe, for exporting to the visualization fcn
def export_data(data, session_name):
    cols = ['mode', 'm', 'p_x', 'a', 'b', 'a_x', 'a_y', 'b_x', 'b_y']
    df = pd.DataFrame(columns=cols)
    for period in flatten(data):
        for key in period:
            # convert all dict values to lists to allow creation of dataframe
            period[key] = [period[key]]
        df1 = pd.DataFrame(period)
        df = df.append(df1)

    df.to_csv('visualization/data/config_' + session_name + '.csv')



def checkValidity(flattened_data):
    for period in flattened_data:
        if 'prob_a' in period:
            if period['prob_a'] < 0 or period['prob_a'] > 100:
                print('ERROR: invalid prob_a in round', flattened_data.index(period), ': prob_a is: ',
                    period['prob_a'], ' but must be a number between 0 and 100')
                return 0
    return 1

def numberOfPeriod():
    return len(flatten(data))


# CHECK WHAT HE WANTS FOR PROBABILITY AND FIXED FOR ALT OWNRISKSa
def fill_defaults(data):
    newdata = copy.deepcopy(data)
    for block in newdata:
        for dic in block:
            if dic['mode'] in ['sec_1bl_1ch', 'sec_2bl_1ch', 'sec_1bl_2ch', 'sec_ownrisk']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'label' not in dic:
                    dic['label'] = {'x': 'Estado A (' + str(dic['prob_a']) + '%)', 'y': 'Estado B (' + str(100 - dic['prob_a']) + '%)'}
            elif dic['mode'] in ['sec_ownrisk_fixedother', 'sec_otherrisk_ownfixed']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'fixed' not in dic and 'a' in dic and 'b' in dic: #check if this is what he wants here
                    dic['fixed'] = {'m': dic['a'] + dic['b'], 'p_x': 1, 'p_y': 1, 'a': dic['a']}
                if 'label' not in dic:
                    dic['label'] = {'x': 'Estado A (' + str(dic['prob_a']) + '%)', 'y': 'Estado B (' + str(100 - dic['prob_a']) + '%)'}
            elif dic['mode'] == 'probability':
                if 'label' not in dic:
                    dic['label'] = {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}
            elif dic['mode'] in ['det_giv']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'label' not in dic:
                    dic['label'] = {'x': 'Tus fichas', 'y': 'Las fichas de tu pareja'}
    return newdata

def getDynamicValues():
    dynamic_values = fill_defaults(data)
    if checkValidity(flatten(dynamic_values)) == 0:
        return 0
    return dynamic_values

def getChosenRounds():
    if len(chosen_rounds) == 0:
        return None
    else:
        return chosen_rounds


# Syntax for data dictionaries
# {'mode': 'det_giv', 'm': 50, 'p_x': 0.5, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': "Partner's Tokens"}}
# {'mode': 'sec_1bl_1ch', 'm': 50, 'p_x': 0.6, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)', 'y': 'State B (50%)'}}
# {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)', 'y': 'State B (50%)'}}
# {'mode': 'sec_2bl_1ch', 'm': 50, 'p_x': 0.6, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)', 'y': 'State B (50%)'}}
# {'mode': 'sec_ownrisk', 'm': 50, 'p_x': 0.6, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)', 'y': 'State B (50%)'}}
# {'mode': 'sec_ownrisk_fixedother', 'm': 50, 'p_x': 0.6, 'a': 30, 'b': 13.3, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 43.3, 'p_x': 1, 'p_y': 1, 'a': 30}, 'label': {'x': 'State A (50%)', 'y': 'State B (50%)'}}
# {'mode': 'sec_otherrisk_ownfixed', 'm': 50, 'p_x': 0.6, 'a': 30, 'b': 13.3, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 43.3, 'p_x': 1, 'p_y': 1, 'a': 30}, 'label': {'x': 'State A (50%)', 'y': 'State B (50%)'}}
# {'mode': 'probability', 'a_x': 70, 'a_y': 10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'Your Tokens', 'y': "Partner's Tokens"}}

