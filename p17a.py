import copy, sys, re

def convert(lines):
    data = []
    x_max = y_max = 0
    x_min = y_min = 10000
    for line in lines : 
        match = re.search("^(.)=(.*), (.)=(.*)$", line.strip()) 
        if match :
            (x_ind,y_ind) = (2,4) if match.group(1)=='x' else (4,2)
            (x_str,y_str) = (match.group(x_ind),match.group(y_ind))
            # print((x_str,y_str))
            x_vals = [int(x) for x in x_str.split("..")]
            y_vals = [int(y) for y in y_str.split("..")]
            x_min = min(x_min,x_vals[0])
            y_min = min(y_min,y_vals[0])
            x_max = max(x_max,x_vals[-1]+1)
            y_max = max(y_max,y_vals[-1]+1)
            # print(x_vals,y_vals)
            x_range = range(x_vals[0],x_vals[-1]+1)
            y_range = range(y_vals[0],y_vals[-1]+1)

        else :
            raise AttributeError
    print("x",x_min,x_max)
    print("y",y_min,y_max)
    return data


def main(lines):
    pass


print ('Argument List:', str(sys.argv))
data_file = open(sys.argv[1],"r+")  
lines = data_file.readlines()
data = convert(lines)




main(data)