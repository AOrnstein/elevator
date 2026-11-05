import argparse

# Time the elevator takes when moving floors
TIME_PER_FLOOR = 10


def list_of_ints(int_list_str: str):
    """Split the int list string by commas and convert each element to an integer"""
    return [int(x) for x in int_list_str.split(",")]


def parse_args():
    """
    Parse the arguments for the starting floor and list of floors to visit

        CMD start floors

    e.g. Given start=12 floors=2,9,1,32

        CMD 12 2,9,1,32

    Returns:
        starting_floor (int): value of the initial floor
        floors_to_visit (list[int]): list for floor numbers to visit
    """

    parser = argparse.ArgumentParser(
        description="Determine how long it takes an elevator to move between floors"
    )

    parser.add_argument("start", type=int, help="Starting floor number")
    parser.add_argument(
        "floors",
        type=list_of_ints,
        help="A comma separated list of floors to visit (e.g. 1,2,3)",
    )

    args = parser.parse_args()

    return int(args.start), list[int](args.floors)


def time_to_next_floor(start: int, next: int):
    """Returns the time required to move from one floor to another"""
    return abs(next - start) * TIME_PER_FLOOR


def print_output(total_time: int, floors_visited: list[int]):
    """
    Formats and prints the output

        total_time floors_visited

    e.g. Given total_time=560 floors_visited=12,2,9,1,32

        560 12,2,9,1,32
    """
    print(total_time, ",".join(str(floor) for floor in floors_visited))


def calulate_elevator_movement(starting_floor: int, floors_to_visit: list[int]):
    """
    Calculate the time the elevator takes to visit each floor.
    Consecutivly repeated stops at a floor are consolidated into a single stop.

    Returns:
        total_time (int): time taken to move between floors
        floors_visited (list[int]): list of all floors visited, including the initial floor
    """
    floor = starting_floor
    total_time = int(0)
    floors_visited: list[int] = [starting_floor]

    for stop in floors_to_visit:
        # Elevator is already at the floor
        if floor == stop:
            continue

        # Elevator moves to a new floor
        total_time = total_time + time_to_next_floor(floor, stop)
        floors_visited.append(stop)
        floor = stop

    return total_time, floors_visited


def main():
    starting_floor, floors_to_visit = parse_args()
    total_time, floors_visited = calulate_elevator_movement(
        starting_floor, floors_to_visit
    )
    print_output(total_time, floors_visited)


if __name__ == "__main__":
    main()
