package B_02000;

import java.util.*;
import java.lang.Math;

public class B02903 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        
        System.out.print((int)Math.pow((Math.pow(2, n) + 1), 2));
    }
}