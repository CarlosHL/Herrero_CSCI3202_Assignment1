import stack, queue, binaryTree, graph


"""
Carlos Herrero 09 / 04 / 2015
Assignment 1 - Introduction to Artificial Intelligence, CU Boulder
Test class.
All the required tests for the assignment are in this class.
Additional  test for all the methods are in comments
"""


# Testing the queue
print '_' * 10, "Testing the queue", '_' * 10

#Create the queue
q = queue.QueueIA()

# Add values to the queue
print "Adding in range (1, 11)"
for i in range(1, 11):
  q.add(i)

# Pop values  
print "Dequeue"
for i in range(0, 10):
  q.pop()

# Add invalid values to the queue  
#q.add("Hello World!")
#q.add(3.4)

# Pop when is empty
#q.pop()




# Testing the stack
print '_' * 10, "Testing the stack", '_' * 10

# Create the stack
new_stack = stack.Stack()

print "Adding in range (1, 11)"

# Pushing values
for i in range(1, 11):
  new_stack.push(i)

# Check the size
# print "Size is: ", new_stack.checksize()

print "Popping all the stack's values"

# Popping the values
while not new_stack.isEmpty():
  n = new_stack.pop()
  print n

# Pop when it is empty
# new_stack.pop()

# Add a non valid object
# new_stack.push("NOT VALID!")



# Testing the binary Tree
print '_' * 10, "Testing the binary tree", '_' * 10

print "Adding values to the tree"

tree = binaryTree.Tree()

tree.add(3, 8)
tree.add(4, 8)
tree.add(5, 3)
tree.add(7, 4)
tree.add(9, 3)
tree.add(1, 4)
tree.add(2, 5)
tree.add(6, 5)
tree.add(10, 2)

# Add a node to a parent with two children
#tree.add(13, 3)

# Add a node to an inexistent parent
#tree.add(13, 14)


# Print only direct children of root
#tree.print_parent_children(tree.node)

# Print children of node 4
#current_node = tree.search(4, tree.node)
#tree.print_parent_children(current_node)

print  "Printing the tree with ten integers"
tree.print_subtree(tree.node)
tree.delete(10)
tree.delete(2)
tree.delete(1)

# Delete a node with two children
#tree.delete(8)

# Delete an inexistent node
#tree.delete(50)



# Test the graph
print "Printing the tree after deleting 10, 2 and 1 "
tree.print_subtree(tree.node)

print '_' * 10, "Testing the graph", '_' * 10
graph = graph.Graph()

# Add vertices
for i in range (1, 21):
  graph.addVertex(i)
  
# Add an existing vertex
#graph.addVertex(2)
  
for i in range (1, 11):
  graph.addEdge(i, i+1)

# Create an edge between not existing vertex
#graph.addEdge(345, 1000)

for i in range (10, 19):
  graph.addEdge(i, 20-i)
  
for i in range (1, 6):
  graph.findVertex(i)
