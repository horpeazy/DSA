import sys

def calc_dist(start, end):
    """ calculate shortest distance between two points """
    dist = ((end[1] - start[1])**2 + (end[0] - start[0])**2)**0.5
    return dist

def shortest_path(M,start,goal):
    """"
    Calculate the shortest path between two points on a map
    
    Args:
    M(map object) - map
    start(int) - start position
    goal(int) - end position
    
    """
    frontiers = {start: 0}
    goal_pos = M.intersections[goal]
    prev_map = {}
    path = [goal]
    current = start
    visited = set()
    
    if start >= len(M.intersections) or goal >= len(M.intersections):
        return
    
    while current != goal:
        curr_dist = frontiers[current]
        curr_pos = M.intersections[current]

        for intersection in M.roads[current]:             #add intersections and corresponding dist ti dist_map
            if intersection in visited:
                continue
            if intersection in frontiers:
                pos = M.intersections[intersection]           # coordinates
                dist = calc_dist(pos, curr_pos) + curr_dist
                if dist < frontiers[intersection]:
                    frontiers[intersection] = dist
                    prev_map[intersection] = current
                    continue
            else:
                pos = M.intersections[intersection]           # coordinates
                dist = calc_dist(pos, curr_pos) + curr_dist
                frontiers[intersection] = dist
                prev_map[intersection] = current              # store prev intersection to aid tracing path
        frontiers.pop(current)                             # remove visted intersection from dist_map
        visited.add(current)

        # get intersection with shortest path using (f + g)
        current = min(frontiers.keys(), key=lambda x: frontiers[x] + calc_dist(M.intersections[x], goal_pos))

    # retrieve the path
    while current != start:
        path = [prev_map[current]] + path
        current = prev_map[current]

    return path