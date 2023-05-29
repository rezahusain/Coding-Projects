package edu.uic.cs474.s23.a3;

import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class A3Solution implements StreamProcessor{
    @Override
    public List<Integer> problem1(List<Integer> input) {

        return input
                .stream()
                .filter(s -> Integer.signum(s) == 1)
                .collect(Collectors.toList());
    }

    @Override
    public Map<Integer, HasId> problem2(List<HasId> input) {
        HashMap<Integer, HasId> result = new HashMap<>();
        input
                .stream()
                .forEach((s) -> result.put(s.getId(), s));
        return result;
    }

    @Override
    public Set<String> problem3(String[] array1, String[] array2) {
        Set<String> result;
        result =
        Arrays.stream(array1)
                .filter(s -> Arrays.asList(array2).contains(s))
                .collect(Collectors.toSet());
        return result;

    }

    @Override
    public Map<String, Long> problem4(List<List<String>> input) {
        long count = 0;
        Map<String, Long> result = new HashMap<>();
        List<String> merger;
        merger = input
                .stream()
                .flatMap(s -> s.stream())
                .collect(Collectors.toList());

        result = merger
                .stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        return result;
    }

    @Override
    public Set<Course> problem5(List<Semester> input) {
        Set<Course> result = new HashSet<>();
        List<Course> courses;
        result = input
                .stream()
                .flatMap(s -> s.courses.stream())
                .filter(s -> s.students > 20)
                .collect(Collectors.toSet());
        return result;
    }

    @Override
    public Map<String, Set<String>> problem6(List<ClassOrInterfaceDeclaration> input) {
        return null;
    }
}
