def overall(n):
    '''Given a list of numbers and a number k, return whether any two numbers from the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

    #Importing Library
    import time
    import random
    import matplotlib.pyplot as plt

    def sumk(l,k):
        '''A function that returns true when any two numbers add up to another number k with with O(n^2)'''
        for x in l:
            for y in l:
                if x+y == k:
                    return True
        return False

    def sumk_fast(l,k):
        '''A function that returns true when any two numbers add up to another number k with with O(n)'''
        for i in l:
            if (k-i) in l:
                return True
        return False

    def timetake(fun,loops):
        '''A function to time sumk and sumk_fast and plot the time taken in a graph '''
        timecapture = list()
        for n in range(loops):
            l = random.sample(list(range(n*10)),n)
            start = time.time()
            ans = fun(l,17)
            end = time.time()
            timecapture.append(end-start)
        return timecapture

    #Visualizing overall
    f, (p1, p2) = plt.subplots(1, 2, figsize=(15,5),sharey=True)
    p1.plot(range(n),timetake(sumk,n))
    p1.set_title("Time taken by SUMK function which is O(n^2)")
    p1.set_xlabel("# of elements in list")
    p1.set_ylabel("Time Taken in seconds")
    p2.plot(range(n),timetake(sumk_fast,n),color='green')
    p2.set_xlabel("# of elements in list")
    p2.set_title("Time taken by SUMK_fast function which is O(n)")
    p2.set_ylabel("Time Taken in seconds")
