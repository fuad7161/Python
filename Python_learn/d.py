def generate(len):
    tem = []
    tem1 = []
    for i in range(1,len+1):
        tem.append(i)
        tem1.append(i*(-1)**i)
    return (tem , tem1)