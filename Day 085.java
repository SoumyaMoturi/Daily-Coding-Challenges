/******************************************************************************
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

*******************************************************************************/
import java.util.*;

public class Main
{
	public static void main(String[] args) {
		int x=10;
		int y=20;
		Scanner s = new Scanner(System.in);
		int b = s.nextInt();
		try{
		    int r = x/b;
		    System.out.println("X value : " + x);
		}
		catch(Exception e){
		    System.out.println("Y value : "+ y);
		}
	}
}
