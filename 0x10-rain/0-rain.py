#!/usr/bin/python3
'''
Module - Rain
'''


def rain(walls):
    '''
    Function to calculate how much water can be on pool
    @walls: Pool Walls
    Return: Amount of water retained
    '''
    bucket = []
    pool = len(walls)
    water = 0

    for i in range(pool):
        while(len(bucket) != 0 and (walls[bucket[-1]] < walls[i])):
            popWall = walls[bucket[-1]]
            bucket.pop()
            if(len(bucket) == 0):
                break
            distance = i - bucket[-1] - 1
            minWall = min(walls[bucket[-1]], walls[i]) - popWall
            water += distance * minWall
        bucket.append(i)
    return water
