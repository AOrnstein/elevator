
import argparse

def list_of_ints(int_list_str:str):
    ''' Split the int list string by commas and convert each element to an integer '''
    return [int(x) for x in int_list_str.split(',')]

def parse_args():
    ''' 
    Parse the arguments for the starting floor and list of floors to visit  
        
        CMD start floors

    e.g. Given start=12 floors=2,9,1,32

        CMD 12 2,9,1,32
        
    Returns:
        starting_floor, floors_to_visit 
    '''

    parser = argparse.ArgumentParser(description="Determine how long it takes an elevator to move between floors")

    parser.add_argument('start', type=int, help="Starting floor number")
    parser.add_argument('floors', type=list_of_ints, help="A comma separated list of floors to visit (e.g. 1,2,3)")

    args = parser.parse_args()

    return int(args.start), list[int](args.floors)

def main():
    starting_floor, floors_to_visit  = parse_args()

if __name__ == "__main__":
    main()