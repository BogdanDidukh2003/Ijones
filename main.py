class Coordinate:
    i: int
    j: int

    def __init__(self, i, j):
        self.i = i
        self.j = j


def main(path_to_plates: str):
    plates = open(path_to_plates, 'r').read().split('\n')[0:]
    combinations_number = start_counting(plates)
    with open("ijones.out", "w") as ijones_out:
        ijones_out.write(str(combinations_number))
        ijones_out.close()


def start_counting(plates: list):
    plates_width = len(plates[0])
    plates_height = len(plates)
    if len(plates) == 1:
        return count_combinations_at_coordinates([Coordinate(0, plates_width - 1)], plates)
    if len(plates) > 1:
        return count_combinations_at_coordinates(
            [Coordinate(0, plates_width - 1), Coordinate(plates_height - 1, plates_width - 1)], plates)


def count_combinations_at_coordinates(goal_coordinates: list[Coordinate], plates: list):
    combinations_number = len(goal_coordinates)
    for i in goal_coordinates:
        parents_coordinates = find_coordinates_with_similar_letter(i, plates)
        if len(parents_coordinates) > 0:
            combinations_number += count_combinations_at_coordinates(parents_coordinates, plates) - 1
    return combinations_number


def find_coordinates_with_similar_letter(input_coordinates: Coordinate, plates: list):
    symbol_value = plates[input_coordinates.i][input_coordinates.j]
    coordinates_with_similar_letter: list[Coordinate] = []
    for i in range(len(plates)):
        for j in range(input_coordinates.j):
            if plates[i][j] == symbol_value:
                coordinates_with_similar_letter.append(Coordinate(i, j))
    if input_coordinates.j != 0 and plates[input_coordinates.i][input_coordinates.j - 1] != symbol_value:
        coordinates_with_similar_letter.append(Coordinate(input_coordinates.i, input_coordinates.j - 1))
    return coordinates_with_similar_letter


if __name__ == '__main__':
    main("ijones.in")
