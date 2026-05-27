# Simple Programming
Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file:
(https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys)

## ขั้นตอนในการ run
 1. ```cd zero-or-one```
 2. ```python read-file.py```
## Code
```python
count  =  0
zero  =  0
one  =  0
with  open('data.dat','r') as  file:
	content  =  file.read()
	for  line  in  content:
		if  line  ==  '\n':
			if  zero  %  3  ==  0  or  one  %  2  ==  0:
				count  +=  1
			zero  =  0
			one  =  0
		if  line  ==  '0':
			zero  +=  1
		elif  line  ==  '1':
			one  +=  1
print(count)
file.close()
```
Flag : `6662`

