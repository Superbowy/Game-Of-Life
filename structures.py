def glider_gun(i, j):
    liste = [(i, j), (i, j+1), (i+1, j), (i+1, j+1), (i+10, j),
             (i+10, j+1), (i+10, j+2), (i+11, j -
                                        1), (i+12, j-2), (i+13, j-2), (i+11, j+3),
             (i+12, j+4), (i+13, j+4), (i+14, j +
                                        1), (i+15, j+3), (i+16, j+2), (i+16, j+1),
             (i+17, j+1), (i+16, j+0), (i+15, j -
                                        1), (i+20, j), (i+21, j), (i+21, j-1),
             (i+20, j-1), (i+20, j-2), (i+21, j -
                                        2), (i+22, j+1), (i+22, j-3), (i+24, j-3),
             (i+24, j-4), (i+24, j+1), (i+24, j +
                                        2), (i+35, j-2), (i+34, j-2), (i+34, j-1),
             (i+35, j-1)]
    return liste
