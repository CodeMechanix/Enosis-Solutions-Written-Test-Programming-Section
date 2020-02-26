

def sequence_of_series():
    i = 10
    j = 2
    for k in range(1,20):
        if k>=1 and k<=10:
            print(i)
            i = i-1
        else:
            print(j)
            j = j+1

sequence_of_series()