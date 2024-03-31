from datetime import datetime
import time


# Part 1
def clock(n):
  """
    Shows the time. Updates every second.
    
    Parameters:
    n
       number of seconds to update by
    
    Returns
    ---------
    Nothing
    
    Example:
    >>> clock(3)
    12:59:17
    
  """
    # Your code here
    
  i = 0
  while i < n:
    timeNow = datetime.now().time()
    timeArr = [str(timeNow.hour), str(timeNow.minute), str(timeNow.second)]
    for x in timeArr:
      
      if len(x) == 1:
        timeArr[timeArr.index(x)] = f"0{x}"
    
    print(f"{timeArr[0]}:{timeArr[1]}:{timeArr[2]}", end = "\r")
    time.sleep(1)
    i += 1


# Part 2
def lcm(a, b):
    # Your code here
  """
    Calculates the LCM of two integers
    Input:
    a, b where a and b are integers
    Returns:
    The lowest common multiple of A and B
  """
  
  original_a = a
  original_b = b
  while a != b:
    if a < b:
      # a is smaller
      a += original_a
    else:
      b += original_b
  return a
    


# Part 3
def gcf(a, b):
  """
    Calculates the HCF of two integers
    Input:
    a, b where a and b are integers
    Returns:
    The highest common factor of A and B
  """
  
    # Your code here
  
  while(b != 0):
    
    remainder = divmod(a, b)[1]
    a = b
    b = remainder
    if b == 0:
      return a
 
gcf(12, 60)
