from typing import Optional


class Node:

  def __init__(self, data: int):
    self.data: int = data
    self.left: Optional[Node] = None
    self.right: Optional[Node] = None


#optional used for; we can assign self.left or self.right to either node and none


def merge_bst(root1, root2):
  #if roots one of them is empty
  if root1 is None:
    return root2
  if root2 is None:
    return root1

  # Perform an in-order traversal on root1
  stack = []
  current = root1
  while current is not None or stack:
    while current is not None:
      stack.append(current)
      current = current.left

    current = stack.pop()

    # Insert the current element into root2
    root2 = insert_node(root2, current.data)

    current = current.right

  return root2


def insert_node(root, data):
  if root is None:
    return Node(data)

  if data < root.data:
    root.left = insert_node(root.left, data)
  else:
    root.right = insert_node(root.right, data)

  return root


# for perform in-order traversal on BST
def inorder_traversal(root, result):
  if root is None:
    return

  inorder_traversal(root.left, result)
  result.append(root.data)
  inorder_traversal(root.right, result)


# for find the kth smallest element in BST
def find_kth_smallest(root, k):
  stack = []
  current = root
  count = 0

  while current is not None or stack:
    while current is not None:
      stack.append(current)
      current = current.left

    current = stack.pop()
    count += 1

    if count == k:
      return current.data

    current = current.right

  return None


# for construct a balanced BST from a sorted array
def construct_balanced_bst(arr, start, end):
  if start > end:
    return None

  mid = (start + end) // 2
  root = Node(arr[mid])

  root.left = construct_balanced_bst(arr, start, mid - 1)
  root.right = construct_balanced_bst(arr, mid + 1, end)

  return root


# for balance a BST
def balance_bst(root):
  arr = []
  inorder_traversal(root, arr)
  balanced_root = construct_balanced_bst(arr, 0, len(arr) - 1)
  return balanced_root


# for find elements within a specified value range in BST
def find_elements_in_range(root, low, high):
  result = []
  in_order_traversal_with_range_check(root, low, high, result)
  return result


# for perform in-order traversal on BST and find elements within a range
def in_order_traversal_with_range_check(root, low, high, result):
  if root is None:
    return

  if root.data > low:
    in_order_traversal_with_range_check(root.left, low, high, result)

  if low <= root.data <= high:
    result.append(root.data)

  if root.data < high:
    in_order_traversal_with_range_check(root.right, low, high, result)


def main():
  # Create BSTs to merge
  root1 = Node(4)
  root1.left = Node(2)
  root1.right = Node(6)

  root2 = Node(5)
  root2.left = Node(3)
  root2.right = Node(7)

  ##############################################################
  # a) Merge BSTs
  merged_root = merge_bst(root1, root2)

  # Perform in-order traversal on merged BST
  result = []
  inorder_traversal(merged_root, result)
  print("Merged BST:", result)

  ###############################################################
  # b) Find the kth smallest element
  k = 3
  kth_smallest = find_kth_smallest(merged_root, k)
  print("kth smallest:", kth_smallest)

  ###############################################################
  # c) Balance the BST
  balanced_root = balance_bst(merged_root)

  # Perform in-order traversal on balanced BST
  result = []
  inorder_traversal(balanced_root, result)
  print("Balanced: ", result)

  ###############################################################
  # d) Find elements within the range
  low = 3
  high = 6
  elements = find_elements_in_range(merged_root, low, high)
  print("In range: ", elements)


if __name__ == "__main__":
  main()
