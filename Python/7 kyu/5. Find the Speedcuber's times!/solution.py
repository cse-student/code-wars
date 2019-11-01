def cube_times(times):
    fastest = min(times)
    times.remove(fastest)
    times.remove(max(times))
    avg = round(sum(times)/3,2)
    return (avg, fastest)