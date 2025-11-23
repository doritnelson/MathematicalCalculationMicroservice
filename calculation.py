def sum_nums(int_array):
    result = 0
    for num in int_array:
        result += num
    return result

def average(int_array):
    result = 0
    for num in int_array:
        result += num
    result = result / len(int_array)
    return result

def calculate(request):
    int_array = request["int_array"]
    if request["action"] == "total":
        return sum_nums(int_array)
    elif request["action"] == "average":
        return average(int_array)
    elif request["action"] == "difference":
        return abs(int_array[1] - int_array[0])
    return False
