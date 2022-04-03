def pillars(num_pill, dist, width):
    if (num_pill < 2):
        return 0
    
    separation_distance = (num_pill-1) * (dist * 100)
    pillar_width = (num_pill -2) * width
    return separation_distance + pillar_width