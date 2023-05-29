package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

import static edu.uic.cs474.s23.a3.Test03_CommonStrings.generateRandomString;

public class Test04_WordCount {

    @Test
    public void test01() {
        StreamProcessor processor = Main.getProcessor();

        String[] words1 = { "a", "list", "of", "various", "words" };
        String[] words2 = { "another", "list", "of", "several", "different", "words" };
        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();
        Collections.addAll(list1, words1);
        Collections.addAll(list2, words2);

        Map<String, Long> expected = new HashMap<>();
        List<String> list3 = new ArrayList<>();
        list3.addAll(list1);
        list3.addAll(list2);
        for(String s : list3){
            Long count = expected.get(s);
            if(count == null) expected.put(s, (long) 1);
            else expected.put(s, count + 1);
        }

        List<List<String>> input = new ArrayList<>();
        input.add(list1);
        input.add(list2);
        Assert.assertEquals(expected, processor.problem4(input));
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
        List<String> list3 = new ArrayList<>();

        for (int i = 0 ; i < 10 ; i++) {
            list1.add(source[r.nextInt(source.length)]);
            list2.add(source[r.nextInt(source.length)]);
            list3.add(source[r.nextInt(source.length)]);
        }

        Map<String, Long> expected = new HashMap<>();
        List<String> lists = new ArrayList<>();
        lists.addAll(list1);
        lists.addAll(list2);
        lists.addAll(list3);
        for(String s : lists){
            Long count = expected.get(s);
            if(count == null) expected.put(s, (long) 1);
            else expected.put(s, count + 1);
        }

        List<List<String>> input = new ArrayList<>();
        input.add(list1);
        input.add(list2);
        input.add(list3);

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected, processor.problem4(input));
    }
}
