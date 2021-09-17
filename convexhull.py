import data_structures as dt
import math

#implementacao por gift wrapping
def gift_wrap(points):
    hull_points = []

    min_point = dt.Point(math.inf, math.inf)
    min_point_index = 0
    for i in range(len(points)):
        p = points[i]
        if p.y < min_point.y:
            min_point = p
            min_point_index = i
        if p.y == min_point.y:
            if p.x > min_point.x:
                min_point = p
                min_point_index = i
    hull_points.append(min_point)
    
    first_segment_point = dt.Point(math.inf, math.inf)
    min_angle = math.inf
    x_axis = dt.Vec(1, 0)
    for p in points:
        if p != min_point:
            test_vector = p - min_point
            test_angle = test_vector.pseudoangle(x_axis)
            if test_angle < min_angle:
                first_segment_point = p
                min_angle = test_angle

    hull_points.append(first_segment_point)

    last_point = dt.Point(math.inf, math.inf)
    while(last_point != min_point):
        #Pegamos os dois últimos pontos adicionados ao fecho para formar o vetor de teste
        first_point = hull_points[len(hull_points)-2]
        second_point = hull_points[len(hull_points)-1]
        current_vector = second_point - first_point
        
        max_pseudo_angle = math.inf

        for p in points:
            if dt.orient(first_point, second_point, p) >= 0 :
                test_vector = p - second_point
                test_angle = current_vector.pseudoangle(test_vector)
                if max_pseudo_angle > test_angle:
                    max_pseudo_angle = test_angle
                    last_point = p

        print(f'{last_point}')
        hull_points.append(last_point)

    return hull_points