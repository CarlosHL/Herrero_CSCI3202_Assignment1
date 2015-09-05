
class Graph(object):
  """
  Graph class.
  In this implementation, a vertex can have edges with himself.
  """
  # Initializes the graph
  def __init__(self):
    self.graph = { }

  # Add a vertex to the graph
  def addVertex(self, value):
    notExist = True 
    # Search the vertex in the graph
    for node in self.graph:
      if node == value:
        print "Vertex already exist"
    # Add the vertex to the graph if it does not exist in the graph    
    if notExist:
      self.graph[value] = []
  
  # Add an edge between two vertices
  def addEdge(self, value1, value2):
    exist_value1 = None
    exist_value2 = None
    # Search the vertex in the graph
    for node in self.graph:
      if node == value1:
        exist_value1 = True
      if node == value2:
        exist_value2 = True
    # Print a message if at least one vertex does not exist    
    if not exist_value1 or not exist_value2:
      print "One or more vertices not found"
    # Create an edge between two vertices   
    else:
      self.graph[value1].append(value2)
      self.graph[value2].append(value1)
    
  # Find a vertex in the graph, print his edges
  def findVertex(self, value):
    exist_value1 = None
    for node in self.graph:
      if node == value:
        print "Adjacent values of ", node, "are: ", self.graph[value]
        exist_value1 = True
    # Print a message if the vertex does not exists    
    if  not exist_value1:  
      print "Vertex not found"