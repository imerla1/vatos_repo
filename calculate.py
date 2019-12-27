def calculate(n):
    'Tu n udris 1-s daabrunebs 1-s sxva shemtxveashi output lists emateba yvela mteli gamyofi magrad daabrunebs lists meore wevrs'
    i = 1
    ai = [] # Output list
    while i <= n : 
        if (n % i==0) : 
            ai.append(i)
        i = i + 1

    if n == 1:
        return 1
    else:
        return ai[1]