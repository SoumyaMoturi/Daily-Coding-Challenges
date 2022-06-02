
/*
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child mustbe greater than or equal to the root.

*/



class Node
{
    int data;
	Node right,left;
	Node(int data){
	    this.data = data;
	    this.left = this.right = null;
	}

}
class Main
{

static boolean isBST(Node root)
{
	if (root == null)
		return true;
		
	if (root.left != null && root.data <= root.left.data)
		return false;

	if (root.right != null && root.data >= root.right.data)
		return false;

	return isBST(root.left) &&
		isBST(root.right);
}


public static void main(String args[])
{
    Node root = new Node(3);
	root.left = new Node(2);
	root.right = new Node(5);
	root.left.left = new Node(1);
	root.left.right = new Node(4);
	System.out.println( isBST(root)? "Given Tree is a BST" : "Given Tree is  not  a BST");
}
}
