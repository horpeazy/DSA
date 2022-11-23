import sys

def calc_dist(start, end):
    """ calculate shortest distance between two points """
    dist = ((end[1] - start[1])**2 + (end[0] - start[0])**2)**0.5
    return dist

def shortest_path(M,start,goal):
    print("shortest path called")
    dist_map = {start: 0}
    goal_pos = M.intersections[goal]
    prev_map = {}
    path = [goal]
    current = start
    
    if start >= len(M.intersections) or end >= len(M.intersections):
        return
    
    while current != goal:
        curr_dist = dist_map[current]
        curr_pos = M.intersections[current]

        for intersection in M.roads[current]:             #add intersections and corresponding dist ti dist_map
            pos = M.intersections[intersection]           # coordinates
            dist = calc_dist(pos, curr_pos)
            dist_map[intersection] = dist + curr_dist
        dist_map.pop(current)                             # remove visted intersection from dist_map
        prev = current

        # get intersection with shortest path using (f + g)
        current = min(dist_map.keys(), key=lambda x: dist_map[x] + calc_dist(M.intersections[x], goal_pos))
        prev_map[current] = prev                          # store prev intersection to aid tracing path

    # retrieve the path
    while current != start:
        path = [prev_map[current]] + path
        current = prev_map[current]

    return path
