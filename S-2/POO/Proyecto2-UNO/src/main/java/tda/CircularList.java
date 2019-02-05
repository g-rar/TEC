package tda;

import java.util.Random;

public class CircularList<T> {

    private DNode<T> entry;
    private int size;

    public CircularList() {
        entry = null;
        size = 0;
    }

    public CircularList(T pEntry) {
        entry = new DNode<T>(pEntry);
        size = 1;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int getSize() {
        return size;
    }

    public void add(T value) {
        DNode<T> node = new DNode<T>(value);
        if (size > 1) {
            entry.getPrev().setNext(node);
            node.setPrev(entry.getPrev());
            entry.setPrev(node);
            node.setNext(entry);
        } else if (size == 1) {
            entry.setNext(node);
            entry.setPrev(node);
            node.setNext(entry);
            node.setPrev(entry);
        } else {
            entry = node;
        }
        size++;
    }

    public T remove(int pIndex) {
        T result = null;
        if (!isEmpty() & pIndex < size & pIndex >= 0) {
            DNode<T> searchPointer = entry;
            if (size != 1) {
                int i;
                for ( i = 0 ; i < pIndex; i++) {
                    searchPointer = searchPointer.getNext();
                }
                result = getValue(i);
                if (searchPointer == entry) {
                    entry = entry.getNext();
                }
                searchPointer.getPrev().setNext(searchPointer.getNext());
                searchPointer.getNext().setPrev(searchPointer.getPrev());
                searchPointer.setNext(null);
                searchPointer.setPrev(null);
            } else {
                entry = null;
            }
            size--;
        }
        return result;
    }

    public boolean remove(T toRemove) {
        boolean result = false;

        if (!isEmpty()) {
            DNode<T> searchPointer = entry.getNext();
            if (size != 1) {
                while (searchPointer != entry & searchPointer.getValue() != toRemove) {
                    searchPointer = searchPointer.getNext();
                }

                if (searchPointer.getValue() == toRemove) {
                    result = true;

                    if (searchPointer == entry) {
                        entry = entry.getNext();
                    }

                    searchPointer.getPrev().setNext(searchPointer.getNext());
                    searchPointer.getNext().setPrev(searchPointer.getPrev());
                    searchPointer.setNext(null);
                    searchPointer.setPrev(null);
                }
            } else {
                entry = null;
            }
            size--;

        }

        return result;
    }

    public void swap(int a, int b) {
        if (a != b & size > a & a > b & b > 0) {
            DNode<T> SearchPointer = entry.getNext();
            DNode<T> aPointer = null;
            DNode<T> bPointer = null;

            for (int i = 1; i < a + 1; i++) {
                if (i == a) {
                    aPointer = SearchPointer;
                }
                if (i == b) {
                    bPointer = SearchPointer;
                }
                SearchPointer = SearchPointer.getNext();
            }

            if (a - b != 1) {
                DNode<T> xPointer = aPointer.getNext();
                aPointer.getNext().setPrev(bPointer);
                aPointer.getPrev().setNext(bPointer);
                bPointer.getPrev().setNext(aPointer);
                bPointer.getNext().setPrev(aPointer);
                aPointer.setNext(bPointer.getNext());
                bPointer.setNext(xPointer);
                xPointer = aPointer.getPrev();
                aPointer.setPrev(bPointer.getPrev());
                bPointer.setPrev(xPointer);
            } else {
                bPointer.setNext(aPointer.getNext());
                aPointer.setPrev(bPointer.getPrev());
                bPointer.getPrev().setNext(aPointer);
                aPointer.getNext().setPrev(bPointer);
                bPointer.setPrev(aPointer);
                aPointer.setNext(bPointer);
            }
        }
    }

    public void rotate(int n) {
        if (0 < n & n < size) {
            for (int i = 0; i < n; i++) {
                entry = entry.getNext();
            }
        }
    }
    
    public void rotate(int n, boolean r) {
        if (0 < n & n < size) {
            for (int i = 0; i < n; i++) {
                entry = r ? entry.getPrev() : entry.getNext() ;
            }
        }
    }
    
    public void scramble(int ns) {
        Random rand = new Random();
        for (int i = 0; i < ns; i++) {
            int n1 = rand.nextInt(size / 2) + size / 2;
            int n2 = rand.nextInt(n1);
            swap(n1, n2);
            rotate(n1);
        }
    }

    public String toString() {
        String returnValue = "[";
        DNode<T> searchPointer = entry;

        for (int i = 0; i < size; i++) {
            returnValue += searchPointer.toString() + ", ";
            searchPointer = searchPointer.getNext();
        }

        if (returnValue.endsWith(", ")) {
            returnValue = returnValue.substring(0, returnValue.length() - 2);
        }
        returnValue += "]";

        return returnValue;
    }

    public T getValue(int p) {
        DNode<T> search = entry;
        int count = 0;
        while (search != null && p != count) {
            search = search.getNext();
            count++;
        }
        return search.getValue();
    }

}
