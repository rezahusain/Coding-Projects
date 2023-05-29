package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class Test08_CommonMethods {

    @Test
    public void testCommon() {
        Main main = new Main();
        main.processClass("edu.uic.cs474.s23.a3.Test08_CommonMethods");

        Map<String, Set<String>> expected = new HashMap<>();
        expected.put("A", new HashSet<>(List.of("B")));
        expected.put("B", new HashSet<>(List.of("A", "C")));
        expected.put("C", new HashSet<>(List.of("B")));

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected, processor.problem6(main.getClasses()));
    }


    public static class A {
        public void method1() { }
    }

    public static class B {
        public void method1() { }
        public void method2() { }
    }

    public static class C {
        public void method2() { }
    }
}
