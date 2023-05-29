package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

import static edu.uic.cs474.s23.a3.Test03_CommonStrings.generateRandomString;
import static edu.uic.cs474.s23.a3.season.*;

public class Test07_DupClasses {

    @Test
    public void test01() {
        Semester fa21 = new Semester(2021, FALL);
        fa21.addCourse(new Course(12345, "CS 474", 60));
        fa21.addCourse(new Course(12443, "CS 476", 45));
        fa21.addCourse(new Course(12443, "CS 521", 20));
        Semester sp22 = new Semester(2022, SPRING);
        sp22.addCourse(new Course(51234, "CS 494", 15));
        sp22.addCourse(new Course(51234, "CS 476", 50));
        sp22.addCourse(new Course(51234, "CS 474", 90));

        Set<Course> expected = new HashSet<>();
        for (Course c : fa21.courses)
            if(c.students > 20) expected.add(c);
        for (Course c : sp22.courses)
            if(c.students > 20) expected.add(c);

        List<Semester> input = new ArrayList<>();
        input.add(fa21);
        input.add(sp22);

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected, processor.problem5(input));
    }

    @Test
    public void testRandom() {
        Random r = new Random();

        Semester s1 = new Semester(r.nextInt(2030), FALL);
        Semester s2 = new Semester(r.nextInt(2030), SPRING);
        Semester s3 = new Semester(r.nextInt(2030), SUMMER);

        Course[] source = new Course[6];
        for(int i = 0; i < source.length; i++)
            source[i] = new Course(r.nextInt(99999), generateRandomString(), r.nextInt(40));

        for(int i = 0; i < 4; i++){
            s1.addCourse(source[r.nextInt(source.length)]);
            s2.addCourse(source[r.nextInt(source.length)]);
            s3.addCourse(source[r.nextInt(source.length)]);
        }

        Set<Course> expected = new HashSet<>();
        for (Course c : s1.courses)
            if(c.students > 20) expected.add(c);
        for (Course c : s2.courses)
            if(c.students > 20) expected.add(c);
        for (Course c : s3.courses)
            if(c.students > 20) expected.add(c);

        List<Semester> input = new ArrayList<>();
        input.add(s1);
        input.add(s2);
        input.add(s3);

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected, processor.problem5(input));
    }
}
