
def  parsing(data:str):
    numbres = []
    for elm in data:
        numbres.append(elm[1])
    return numbres

def sensor_analysis(sensor_data):
    numbres = parsing(sensor_data)
    mean = sum(numbres)/len(numbres)
    s = 0
    for num in numbres:
        a = (num - mean)
        s += a ** 2
    s = s / (len(numbres) - 1) 
    v = s ** 0.5
    return ( round(mean,4), round(v,4) )



