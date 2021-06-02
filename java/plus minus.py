import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
    float positive=new Float(0);
    float negative=new Float(0);
    float zero=new Float(0);
    int n=arr.size();
    for(int i=0;i<n;i++){
        if(arr.get(i)>0){
            positive+=1;
        }
        else if(arr.get(i)<0){
            negative+=1;
        }
        else{
            zero+=1;
        }
    }
        //  String.format("%.5f", b)
    System.out.println(String.format("%.6f",positive/n));
    System.out.println(String.format("%.6f",negative/n));            
    System.out.println(String.format("%.6f",zero/n));    
            

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
