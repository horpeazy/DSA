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
    visited = set()
    
    if start >= len(M.intersections) or goal >= len(M.intersections):
        return
    
    while current != goal:
        curr_dist = dist_map[current]
        curr_pos = M.intersections[current]

        for intersection in M.roads[current]:             #add intersections and corresponding dist ti dist_map
            if intersection in visited:
                continue
            if intersection in dist_map:
                pos = M.intersections[intersection]           # coordinates
                dist = calc_dist(pos, curr_pos) + curr_dist
                if dist < dist_map[intersection]:
                    dist_map[intersection] = dist
                    prev_map[intersection] = current
                    continue
            else:
                pos = M.intersections[intersection]           # coordinates
                dist = calc_dist(pos, curr_pos) + curr_dist
                dist_map[intersection] = dist
                prev_map[intersection] = current              # store prev intersection to aid tracing path
        dist_map.pop(current)                             # remove visted intersection from dist_map
        visited.add(current)

        # get intersection with shortest path using (f + g)
        current = min(dist_map.keys(), key=lambda x: dist_map[x] + calc_dist(M.intersections[x], goal_pos))

    # retrieve the path
    while current != start:
        path = [prev_map[current]] + path
        current = prev_map[current]

    return path
