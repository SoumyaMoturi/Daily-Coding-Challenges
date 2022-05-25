/******************************************************************************
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

*******************************************************************************/
public class Main
{
	public static void main(String[] args) {
		int a=25;
		int b=5;
		int c=0;
		while(a > 0 && a >= b){
		    a=a-b;
		    c++;
		}
		System.out.println(c);
	}
}
