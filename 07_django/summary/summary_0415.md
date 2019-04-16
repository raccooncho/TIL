### DB

##### M : N Database

* Student ( 1 : M ) Enrollment ( N : 1 ) Lecture

```python
class Student(models.Model):
    name = models.CharField(max_length=30, default='No Name')
    
    
class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    
    
class Lecture(models.Model):
    title = models.CharField(max_length=100, default='No Name')
    students = models.ManyToManyField(Student)
```



##### 1 : 1 Database

* User ( 1 : 1 ) Profile

```python

```



