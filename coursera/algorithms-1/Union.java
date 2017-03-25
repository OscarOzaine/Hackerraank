/*
input:
10
4 3
3 8
6 5
9 4
2 1
8 9
5 0
7 2
6 1
1 0
6 7

*/

import java.util.Scanner;

//Union too expensive(N array accesses)
//Trees are flat, but too expensive to keep them flat
class QuickFindUF
{
	private int[] id;

	public QuickFindUF(int N)
	{
		id = new int[N];
		for (int x = 0; x < N; x++)
		{
			id[x] = x;
		}
	}

	public boolean connected(int p, int q)
	{
		return id[p] == id[q];
	}

	public void union(int p, int q)
	{
		int pid = id[p];
		int qid = id[q];
		for (int x = 0; x < id.length; x++)
		{
			if (id[x] == pid)
				id[x] = qid;
		}
	}
}

//trees can get tall
//find too expensive (could be N array accesses)
class QuickUnionUF
{
	private int[] id;

	public QuickUnionUF(int N)
	{
		id = new int[N];
		for (int i = 0; i < N; i++)
			id[i] = i;
	}

	private int root(int i)
	{
		while(i != id[i]) {
			i = id[i];
		}
		return i;
	}

	public boolean connected(int p, int q)
	{
		return root(p) == root(q);
	}

	public void union(int p, int q)
	{
		int i = root(p);
		int j = root(p);
		id[i] = j;
	}
}

public class Union {

	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		/*
		System.out.println(n);

		for(int x = 0; x < n; x++)
		{
			System.out.println(x);
		}
		*/
		QuickUnionUF uf = new QuickUnionUF(n);
		for (int x = 0; x <= n; x++)
		{
			int p = scan.nextInt();
			int q = scan.nextInt();

			if (!uf.connected(p, q))
			{
				uf.union(p, q);
				//System.out.println(p + " " + q);
			}
		}
		/*
		while(!scan.isEmpty())
		{
			int p = scan.nextInt();
			int q = scan.nextInt();

			if (!uf.connected(p, q))
			{
				uf.union(p, q);
				System.out.println(p + " " + q);
			}
		}
		*/
	}

}

