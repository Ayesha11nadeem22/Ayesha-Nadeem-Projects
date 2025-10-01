#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include&quot;student.data.h&quot;
// Structure to represent student information
struct Student
{
char name[15];
char father_name[20];
char phone_no[30];
char grade[5];
char address[40];
int attendence;
int rollNumber;
float marks;
};
// Function to add student information
int addStudent(struct Student students, int count)
{
printf(&quot; \n ENTER STUDENT INFORMATION AS GIVEN \n&quot;);
printf(&quot;1.Enter student name: &quot;);
scanf_s(&quot;%s&quot;,&amp;students.name, 15);
printf(&quot;2.Enter student phone Number:&quot;);
scanf_s(&quot; %s&quot;, &amp;students.phone_no, 30);
printf(&quot;3.Enter the student Grade:&quot;);
scanf_s(&quot; %s&quot;, &amp;students.grade, 5);
printf(&quot;4.Enter student total marks: &quot;);
scanf_s(&quot;%f&quot;, &amp;students.marks);

printf(&quot;5.Enter Student Father Name:&quot;);
scanf_s(&quot;%s&quot;,&amp;students.father_name,20);
printf(&quot;6.Enter student roll number: &quot;);
scanf_s(&quot;%d&quot;,&amp;students.rollNumber);
printf(&quot;7.Enter Student Attendence:&quot;);
scanf_s(&quot;%d&quot;, &amp;students.attendence);
printf(&quot;8.Enter Student Home Address:&quot;);
scanf_s(&quot;%s&quot;, &amp;students.address, 40);

FILE* f;
fopen_s(&amp;f, &quot;C:\\student data\\abc.txt&quot;, &quot;a&quot;);
if (f == NULL)
{
printf(&quot;Error Opening File.......\n&quot;);
}
fprintf(f,&quot;%s %d %s %f %s %s %d %s&quot;,
students.name,students.rollNumber,students.phone_no,
students.marks, students.grade, students.address,
students.attendence,students.father_name);
fclose(f);
return (count)++;
}
// Function to display all student information
void displayStudents(struct Student students, int r)
{
printf(&quot;\nStudent Information:\n&quot;);
for (int i = 0; i &lt; r; i++)
{
printf(&quot;Name: %s\n&quot;, students.name);
printf(&quot;Father Name:%s&quot;, students.father_name);
printf(&quot;Roll Number: %d\n&quot;, students.rollNumber);
printf(&quot;Marks: %.2f\n&quot;, students.marks);
printf(&quot;Phone Number:%s&quot;, students.phone_no);
printf(&quot;Grade:%s&quot;, students.grade);

printf(&quot;Address:%s&quot;, students.address);
printf(&quot;Attendence:%d&quot;, students.attendence);
printf(&quot;\n&quot;);
printf(&quot;*******************************************\n&quot;);
}
}
int main()
{
int select,r;
int count = 0;
struct Student students[50];
do
{
printf(&quot; ***MENU OF STUDENT INFORMATION SYSTEM***\n&quot;);
printf(&quot;\n&quot;);
printf(&quot;Select 1 to add Students Information\n&quot;);
printf(&quot;Select 2 to Display Students Information\n&quot;);
printf(&quot;Select 3 to Exit\n&quot;);
printf(&quot;Select any one[1,2,3]: &quot;);
scanf_s(&quot;%d&quot;,&amp;select);

switch (select)
{
case 1:
if (count &lt; 50)
{
r=addStudent(students[50],count);
printf(&quot;Information added successfully!\n&quot;);
}
else
{
printf(&quot;Maximum number of students reached!\n&quot;);
}
break;
case 2:
displayStudents(students[50],r);
break;

case 3:
printf(&quot;Exiting the program. Goodbye!\n&quot;);
break;
default:
printf(&quot;Invalid choice. Please try again............\n&quot;);
}
} while (select != 3);
data();
return 0;
}
#pragma once
void data()
{
printf(&quot;PROGRAM RUNS SUCSESSFULLY&quot;);
}