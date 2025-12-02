def count_zero_positions(filename, part):
    position = 50 
    zero_hits = 0 

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                step = -1
            elif direction == "R":
                step = 1
            else:
                raise ValueError(f"Invalid rotation: {line}")

            if part == 1:
                position = (position + step * distance) % 100
                if position == 0:
                    zero_hits += 1
            elif part == 2:
                for _ in range(distance):
                    position = (position + step) % 100
                    if position == 0:
                        zero_hits += 1

    return zero_hits

print(count_zero_positions("./day1.txt",1))

print(count_zero_positions("./day1.txt",2))