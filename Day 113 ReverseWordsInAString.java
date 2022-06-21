/******************************************************************************


This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String line=s.nextLine();
		String[] arr = line.split(" ");
		line="";
		for(int i=arr.length-1;i>=0;i--){
		    line+=arr[i]+" ";
		}
		System.out.println(line);
	}
}
