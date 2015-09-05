class Node(object):
 
  # Initializes the node object
  def __init__(self, key):
    self.left_child = None
    self.right_child= None
    self.key = key
    self.parent = None

class Tree(Node):
  """
  Binary Tree class.
  In this implementation, every node key should be unique.
  """
  # Initializes the tree, creates the root
  def __init__(self):
    self.node = Node(8)


  # Auxiliar  recursive search method, return the node whose key is value
  def search(self, value, node):
    # If the key of the node is the same than the value, return the node
    if node.key == value:
      return node 
    # If the key of the node is different than the value, check the children
    else:
      if node.left_child and node.right_child:
         firstnode, secondnode = self.search(value, node.left_child), self.search(value, node.right_child)
         if firstnode != None:
            return firstnode
         else:
            return secondnode
      if node.left_child:
        return self.search(value, node.left_child)
      if node.right_child:
        return self.search(value, node.right_child)


   # Add a node to the tree. The node is the child of parentValue 
  def add(self, value, parentValue):
    # Search the parent
    parent = self.search(parentValue, self.node)
    if parent: 
      new_node = Node(value)
      
      # If the parent has not left child, new_node is the left child
      if parent.left_child is None:
        parent.left_child = new_node
        new_node.parent = parent
        #print "The father of: ", new_node.key, "is: ", new_node.parent.key
        
      # If the parent has not right child, new_node is the right child
      elif parent.right_child is None:
        parent.right_child = new_node
        new_node.parent = parent
        #print "The father of: ", new_node.key, "is: ", new_node.parent.key
      
      # If parent has two children, the node is not added 
      else:
        print "Parent has two children, node not added"
        
    # Print a message if the parent is not found in the tree
    else:
      print "Parent not found"


  # Delete a value of the tree if it has no children
  def delete(self, value):
    # Search the node to delete
    del_node = self.search(value, self.node)
    
    if del_node:
      # If the node at least one child, it is not deleted
      if del_node.left_child or del_node.right_child:
        print "Node not deleted, has children"
      # Delete the node
      else:
        if del_node == del_node.parent.left_child:
          del_node.parent.left_child = None
          del del_node
        else:
          del_node.parent.right_child = None
          del del_node  
    # Print a message if the node is not found      
    else:
      print "Node not found."
      
  # Print only the current node and the direct children
  def print_parent_children(self, current_node):
    if current_node.left_child and current_node.right_child:
      print "Father is ", current_node.key, "and children are ", current_node.left_child.key, current_node.right_child.key
    elif current_node.left_child:
      print "Father is ", current_node.key, "and left child is ", current_node.left_child.key
    elif current_node.right_child:
      print "Father is ", current_node.key, "and right child is ", current_node.right_child.key
    else:
      print "Father is ", current_node.key
      
  # Recursive method, print the subtree of the current node. Printe left children first
  def print_subtree(self, current_node):
      print current_node.key
      if current_node.left_child:
        self.print_subtree(current_node.left_child)
      if current_node.right_child:
        self.print_subtree(current_node.right_child)
        
    







