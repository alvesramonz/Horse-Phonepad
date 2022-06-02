def get_reachable_numbers(position):
    reachable = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8], 
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    reachable_numbers = reachable.get(position)
    return reachable_numbers


def recursive_arrangement(initial_position, hops, arrangement=None):
    if arrangement is None:
        arrangement = [initial_position]

    if hops == 0:
        yield arrangement
        return

    for reachable_number in get_reachable_numbers(initial_position):
        yield from recursive_arrangement(
            reachable_number, hops - 1, arrangement + [reachable_number])


def count_reachable_numbers_dialed(initial_position, hops):
    distinct_numbers_arrangement = 0

    for numbers_arrangement in recursive_arrangement(initial_position, hops):
        distinct_numbers_arrangement += 1

    return distinct_numbers_arrangement


def menu_hud_options():
    print("\n")
    print("[1] Start HPG (Horse Phonepad Game) ")
    print("[0] Close HPG (Horse Phonepad Game) ")
    print("    Option: ")
    option = input()

    return str(option)


def phonepad_hud_positions():
    print("\n\nChoose your initial position (0-9).")
    print("")
    print("1  2  3")
    print("4  5  6")
    print("7  8  9")
    print("*  0  #")
    print("\nPosition: ")
    position = input()
    print("\nHow many hops: ")
    hops = input()

    return position, hops


def horse_phonepad_game_start():
    initial_position, hops = phonepad_hud_positions()

    if hops <= "0":
        horse_phonepad_game_answer(initial_position, hops, 1)
        return

    response = count_reachable_numbers_dialed(int(initial_position), int(hops))
    horse_phonepad_game_answer(initial_position, hops, response)


def horse_phonepad_game_answer(initial_position, hops, result):
    if int(initial_position) == 5:
        print("\nHow many distinct numbers can you dial in " + str(hops) + " hops from a particular starting position?")
        print("ANSWER: " + "0" + ". There's no possible hop starting at 5.")
        return
    
    print("\nHow many distinct numbers can you dial in " + str(hops) + " hops from a particular starting position?")
    print("ANSWER: " + str(result) + " possible hops starting at " + str(initial_position))
    return


def main():
    horse_phonepad_running = True
    
    while horse_phonepad_running:
        option = menu_hud_options()

        if option == "0":
            print("\n Bye bye o/")
            return
        elif option == "1":
            horse_phonepad_game_start()
        else:
            print("\nInvalid option!")


if __name__ == '__main__':
    main()