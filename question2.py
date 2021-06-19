def myarea(height):

    left = 0  #pointer to traverse the array from left 
    right =  len(height) - 1 #pointer to traverse the array from right
    area = 0
    while left != right:
        new_area = (right-left) * min(height[left] , height[right])
        area = max(area , new_area)
        #print("We are at {} and {} and the area is {} ".format(height[left] , height[right], new_area))

        if height[left] < height[right]:
                left =  left+ 1
        else:
                right = right - 1
                
    print(area)
