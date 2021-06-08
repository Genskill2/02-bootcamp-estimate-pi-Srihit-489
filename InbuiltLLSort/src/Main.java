import java.util.Collections;
import java.util.LinkedList;
import java.util.ListIterator;

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> mylist = new LinkedList<Integer>();
        mylist.add(2);
        mylist.add(6);
        mylist.add(3);
        mylist.addFirst(9);
        mylist.add(7);
        printList(mylist);
        Collections.sort(mylist);
        printList(mylist);
    }
    public static void printList(LinkedList<Integer> mylist){
        ListIterator<Integer> itr = mylist.listIterator();
        while(itr.hasNext()){
            int data = itr.next();
            System.out.print(data+" ");
        }
        System.out.println();
    }
}
