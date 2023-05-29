package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class Test01_GetPos {

    @Test
    public void test01() {
        StreamProcessor processor = Main.getProcessor();

        List<Integer> l = new ArrayList<>();
        Integer[] elements = { 1, -2, 3, -4, 6 };
        Collections.addAll(l, elements);

        Integer[] expected = { 1, 3, 6 };

        Assert.assertArrayEquals(expected, processor.problem1(l).toArray());
    }

    @Test
    public void testRandom() {
        Random r = new Random();
        List<Integer> l = new ArrayList<>();
        Integer[] elements = new Integer[10];

        for (int i = 0 ; i < elements.length ; i++) {
            elements[i] = r.nextInt();
        }
        Collections.addAll(l, elements);

        List<Integer> expected = new ArrayList<>();
        for(int i = 0; i < elements.length; i++) {
            int element = elements[i];
            if (element > 0) expected.add(element);
        }

        StreamProcessor processor = Main.getProcessor();
        Assert.assertArrayEquals(expected.toArray(), processor.problem1(l).toArray());
    }
}
