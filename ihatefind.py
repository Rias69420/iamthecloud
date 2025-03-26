def why(y):
    max_es_gribu_sevi_izmest_pa_logu = y[0]
    for elements in y:
        if elements > max_es_gribu_sevi_izmest_pa_logu:
                max_es_gribu_sevi_izmest_pa_logu = elements
    return max_es_gribu_sevi_izmest_pa_logu
c =[1, 9, 12, 104, 329, 43]    
y = why(c)

print(f"C++ vieglak kodet:{c}")
