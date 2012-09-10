#!usr/bin/python
# this a binary tree implementaion in python


import sys
import os

def insert(tree, element):
	if tree == None:
		return (None,element,None)
	else:
		left_child = tree[0]
		this_element = tree[1]
		right_child = tree[2]
		if element <= this_element:
			new_left_child = insert(left_child,element)
			return(new_left_child,this_element,right_child)
		else:
			new_right_child = insert(right_child,element)
			return(left_child,this_element,new_right_child)
	

## a recursive proc
def print_tree(tree):
	if tree == None:
		return
	else:
		left_child = tree[0]
		this_element = tree[1]
		right_child = tree[2]
		print_tree(left_child)
		print this_element

		print_tree(right_child)

# finding if an element is in the tree
def contains(tree,element):
	if tree == None:
		return False
	else:	
		left_child = tree[0]
		this_element = tree[1]
		right_child = tree[2]
		if this_element == this_element:
			return True
		elif this_element > element:
			return contains(left_child,element)
		else:
			return contains(right_child,element)

def insert_in_tree(tree, element):
	temp = tree 
	tree = insert(temp, element)
	return tree

def main():
	tree = None
	while True:
		element = raw_input("enter name(enter q to quit adding name) : ")
		if element != "q":
			tree=insert_in_tree(tree, element)
		else:
			break


	#t1 = insert_in_tree(tree,"aashish")
	#t2 = insert(t1, "vinny")
	#t3 = insert(t2, "jikky")
	#t4 = insert(t3, "rohit")
	# printing the tree 
	print_tree(tree)
	#print contains("midpoint", t4)

if __name__ == "__main__":
	main()


	
