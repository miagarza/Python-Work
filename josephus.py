'''

Description: create a circular linked list having the number of soldier specified. 
Your program will print out the order in which the soldiers get eliminated.

'''


import sys


#represents a link between data items
class Link(object):
  def __init__(self,data, next_link=None):
    self.data=data 
    self.next=next_link #changed



class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.last=None

  
  # Insert an element (value) in the list
  def insert ( self, data ):
    new_link=Link(data)
    if self.last is None:
      new_link.next=new_link
    else:
      new_link.next=self.last.next
      self.last.next=new_link
    self.last=new_link


  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    if self.last is None:
      return None
    current=self.last.next
    while True:
      if current.data==data:
        return current
      if current.data==self.last:
        return None #redundant with loop above
      current=current.next


  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
    if self.last is None:
      return None
    
    previous=self.last
    current=self.last.next

    while current.data != data:
      if current== self.last:
        return None
      previous=current
      current=current.next

    if current.next==current:
      self.last=None
    else:
      previous.next=current.next
      if current==self.last:
        self.last=previous
    return current



  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    current= start
    for i in range(n-1):
      current=current.next

    data=current.data
    next_link=current.next

    self.delete(data)
    return data, next_link

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    if not self.last:
      return "[]"
    vars=[]
    current=self.last.next
    while True:
      vars.append(str(current.data))
      if current == self.last:
        break
      current=current.next
    return "["+", ".join(vars)+"]"





def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  circle=CircularList()
  for i in range(1, num_soldiers+1):
    circle.insert(i)
  current=circle.find(start_count)
  for i in range(1, num_soldiers+1):
    data, current = circle.delete_after(current,elim_num)
    #paraell?
    print(data)


  
if __name__ == "__main__":
  main()
