import numpy as np 

def menu_hud_options():
    print("\n")
    print("[1] Start HPG (Horse Phonepad Game) ")
    print("[0] Close HPG (Horse Phonepad Game) ")
    print("    Option: ")
    option = input()

    return option


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

    reachable = {
        "0": [[8, 5, 4], [8, 5, 6]],
        "1": [[2, 3, 6], [2, 5, 8], [4, 5, 6], [4, 7, 8]],
        "2": [[5, 8, 7], [5, 8, 9], [3, 6, 9], [1, 4, 7]],
        "3": [[2, 1, 4], [2, 5, 8], [6, 5, 4], [6, 9, 8]], 
        "4": [[1, 2, 3], [5, 6, 3], [7, 8, 9], [5, 6, 9], [5, 8, 0]],
        "5": [],
        "6": [[3, 2, 1], [9, 8, 7], [5, 4, 1], [5, 4, 7], [5, 8, 0]],
        "7": [[4, 1, 2], [8, 5, 2], [4, 5, 6], [8, 9, 6]],
        "8": [[9, 6, 3], [7, 4, 1], [5, 2, 3], [5, 2, 1]],
        "9": [[8, 7, 4], [6, 5, 4], [8, 5, 2], [6, 3, 2]]
    }

    possible_hops = reachable.get(initial_position, "Invalid inicial position.")

    if type(possible_hops) == str:
        print("\n" + possible_hops)
        return

    calculate_horse_phonepad_game(initial_position, possible_hops, hops)


def calculate_maximum_distinct_numbers(possible_hops):
    distinct_numbers = []
    distinct_numbers_count = 0
    for possible_hop in possible_hops:
        for number in possible_hop:
            if number not in distinct_numbers:
                distinct_numbers.append(number)
                distinct_numbers_count += 1
    
    return distinct_numbers_count


def calculate_at_least_distinct_numbers(initial_position, possible_hops, hops):
    distinct_numbers_count_at_least = 0
    distinct_numbers_count_maximum = 0

    if hops == "1":
        distinct_numbers_count_at_least = 4
        distinct_numbers_count_maximum = 4

    elif hops == "2":
        # if initial_position in [2, 8, 4, 6]:
        #     distinct_numbers_count_at_least = 5
        #     distinct_numbers_count_maximum = distinct_numbers_count_at_least + 2
        # else:
        #     distinct_numbers_count_at_least = 6
        #     distinct_numbers_count_maximum = distinct_numbers_count_at_least + 1

        # for possible_hop_index in range(len(possible_hops) - 1):
        #     com_arrays.append(np.array(np.meshgrid(possible_hops[possible_hop_index], possible_hops[possible_hop_index + 1])).T.reshape(-1, 4))

        algo = np.array(np.meshgrid(possible_hops[0], possible_hops[1], possible_hops[2], possible_hops[3])).T.reshape(-1, 4)

        print(algo)

    # elif hops == "3":
    #     if initial_position in [2, 8, 4, 6,]:
    #         distinct_numbers_count_at_least = 7
    #         distinct_numbers_count_maximum = 9
    #     else:
    #         distinct_numbers_count_at_least = 8
    #         distinct_numbers_count_maximum = 8

    # elif hops == "4":
    #     # distinct_numbers_count_at_least = 9
    #     # distinct_numbers_count_maximum = 10
        
    #     for possible_hop in range(len(possible_hops)):
    #         for possible_hop in possible_hops:
    #             com_arrays = np.array(np.meshgrid(possible_hops[0], possible_hops[1], possible_hops[2], possible_hops[3], possible_hops[4])).T.reshape(-1, 4)


    return distinct_numbers_count_at_least, distinct_numbers_count_maximum


def calculate_horse_phonepad_game(initial_position, possible_hops, hops):
    if not possible_hops:
        print("\nHow many distinct numbers can you dial in " + str(hops) + " hops from a particular starting position?")
        print("Answer: " + "0" + ". There's no possible hop starting at 5.")
        return
    
    possible_hops_by_position = len(possible_hops)

    if int(hops) >= possible_hops_by_position:
        distinct_numbers = calculate_maximum_distinct_numbers(possible_hops)
        
        print("\nHow many distinct numbers can you dial in " + str(hops) + " hops from a particular starting position?")
        print("Answer: " + str(distinct_numbers))
        print("Possible hops at " + str(initial_position))
        for possible_hop in possible_hops:
            print(possible_hop)
    else:
        at_least_distinct_numbers, maximum_distinct_numbers = calculate_at_least_distinct_numbers(initial_position, possible_hops, hops)

        print("\nHow many distinct numbers can you dial in " + str(hops) + " hops from a particular starting position?")
        print("At least: " + str(at_least_distinct_numbers))
        print("Maximum: " + str(maximum_distinct_numbers))
        print("Possible hops at " + str(initial_position))
        for possible_hop in possible_hops:
            print(possible_hop)


def main():
    horse_phonepad_running = True
    
    while horse_phonepad_running:
        option = menu_hud_options()
        
        switch = {
            1: horse_phonepad_game_start(),
            0: "exit"
        }
        
        case_response = switch.get(option, "\nInvalid option!")

        if case_response == "exit":
            print("\n Bye bye o/")
            return


if __name__ == '__main__':
    main()