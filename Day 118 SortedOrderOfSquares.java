/******************************************************************************

This problem was asked by Google.
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

*******************************************************************************/
import java.util.*;
import java.util.Arrays;
public class Main
{
	public static void main(String[] args) {
	    
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int arr[] = new int[n];
		for(int i=0;i<n;i++)
		    arr[i] = s.nextInt();
		Arrays.sort(arr);
		for(int i=0;i<n;i++){
		    arr[i]=arr[i]*arr[i];
		}
		Arrays.sort(arr);
		for(int i=0;i<n;i++)
		    System.out.print(arr[i]+" ");
		
	}
}
