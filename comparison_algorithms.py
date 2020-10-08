#modules
import math

#function for cosine similarity
def get_cosine_similarity(x_dim, y_dim):
    #input: equal dimension vectors of items x and y (each as a list)
    #output: cosine similarity score of the items x and y
    xy_sum_product, x_sum_squares, y_sum_squares = 0, 0, 0
    for x, y in zip(x_dim, y_dim):
        #compute squares and add to squared summation value
        x_sum_squares += x**2
        y_sum_squares += y**2
        #compute product and add to sum of product
        xy_sum_product += x*y
    #get cosine similarity (recall sqrt(x*y)=sqrt(x)*sqrt(y))
    return xy_sum_product/math.sqrt(x_sum_squares*y_sum_squares)

x, y = [1,45,51,10,6,5,1], [10,50,10,11,5,1,8]
print('cosine similarity is:', get_cosine_similarity(x, y))