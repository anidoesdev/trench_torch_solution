def analyze_route(points: list) -> tuple:
    """
    `points` is a list of (x, y) tuples of ints, in the order
    the route visits them. Return a 5-element tuple:

      (visit_counts, bounding_box, path_length,
       net_displacement, revisit_count)

    where:
      - visit_counts: a dictionary mapping each distinct
        (x, y) tuple to how many times it appears in `points`.
      - bounding_box: a tuple ((min_x, min_y), (max_x, max_y))
        covering all points. Compute it with a loop and
        comparisons (do not use min() or max()).
      - path_length: the sum of the Manhattan distances between
        each consecutive pair of points. Use an index loop.
      - net_displacement: the Manhattan distance between the
        first and last point. Obtain the first and last points
        with extended unpacking: first, *_, last = points
        (handle a single-point route separately).
      - revisit_count: len(points) minus the number of distinct
        points, i.e. how many visits were to a point already
        seen.

    An empty `points` returns ({}, None, 0, 0, 0).
    A single point returns:
      ({point: 1}, (point, point), 0, 0, 0)

    `points` and its tuples must not be modified.
    """
    if not points:
        return ({}, None, 0, 0, 0)

    # Edge Case 2: Single-point route
    if len(points) == 1:
        p = points[0]
        return ({p: 1}, (p, p), 0, 0, 0)
    visit_counts = {}
    bounding_box = ()
    min_x = 0
    min_y =  0
    max_y = 0
    max_x = 0
    for p in points:
        x,y = p
        if p in visit_counts:
            visit_counts[p] +=1
        else:
            visit_counts[p] = 1
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    bounding_box = ((min_x,min_y),(max_x,max_y))

    path_length = 0
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i+1]
        path_length += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    first, *_, last = points
    net_displacement = abs(first[0]-last[0]) + abs(first[1]-last[1])
    revisit_count = len(points) - len(visit_counts)
    return (visit_counts,bounding_box,path_length,net_displacement,revisit_count)
