def get_size(w,h,d):
    sa = 2*(w*h) + 2*(w*d) + 2*(h*d)
    v = w*h*d
    return [sa,v]