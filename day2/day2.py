
def is_invalid_id(num):
    num_str = str(num)
    length = len(num_str)
    
    if length % 2 == 0:
        half = length // 2
        if num_str[:half] == num_str[half:]:
            return True
    return False


def is_invalid_id_part2(num):
    num_str = str(num)
    length = len(num_str)
    
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            repeat_unit = num_str[:i]
            if repeat_unit * (length // i) == num_str:
                return True
    return False

def sum_invalid_ids(ranges, part):
    invalid_ids_sum = 0
    
    for r in ranges:
        start, end = map(int, r.split('-')) 
        for id in range(start, end + 1):
            if part ==1 and is_invalid_id(id):
                invalid_ids_sum += id
            if part ==2 and is_invalid_id_part2(id):
                invalid_ids_sum += id
    
    return invalid_ids_sum


ranges  = open('Day2/day2_small.txt').read().strip().split(',')
print(f"Part1: {sum_invalid_ids(ranges,1)}")
print(f"Part2: {sum_invalid_ids(ranges,2)}")