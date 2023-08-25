import numpy as np
import random

def auto_epsilon_lexicase_selection(scores, k, n_parents=1,):
    """Select the best individual according to Auto Epsilon Lexicase Selection, *k* times. 
    The returned list contains the indices of the chosen *individuals*.
    :param scores: The score matrix, where rows the individulas and the columns correspond to scores on different objectives.
    :returns: A list of indices of selected individuals.
    This function uses the :func:`~random.choice` function from the python base
    :mod:`random` module.
    """
    chosen =[]
    for i in range(k*n_parents):
        candidates = list(range(len(scores)))
        cases = list(range(len(scores[0])))
        random.shuffle(cases)
        
        while len(cases) > 0 and len(candidates) > 1:
            errors_for_this_case = scores[candidates,cases[0]]
            median_val = np.median(errors_for_this_case)
            median_absolute_deviation = np.median([abs(x - median_val) for x in errors_for_this_case])
            best_val_for_case = max(errors_for_this_case )
            min_val_to_survive = best_val_for_case - median_absolute_deviation
            candidates = [x for x in candidates if scores[x, cases[0]] >= min_val_to_survive]
            cases.pop(0)
        chosen.append(random.choice(candidates))

    return np.reshape(chosen, (k, n_parents))