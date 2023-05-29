package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class Test09_TransitivelyInheritedMethods {

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


    public static class A {
        public void inherited() { System.out.println("A.inherited()"); }
        public void overriden() { System.out.println("A.overriden()"); }
    }

    public static class B extends A {
        public void overriden() { System.out.println("B.overriden()"); }
    }

    public static class C extends B {
        public void overriden() { System.out.println("C.overriden()"); }
    }

    public static class D extends C {
        public void overriden() { System.out.println("D.overriden()"); }
    }

    public static class E extends D {
        public void overriden() { System.out.println("E.overriden()"); }
    }

    public static class F extends E {
        public void overriden() { System.out.println("F.overriden()"); }
    }

    public static class G extends F {
        public void overriden() { System.out.println("G.overriden()"); }
    }
}
