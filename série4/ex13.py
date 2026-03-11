for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            n = i*100 + j*10 + k*1
            m = i*i*i+j*j*j+k*k*k
            if n == m:
                print(n)