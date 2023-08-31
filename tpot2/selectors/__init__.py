from .lexicase_selection import lexicase_selection
from .max_weighted_average_selector import max_weighted_average_selector
from .random_selector import random_selector
from .tournament_selection import tournament_selection
from .tournament_selection_dominated import tournament_selection_dominated
from .epsilon_lexicase_selection import auto_epsilon_lexicase_selection
from .nsgaii import nondominated_sorting, crowding_distance, dominates, survival_select_NSGA2


SELECTORS =     {"lexicase":lexicase_selection,
                "max_weighted_average":max_weighted_average_selector,
                "random":random_selector,
                "tournament":tournament_selection,
                "tournament_dominated":tournament_selection_dominated,
                "nsgaii":survival_select_NSGA2,
                "auto_epsilon_lexicase": auto_epsilon_lexicase_selection,
                }