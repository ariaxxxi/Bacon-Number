#!/usr/bin/env python3

import pickle


def transform_data(raw_data):
    d = {}
    for item in raw_data:
        # print(type(item))
        k,v,m = item
        d.setdefault(k,[]).append(v)
        d.setdefault(v,[]).append(k)
    return d    



def acted_together(database, actor_id_1, actor_id_2):

    if actor_id_2 in set(database[actor_id_1]):
        return True
    elif actor_id_1 in set(database[actor_id_2]):
        return True
    elif actor_id_1 == actor_id_2:
        return True
    else:
        return False


def exist(database, actor_id):
    if actor_id in set(database.keys()):
        return True
    else:
        return False



def actors_with_bacon_number(database, n):
    ls = {4724}
    all_actor = {4724}


    def factorial(n, ls):
        for i in range(1,n+1):
            # print("hi")
            newls  = set()             #create a set list for (n) layer   

            for actor_id in ls:
                for elm in database[actor_id] :
                    if elm not in all_actor :
                        newls.add(elm) 
                        all_actor.add(elm)
            if newls == set():
                break
            ls = newls 
        return ls
   
    return factorial(n, ls)
   


def bacon_path(database, actor_id):
    path = [actor_id]

    def factorial(n):
        if actor_id in actors_with_bacon_number(database, n):
            return n
        else:
            return factorial(n+1)
    
    if exist(database, actor_id) == False:
        return None

    else:
        level = factorial(0)
        print(level)
        def fact(actor_id,n):
            if n == 0:
                return path
            else:
                for id_next in actors_with_bacon_number(database, n-1):
                    if acted_together(database, actor_id, id_next) == True :           
                        path.insert(0,id_next)
                        return fact(id_next, n-1)   
        return fact(actor_id,level)



def actor_to_actor1_number(database, actor_id_1, n):
    ls = {actor_id_1}
    all_actor = {actor_id_1}
    def factorial(n, ls):
        for i in range(1,n+1):

            newls  = set()   
            for actor_id in ls:
                for elm in database[actor_id] :
                    if elm not in all_actor :
                        newls.add(elm) 
                        all_actor.add(elm)
            if newls == set():
                break
            ls = newls       
        return ls
    return factorial(n, ls)
   


def actor_to_actor_path(database, actor_id_1, actor_id_2):
    path = [actor_id_2]
    def factorial(n):
        if actor_id_2 in actor_to_actor1_number(database,actor_id_1, n):
            return n
        else:
            return factorial(n+1)
    
    level = factorial(0)

    if exist(database, actor_id_2) == False:
        return None
    else:
        def fact(actor_id_2,n):
            if n == 0:
                return path
            else:
                for id_next in actor_to_actor1_number(database,actor_id_1, n-1):
                    if acted_together(database, actor_id_2, id_next) == True :
  
                        path.insert(0,id_next)
                        return fact(id_next, n-1)   

        return fact(actor_id_2,level)


def get_movie_list(database, actor_id, goal_actor):
    path = actor_to_actor_path(database, actor_id, goal_actor)
    movie = []
    for i in range(len(path)-1):
        actor_tuple = (path[i],path[i+1])
        for item in database:
            if actor_tuple == (item[0],item[1]):
                movie.append(item[2])
            elif actor_tuple == (item[1],item[0]):
                movie.append(item[2])
    return movie       

def actor_path(database, actor_id, goal_test_function):
    path = []
    min_path = None
    # print(min_path)
    for actor_2 in database.keys():
        # print("1")
        if goal_test_function(actor_2) == True:
            ls = actor_to_actor_path(database, actor_id, actor_2)  
            path.append(ls)
            # print('2')    
        if len(path)>0:    
            min_path = min(path, key=len)
        else:
            min_path = None
    return min_path


if __name__ == '__main__':
    # options: tiny, small, large
    with open('resources/large.pickle', 'rb') as f:
        database = pickle.load(f)
    with open('resources/names.pickle', 'rb') as n:
        namedb = pickle.load(n)
    with open('resources/movies.pickle', 'rb') as m:
        moviedb = pickle.load(m)
  
    database = transform_data(database)


    # print(namedb['Daniel Olbrychski'])
    # name1 = [k for k,v in namedb.items() if v == 1367972]
    # name2 = [k for k,v in namedb.items() if v == 1338716]
    # name3 = [k for k,v in namedb.items() if v == 1345461]
    # name4 = [k for k,v in namedb.items() if v == 1345462]
    # idnum = namedb['Carmen Maura']
    # print(idnum)
    # print(name1,name2,name3,name4)
    # print(database)
    # print(transform_data(database))
    # print(acted_together(database, 4724, 9210))
    # actor1 = namedb['Kaj Nilsson']
    # actor2 = namedb['Mats Bergman']
    # print(acted_together(database, actor1, actor2))
    # print(actors_with_bacon_number(database, 1))

    # print(bacon_path(database, 46866))
#   print(actor_to_actor1_number(database, 4724, 1))
    # print(set())
    # print(actor_to_actor_path(database, 43011, 1204555))
    # print(actor_path(database, 4724, 46866))
    # print(actor_to_actor_path(database, 46866))
