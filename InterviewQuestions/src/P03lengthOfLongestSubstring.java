public class P03lengthOfLongestSubstring {
    public static void main(String[] args) throws Exception {
        String[] data = { "Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD",
                " Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind" };

        // for the data
        for (String i : data) {
            String[] split = i.split(",");
            for (String j : split) {
                System.out.println(j);

            }
        }
    }
}
