package B_01000;

import java.util.Scanner;
import java.util.Calendar;

public class B01924 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        int day = sc.nextInt();
        sc.close();

        Calendar cal = Calendar.getInstance();
        cal.set(2007, 0, 1);
        cal.add(Calendar.MONTH, month - 1);
        cal.add(Calendar.DATE, day - 1);

        int dayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
        String[] days = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

        System.out.println(days[dayOfWeek-1]);
    }
}