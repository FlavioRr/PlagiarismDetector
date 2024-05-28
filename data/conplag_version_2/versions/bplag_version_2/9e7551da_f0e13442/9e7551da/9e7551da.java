import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
// نورت الكود يا كبير اتفضل

// يا رب Accepted
public class InterestingStory {
    private static int[] freq;
    private static String[] strs;

    private static int[] countAlpha(char alpha) {

        int[] count = new int[strs.length];

        for (int i = 0; i < strs.length; i++)
            for (char c : strs[i].toCharArray())
                count[i] += c == alpha ? -1 : 1;

        return count;
    }

    private static int solve(char alpha) {
        int[] res = countAlpha(alpha);

        Arrays.sort(res);

        int freqSum = 0;
        for (int j : freq) freqSum += j;

        freqSum -= freq[alpha - 'a'];


        int k = res.length - 1;

        //System.out.println(freq[alpha - 'a'] + " " + freqSum);

        while (k >= 0 && freq[alpha - 'a'] <= freqSum) {
            //System.out.println(freq[alpha - 'a'] + " " + freqSum);
            freqSum -= res[k--];
        }
        return k + 1;
    }

    public static void main(String[] args) {
        FastReader in = new FastReader();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

        int t = in.nextInt();
        while (t-- > 0) {

            int n = in.nextInt();
            freq = new int[7];
            strs = new String[n];

            for (int i = 0; i < n; i++)
                strs[i] = in.nextLine();

            for (String str : strs)
                for (char c : str.toCharArray())
                    freq[c - 'a']++;

            int max = 0;

//            int x = solve('d');
//            out.println(x);

            for (char c = 'a'; c < 'f'; c++)
                max = Math.max(max, solve(c));

//            int[] arr = countAlpha('d');
//            Arrays.sort(arr);
//
//            for (int i : arr)
//                out.println(i);


            out.println(max);

        }

        out.close();
    }

    
}
