#module to prepare data for evaluation and model generation
#use surprise model_selection package for this 
# https://surprise.readthedocs.io/en/stable/model_selection.html
from surprise.model_selection import split

def load_data():
    pass

class EvaluationData():
    def __init__(self):
        self.full_dataset = load_data()

    def train_test_dataset(self):
        return split.train_test_split(self.full_dataset, test_size=0.3, random_state=1)

    def full_train_dataset(self):
        return self.full_dataset

    def leave_one_out_dataset(self):
        return split.LeaveOneOut(n_splits=5, random_state=1, min_n_ratings=1)

    def anti_test_dataset(self):
        pass
    
    
