// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

// Input: l1 = [0], l2 = [0]
// Output: [0]

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]
class P02AddLinkList {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // the pointer stays
        ListNode result = new ListNode(0);
        // this pointer does go to the end of the list
        ListNode pointer = result;

        int carry = 0;

        while (l1 != null || l2 != null || carry == 1) {
            int sum = 0;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            sum += carry;
            carry = sum / 10;
            ListNode temp = new ListNode(sum % 10);
            pointer.next = temp;
            pointer = pointer.next;
        }
        return result.next;
    }

    public static void main(String[] args) throws Exception {
        // System.out.println();
        ListNode t0 = new ListNode(3);
        ListNode t1 = new ListNode(4, t0);
        ListNode t2 = new ListNode(2, t1);
        ListNode v0 = new ListNode(4);
        ListNode v1 = new ListNode(6, v0);
        ListNode v2 = new ListNode(5, v1);

        ListNode result = addTwoNumbers(t2, v2);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }

        // l1 = l1.next;
        // l1 = 2;

        // l1.next();

    }
    // make a java main class?
}