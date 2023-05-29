package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class Test03_CommonStrings {

    @Test
    public void test01() {
        StreamProcessor processor = Main.getProcessor();

        String[] list1 = { "a", "list", "of", "various", "words" };
        String[] list2 = { "another", "list", "of", "several", "different", "words" };
        Set<String> expected = new HashSet<>();
        expected.add("list");
        expected.add("of");
        expected.add("words");

        Assert.assertEquals(expected, processor.problem3(list1, list2));
    }

    @Test
    public void testRandom() {
        Random r = new Random();

        String[] source = new String[15];
        for(int i = 0; i < source.length; i++){
            source[i] = generateRandomString();
        }

        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        for (int i = 0 ; i < 10 ; i++) {
            list1.add(source[r.nextInt(source.length)]);
            list2.add(source[r.nextInt(source.length)]);
        }

        Set<String> expected = new HashSet<>();
        for (String s : list1)
            if(list2.contains(s)) expected.add(s);

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected,
                processor.problem3(list1.toArray(String[]::new), list2.toArray(String[]::new)));
    }

    public static String generateRandomString() {
        Random r = new Random();
        char[] chars = new char[10];
        for (int i = 0 ; i < chars.length ; i++) {
            if (r.nextBoolean()) {
                // Lowercase
                int start = 'a';
                int c = r.nextInt('z'-'a');
                chars[i] = (char)('a' + c);
            } else if (r.nextBoolean()) {
                // Uppercase
                int start = 'A';
                int c = r.nextInt('Z'-'A');
                chars[i] = (char)('A' + c);
            } else {
                // Number
                int start = '0';
                int c = r.nextInt('9'-'0');
                chars[i] = (char)('0' + c);
            }
        }

        return new String(chars);
    }
}
