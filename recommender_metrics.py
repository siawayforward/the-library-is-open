#import modules
from surprise import accuracy
from algorithm_data import *

#module including all methods that calculate the effectiveness of a recommender system
class RecommenderMetrics:

    def mean_absolute_error(self, predictions):
        return accuracy.mae(predictions, verbose=False)

    def root_mean_square_error(self, predictions):
        return accuracy.rmse(predictions, verbose=False)

    #leave one-out cross validation
    def LOO_CV_hit_rate(self):
        pass
    
    def average_reciprocal_hit_rank(self):
        pass

    def cumulative_hit_rate(self):
        pass

    def rating_hit_rate(self):
        pass

    def coverage(self):
        pass

    def diversity(self):
        pass

    def novelty(self):
        pass

    def churn(self):
        pass

    def responsiveness(self):
        pass


