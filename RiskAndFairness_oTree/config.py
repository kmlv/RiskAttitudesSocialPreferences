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

import random
import copy
import pandas as pd

# if you want to turn off shuffling, change this to False
shuffle = True
 # randomiza numero de tareas por bloque
shuffle2 = True

# this will be a list, each element of which is the paying round for a group.
# With the default of 16 participants, there will be 8 groups, so chosen_rounds
# should never have more than 8 elements.
# If chosen rounds is empty, models.py will randomly assign the chosen round for each group.
# indexing starts at 1, not 0
chosen_rounds = []

data = [
    [
{'mode': 'sec_1bl_1ch', 'm': 	50.000	, 'p_x': 	1.000	},
{'mode': 'sec_1bl_1ch', 'm': 	50.773	, 'p_x': 	1.031	},
{'mode': 'sec_1bl_1ch', 'm': 	48.750	, 'p_x': 	0.950	},
{'mode': 'sec_1bl_1ch', 'm': 	52.778	, 'p_x': 	1.111	},
{'mode': 'sec_1bl_1ch', 'm': 	45.000	, 'p_x': 	0.800	},
{'mode': 'sec_1bl_1ch', 'm': 	58.333	, 'p_x': 	1.333	},
{'mode': 'sec_1bl_1ch', 'm': 	42.500	, 'p_x': 	0.700	},
{'mode': 'sec_1bl_1ch', 'm': 	62.879	, 'p_x': 	1.515	},
{'mode': 'sec_1bl_1ch', 'm': 	40.000	, 'p_x': 	0.600	},
{'mode': 'sec_1bl_1ch', 'm': 	75.000	, 'p_x': 	2.000	},
{'mode': 'sec_1bl_1ch', 'm': 	43.500	, 'p_x': 	0.700	},
{'mode': 'sec_1bl_1ch', 'm': 	76.879	, 'p_x': 	1.515	},
{'mode': 'sec_1bl_1ch', 'm': 	89.000	, 'p_x': 	0.600	},
{'mode': 'sec_1bl_1ch', 'm': 	55.000	, 'p_x': 	2.000	},
{'mode': 'sec_1bl_1ch', 'm': 	55.000	, 'p_x': 	2.000	},
    ],
    [
{'mode': 'sec_2bl_1ch', 'm': 	50.000	, 'p_x': 	1.000	},
{'mode': 'sec_2bl_1ch', 'm': 	50.773	, 'p_x': 	1.031	},
{'mode': 'sec_2bl_1ch', 'm': 	48.750	, 'p_x': 	0.950	},
{'mode': 'sec_2bl_1ch', 'm': 	52.778	, 'p_x': 	1.111	},
{'mode': 'sec_2bl_1ch', 'm': 	45.000	, 'p_x': 	0.800	},
{'mode': 'sec_2bl_1ch', 'm': 	58.333	, 'p_x': 	1.333	},
{'mode': 'sec_2bl_1ch', 'm': 	42.500	, 'p_x': 	0.700	},
{'mode': 'sec_2bl_1ch', 'm': 	62.879	, 'p_x': 	1.515	},
{'mode': 'sec_2bl_1ch', 'm': 	40.000	, 'p_x': 	0.600	},
{'mode': 'sec_2bl_1ch', 'm': 	75.000	, 'p_x': 	2.000	},
{'mode': 'sec_2bl_1ch', 'm': 	35.000	, 'p_x': 	0.400	},
{'mode': 'sec_2bl_1ch', 'm': 	100.758	, 'p_x': 	3.030	},
{'mode': 'sec_2bl_1ch', 'm': 	73.000	, 'p_x': 	1.550	},
{'mode': 'sec_2bl_1ch', 'm': 	31.000	, 'p_x': 	1.400	},
{'mode': 'sec_2bl_1ch', 'm': 	101.758	, 'p_x': 	4.030	},
    ],
    [
{'mode': 'det_giv', 'm': 37.7, 'p_x':0.41},
{'mode': 'det_giv', 'm': 33.29, 'p_x':0.32},
{'mode': 'det_giv', 'm': 51.32, 'p_x':1.05},
{'mode': 'det_giv', 'm': 52.78, 'p_x':1.11},
{'mode': 'det_giv', 'm': 58.33, 'p_x':1.33},
{'mode': 'det_giv', 'm': 62.88, 'p_x':1.52},
{'mode': 'det_giv', 'm': 75, 'p_x':2},
{'mode': 'det_giv', 'm': 100.76, 'p_x':3.03},
{'mode': 'det_giv', 'm': 50, 'p_x':1},
{'mode': 'det_giv', 'm': 48.75, 'p_x':0.95},
{'mode': 'det_giv', 'm': 47.5, 'p_x':0.9},
{'mode': 'det_giv', 'm': 43.75, 'p_x':0.75},
{'mode': 'det_giv', 'm': 41.5, 'p_x':0.66},
{'mode': 'det_giv', 'm': 37.5, 'p_x':0.5},
{'mode': 'det_giv', 'm': 33.25, 'p_x':0.33},
    ],
    [
{'mode': 'probability', 'a_x': 40, 'a_y': 5, 'b_x': 5, 'b_y': 51.666},
{'mode': 'probability', 'a_x': 38.2, 'a_y': 5, 'b_x': 5, 'b_y': 55.303},
{'mode': 'probability', 'a_x': 35, 'a_y': 5, 'b_x': 5, 'b_y': 65},
{'mode': 'probability', 'a_x': 31.6, 'a_y': 5, 'b_x': 5, 'b_y': 85.606},
{'mode': 'probability', 'a_x': 45, 'a_y': 5, 'b_x': 5, 'b_y': 45},
{'mode': 'probability', 'a_x': 25, 'a_y': 25, 'b_x': 5, 'b_y': 45},
{'mode': 'probability', 'a_x': 25, 'a_y': 25, 'b_x': 45, 'b_y': 5},
{'mode': 'probability', 'a_x': 51.666, 'a_y': 5, 'b_x': 5, 'b_y': 40},
{'mode': 'probability', 'a_x': 55.303, 'a_y': 5, 'b_x': 5, 'b_y': 38.2},
{'mode': 'probability', 'a_x': 65, 'a_y': 5, 'b_x': 5, 'b_y': 35},
{'mode': 'probability', 'a_x': 85.606, 'a_y': 5, 'b_x': 5, 'b_y': 31.6},
{'mode': 'probability', 'a_x': 70, 'a_y': 5, 'b_x': 5, 'b_y': 35},
{'mode': 'probability', 'a_x': 85.604, 'a_y': 5, 'b_x': 5, 'b_y': 31.6},
{'mode': 'probability', 'a_x': 27, 'a_y': 5, 'b_x': 5, 'b_y': 47},
{'mode': 'probability', 'a_x': 42, 'a_y': 5, 'b_x': 5, 'b_y': 47.68},
    ],
    #[
        #{'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': 0.5},
        # {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': .333, 'prob_a': 30},
        # {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': 0.25, 'prob_a': 30},
        # {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': 0.2},
        # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': 1},
        # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': .667},
        # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': 0.5},
        # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': 0.4},
        # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 1.5},
        # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 1},
        # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': .75},
        # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 0.6},
    #],
    #[
        #{'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': 1,       'a': 5, 'b': 5},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .667,    'a': 5, 'b': 5},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .5,      'a': 5, 'b': 5},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .4,      'a': 5, 'b': 5},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': 1,       'a': 23, 'b': 23, 'prob_a': 30},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .667,    'a': 23, 'b': 23, 'prob_a': 30},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .5,      'a': 23, 'b': 23},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .4,      'a': 23, 'b': 23},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': 1,       'a': 60, 'b': 60},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .667,    'a': 60, 'b': 60},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .5,      'a': 60, 'b': 60},
        # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .4,      'a': 60, 'b': 60},
    #],
    #[
     #   {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': 1,       'a': 15, 'b': 5},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': .667,    'a': 15, 'b': 5},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': .5,      'a': 5, 'b': 15, 'prob_a': 30},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': .4,      'a': 5, 'b': 15, 'prob_a': 30},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': 1,       'a': 13, 'b': 23},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': .667,    'a': 13, 'b': 23},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': .5,      'a': 23, 'b': 13},
        # {'mode': 'sec_otherrisk_ownfixed', 'm': 40, 'p_x': .4,      'a': 23, 'b': 13}
    #],
    #[
        #{'mode': 'sec_1bl_2ch', 'm': 20, 'p_x': 0.5},
        # {'mode': 'sec_1bl_2ch', 'm': 20, 'p_x': .333},
        # {'mode': 'sec_1bl_2ch', 'm': 30, 'p_x': 0.25},
        # {'mode': 'sec_1bl_2ch', 'm': 20, 'p_x': 0.2},
        # {'mode': 'sec_1bl_2ch', 'm': 40, 'p_x': 1},
        # {'mode': 'sec_1bl_2ch', 'm': 40, 'p_x': .667},
        # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 0.5, 'prob_a': 30},
        # {'mode': 'sec_1bl_2ch', 'm': 40, 'p_x': 0.4, 'prob_a': 30},
    #]
]

#aleatorizar numero de tareas por bloque
if shuffle2 == True:
    
    data2 = []
    for block in data:
        #elegir un numero random dentro del intervalo (1,nro_tasks_por_bloque)
        rand = random.randint(1,len(block)) 
        data2.append(random.sample(block,k=rand)) #colocar k=rand si desea aleatorizar el nro de tasks por bloque

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
    # shuffle each dict within each block
    for block in data:
        shuffled_data.append(random.sample(block, k=len(block))) ##randomiza el orden de las tareas por bloque

    # shuffle each block
    
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
                    dic['label'] = {'x': 'State A (' + str(dic['prob_a']) + '%)', 'y': 'State B (' + str(100 - dic['prob_a']) + '%)'}
            elif dic['mode'] in ['sec_ownrisk_fixedother', 'sec_otherrisk_ownfixed']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'fixed' not in dic and 'a' in dic and 'b' in dic: #check if this is what he wants here
                    dic['fixed'] = {'m': dic['a'] + dic['b'], 'p_x': 1, 'p_y': 1, 'a': dic['a']}
                if 'label' not in dic:
                    dic['label'] = {'x': 'State A (' + str(dic['prob_a']) + '%)', 'y': 'State B (' + str(100 - dic['prob_a']) + '%)'}
            elif dic['mode'] == 'probability':
                if 'label' not in dic:
                    dic['label'] = {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}
            elif dic['mode'] in ['det_giv']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'label' not in dic:
                    dic['label'] = {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}
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