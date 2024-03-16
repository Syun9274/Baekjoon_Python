package B_02000;

import java.util.*;

public class B02720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] tmp = new int[]{25, 10, 5, 1};
        
        for(int i = 0; i < t; i++) {
        	int c = sc.nextInt();
        	int[] coin = new int[4];
        	
        	for(int j = 0; j < 4; j++) {
        		coin[j] = c / tmp[j];
        		c = c % tmp[j];
        		
        		System.out.print(coin[j] + " ");
        	}
        	
        	System.out.println();
        }
        
        sc.close();
    }
}
