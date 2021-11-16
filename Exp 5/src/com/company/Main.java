package com.company;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> sortedArray1 = new ArrayList<Integer>();
        ArrayList<Integer> sortedArray2 = new ArrayList<Integer>();
        for (int i = 0; i < 1000; i++) {
            sortedArray2.add(i);
        }
        for (int i = 2000; i < 3000; i++) {
            sortedArray1.add(i);
        }


        mergeTwoSortedArray(sortedArray1, sortedArray2);
    }

    private static void mergeTwoSortedArray(ArrayList<Integer> sortedArray1, ArrayList<Integer> sortedArray2) {
        ArrayList<Integer> rawArraylist = new ArrayList<Integer>();
        rawArraylist.addAll(sortedArray1);
        rawArraylist.addAll(sortedArray2);
        Collections.sort(rawArraylist);
        System.out.println(rawArraylist);
    }
}
