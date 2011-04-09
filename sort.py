#!/usr/bin/env python

from os import listdir
from math import sqrt

titlename = "/root/hack/lern/datasets/netflix/download/movie_titles.txt"
dataset = "/root/hack/lern/datasets/netflix/download/training_set"

class Sort(object):
    """ Returns recommendations """

    def __init__(self,titlename,dataset):
        self.titlename = titlename
        self.dataset = dataset
        self.titles = self.collect_titles()
        self.files = self.listdir(dataset) # returns list of all mv_ files (17770)
        self.users = self.build_users()

    def collect_titles(self):
        """ Iterates through movie_titles.txt """
        titles = {}
        fin = open(self.titlename,'rb')
        for line in fin:
            line = line.strip().split(',')
            # [movie_id, title, date]
            titles[line[0]] = []
            titles[line[0]].append([line[1],line[2]])

        return titles

    def build_users(self):
        """ Returns list of User objects """
        """ Returns 2D dictionary of form
        {user_id: {movie: rating, movie2: rating}}, etc"""
        users = {}
        # {user_id : User(user_id)}
        for fil in self.files:
            fin = open(fil,'rb')
            movie_id = fin.readline().strip() # first line is movie id

            for line in fin:
                # Line of form [user_id, rating, date]
                line.strip().split(',')
                user_id, rating = line[0],line[1]
                if user_id not in users:
                    user = User(user_id)
                    users[user.name] = user
                user.add_movie(movie_id,rating)

        return users

    def compare(self,user1,user2):
        pass

    def pearson(self):
        pass


class User(object):

    def __init__(self, name):
        self.name = name
        self.movies = {}

    def add_movie(self,movie,rating):
        if movie not in self.movies:
            movies[movie] = rating


def sim_pearson(prefs,p1,p2):
# Calculate top-rated movies
    """
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    n = len(si) # number of elements

    if n == 0: return 0 # no ratings in common
    """

    # Add up preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sum up squares
    sum1Sq = sum([prefs[p1][it]**2 for it in si])
    sum2Sq = sum([prefs[p2][it]**2 for it in si])

    # Sump up products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate Pearson score
    num = pSum - ((sum1*sum2)/n)
    den = sqrt((sum1Sq - (sum1**2)/n)*(sum2Sq - (sum2**2)/n))

    return num/den


if __name__ == "__main__":
    pass
