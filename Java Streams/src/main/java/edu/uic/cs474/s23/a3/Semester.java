package edu.uic.cs474.s23.a3;

import java.util.ArrayList;
import java.util.List;

enum season { FALL, SPRING, SUMMER }

public class Semester {
    int year;
    season time;
    List<Course> courses = new ArrayList<>();

    public Semester(int year, season s){
        this.year = year;
        this.time = s;
    }

    public void addCourse(Course c){
        courses.add(c);
    }
}

class Course{
    int number;
    String name;
    int students;

    public Course(int number, String name, int students){
        this.number = number;
        this.name = name;
        this.students = students;
    }

    public String toString(){
        return name + ": " + students + " students";
    }
}
