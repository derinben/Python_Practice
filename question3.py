def find_index(gaslist , costlist):
  if (sum(gaslist) - sum(costlist) < 0):   #since it is a circular path and guaranteed to have one solution
            return -1
        
        start_index = 0    
        gas_tank = 0       # gas available in car 
              
        for i in range(len(gaslist)):
            gas_tank = gas_tank + gaslist[i] - costlist[i]
            
            if gas_tank < 0:   # change the starting point if the car doesn't have enough gas to move ahead
                start_index = i+1
                gas_tank = 0   # Re-initialize the gas tank to 0 as we begin from a new starting point.
            
        return start_index
