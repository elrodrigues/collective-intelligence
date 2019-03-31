# A dictionary of movie critics and their ratings of a small
# set of movies
mv = ['Lady in the Water', 'Snakes on a Plane', 'Just My Luck', 'Superman Returns', 'You, Me and Dupree', 'The Night Listener']
critics = {
        'Lisa Rose': {mv[0]: 2.5, mv[1]: 3.5, mv[2]: 3.0, mv[3]: 3.5,
            mv[4]: 2.5, mv[5]: 3.0},
        'Gene Seymour': {mv[0]: 3.0, mv[1]: 3.5, mv[2]: 1.5, mv[3]: 5.0,
            mv[4]: 3.5, mv[5]: 3.0},
        'Michael Phillips': {mv[0]: 2.5, mv[1]: 3.0, mv[3]: 4.0,
            mv[4]: 2.5},
        'Claudia Puig': {mv[1]: 3.5, mv[2]: 3.0, mv[3]: 4.0, mv[4]: 2.5,
            mv[5]: 4.5},
        'Mick LaSalle': {mv[0]: 3.0, mv[1]: 4.0, mv[2]: 2.0, mv[3]: 3.0,
            mv[4]: 2.0, mv[5]: 3.0},
        'Jack Matthews': {mv[0]: 3.0, mv[1]: 4.0, mv[3]: 5.0, mv[4]: 3.5,
            mv[5]: 3.0},
        'Toby': {mv[1]: 4.5, mv[3]: 4.0, mv[4]: 1.0}
        }
from math import sqrt

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, p1, p2):
    # Get list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # if they have no ratings in common, return 0
    if len(si) == 0: return 0

    # add up squares of differences
    sum_of_sq = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in si])
    return 1 / (1 + sum_of_sq)
# end sin_distance]

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)
    if n == 0: return 0

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq - pow(sum1, 2)/n) * (sum2Sq - pow(sum2, 2)/n))
    if den == 0: return 0

    return num/den
# end sim_pearson
