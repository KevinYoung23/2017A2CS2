# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:27:49 2018

@author: Kevin Young
"""

class Course:
    def __init__(self, t, m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = Assessment 
        
    def addlesson(self, t, d, r):
        self.__NumberOfLessons = self.__NumberOfLessons + 1
        self.__CourseLesson.append(Lesson(t,d,r))
    
    def addassessment(self, t, m):
        self.__CourseAssessment = Assessment(t,m)
        
    def outputcoursedetails(self):
        print(self.__CourseTitle, "Maximum number: ", self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].outputdetails())
            

class Lesson:
    def __init__(self, t, d, r):
        self.__LessonTitle = t 
        self.__DurationMinutes = d 
        self.__RequiresLab = r

    def outputlessondetails(self):
        print(self.__LessonTitle)
        print(self.__DurationMinutes)       
        print()
        
class Assessment:
    def __init__(self, t, m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m
        
    def outputassessmentdetails(self):
         print(self.__AssessmentTitle)
         print("  Marks: ", self.__MaxMarks) 