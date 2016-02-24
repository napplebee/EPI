# Initial code in JAVA has copyright © 2002–2015, Robert Sedgewick and Kevin Wayne.
# A symbol table implemented using a left-leaning red-black BST.
# This is the 2-3 version.

RED = True
BLACK = False


class Node(object):
    key = None
    value = None  # associated data
    left = None
    right = None
    color = None  #color of parent link
    count = None  # subtree count

    def __init__(self, key, value, color, count):
        self.key = key;
        self.val = value;
        self.color = color;
        self.count = count;


# noinspection PyPep8Naming
class RedBlackBST(object):
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def is_empty(self):
        return self.root is None

    # Node helper methods
    @staticmethod
    def isRed(node):
        if node is None:
            return False
        return node.color == RED;

    @staticmethod
    def _size(node):
        """
        number of node in subtree rooted at node; 0 if node is null
        """
        if node is None:
            return 0
        return node.count;

    def get(self, key):
        """
        Returns the value associated with the given key.
        """
        if key is None:
            return None

        return self._get(self.root, key)

    @staticmethod
    def _get(node, key):
        while node is not None:
            if key < node.key:
                node = node.left;
            elif key > node.key:
                node = node.right;
            else:
                return node.val;

        return None;

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        """
        Inserts the specified key-value pair into the symbol table, overwriting the old
        value with the new value if the symbol table already contains the specified key.
        Deletes the specified key (and its associated value) from this symbol table
        if the specified value is None.
        """
        if key is None:
            raise ValueError("first argument to put() is null")

        if val is None:
            self.delete(key)
            return

        self.root = self._put(self.root, key, val);
        root.color = BLACK;

    def _put(self, node, key, val):
        """
        insert the key-value pair in the subtree rooted at node
        """
        if node is None:
            return Node(key, val, RED, 1);

        if key < node.key:
            node.left  = self._put(node.left,  key, val);
        elif key > node.key:
            node.right = self._put(node.right, key, val);
        else:
            node.val = val;

        # fix-up any right-leaning links
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        node.count = self._size(node.left) + self._size(node.right) + 1;

        return node;

    def delete_min(self):
        """
        Removes the smallest key and associated value from the symbol table.
        """
        if self.is_empty():
            raise Exception("BST is empty");

        # if both children of root are black, set root to red
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED;

        self.root = self._delete_min(self.root);
        if not self.is_empty():
            self.root.color = BLACK;

    def _delete_min(self, node):
        """
        delete the key-value pair with the minimum key rooted at node
        """
        if node.left is None:
            return None;

        if not self.isRed(node.left) and not self.isRed(node.left.left):
            node = self.moveRedLeft(node)

        node.left = self._delete_min(node.left)
        return self.balance(node);

    def deleteMax(self):
        """
        Removes the largest key and associated value from the symbol table.
        """
        if self.is_empty():
            raise Exception("BST is empty");

        # if both children of root are black, set root to red
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED;

        self.root = self._deleteMax(self.root);
        if not self.is_empty():
            self.root.color = BLACK;

    def _deleteMax(self, node):
        """
        delete the key-value pair with the maximum key rooted at h
        """
        if self._is_red(node.left):
            node = self.rotateRight(node);

        if node.right is None:
            return None;

        if not self.isRed(node.right) and not self.isRed(node.right.left):
            node = self.moveRedRight(node);

        node.right = self._deleteMax(node.right);

        return self.balance(node);

    def delete(self, key):
        """
        Removes the specified key and its associated value from this symbol table
        """
        if key is None:
            raise ValueError("argument to delete() is null")

        if not self.contains(key):
            return

        # if both children of root are black, set root to red
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED

        self.root = self._delete(self.root, key)
        if not self.isEmpty():
            root.color = BLACK

    def _delete(self, node, key):
        """
        delete the key-value pair with the given key rooted at node
        """
        if key < node.key:
            if not self.isRed(node.left) and not self.isRed(node.left.left):
                h = self.moveRedLeft(node)
            h.left = self._delete(node.left, key);
        else:
            if self.isRed(node.left):
                node = self.rotateRight(node)
            if key == node.key and node.right is None:
                return None
            if not self.isRed(node.right) and not self.isRed(node.right.left):
                node = self.moveRedRight(node)
            if key == node.key:
                x = min(node.right)
                node.key = x.key
                node.val = x.val
                # node.val = self.get(node.right, min(node.right).key);
                # node.key = self.min(node.right).key;
                node.right = self._deleteMin(node.right)
            else:
                node.right = self._delete(node.right, key)
        return self.balance(node)

    def rotateRight(self, node):
        """
        make a left-leaning link lean to the right
        """
        x = node.left;
        node.left = x.right;
        x.right = node;
        x.color = x.right.color;
        x.right.color = RED;
        x.count = node.count;
        node.count = self.size(node.left) + self.size(node.right) + 1;
        return x;

    def rotateLeft(self, node):
        """
        make a right-leaning link lean to the left
        """
        x = node.right;
        node.right = x.left;
        x.left = node;
        x.color = x.left.color;
        x.left.color = RED;
        x.count = node.count;
        node.count = self.size(node.left) + self.size(node.right) + 1;
        return x;

    def flipColors(self, node):
        """
        flip the colors of a node and its two children
        """
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color


    def moveRedLeft(self, node):
        """
        Assuming that node is red and both node.left and node.left.left
        are black, make node.left or one of its children red.
        assert node is not None
        assert isRed(node) and not isRed(node.left) and not isRed(node.left.left)
        """
        self.flipColors(node);
        if self.isRed(node.right.left):
            node.right = self.rotateRight(node.right)
            node = self.rotateLeft(node)
            self.flipColors(node)

        return node

    def moveRedRight(self, node):
        """
        Assuming that h is red and both h.right and h.right.left
        are black, make h.right or one of its children red.
        assert node is not None
        assert isRed(node) and not isRed(node.right) and not isRed(node.right.left)
        """
        self.flipColors(node)
        if self.isRed(node.left.left):
            node = self.rotateRight(node)
            self.flipColors(node)
        return node

    def balance(self, node):
        """
        restore red-black tree invariant
        assert node is not None
        """
        if self.isRed(node.right):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)

        node.count = self._size(node.left) + self._size(node.right) + 1
        return node

#
# public class RedBlackBST<Key extends Comparable<Key>, Value> {
#
#    /***************************************************************************
#     *  Utility functions.
#     ***************************************************************************/
#
#     /**
#      * Returns the height of the BST (for debugging).
#      * @return the height of the BST (a 1-node tree has height 0)
#      */
#     public int height() {
#         return height(root);
#     }
#     private int height(Node x) {
#         if (x == null) return -1;
#         return 1 + Math.max(height(x.left), height(x.right));
#     }
#
#    /***************************************************************************
#     *  Ordered symbol table methods.
#     ***************************************************************************/
#
#     /**
#      * Returns the smallest key in the symbol table.
#      * @return the smallest key in the symbol table
#      * @throws NoSuchElementException if the symbol table is empty
#      */
#     public Key min() {
#         if (isEmpty()) throw new NoSuchElementException("called min() with empty symbol table");
#         return min(root).key;
#     }
#
#     // the smallest key in subtree rooted at x; null if no such key
#     private Node min(Node x) {
#         // assert x != null;
#         if (x.left == null) return x;
#         else                return min(x.left);
#     }
#
#     /**
#      * Returns the largest key in the symbol table.
#      * @return the largest key in the symbol table
#      * @throws NoSuchElementException if the symbol table is empty
#      */
#     public Key max() {
#         if (isEmpty()) throw new NoSuchElementException("called max() with empty symbol table");
#         return max(root).key;
#     }
#
#     // the largest key in the subtree rooted at x; null if no such key
#     private Node max(Node x) {
#         // assert x != null;
#         if (x.right == null) return x;
#         else                 return max(x.right);
#     }
#
#
#     /**
#      * Returns the largest key in the symbol table less than or equal to <tt>key</tt>.
#      * @param key the key
#      * @return the largest key in the symbol table less than or equal to <tt>key</tt>
#      * @throws NoSuchElementException if there is no such key
#      * @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
#      */
#     public Key floor(Key key) {
#         if (key == null) throw new NullPointerException("argument to floor() is null");
#         if (isEmpty()) throw new NoSuchElementException("called floor() with empty symbol table");
#         Node x = floor(root, key);
#         if (x == null) return null;
#         else           return x.key;
#     }
#
#     // the largest key in the subtree rooted at x less than or equal to the given key
#     private Node floor(Node x, Key key) {
#         if (x == null) return null;
#         int cmp = key.compareTo(x.key);
#         if (cmp == 0) return x;
#         if (cmp < 0)  return floor(x.left, key);
#         Node t = floor(x.right, key);
#         if (t != null) return t;
#         else           return x;
#     }
#
#     /**
#      * Returns the smallest key in the symbol table greater than or equal to <tt>key</tt>.
#      * @param key the key
#      * @return the smallest key in the symbol table greater than or equal to <tt>key</tt>
#      * @throws NoSuchElementException if there is no such key
#      * @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
#      */
#     public Key ceiling(Key key) {
#         if (key == null) throw new NullPointerException("argument to ceiling() is null");
#         if (isEmpty()) throw new NoSuchElementException("called ceiling() with empty symbol table");
#         Node x = ceiling(root, key);
#         if (x == null) return null;
#         else           return x.key;
#     }
#
#     // the smallest key in the subtree rooted at x greater than or equal to the given key
#     private Node ceiling(Node x, Key key) {
#         if (x == null) return null;
#         int cmp = key.compareTo(x.key);
#         if (cmp == 0) return x;
#         if (cmp > 0)  return ceiling(x.right, key);
#         Node t = ceiling(x.left, key);
#         if (t != null) return t;
#         else           return x;
#     }
#
#     /**
#      * Return the kth smallest key in the symbol table.
#      * @param k the order statistic
#      * @return the kth smallest key in the symbol table
#      * @throws IllegalArgumentException unless <tt>k</tt> is between 0 and
#      *     <em>N</em> &minus; 1
#      */
#     public Key select(int k) {
#         if (k < 0 || k >= size()) throw new IllegalArgumentException();
#         Node x = select(root, k);
#         return x.key;
#     }
#
#     // the key of rank k in the subtree rooted at x
#     private Node select(Node x, int k) {
#         // assert x != null;
#         // assert k >= 0 && k < size(x);
#         int t = size(x.left);
#         if      (t > k) return select(x.left,  k);
#         else if (t < k) return select(x.right, k-t-1);
#         else            return x;
#     }
#
#     /**
#      * Return the number of keys in the symbol table strictly less than <tt>key</tt>.
#      * @param key the key
#      * @return the number of keys in the symbol table strictly less than <tt>key</tt>
#      * @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
#      */
#     public int rank(Key key) {
#         if (key == null) throw new NullPointerException("argument to rank() is null");
#         return rank(key, root);
#     }
#
#     // number of keys less than key in the subtree rooted at x
#     private int rank(Key key, Node x) {
#         if (x == null) return 0;
#         int cmp = key.compareTo(x.key);
#         if      (cmp < 0) return rank(key, x.left);
#         else if (cmp > 0) return 1 + size(x.left) + rank(key, x.right);
#         else              return size(x.left);
#     }
#
#    /***************************************************************************
#     *  Range count and range search.
#     ***************************************************************************/
#
#     /**
#      * Returns all keys in the symbol table as an <tt>Iterable</tt>.
#      * To iterate over all of the keys in the symbol table named <tt>st</tt>,
#      * use the foreach notation: <tt>for (Key key : st.keys())</tt>.
#      * @return all keys in the sybol table as an <tt>Iterable</tt>
#      */
#     public Iterable<Key> keys() {
#         if (isEmpty()) return new Queue<Key>();
#         return keys(min(), max());
#     }
#
#     /**
#      * Returns all keys in the symbol table in the given range,
#      * as an <tt>Iterable</tt>.
#      * @return all keys in the sybol table between <tt>lo</tt>
#      *    (inclusive) and <tt>hi</tt> (exclusive) as an <tt>Iterable</tt>
#      * @throws NullPointerException if either <tt>lo</tt> or <tt>hi</tt>
#      *    is <tt>null</tt>
#      */
#     public Iterable<Key> keys(Key lo, Key hi) {
#         if (lo == null) throw new NullPointerException("first argument to keys() is null");
#         if (hi == null) throw new NullPointerException("second argument to keys() is null");
#
#         Queue<Key> queue = new Queue<Key>();
#         // if (isEmpty() || lo.compareTo(hi) > 0) return queue;
#         keys(root, queue, lo, hi);
#         return queue;
#     }
#
#     // add the keys between lo and hi in the subtree rooted at x
#     // to the queue
#     private void keys(Node x, Queue<Key> queue, Key lo, Key hi) {
#         if (x == null) return;
#         int cmplo = lo.compareTo(x.key);
#         int cmphi = hi.compareTo(x.key);
#         if (cmplo < 0) keys(x.left, queue, lo, hi);
#         if (cmplo <= 0 && cmphi >= 0) queue.enqueue(x.key);
#         if (cmphi > 0) keys(x.right, queue, lo, hi);
#     }
#
#     /**
#      * Returns the number of keys in the symbol table in the given range.
#      * @return the number of keys in the sybol table between <tt>lo</tt>
#      *    (inclusive) and <tt>hi</tt> (exclusive)
#      * @throws NullPointerException if either <tt>lo</tt> or <tt>hi</tt>
#      *    is <tt>null</tt>
#      */
#     public int size(Key lo, Key hi) {
#         if (lo == null) throw new NullPointerException("first argument to size() is null");
#         if (hi == null) throw new NullPointerException("second argument to size() is null");
#
#         if (lo.compareTo(hi) > 0) return 0;
#         if (contains(hi)) return rank(hi) - rank(lo) + 1;
#         else              return rank(hi) - rank(lo);
#     }
#
#
#    /***************************************************************************
#     *  Check integrity of red-black tree data structure.
#     ***************************************************************************/
#     private boolean check() {
#         if (!isBST())            StdOut.println("Not in symmetric order");
#         if (!isSizeConsistent()) StdOut.println("Subtree counts not consistent");
#         if (!isRankConsistent()) StdOut.println("Ranks not consistent");
#         if (!is23())             StdOut.println("Not a 2-3 tree");
#         if (!isBalanced())       StdOut.println("Not balanced");
#         return isBST() && isSizeConsistent() && isRankConsistent() && is23() && isBalanced();
#     }
#
#     // does this binary tree satisfy symmetric order?
#     // Note: this test also ensures that data structure is a binary tree since order is strict
#     private boolean isBST() {
#         return isBST(root, null, null);
#     }
#
#     // is the tree rooted at x a BST with all keys strictly between min and max
#     // (if min or max is null, treat as empty constraint)
#     // Credit: Bob Dondero's elegant solution
#     private boolean isBST(Node x, Key min, Key max) {
#         if (x == null) return true;
#         if (min != null && x.key.compareTo(min) <= 0) return false;
#         if (max != null && x.key.compareTo(max) >= 0) return false;
#         return isBST(x.left, min, x.key) && isBST(x.right, x.key, max);
#     }
#
#     // are the size fields correct?
#     private boolean isSizeConsistent() { return isSizeConsistent(root); }
#     private boolean isSizeConsistent(Node x) {
#         if (x == null) return true;
#         if (x.N != size(x.left) + size(x.right) + 1) return false;
#         return isSizeConsistent(x.left) && isSizeConsistent(x.right);
#     }
#
#     // check that ranks are consistent
#     private boolean isRankConsistent() {
#         for (int i = 0; i < size(); i++)
#             if (i != rank(select(i))) return false;
#         for (Key key : keys())
#             if (key.compareTo(select(rank(key))) != 0) return false;
#         return true;
#     }
#
#     // Does the tree have no red right links, and at most one (left)
#     // red links in a row on any path?
#     private boolean is23() { return is23(root); }
#     private boolean is23(Node x) {
#         if (x == null) return true;
#         if (isRed(x.right)) return false;
#         if (x != root && isRed(x) && isRed(x.left))
#             return false;
#         return is23(x.left) && is23(x.right);
#     }
#
#     // do all paths from root to leaf have same number of black edges?
#     private boolean isBalanced() {
#         int black = 0;     // number of black links on path from root to min
#         Node x = root;
#         while (x != null) {
#             if (!isRed(x)) black++;
#             x = x.left;
#         }
#         return isBalanced(root, black);
#     }
#
#     // does every path from the root to a leaf have the given number of black links?
#     private boolean isBalanced(Node x, int black) {
#         if (x == null) return black == 0;
#         if (!isRed(x)) black--;
#         return isBalanced(x.left, black) && isBalanced(x.right, black);
#     }
#
#
#     /**
#      * Unit tests the <tt>RedBlackBST</tt> data type.
#      */
#     public static void main(String[] args) {
#         RedBlackBST<String, Integer> st = new RedBlackBST<String, Integer>();
#         for (int i = 0; !StdIn.isEmpty(); i++) {
#             String key = StdIn.readString();
#             st.put(key, i);
#         }
#         for (String s : st.keys())
#             StdOut.println(s + " " + st.get(s));
#         StdOut.println();
#     }
# }
#
#
