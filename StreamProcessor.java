package edu.uic.cs474.s23.a3;

import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;

import java.util.List;
import java.util.Map;
import java.util.Set;

public interface StreamProcessor {
    List<Integer> problem1(List<Integer> input);

    Map<Integer, HasId> problem2(List<HasId> input);

    Set<String> problem3(String[] array1, String[] array2);

    Map<String, Long> problem4(List<List<String>> input);

    Set<Course> problem5(List<Semester> input);

    Map<String, Set<String>> problem6(List<ClassOrInterfaceDeclaration> input);
}
