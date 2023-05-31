Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class rating:
...     def __init__(self, a, m, b):
...         self.a = a
...         self.m = m
...         self.b = b
... 
...     @property
...     def calc(self):
...         e = (self.a + 4 * self.m + self.b) / 6
...         sd = (self.b - self.a) / 6
...         ci_max = e + 2 * sd
...         ci_min = e - 2 * sd
... 
...         return ci_min, ci_max
... 
... 
... count_tasks = int(input('How many tasks do you want to solve?: '))
... 
... for i in range(0, count_tasks):
...     a = int(input('Enter 1st number: '))
...     m = int(input('Enter 2nd number: '))
...     b = int(input('Enter 3rd number: '))
... 
...     obj = rating(a, m, b)
... 
