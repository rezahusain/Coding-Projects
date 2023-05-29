package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class Test10_Debug {

    @Test
    public void testCommon() {
        Main main = new Main();
        main.processClass("edu.uic.cs474.s23.a3.Test09_TransitivelyInheritedMethods");

        Map<String, Set<String>> expected = new HashMap<>();
        expected.put("A", new HashSet<>(Arrays.asList("B", "C", "D", "E", "F", "G")));
        expected.put("B", new HashSet<>(Arrays.asList("A", "C", "D", "E", "F", "G")));
        expected.put("C", new HashSet<>(Arrays.asList("A", "B", "D", "E", "F", "G")));
        expected.put("D", new HashSet<>(Arrays.asList("A", "B", "C", "E", "F", "G")));
        expected.put("E", new HashSet<>(Arrays.asList("A", "B", "C", "D", "F", "G")));
        expected.put("F", new HashSet<>(Arrays.asList("A", "B", "C", "D", "E", "G")));
        expected.put("G", new HashSet<>(Arrays.asList("A", "B", "C", "D", "E", "F")));

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected, processor.problem6(main.getClasses()));
    }

    public static class Holder {
        public final Object field;

        public Holder(Object field) { this.field = field; }
    }

    public static class A {
        public String s;

        public String debug() throws Exception {
            return this.s;
        }

    }

    public static class B extends A {
        public static String debug(B b) throws Exception {
            return b.s;
        }

        public String toString() {
            return null;
        }
    }

    public static class C extends B {
        public static String debug(String s) throws Exception {
            return "Wrong method String";
        }

        public static String debug(D d) throws Exception {
            return "Wrong method D";
        }

        public static String debug(B b) throws Exception {
            return "Correct method!";
        }

    }

    public static class D {
        public static String debug(Object o) throws Exception {
            throw new Exception();
        }
    }

    public static class E {
        public String toString() {
            return null;
        }
    }

    public static class F {
        public String toString() {
            return null;
        }
    }
}
