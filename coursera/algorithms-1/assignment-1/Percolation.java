package assignment;

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation 
{
    private boolean[][] opened;
    private int top = 0;
    private int bottom;
    private int size;
    private WeightedQuickUnionUF quickFind;

    // Create n-by-n grid, with all sites blocked
    public Percolation(int n) 
    {
        this.size = n;
        this.bottom = n * n + 1;
        this.quickFind = new WeightedQuickUnionUF(n * n + 2);
        opened = new boolean[n][n];
    }

    // Open site (row, col) if it is not open already
    public void open(int i, int j) 
    {
        opened[i - 1][j - 1] = true;
        if (i == 1)
            this.quickFind.union(getQFIndex(i, j), this.top);
        
        if (i == this.size)
            this.quickFind.union(getQFIndex(i, j), this.bottom);

        if (j > 1 && isOpen(i, j - 1)) 
            this.quickFind.union(getQFIndex(i, j), getQFIndex(i, j - 1));

        if (j < this.size && isOpen(i, j + 1)) 
            this.quickFind.union(getQFIndex(i, j), getQFIndex(i, j + 1));
        
        if (i > 1 && isOpen(i - 1, j)) 
            this.quickFind.union(getQFIndex(i, j), getQFIndex(i - 1, j));
        
        if (i < this.size && isOpen(i + 1, j)) 
            this.quickFind.union(getQFIndex(i, j), getQFIndex(i + 1, j));
    }

    // Is site (row, col) open?
    public boolean isOpen(int i, int j) 
    {
        return opened[i - 1][j - 1];
    }

    // Is site (row i, column j) full?
    public boolean isFull(int i, int j) 
    {
        if (0 < i && i <= this.size && 0 < j && j <= this.size) {
            return this.quickFind.connected(this.top, getQFIndex(i , j));
        } else {
            throw new IndexOutOfBoundsException();
        }
    }

    // Does the system percolate?
    public boolean percolates() 
    {
        return this.quickFind.connected(this.top, this.bottom);
    }

    private int getQFIndex(int i, int j) 
    {
        return this.size * (i - 1) + j;
    }
}
