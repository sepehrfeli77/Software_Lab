package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> sortedArray1 = new ArrayList<Integer>();
        ArrayList<Integer> sortedArray2 = new ArrayList<Integer>();
        /*
            use 20000 for bubble sort and 10e6 for efficient sort
         */
        for (int i = 0; i < 20000; i++) {
            sortedArray2.add(i);
        }
        for (int i = sortedArray2.size(); i < (2 * sortedArray2.size()); i++) {
            sortedArray1.add(i);
        }
        mergeTwoSortedArray(sortedArray1, sortedArray2);
    }

    private static void mergeTwoSortedArray(ArrayList<Integer> sortedArray1, ArrayList<Integer> sortedArray2) {
        ArrayList<Integer> rawArraylist = new ArrayList<Integer>();
        rawArraylist.addAll(sortedArray1);
        rawArraylist.addAll(sortedArray2);

        bubbleSort(rawArraylist);
//        efficientSort(sortedArray1, sortedArray2, rawArraylist);

    }
    static void bubbleSort(ArrayList<Integer> arr){
        int n = arr.size();
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (arr.get(j) > arr.get(j+1)){
                    // swap arr[j+1] and arr[j]
                    int temp = arr.get(j);
                    arr.set(j,arr.get(j+1));
                    arr.set(j+1, temp);
                }
    }
    static void efficientSort(ArrayList<Integer> sortedArray1, ArrayList<Integer> sortedArray2, ArrayList<Integer> rawArraylist){
        int pointer1 = 0, pointer2 = 0;

        while((pointer1 < sortedArray1.size()) && (pointer2 < sortedArray2.size())){
            if(sortedArray1.get(pointer1) <= sortedArray2.get(pointer2)) {
                rawArraylist.add(sortedArray1.get(pointer1));
                pointer1 += 1;
            }
            else {
                rawArraylist.add(sortedArray2.get(pointer2));
                pointer2 += 1;
            }
        }
        while (pointer1 < sortedArray1.size()){
            rawArraylist.add(sortedArray1.get(pointer1));
            pointer1 += 1;
        }
        while (pointer2 < sortedArray2.size()){
            rawArraylist.add(sortedArray2.get(pointer2));
            pointer2 += 1;
        }
    }
}
