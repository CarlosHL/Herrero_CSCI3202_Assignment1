import 	Queue

class QueueIA(object):
  
  #Initializes the queue
  def __init__(self):
    self.queue = Queue.Queue()
  
  #Add a value to the queue
  def add(self, value):
    #if the value is an integer, add it
    if isinstance( value, int ): # True
       self.queue.put(value)
    else:
      print "Not added, not an integer!"
      
      
  #Pop a value of the queue
  def pop(self):
    #only pops if the queue is not empty
    if self.queue.empty():
      print "Queue is empty"
    else:
      self.queue.get()

    

 