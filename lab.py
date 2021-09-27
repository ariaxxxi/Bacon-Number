#!/usr/bin/env python3

import pickle
# NO ADDITIONAL IMPORTS ALLOWED!

# Note that part of your checkoff grade for this lab will be based on the
# style/clarity of your code.  As you are working through the lab, be on the
# lookout for things that would be made clearer by comments/docstrings, and for
# opportunities to rearrange aspects of your code to avoid repetition (for
# example, by introducing helper functions).  See the following page for more
# information: https://py.mit.edu/fall21/notes/style

# enter tiny,small,large database, return pair of actor
def transform_data(raw_data):
    actor1 = []
    actor2 = []
    movie = []
    for item in raw_data:
        actor1.append(item[0])
        actor2.append(item[1])
        # movie.append(itesm[2])
    actor_tuple = [(actor1[i], actor2[i]) for i in range(0, len(actor1))]
    return actor_tuple


def acted_together(database, actor_id_1, actor_id_2):
    actor_tuple = transform_data(database)
    if actor_id_1 == actor_id_2:
        return True
    if (actor_id_1, actor_id_2) in actor_tuple:
        return True
    elif (actor_id_2, actor_id_1) in actor_tuple:
        return True
    return False


def exist(database, actor_id):
    actor1 = []
    actor2 = []
    movie = []
    for item in database:
        actor1.append(item[0])
        actor2.append(item[1])

    if actor_id in actor1:
        return True
    elif actor_id in actor2:
        return True
    else:
        return False

def actors_with_bacon_number(database, n):
    ls = {4724}
    all_actor = [4724]
    actor_tuple = transform_data(database)


    def factorial(n, ls):
        for i in range(1,n+1):
            # print("hi")
            nls  = set()                   
            for item in actor_tuple:              
                if item[0] in ls:
                    if item[1] not in all_actor:
                        nls.add(item[1])
                        all_actor.append(item[1])
                elif item[1] in ls:
                    if item[0] not in all_actor:
                        nls.add(item[0])
                        all_actor.append(item[0])       
            ls = nls       
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
        # print(level)
        def fact(actor_id,n):
            if n == 0:
                return path
            else:
                for id_next in actors_with_bacon_number(database, n-1):
                    # print("original:",actor_id)
                    # print("previous id:",id_next)
                    if acted_together(database, actor_id, id_next) == True :
                        # print("hi")
                        # print("id_new_original:",id_next)

                        path.insert(0,id_next)
                        # print("id_new_original:",id_next)
                        return fact(id_next, n-1)   
        return fact(actor_id,level)


def actor_to_actor1_number(database, actor_id_1, n):
    ls = {actor_id_1}
    all_actor = [actor_id_1]
    actor_tuple = transform_data(database)

    def factorial(n, ls):
        for i in range(1,n+1):
            # print("hi")
            nls  = set()                   
            for item in actor_tuple:              
                if item[0] in ls:
                    if item[1] not in all_actor:
                        nls.add(item[1])
                        all_actor.append(item[1])
                elif item[1] in ls:
                    if item[0] not in all_actor:
                        nls.add(item[0])
                        all_actor.append(item[0])       
            ls = nls       
        return ls
   
    return factorial(n, ls)
   


def actor_to_actor_path(database, actor_id_1, actor_id_2):
    path = [actor_id_1]
    def factorial(n):
        if actor_id_2 in actor_to_actor1_number(database,actor_id_1, n):
            return n
        else:
            return factorial(n+1)
    
    level = factorial(0)
    print(level)

    if exist(database, actor_id_2) == False:
        return None
    else:
        def fact(actor_id_2,n):
            if n == 0:
                return path
            else:
                for id_next in actor_to_actor1_number(database,actor_id_1, n-1):
                    # print("original:",actor_id_1)
                    # print("previous id:",id_next)
                    if acted_together(database, actor_id_2, id_next) == True :
                        # print("hi")
                        # print("id_new_original:",id_next)

                        path.insert(0,id_next)
                        # print("id_new_original:",id_next)
                        return fact(id_next, n-1)   

        return fact(actor_id_2,level)




def actor_path(database, actor_id_1, goal_test_function):
    raise NotImplementedError("Implement me!")


def actors_connecting_films(database, film1, film2):
    raise NotImplementedError("Implement me!")


if __name__ == '__main__':
    # options: tiny, small, large
    with open('resources/small.pickle', 'rb') as f:
        database = pickle.load(f)
    with open('resources/names.pickle', 'rb') as n:
        namedb = pickle.load(n)
    with open('resources/movies.pickle', 'rb') as m:
        moviedb = pickle.load(m)
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
    # print(acted_together(database, 2876, 1640))
    # actor1 = namedb['Kaj Nilsson']
    # actor2 = namedb['Mats Bergman']
    # print(acted_together(database, actor1, actor2))
    # print(actors_with_bacon_number(database, 1))
    # print(actors_with_bacon_number(database, 1))
    # print(actors_with_bacon_number(database, 2))
    # print(actor_to_actor1_number(database, 4724, 2))

    # print(exist(database, 4724))
    print(bacon_path(database, 46866))
    print(actor_to_actor_path(database, 4724, 46866))
    # print(actor_to_actor_path(database, 46866))
