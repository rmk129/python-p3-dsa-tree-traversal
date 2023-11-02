class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    print(self.root['id'] == id)

    if self.root['id'] == id:
      return self.root
    else:
      for child in self.root['children']:
          new_tree = Tree(child)
          return new_tree.get_element_by_id(id)
          
