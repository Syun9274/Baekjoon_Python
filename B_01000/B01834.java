package B_01000;

import java.util.Scanner;

public class B01834 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long n = sc.nextInt();
        sc.close();
        
        long ans = 0;
        for(int i = 1; i < n; i++) {
        	ans += n * i + i;
        }
        
        System.out.println(ans);
    }
}