import numpy as np
from util import item_item_collab_filtering

def main():
    example = np.array([[1.0,-1,3,-1,-1,5,-1,-1,5,-1,4,-1],[-1,-1,5,4,-1,-1,4,-1,-1,2,1,3],[2,4,-1,1,2,-1,3,-1,4,3,5,-1],[-1,2,4,-1,5,-1,-1,4,-1,-1,2,-1],[-1,-1,4,3,4,2,-1,-1,-1,-1,2,5],[1,-1,3,-1,3,-1,-1,2,-1,-1,4,-1]])
    print example
    print item_item_collab_filtering(example, 2, -1)
    


if __name__ == '__main__':
    main()