!
p
i
p
 
i
n
s
t
a
l
l
 
p
a
n
d
a
s
 
n
u
m
p
y
 
m
a
t
p
l
o
t
l
i
b
 
s
e
a
b
o
r
n
 
s
c
i
p
y
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p


i
m
p
o
r
t
 
m
a
t
p
l
o
t
l
i
b
.
p
y
p
l
o
t
 
a
s
 
p
l
t


i
m
p
o
r
t
 
s
e
a
b
o
r
n
 
a
s
 
s
n
s


f
r
o
m
 
s
c
i
p
y
.
o
p
t
i
m
i
z
e
 
i
m
p
o
r
t
 
m
i
n
i
m
i
z
e


i
m
p
o
r
t
 
r
a
n
d
o
m


i
m
p
o
r
t
 
c
o
p
y
d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(
v
r
_
s
c
o
r
e
,
 
h
r
_
s
c
o
r
e
,
 
s
y
n
e
r
g
y
_
s
c
o
r
e
,
 
a
l
p
h
a
,
 
b
e
t
a
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
t
h
e
 
o
v
e
r
a
l
l
 
A
I
-
R
e
a
d
i
n
e
s
s
 
S
c
o
r
e
.
"
"
"


 
 
 
 
#
 
E
n
s
u
r
e
 
s
c
o
r
e
s
 
a
r
e
 
w
i
t
h
i
n
 
0
-
1
0
0


 
 
 
 
v
r
_
s
c
o
r
e
 
=
 
n
p
.
c
l
i
p
(
v
r
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)


 
 
 
 
h
r
_
s
c
o
r
e
 
=
 
n
p
.
c
l
i
p
(
h
r
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)


 
 
 
 
s
y
n
e
r
g
y
_
s
c
o
r
e
 
=
 
n
p
.
c
l
i
p
(
s
y
n
e
r
g
y
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)




 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
A
I
-
R


 
 
 
 
a
i
_
r
 
=
 
(
a
l
p
h
a
 
*
 
v
r
_
s
c
o
r
e
)
 
+
 
(
(
1
 
-
 
a
l
p
h
a
)
 
*
 
h
r
_
s
c
o
r
e
)
 
+
 
(
b
e
t
a
 
*
 
s
y
n
e
r
g
y
_
s
c
o
r
e
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
a
i
_
r
,
 
0
,
 
1
0
0
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y


p
r
i
n
t
(
f
"
T
e
s
t
 
A
I
-
R
 
s
c
o
r
e
:
 
{
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(
v
r
_
s
c
o
r
e
=
7
5
,
 
h
r
_
s
c
o
r
e
=
8
0
,
 
s
y
n
e
r
g
y
_
s
c
o
r
e
=
5
1
,
 
a
l
p
h
a
=
0
.
6
,
 
b
e
t
a
=
0
.
1
5
)
:
.
2
f
}
"
)
#
 
D
e
f
i
n
e
 
d
e
f
a
u
l
t
 
p
a
r
a
m
e
t
e
r
s
 
f
o
r
 
\
a
l
p
h
a
 
a
n
d
 
\
b
e
t
a


P
A
R
A
M
S
 
=
 
{


 
 
 
 
'
a
l
p
h
a
'
:
 
0
.
6
,


 
 
 
 
'
b
e
t
a
'
:
 
0
.
1
5
,


 
 
 
 
'
l
a
m
b
d
a
_
g
r
o
w
t
h
'
:
 
0
.
3
,


 
 
 
 
'
g
a
m
m
a
_
r
e
g
i
o
n
a
l
'
:
 
0
.
2
,


 
 
 
 
'
h
r
_
b
a
s
e
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
w
e
i
g
h
t
'
:
 
0
.
3
0
,


 
 
 
 
 
 
 
 
'
j
o
b
_
g
r
o
w
t
h
_
w
e
i
g
h
t
'
:
 
0
.
3
0
,


 
 
 
 
 
 
 
 
'
w
a
g
e
_
p
r
e
m
i
u
m
_
w
e
i
g
h
t
'
:
 
0
.
2
5
,


 
 
 
 
 
 
 
 
'
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
_
w
e
i
g
h
t
'
:
 
0
.
1
5


 
 
 
 
}
,


 
 
 
 
'
t
h
e
t
a
_
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
w
e
i
g
h
t
'
:
 
0
.
3
0
,


 
 
 
 
 
 
 
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
w
e
i
g
h
t
'
:
 
0
.
3
5
,


 
 
 
 
 
 
 
 
'
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
w
e
i
g
h
t
'
:
 
0
.
2
0
,


 
 
 
 
 
 
 
 
'
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
w
e
i
g
h
t
'
:
 
0
.
1
5


 
 
 
 
}
,


 
 
 
 
'
g
a
m
m
a
_
e
x
p
e
r
i
e
n
c
e
_
d
e
c
a
y
'
:
 
0
.
1
5
,


 
 
 
 
'
d
o
m
a
i
n
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
p
o
r
t
f
o
l
i
o
_
w
e
i
g
h
t
'
:
 
0
.
4
,


 
 
 
 
 
 
 
 
'
r
e
c
o
g
n
i
t
i
o
n
_
w
e
i
g
h
t
'
:
 
0
.
3
,


 
 
 
 
 
 
 
 
'
c
r
e
d
e
n
t
i
a
l
s
_
w
e
i
g
h
t
'
:
 
0
.
3


 
 
 
 
}
,


 
 
 
 
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
4
5
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
3
5
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
2
0


 
 
 
 
}


}




#
 
I
n
i
t
i
a
l
i
z
e
 
p
l
a
c
e
h
o
l
d
e
r
 
v
a
l
u
e
s
 
f
o
r
 
V
R
,
 
H
R
R
,
 
a
n
d
 
S
y
n
e
r
g
y
%


v
r
_
p
l
a
c
e
h
o
l
d
e
r
 
=
 
7
5


h
r
_
p
l
a
c
e
h
o
l
d
e
r
 
=
 
8
0


s
y
n
e
r
g
y
_
p
l
a
c
e
h
o
l
d
e
r
 
=
 
5
1
.
0




#
 
E
x
e
c
u
t
e
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
 
w
i
t
h
 
t
h
e
s
e
 
p
l
a
c
e
h
o
l
d
e
r
 
v
a
l
u
e
s


f
i
n
a
l
_
a
i
_
r
_
p
l
a
c
e
h
o
l
d
e
r
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(
v
r
_
p
l
a
c
e
h
o
l
d
e
r
,
 
h
r
_
p
l
a
c
e
h
o
l
d
e
r
,
 
s
y
n
e
r
g
y
_
p
l
a
c
e
h
o
l
d
e
r
,
 
P
A
R
A
M
S
[
'
a
l
p
h
a
'
]
,
 
P
A
R
A
M
S
[
'
b
e
t
a
'
]
)




p
r
i
n
t
(
f
"
P
l
a
c
e
h
o
l
d
e
r
 
V
^
R
:
 
{
v
r
_
p
l
a
c
e
h
o
l
d
e
r
}
"
)


p
r
i
n
t
(
f
"
P
l
a
c
e
h
o
l
d
e
r
 
H
R
^
R
:
 
{
h
r
_
p
l
a
c
e
h
o
l
d
e
r
}
"
)


p
r
i
n
t
(
f
"
P
l
a
c
e
h
o
l
d
e
r
 
S
y
n
e
r
g
y
%
:
 
{
s
y
n
e
r
g
y
_
p
l
a
c
e
h
o
l
d
e
r
}
"
)


p
r
i
n
t
(
f
"
C
a
l
c
u
l
a
t
e
d
 
A
I
-
R
 
w
i
t
h
 
p
l
a
c
e
h
o
l
d
e
r
 
v
a
l
u
e
s
:
 
{
f
i
n
a
l
_
a
i
_
r
_
p
l
a
c
e
h
o
l
d
e
r
:
.
2
f
}
"
)
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p


i
m
p
o
r
t
 
p
y
t
e
s
t


i
m
p
o
r
t
 
r
a
n
d
o
m




#
 
T
h
e
 
f
u
n
c
t
i
o
n
s
 
t
o
 
b
e
 
t
e
s
t
e
d
 
a
r
e
 
d
e
f
i
n
e
d
 
h
e
r
e
 
w
i
t
h
i
n
 
t
h
e
 
t
e
s
t
 
f
i
l
e
.


#
 
T
h
i
s
 
e
n
s
u
r
e
s
 
t
e
s
t
s
 
a
r
e
 
s
e
l
f
-
c
o
n
t
a
i
n
e
d
 
a
n
d
 
r
u
n
 
a
g
a
i
n
s
t
 
a
 
c
o
n
s
i
s
t
e
n
t
 
v
e
r
s
i
o
n
 
o
f
 
t
h
e
 
f
u
n
c
t
i
o
n
s
.




d
e
f
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
n
u
m
_
e
m
p
l
o
y
e
e
s
=
5
0
)
:


 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
{


 
 
 
 
 
 
 
 
'
e
m
p
l
o
y
e
e
_
i
d
'
:
 
[
f
'
E
M
P
{
i
:
0
3
d
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
n
u
m
_
e
m
p
l
o
y
e
e
s
)
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
r
o
l
e
'
:
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
[
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
,
 
'
M
L
 
E
n
g
i
n
e
e
r
'
,
 
'
A
I
 
E
t
h
i
c
i
s
t
'
,
 
'
B
u
s
i
n
e
s
s
 
A
n
a
l
y
s
t
'
,
 
'
H
R
 
S
p
e
c
i
a
l
i
s
t
'
]
,
 
k
=
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
e
p
a
r
t
m
e
n
t
'
:
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
[
'
R
&
D
'
,
 
'
E
n
g
i
n
e
e
r
i
n
g
'
,
 
'
H
R
'
,
 
'
M
a
r
k
e
t
i
n
g
'
,
 
'
F
i
n
a
n
c
e
'
]
,
 
k
=
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
0
,
 
2
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
e
d
u
c
a
t
i
o
n
_
l
e
v
e
l
'
:
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
[
'
H
S
+
C
o
u
r
s
e
w
o
r
k
'
,
 
'
A
s
s
o
c
i
a
t
e
\
'
s
/
C
e
r
t
i
f
i
c
a
t
e
'
,
 
'
B
a
c
h
e
l
o
r
\
'
s
'
,
 
'
M
a
s
t
e
r
\
'
s
'
,
 
'
P
h
D
'
]
,
 
k
=
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
2
0
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
4
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
5
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
7
,
 
1
.
2
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,
 
#
 
R
e
l
a
t
i
v
e
 
t
o
 
w
i
t
h
o
u
t
 
A
I


 
 
 
 
 
 
 
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
5
,
 
1
.
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
i
m
e
_
w
i
t
h
o
u
t
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
1
.
0
,
 
1
.
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,
 
#
 
R
e
l
a
t
i
v
e
 
t
o
 
w
i
t
h
 
A
I


 
 
 
 
 
 
 
 
'
t
i
m
e
_
w
i
t
h
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
7
,
 
1
.
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
e
r
r
o
r
s
_
c
a
u
g
h
t
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
5
,
 
2
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
o
t
a
l
_
a
i
_
e
r
r
o
r
s
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
1
5
,
 
3
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
p
p
r
o
p
r
i
a
t
e
_
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
1
0
,
 
2
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
o
t
a
l
_
d
e
c
i
s
i
o
n
s
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
2
0
,
 
3
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
0
5
,
 
0
.
2
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
h
o
u
r
s
_
i
n
v
e
s
t
e
d
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
5
0
,
 
5
0
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
p
o
r
t
f
o
l
i
o
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
2
0
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
r
e
c
o
g
n
i
t
i
o
n
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
1
0
,
 
8
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
c
r
e
d
e
n
t
i
a
l
s
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
c
o
g
n
i
t
i
v
e
_
f
l
e
x
i
b
i
l
i
t
y
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
4
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
s
o
c
i
a
l
_
e
m
o
t
i
o
n
a
l
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
s
t
r
a
t
e
g
i
c
_
c
a
r
e
e
r
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
5
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)


 
 
 
 
}


 
 
 
 
#
 
A
d
d
 
g
e
n
e
r
i
c
 
s
k
i
l
l
s
 
f
o
r
 
s
k
i
l
l
 
m
a
t
c
h


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
]
 
=
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
0
,
 
1
0
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
 
#
 
C
o
r
r
e
c
t
e
d
 
s
y
n
t
a
x
 
f
o
r
 
i
n
n
e
r
 
s
t
r
i
n
g
 
l
i
t
e
r
a
l




 
 
 
 
d
f
 
=
 
p
d
.
D
a
t
a
F
r
a
m
e
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)




 
 
 
 
#
 
N
o
r
m
a
l
i
z
e
 
s
c
o
r
e
s
 
t
o
 
0
-
1
0
0
 
w
h
e
r
e
 
a
p
p
l
i
c
a
b
l
e
 
(
t
h
e
s
e
 
a
r
e
 
r
a
w
 
i
n
p
u
t
s
)


 
 
 
 
d
f
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
]
 
=
 
(
d
f
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
'
]
 
/
 
d
f
[
'
t
o
t
a
l
_
a
i
_
e
r
r
o
r
s
'
]
 
*
 
1
0
0
)
.
f
i
l
l
n
a
(
0
)


 
 
 
 
d
f
[
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
]
 
=
 
(
d
f
[
'
a
p
p
r
o
p
r
i
a
t
e
_
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
'
]
 
/
 
d
f
[
'
t
o
t
a
l
_
d
e
c
i
s
i
o
n
s
'
]
 
*
 
1
0
0
)
.
f
i
l
l
n
a
(
0
)




 
 
 
 
#
 
E
n
s
u
r
e
 
n
o
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
f
o
r
 
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
 
a
n
d
 
t
i
m
e
_
w
i
t
h
_
a
i


 
 
 
 
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
_
s
a
f
e
'
]
 
=
 
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
'
]
.
r
e
p
l
a
c
e
(
0
,
 
n
p
.
n
a
n
)


 
 
 
 
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
_
s
a
f
e
'
]
 
=
 
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
'
]
.
r
e
p
l
a
c
e
(
0
,
 
n
p
.
n
a
n
)




 
 
 
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
 
=
 
(
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
_
a
i
'
]
 
/
 
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
_
s
a
f
e
'
]
)
 
*
 
\


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(
d
f
[
'
t
i
m
e
_
w
i
t
h
o
u
t
_
a
i
'
]
 
/
 
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
_
s
a
f
e
'
]
)


 
 
 
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
 
=
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
.
f
i
l
l
n
a
(
0
)
 
#
 
F
i
l
l
 
N
a
N
 
i
f
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
o
c
c
u
r
r
e
d




 
 
 
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
]
 
=
 
n
p
.
c
l
i
p
(
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
 
*
 
5
0
,
 
0
,
 
1
0
0
)
 
#
 
S
c
a
l
e
 
a
n
d
 
c
l
i
p
 
f
o
r
 
i
n
i
t
i
a
l
 
S
_
i
2




 
 
 
 
r
e
t
u
r
n
 
d
f




d
e
f
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
(
)
:


 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
 
=
 
{


 
 
 
 
 
 
 
 
'
o
c
c
u
p
a
t
i
o
n
'
:
 
[
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
,
 
'
M
L
 
E
n
g
i
n
e
e
r
'
,
 
'
A
I
 
E
t
h
i
c
i
s
t
'
,
 
'
B
u
s
i
n
e
s
s
 
A
n
a
l
y
s
t
'
,
 
'
H
R
 
S
p
e
c
i
a
l
i
s
t
'
]
,


 
 
 
 
 
 
 
 
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l
'
:
 
[
8
5
,
 
9
0
,
 
7
5
,
 
6
0
,
 
5
0
]
,


 
 
 
 
 
 
 
 
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
'
:
 
[
5
0
0
0
,
 
4
0
0
0
,
 
1
0
0
0
,
 
1
5
0
0
0
,
 
1
2
0
0
0
]
,


 
 
 
 
 
 
 
 
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
_
p
l
u
s
_
1
0
'
:
 
[
8
0
0
0
,
 
7
5
0
0
,
 
2
0
0
0
,
 
1
6
0
0
0
,
 
1
1
0
0
0
]
,


 
 
 
 
 
 
 
 
'
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
'
:
 
[
1
4
0
0
0
0
,
 
1
5
0
0
0
0
,
 
1
2
0
0
0
0
,
 
9
0
0
0
0
,
 
8
0
0
0
0
]
,


 
 
 
 
 
 
 
 
'
m
e
d
i
a
n
_
w
a
g
e
'
:
 
[
1
1
0
0
0
0
,
 
1
2
0
0
0
0
,
 
1
0
0
0
0
0
,
 
7
5
0
0
0
,
 
6
5
0
0
0
]
,


 
 
 
 
 
 
 
 
'
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
:
 
[
1
8
,
 
1
8
,
 
1
6
,
 
1
6
,
 
1
4
]
,


 
 
 
 
 
 
 
 
'
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
:
 
[
3
,
 
4
,
 
2
,
 
2
,
 
1
]
,


 
 
 
 
 
 
 
 
'
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
'
:
 
[
0
.
8
,
 
0
.
9
,
 
0
.
7
,
 
0
.
6
,
 
0
.
5
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
p
o
s
t
i
n
g
s
_
c
u
r
r
e
n
t
_
m
o
n
t
h
'
:
 
[
1
2
0
,
 
1
1
0
,
 
4
0
,
 
8
0
,
 
7
0
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
p
o
s
t
i
n
g
s
_
p
r
e
v
_
m
o
n
t
h
'
:
 
[
1
0
0
,
 
1
0
0
,
 
3
5
,
 
8
5
,
 
7
5
]
,


 
 
 
 
 
 
 
 
'
n
a
t
i
o
n
a
l
_
a
v
g
_
d
e
m
a
n
d
'
:
 
[
1
0
0
,
 
1
0
0
,
 
1
0
0
,
 
1
0
0
,
 
1
0
0
]


 
 
 
 
}


 
 
 
 
#
 
A
d
d
 
r
e
q
u
i
r
e
d
 
s
k
i
l
l
s
 
a
n
d
 
i
m
p
o
r
t
a
n
c
e


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
]
 
=
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
0
,
 
l
e
n
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
'
o
c
c
u
p
a
t
i
o
n
'
]
)
)
 
#
 
C
o
r
r
e
c
t
e
d
 
s
y
n
t
a
x
 
f
o
r
 
i
n
n
e
r
 
s
t
r
i
n
g
 
l
i
t
e
r
a
l


 
 
 
 
 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
]
 
=
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
1
,
 
1
.
0
,
 
l
e
n
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
'
o
c
c
u
p
a
t
i
o
n
'
]
)
)
 
#
 
C
o
r
r
e
c
t
e
d
 
s
y
n
t
a
x
 
f
o
r
 
i
n
n
e
r
 
s
t
r
i
n
g
 
l
i
t
e
r
a
l




 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
)




d
e
f
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
(
)
:


 
 
 
 
p
a
t
h
w
a
y
_
d
a
t
a
 
=
 
{


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
i
d
'
:
 
[
f
'
P
A
T
H
{
i
:
0
2
d
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
,
 
6
)
]
,


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
n
a
m
e
'
:
 
[
'
A
I
 
F
u
n
d
a
m
e
n
t
a
l
s
 
C
o
u
r
s
e
'
,
 
'
A
d
v
a
n
c
e
d
 
M
L
 
S
p
e
c
i
a
l
i
z
a
t
i
o
n
'
,
 
'
A
I
 
E
t
h
i
c
s
 
&
 
G
o
v
e
r
n
a
n
c
e
'
,
 
'
D
a
t
a
 
S
t
o
r
y
t
e
l
l
i
n
g
 
w
i
t
h
 
A
I
'
,
 
'
H
R
 
A
n
a
l
y
t
i
c
s
 
w
i
t
h
 
A
I
'
]
,


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
t
y
p
e
'
:
 
[
'
O
n
l
i
n
e
 
C
o
u
r
s
e
'
,
 
'
C
e
r
t
i
f
i
c
a
t
i
o
n
'
,
 
'
W
o
r
k
s
h
o
p
'
,
 
'
O
n
l
i
n
e
 
C
o
u
r
s
e
'
,
 
'
C
e
r
t
i
f
i
c
a
t
i
o
n
'
]
,


 
 
 
 
 
 
 
 
'
c
o
s
t
'
:
 
[
5
0
0
,
 
2
0
0
0
,
 
1
0
0
0
,
 
3
0
0
,
 
7
5
0
]
,


 
 
 
 
 
 
 
 
'
t
i
m
e
_
h
o
u
r
s
'
:
 
[
4
0
,
 
1
6
0
,
 
8
0
,
 
3
0
,
 
6
0
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
:
 
[
1
0
,
 
2
5
,
 
5
,
 
3
,
 
5
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
:
 
[
5
,
 
1
0
,
 
1
5
,
 
8
,
 
1
2
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
:
 
[
5
,
 
5
,
 
1
0
,
 
7
,
 
8
]


 
 
 
 
}


 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
p
a
t
h
w
a
y
_
d
a
t
a
)






#
 
P
y
t
e
s
t
 
U
n
i
t
 
T
e
s
t
s


#
 
T
o
 
e
n
s
u
r
e
 
r
e
p
r
o
d
u
c
i
b
i
l
i
t
y
,
 
s
e
t
 
a
 
s
e
e
d
 
f
o
r
 
n
u
m
p
y
 
a
n
d
 
r
a
n
d
o
m


@
p
y
t
e
s
t
.
f
i
x
t
u
r
e
(
a
u
t
o
u
s
e
=
T
r
u
e
)


d
e
f
 
s
e
t
_
r
a
n
d
o
m
_
s
e
e
d
(
)
:


 
 
 
 
n
p
.
r
a
n
d
o
m
.
s
e
e
d
(
4
2
)


 
 
 
 
r
a
n
d
o
m
.
s
e
e
d
(
4
2
)






d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
_
s
t
r
u
c
t
u
r
e
(
)
:


 
 
 
 
d
f
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
1
0
)


 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
d
f
,
 
p
d
.
D
a
t
a
F
r
a
m
e
)


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
d
f
)
 
=
=
 
1
0




 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
 
=
 
[


 
 
 
 
 
 
 
 
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
d
e
p
a
r
t
m
e
n
t
'
,
 
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
,
 
'
e
d
u
c
a
t
i
o
n
_
l
e
v
e
l
'
,


 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
,
 
'
t
o
o
l
s
_
s
c
o
r
e
'
,
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
,
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
,


 
 
 
 
 
 
 
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
_
a
i
'
,
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
'
,
 
'
t
i
m
e
_
w
i
t
h
o
u
t
_
a
i
'
,


 
 
 
 
 
 
 
 
'
t
i
m
e
_
w
i
t
h
_
a
i
'
,
 
'
e
r
r
o
r
s
_
c
a
u
g
h
t
'
,
 
'
t
o
t
a
l
_
a
i
_
e
r
r
o
r
s
'
,


 
 
 
 
 
 
 
 
'
a
p
p
r
o
p
r
i
a
t
e
_
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
'
,
 
'
t
o
t
a
l
_
d
e
c
i
s
i
o
n
s
'
,
 
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
,


 
 
 
 
 
 
 
 
'
h
o
u
r
s
_
i
n
v
e
s
t
e
d
'
,
 
'
d
o
m
a
i
n
_
p
o
r
t
f
o
l
i
o
_
s
c
o
r
e
'
,
 
'
d
o
m
a
i
n
_
r
e
c
o
g
n
i
t
i
o
n
_
s
c
o
r
e
'
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
c
r
e
d
e
n
t
i
a
l
s
_
s
c
o
r
e
'
,
 
'
a
d
a
p
t
i
v
e
_
c
o
g
n
i
t
i
v
e
_
f
l
e
x
i
b
i
l
i
t
y
'
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
s
o
c
i
a
l
_
e
m
o
t
i
o
n
a
l
'
,
 
'
a
d
a
p
t
i
v
e
_
s
t
r
a
t
e
g
i
c
_
c
a
r
e
e
r
'


 
 
 
 
]


 
 
 
 
#
 
A
d
d
 
g
e
n
e
r
i
c
 
s
k
i
l
l
 
c
o
l
u
m
n
s


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
.
a
p
p
e
n
d
(
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
)


 
 
 
 
#
 
A
d
d
 
d
e
r
i
v
e
d
 
c
o
l
u
m
n
s
,
 
i
n
c
l
u
d
i
n
g
 
t
h
e
 
n
e
w
 
s
a
f
e
 
c
o
l
u
m
n
s


 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
.
e
x
t
e
n
d
(
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
,
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
,
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
_
s
a
f
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
t
i
m
e
_
w
i
t
h
_
a
i
_
s
a
f
e
'
,
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
,
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
]
)




 
 
 
 
a
s
s
e
r
t
 
a
l
l
(
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
 
f
o
r
 
c
o
l
 
i
n
 
e
x
p
e
c
t
e
d
_
c
o
l
s
)


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
.
n
u
n
i
q
u
e
(
)
 
=
=
 
1
0




d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
_
e
d
g
e
_
c
a
s
e
s
(
)
:


 
 
 
 
d
f
_
z
e
r
o
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
0
)


 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
d
f
_
z
e
r
o
,
 
p
d
.
D
a
t
a
F
r
a
m
e
)


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
d
f
_
z
e
r
o
)
 
=
=
 
0


 
 
 
 
#
 
E
n
s
u
r
e
 
c
o
l
u
m
n
s
 
a
r
e
 
s
t
i
l
l
 
d
e
f
i
n
e
d
 
e
v
e
n
 
w
i
t
h
 
n
o
 
r
o
w
s
 
(
b
y
 
c
h
e
c
k
i
n
g
 
i
f
 
c
o
l
u
m
n
s
 
e
x
i
s
t
 
a
n
d
 
a
r
e
 
o
f
 
o
b
j
e
c
t
 
t
y
p
e
 
f
o
r
 
s
t
r
i
n
g
 
c
o
l
s
)


 
 
 
 
a
s
s
e
r
t
 
'
e
m
p
l
o
y
e
e
_
i
d
'
 
i
n
 
d
f
_
z
e
r
o
.
c
o
l
u
m
n
s


 
 
 
 
a
s
s
e
r
t
 
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
 
i
n
 
d
f
_
z
e
r
o
.
c
o
l
u
m
n
s






 
 
 
 
d
f
_
o
n
e
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
1
)


 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
d
f
_
o
n
e
,
 
p
d
.
D
a
t
a
F
r
a
m
e
)


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
d
f
_
o
n
e
)
 
=
=
 
1


 
 
 
 
a
s
s
e
r
t
 
d
f
_
o
n
e
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
.
i
l
o
c
[
0
]
 
=
=
 
'
E
M
P
0
0
0
'




d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
_
v
a
l
u
e
_
r
a
n
g
e
s
(
)
:


 
 
 
 
d
f
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
1
0
0
)




 
 
 
 
#
 
C
h
e
c
k
 
n
o
r
m
a
l
i
z
e
d
 
s
c
o
r
e
s
 
a
r
e
 
w
i
t
h
i
n
 
[
0
,
 
1
0
0
]


 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
,
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
,
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
]
:


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
d
f
[
c
o
l
]
.
m
i
n
(
)
 
>
=
 
0


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
d
f
[
c
o
l
]
.
m
a
x
(
)
 
<
=
 
1
0
0


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
o
t
 
d
f
[
c
o
l
]
.
i
s
n
u
l
l
(
)
.
a
n
y
(
)
 
#
 
N
o
 
N
a
N
s




 
 
 
 
#
 
C
h
e
c
k
 
r
a
w
 
s
c
o
r
e
s
 
f
o
r
 
t
y
p
i
c
a
l
 
r
a
n
g
e
s


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
]
.
m
i
n
(
)
 
>
=
 
0


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
]
.
m
a
x
(
)
 
<
 
2
0


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
]
.
m
i
n
(
)
 
>
=
 
3
0


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
]
.
m
a
x
(
)
 
<
=
 
9
5
 
#
 
m
a
x
 
p
o
s
s
i
b
l
e
 
f
o
r
 
r
a
n
d
i
n
t
(
3
0
,
 
9
5
)
 
i
s
 
9
4




 
 
 
 
#
 
C
h
e
c
k
 
r
a
t
i
o
s
 
a
r
e
 
p
o
s
i
t
i
v
e
 
(
s
h
o
u
l
d
 
b
e
 
f
o
r
 
t
h
e
 
o
r
i
g
i
n
a
l
 
v
a
l
u
e
s
,
 
b
e
f
o
r
e
 
p
o
t
e
n
t
i
a
l
 
d
i
v
i
s
i
o
n
s
 
b
y
 
z
e
r
o
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
_
a
i
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
t
i
m
e
_
w
i
t
h
o
u
t
_
a
i
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
'
]
 
>
 
0
)
.
a
l
l
(
)




 
 
 
 
#
 
T
e
s
t
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
h
a
n
d
l
i
n
g
 
i
n
 
n
o
r
m
a
l
i
z
e
d
 
s
c
o
r
e
s
 
b
y
 
e
n
s
u
r
i
n
g
 
f
i
n
i
t
e
 
r
e
s
u
l
t
s


 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
f
i
n
i
t
e
(
d
f
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
]
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
f
i
n
i
t
e
(
d
f
[
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
]
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
f
i
n
i
t
e
(
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
]
)
.
a
l
l
(
)






d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
_
s
t
r
u
c
t
u
r
e
(
)
:


 
 
 
 
d
f
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
(
)


 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
d
f
,
 
p
d
.
D
a
t
a
F
r
a
m
e
)


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
d
f
)
 
=
=
 
5
 
#
 
F
i
x
e
d
 
n
u
m
b
e
r
 
o
f
 
o
c
c
u
p
a
t
i
o
n
s




 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
 
=
 
[


 
 
 
 
 
 
 
 
'
o
c
c
u
p
a
t
i
o
n
'
,
 
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l
'
,
 
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
'
,
 
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
_
p
l
u
s
_
1
0
'
,


 
 
 
 
 
 
 
 
'
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
'
,
 
'
m
e
d
i
a
n
_
w
a
g
e
'
,
 
'
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
,
 
'
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
,


 
 
 
 
 
 
 
 
'
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
'
,
 
'
j
o
b
_
p
o
s
t
i
n
g
s
_
c
u
r
r
e
n
t
_
m
o
n
t
h
'
,
 
'
j
o
b
_
p
o
s
t
i
n
g
s
_
p
r
e
v
_
m
o
n
t
h
'
,


 
 
 
 
 
 
 
 
'
n
a
t
i
o
n
a
l
_
a
v
g
_
d
e
m
a
n
d
'


 
 
 
 
]


 
 
 
 
#
 
A
d
d
 
g
e
n
e
r
i
c
 
s
k
i
l
l
 
a
n
d
 
i
m
p
o
r
t
a
n
c
e
 
c
o
l
u
m
n
s


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
.
a
p
p
e
n
d
(
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
)


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
.
a
p
p
e
n
d
(
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
)




 
 
 
 
a
s
s
e
r
t
 
a
l
l
(
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
 
f
o
r
 
c
o
l
 
i
n
 
e
x
p
e
c
t
e
d
_
c
o
l
s
)


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
o
c
c
u
p
a
t
i
o
n
'
]
.
n
u
n
i
q
u
e
(
)
 
=
=
 
5




d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
_
v
a
l
u
e
_
r
a
n
g
e
s
(
)
:


 
 
 
 
d
f
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
(
)




 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l
'
]
.
m
i
n
(
)
 
>
=
 
5
0


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l
'
]
.
m
a
x
(
)
 
<
=
 
9
0


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
'
]
 
>
 
d
f
[
'
m
e
d
i
a
n
_
w
a
g
e
'
]
)
.
a
l
l
(
)
 
#
 
A
I
-
s
k
i
l
l
e
d
 
w
a
g
e
 
s
h
o
u
l
d
 
b
e
 
h
i
g
h
e
r


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
]
 
>
=
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
'
]
.
m
i
n
(
)
 
>
=
 
0
.
5


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
'
]
.
m
a
x
(
)
 
<
=
 
0
.
9




 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
d
f
[
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
]
.
m
i
n
(
)
 
>
=
 
3
0


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
d
f
[
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
]
.
m
a
x
(
)
 
<
=
 
9
0


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
d
f
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
]
.
m
i
n
(
)
 
>
=
 
0
.
1


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
d
f
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
]
.
m
a
x
(
)
 
<
=
 
1
.
0






d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
_
s
t
r
u
c
t
u
r
e
(
)
:


 
 
 
 
d
f
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
(
)


 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
d
f
,
 
p
d
.
D
a
t
a
F
r
a
m
e
)


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
d
f
)
 
=
=
 
5
 
#
 
F
i
x
e
d
 
n
u
m
b
e
r
 
o
f
 
p
a
t
h
w
a
y
s




 
 
 
 
e
x
p
e
c
t
e
d
_
c
o
l
s
 
=
 
[


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
i
d
'
,
 
'
p
a
t
h
w
a
y
_
n
a
m
e
'
,
 
'
p
a
t
h
w
a
y
_
t
y
p
e
'
,
 
'
c
o
s
t
'
,
 
'
t
i
m
e
_
h
o
u
r
s
'
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
,
 
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
,
 
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'


 
 
 
 
]


 
 
 
 
a
s
s
e
r
t
 
a
l
l
(
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
 
f
o
r
 
c
o
l
 
i
n
 
e
x
p
e
c
t
e
d
_
c
o
l
s
)


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
p
a
t
h
w
a
y
_
i
d
'
]
.
n
u
n
i
q
u
e
(
)
 
=
=
 
5


 
 
 
 
a
s
s
e
r
t
 
d
f
[
'
p
a
t
h
w
a
y
_
n
a
m
e
'
]
.
n
u
n
i
q
u
e
(
)
 
=
=
 
5




d
e
f
 
t
e
s
t
_
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
_
v
a
l
u
e
_
r
a
n
g
e
s
(
)
:


 
 
 
 
d
f
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
(
)




 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
c
o
s
t
'
]
 
>
=
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
t
i
m
e
_
h
o
u
r
s
'
]
 
>
=
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
]
 
>
 
0
)
.
a
l
l
(
)


 
 
 
 
a
s
s
e
r
t
 
(
d
f
[
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
]
 
>
 
0
)
.
a
l
l
(
)
#
 
C
a
l
l
 
t
h
e
 
d
a
t
a
 
g
e
n
e
r
a
t
i
o
n
 
f
u
n
c
t
i
o
n
s
 
t
o
 
c
r
e
a
t
e
 
t
h
e
 
D
a
t
a
F
r
a
m
e
s


d
f
_
e
m
p
l
o
y
e
e
s
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
n
u
m
_
e
m
p
l
o
y
e
e
s
=
5
0
)


d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
(
)


d
f
_
p
a
t
h
w
a
y
s
 
=
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
(
)




#
 
D
i
s
p
l
a
y
 
t
h
e
 
.
h
e
a
d
(
)
 
o
f
 
e
a
c
h
 
D
a
t
a
F
r
a
m
e


p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
.
h
e
a
d
(
)
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
.
h
e
a
d
(
)
)


p
r
i
n
t
(
"
\
n
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
h
e
a
d
(
)
:
"
)


p
r
i
n
t
(
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
h
e
a
d
(
)
)


p
r
i
n
t
(
"
\
n
d
f
_
p
a
t
h
w
a
y
s
.
h
e
a
d
(
)
:
"
)


p
r
i
n
t
(
d
f
_
p
a
t
h
w
a
y
s
.
h
e
a
d
(
)
)




#
 
P
r
i
n
t
 
t
h
e
 
P
A
R
A
M
S
 
d
i
c
t
i
o
n
a
r
y


p
r
i
n
t
(
"
\
n
G
l
o
b
a
l
 
P
A
R
A
M
S
 
d
i
c
t
i
o
n
a
r
y
:
"
)


p
r
i
n
t
(
P
A
R
A
M
S
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
i
_
e
n
h
a
n
c
e
m
e
n
t
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
A
I
-
E
n
h
a
n
c
e
m
e
n
t
 
P
o
t
e
n
t
i
a
l
 
f
o
r
 
a
 
g
i
v
e
n
 
o
c
c
u
p
a
t
i
o
n
.
"
"
"


 
 
 
 
#
 
D
i
r
e
c
t
l
y
 
e
x
t
r
a
c
t
 
t
h
e
 
p
r
e
-
a
g
g
r
e
g
a
t
e
d
 
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l


 
 
 
 
r
e
t
u
r
n
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l
'
]




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y


e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
i
l
o
c
[
0
]


p
r
i
n
t
(
f
"
T
e
s
t
 
A
I
-
E
n
h
a
n
c
e
m
e
n
t
 
P
o
t
e
n
t
i
a
l
 
f
o
r
 
{
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
[
'
o
c
c
u
p
a
t
i
o
n
'
]
}
:
 
{
c
a
l
c
u
l
a
t
e
_
a
i
_
e
n
h
a
n
c
e
m
e
n
t
(
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
)
:
.
2
f
}
"
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
j
o
b
_
g
r
o
w
t
h
_
n
o
r
m
a
l
i
z
e
d
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
n
o
r
m
a
l
i
z
e
d
 
j
o
b
 
g
r
o
w
t
h
 
p
r
o
j
e
c
t
i
o
n
 
f
o
r
 
a
n
 
o
c
c
u
p
a
t
i
o
n
.
"
"
"


 
 
 
 
c
u
r
r
e
n
t
_
j
o
b
s
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
'
]


 
 
 
 
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
1
0
_
y
e
a
r
s
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
_
p
l
u
s
_
1
0
'
]




 
 
 
 
i
f
 
c
u
r
r
e
n
t
_
j
o
b
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0
 
#
 
H
a
n
d
l
e
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o




 
 
 
 
r
a
w
_
g
r
o
w
t
h
_
r
a
t
e
 
=
 
(
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
1
0
_
y
e
a
r
s
 
-
 
c
u
r
r
e
n
t
_
j
o
b
s
)
 
/
 
c
u
r
r
e
n
t
_
j
o
b
s




 
 
 
 
#
 
N
o
r
m
a
l
i
z
e
 
t
o
 
[
0
,
 
1
0
0
]
 
u
s
i
n
g
 
t
h
e
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
a
t
i
o
n


 
 
 
 
#
 
G
r
o
w
t
h
 
r
a
t
e
 
r
a
n
g
e
 
f
o
r
 
n
o
r
m
a
l
i
z
a
t
i
o
n
:
 
g
 
\
i
n
 
[
-
0
.
5
,
 
1
.
5
]


 
 
 
 
#
 
-
0
.
5
 
m
a
p
s
 
t
o
 
0
,
 
1
.
5
 
m
a
p
s
 
t
o
 
1
0
0
.


 
 
 
 
n
o
r
m
a
l
i
z
e
d
_
g
r
o
w
t
h
 
=
 
n
p
.
c
l
i
p
(
(
(
r
a
w
_
g
r
o
w
t
h
_
r
a
t
e
 
+
 
0
.
5
)
 
/
 
2
.
0
)
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




 
 
 
 
r
e
t
u
r
n
 
r
a
w
_
g
r
o
w
t
h
_
r
a
t
e
,
 
n
o
r
m
a
l
i
z
e
d
_
g
r
o
w
t
h




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y


e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
i
l
o
c
[
0
]


r
a
w
_
g
r
o
w
t
h
,
 
n
o
r
m
a
l
i
z
e
d
_
g
r
o
w
t
h
 
=
 
c
a
l
c
u
l
a
t
e
_
j
o
b
_
g
r
o
w
t
h
_
n
o
r
m
a
l
i
z
e
d
(
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
)


p
r
i
n
t
(
f
"
T
e
s
t
 
J
o
b
 
G
r
o
w
t
h
 
f
o
r
 
{
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
[
'
o
c
c
u
p
a
t
i
o
n
'
]
}
:
 
R
a
w
=
{
r
a
w
_
g
r
o
w
t
h
:
.
2
%
}
,
 
N
o
r
m
a
l
i
z
e
d
=
{
n
o
r
m
a
l
i
z
e
d
_
g
r
o
w
t
h
:
.
2
f
}
"
)
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p


i
m
p
o
r
t
 
p
y
t
e
s
t


i
m
p
o
r
t
 
r
a
n
d
o
m




#
 
R
e
-
d
e
f
i
n
i
n
g
 
t
h
e
 
f
u
n
c
t
i
o
n
s
 
a
s
 
p
e
r
 
t
h
e
 
r
e
q
u
i
r
e
m
e
n
t
 
f
o
r
 
s
e
l
f
-
c
o
n
t
a
i
n
e
d
 
t
e
s
t
s
.


#
 
T
h
e
 
p
r
e
v
i
o
u
s
 
S
y
n
t
a
x
E
r
r
o
r
 
w
a
s
 
r
e
s
o
l
v
e
d
 
b
y
 
c
h
a
n
g
i
n
g
 
s
i
n
g
l
e
 
q
u
o
t
e
s
 
'
a
'
 
t
o
 
d
o
u
b
l
e
 
q
u
o
t
e
s
 
"
a
"
 
i
n
 
f
-
s
t
r
i
n
g
s
.


#
 
T
h
i
s
 
c
o
r
r
e
c
t
i
o
n
 
i
s
 
a
p
p
l
i
e
d
 
h
e
r
e
 
a
s
 
w
e
l
l
 
i
n
 
h
e
l
p
e
r
 
f
u
n
c
t
i
o
n
s
 
u
s
e
d
 
b
y
 
t
e
s
t
s
.




d
e
f
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
e
m
p
l
o
y
e
e
s
(
n
u
m
_
e
m
p
l
o
y
e
e
s
=
5
0
)
:


 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
{


 
 
 
 
 
 
 
 
'
e
m
p
l
o
y
e
e
_
i
d
'
:
 
[
f
'
E
M
P
{
i
:
0
3
d
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
n
u
m
_
e
m
p
l
o
y
e
e
s
)
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
r
o
l
e
'
:
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
[
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
,
 
'
M
L
 
E
n
g
i
n
e
e
r
'
,
 
'
A
I
 
E
t
h
i
c
i
s
t
'
,
 
'
B
u
s
i
n
e
s
s
 
A
n
a
l
y
s
t
'
,
 
'
H
R
 
S
p
e
c
i
a
l
i
s
t
'
]
,
 
k
=
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
e
p
a
r
t
m
e
n
t
'
:
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
[
'
R
&
D
'
,
 
'
E
n
g
i
n
e
e
r
i
n
g
'
,
 
'
H
R
'
,
 
'
M
a
r
k
e
t
i
n
g
'
,
 
'
F
i
n
a
n
c
e
'
]
,
 
k
=
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
0
,
 
2
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
e
d
u
c
a
t
i
o
n
_
l
e
v
e
l
'
:
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
[
'
H
S
+
C
o
u
r
s
e
w
o
r
k
'
,
 
'
A
s
s
o
c
i
a
t
e
\
'
s
/
C
e
r
t
i
f
i
c
a
t
e
'
,
 
'
B
a
c
h
e
l
o
r
\
'
s
'
,
 
'
M
a
s
t
e
r
\
'
s
'
,
 
'
P
h
D
'
]
,
 
k
=
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
2
0
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
4
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
5
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
7
,
 
1
.
2
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,
 
#
 
R
e
l
a
t
i
v
e
 
t
o
 
w
i
t
h
o
u
t
 
A
I


 
 
 
 
 
 
 
 
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
5
,
 
1
.
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
i
m
e
_
w
i
t
h
o
u
t
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
1
.
0
,
 
1
.
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,
 
#
 
R
e
l
a
t
i
v
e
 
t
o
 
w
i
t
h
 
A
I


 
 
 
 
 
 
 
 
'
t
i
m
e
_
w
i
t
h
_
a
i
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
7
,
 
1
.
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
e
r
r
o
r
s
_
c
a
u
g
h
t
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
5
,
 
2
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
o
t
a
l
_
a
i
_
e
r
r
o
r
s
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
1
5
,
 
3
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
p
p
r
o
p
r
i
a
t
e
_
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
1
0
,
 
2
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
t
o
t
a
l
_
d
e
c
i
s
i
o
n
s
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
2
0
,
 
3
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
0
5
,
 
0
.
2
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
h
o
u
r
s
_
i
n
v
e
s
t
e
d
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
5
0
,
 
5
0
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
p
o
r
t
f
o
l
i
o
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
2
0
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
r
e
c
o
g
n
i
t
i
o
n
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
1
0
,
 
8
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
c
r
e
d
e
n
t
i
a
l
s
_
s
c
o
r
e
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
c
o
g
n
i
t
i
v
e
_
f
l
e
x
i
b
i
l
i
t
y
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
4
0
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
s
o
c
i
a
l
_
e
m
o
t
i
o
n
a
l
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
s
t
r
a
t
e
g
i
c
_
c
a
r
e
e
r
'
:
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
5
,
 
9
5
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)


 
 
 
 
}


 
 
 
 
#
 
A
d
d
 
g
e
n
e
r
i
c
 
s
k
i
l
l
s
 
f
o
r
 
s
k
i
l
l
 
m
a
t
c
h


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
]
 
=
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
0
,
 
1
0
0
,
 
n
u
m
_
e
m
p
l
o
y
e
e
s
)




 
 
 
 
d
f
 
=
 
p
d
.
D
a
t
a
F
r
a
m
e
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)




 
 
 
 
#
 
N
o
r
m
a
l
i
z
e
 
s
c
o
r
e
s
 
t
o
 
0
-
1
0
0
 
w
h
e
r
e
 
a
p
p
l
i
c
a
b
l
e
 
(
t
h
e
s
e
 
a
r
e
 
r
a
w
 
i
n
p
u
t
s
)


 
 
 
 
#
 
H
a
n
d
l
e
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
g
r
a
c
e
f
u
l
l
y
,
 
t
h
o
u
g
h
 
w
i
t
h
 
r
a
n
d
i
n
t
 
r
a
n
g
e
s
,
 
i
t
'
s
 
u
n
l
i
k
e
l
y
 
t
o
t
a
l
_
a
i
_
e
r
r
o
r
s
/
t
o
t
a
l
_
d
e
c
i
s
i
o
n
s
 
a
r
e
 
0


 
 
 
 
d
f
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
]
 
=
 
(
d
f
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
'
]
 
/
 
d
f
[
'
t
o
t
a
l
_
a
i
_
e
r
r
o
r
s
'
]
 
*
 
1
0
0
)
.
f
i
l
l
n
a
(
0
)


 
 
 
 
d
f
[
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
]
 
=
 
(
d
f
[
'
a
p
p
r
o
p
r
i
a
t
e
_
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
'
]
 
/
 
d
f
[
'
t
o
t
a
l
_
d
e
c
i
s
i
o
n
s
'
]
 
*
 
1
0
0
)
.
f
i
l
l
n
a
(
0
)




 
 
 
 
#
 
E
n
s
u
r
e
 
n
o
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
f
o
r
 
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
 
a
n
d
 
t
i
m
e
_
w
i
t
h
_
a
i


 
 
 
 
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
_
s
a
f
e
'
]
 
=
 
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
'
]
.
r
e
p
l
a
c
e
(
0
,
 
n
p
.
n
a
n
)


 
 
 
 
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
_
s
a
f
e
'
]
 
=
 
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
'
]
.
r
e
p
l
a
c
e
(
0
,
 
n
p
.
n
a
n
)




 
 
 
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
 
=
 
(
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
_
a
i
'
]
 
/
 
d
f
[
'
o
u
t
p
u
t
_
q
u
a
l
i
t
y
_
w
i
t
h
o
u
t
_
a
i
_
s
a
f
e
'
]
)
 
*
 
\


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(
d
f
[
'
t
i
m
e
_
w
i
t
h
o
u
t
_
a
i
'
]
 
/
 
d
f
[
'
t
i
m
e
_
w
i
t
h
_
a
i
_
s
a
f
e
'
]
)


 
 
 
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
 
=
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
.
f
i
l
l
n
a
(
0
)
 
#
 
F
i
l
l
 
N
a
N
 
i
f
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
o
c
c
u
r
r
e
d




 
 
 
 
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
]
 
=
 
n
p
.
c
l
i
p
(
d
f
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
r
a
w
'
]
 
*
 
5
0
,
 
0
,
 
1
0
0
)
 
#
 
S
c
a
l
e
 
a
n
d
 
c
l
i
p
 
f
o
r
 
i
n
i
t
i
a
l
 
S
_
i
2




 
 
 
 
r
e
t
u
r
n
 
d
f




d
e
f
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
o
c
c
u
p
a
t
i
o
n
s
(
)
:


 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
 
=
 
{


 
 
 
 
 
 
 
 
'
o
c
c
u
p
a
t
i
o
n
'
:
 
[
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
,
 
'
M
L
 
E
n
g
i
n
e
e
r
'
,
 
'
A
I
 
E
t
h
i
c
i
s
t
'
,
 
'
B
u
s
i
n
e
s
s
 
A
n
a
l
y
s
t
'
,
 
'
H
R
 
S
p
e
c
i
a
l
i
s
t
'
]
,


 
 
 
 
 
 
 
 
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
p
o
t
e
n
t
i
a
l
'
:
 
[
8
5
,
 
9
0
,
 
7
5
,
 
6
0
,
 
5
0
]
,


 
 
 
 
 
 
 
 
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
'
:
 
[
5
0
0
0
,
 
4
0
0
0
,
 
1
0
0
0
,
 
1
5
0
0
0
,
 
1
2
0
0
0
]
,


 
 
 
 
 
 
 
 
'
p
r
o
j
e
c
t
e
d
_
j
o
b
s
_
t
_
p
l
u
s
_
1
0
'
:
 
[
8
0
0
0
,
 
7
5
0
0
,
 
2
0
0
0
,
 
1
6
0
0
0
,
 
1
1
0
0
0
]
,


 
 
 
 
 
 
 
 
'
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
'
:
 
[
1
4
0
0
0
0
,
 
1
5
0
0
0
0
,
 
1
2
0
0
0
0
,
 
9
0
0
0
0
,
 
8
0
0
0
0
]
,


 
 
 
 
 
 
 
 
'
m
e
d
i
a
n
_
w
a
g
e
'
:
 
[
1
1
0
0
0
0
,
 
1
2
0
0
0
0
,
 
1
0
0
0
0
0
,
 
7
5
0
0
0
,
 
6
5
0
0
0
]
,


 
 
 
 
 
 
 
 
'
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
:
 
[
1
8
,
 
1
8
,
 
1
6
,
 
1
6
,
 
1
4
]
,


 
 
 
 
 
 
 
 
'
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
:
 
[
3
,
 
4
,
 
2
,
 
2
,
 
1
]
,


 
 
 
 
 
 
 
 
'
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
'
:
 
[
0
.
8
,
 
0
.
9
,
 
0
.
7
,
 
0
.
6
,
 
0
.
5
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
p
o
s
t
i
n
g
s
_
c
u
r
r
e
n
t
_
m
o
n
t
h
'
:
 
[
1
2
0
,
 
1
1
0
,
 
4
0
,
 
8
0
,
 
7
0
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
p
o
s
t
i
n
g
s
_
p
r
e
v
_
m
o
n
t
h
'
:
 
[
1
0
0
,
 
1
0
0
,
 
3
5
,
 
8
5
,
 
7
5
]
,


 
 
 
 
 
 
 
 
'
n
a
t
i
o
n
a
l
_
a
v
g
_
d
e
m
a
n
d
'
:
 
[
1
0
0
,
 
1
0
0
,
 
1
0
0
,
 
1
0
0
,
 
1
0
0
]


 
 
 
 
}


 
 
 
 
#
 
A
d
d
 
r
e
q
u
i
r
e
d
 
s
k
i
l
l
s
 
a
n
d
 
i
m
p
o
r
t
a
n
c
e


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
:


 
 
 
 
 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
]
 
=
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
3
0
,
 
9
0
,
 
l
e
n
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
'
o
c
c
u
p
a
t
i
o
n
'
]
)
)


 
 
 
 
 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
]
 
=
 
n
p
.
r
a
n
d
o
m
.
u
n
i
f
o
r
m
(
0
.
1
,
 
1
.
0
,
 
l
e
n
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
[
'
o
c
c
u
p
a
t
i
o
n
'
]
)
)




 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
)




d
e
f
 
g
e
n
e
r
a
t
e
_
s
y
n
t
h
e
t
i
c
_
p
a
t
h
w
a
y
s
(
)
:


 
 
 
 
p
a
t
h
w
a
y
_
d
a
t
a
 
=
 
{


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
i
d
'
:
 
[
f
'
P
A
T
H
{
i
:
0
2
d
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
,
 
6
)
]
,


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
n
a
m
e
'
:
 
[
'
A
I
 
F
u
n
d
a
m
e
n
t
a
l
s
 
C
o
u
r
s
e
'
,
 
'
A
d
v
a
n
c
e
d
 
M
L
 
S
p
e
c
i
a
l
i
z
a
t
i
o
n
'
,
 
'
A
I
 
E
t
h
i
c
s
 
&
 
G
o
v
e
r
n
a
n
c
e
'
,
 
'
D
a
t
a
 
S
t
o
r
y
t
e
l
l
i
n
g
 
w
i
t
h
 
A
I
'
,
 
'
H
R
 
A
n
a
l
y
t
i
c
s
 
w
i
t
h
 
A
I
'
]
,


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
t
y
p
e
'
:
 
[
'
O
n
l
i
n
e
 
C
o
u
r
s
e
'
,
 
'
C
e
r
t
i
f
i
c
a
t
i
o
n
'
,
 
'
W
o
r
k
s
h
o
p
'
,
 
'
O
n
l
i
n
e
 
C
o
u
r
s
e
'
,
 
'
C
e
r
t
i
f
i
c
a
t
i
o
n
'
]
,


 
 
 
 
 
 
 
 
'
c
o
s
t
'
:
 
[
5
0
0
,
 
2
0
0
0
,
 
1
0
0
0
,
 
3
0
0
,
 
7
5
0
]
,


 
 
 
 
 
 
 
 
'
t
i
m
e
_
h
o
u
r
s
'
:
 
[
4
0
,
 
1
6
0
,
 
8
0
,
 
3
0
,
 
6
0
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
:
 
[
1
0
,
 
2
5
,
 
5
,
 
3
,
 
5
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
:
 
[
5
,
 
1
0
,
 
1
5
,
 
8
,
 
1
2
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
:
 
[
5
,
 
5
,
 
1
0
,
 
7
,
 
8
]


 
 
 
 
}


 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
p
a
t
h
w
a
y
_
d
a
t
a
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
w
a
g
e
_
p
r
e
m
i
u
m
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
w
a
g
e
 
p
r
e
m
i
u
m
 
f
o
r
 
a
n
 
o
c
c
u
p
a
t
i
o
n
.
"
"
"


 
 
 
 
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
'
]


 
 
 
 
m
e
d
i
a
n
_
w
a
g
e
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
m
e
d
i
a
n
_
w
a
g
e
'
]




 
 
 
 
i
f
 
m
e
d
i
a
n
_
w
a
g
e
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0




 
 
 
 
w
a
g
e
_
p
r
e
m
i
u
m
 
=
 
(
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
 
-
 
m
e
d
i
a
n
_
w
a
g
e
)
 
/
 
m
e
d
i
a
n
_
w
a
g
e


 
 
 
 
#
 
N
o
r
m
a
l
i
z
e
 
t
o
 
a
 
0
-
1
0
0
 
s
c
a
l
e
;
 
a
s
s
u
m
i
n
g
 
t
y
p
i
c
a
l
 
p
r
e
m
i
u
m
s
 
a
r
e
 
b
e
t
w
e
e
n
 
-
0
.
2
 
a
n
d
 
0
.
5


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
(
(
w
a
g
e
_
p
r
e
m
i
u
m
 
+
 
0
.
2
)
 
/
 
0
.
7
)
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
e
n
t
r
y
 
a
c
c
e
s
s
i
b
i
l
i
t
y
 
f
o
r
 
a
n
 
o
c
c
u
p
a
t
i
o
n
.
"
"
"


 
 
 
 
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
]


 
 
 
 
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
]




 
 
 
 
#
 
U
s
i
n
g
 
t
h
e
 
f
o
r
m
u
l
a
:
 
1
 
-
 
(
t
o
t
a
l
_
y
e
a
r
s
 
/
 
1
0
)
 
f
o
r
 
a
 
s
i
m
p
l
e
r
 
r
a
n
g
e
 
a
d
j
u
s
t
m
e
n
t


 
 
 
 
a
c
c
e
s
s
_
s
c
o
r
e
 
=
 
1
 
-
 
(
(
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
 
+
 
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
)
 
/
 
1
0
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
a
c
c
e
s
s
_
s
c
o
r
e
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)






#
 
P
y
t
e
s
t
 
u
n
i
t
 
t
e
s
t
s


c
l
a
s
s
 
T
e
s
t
H
R
R
C
o
m
p
o
n
e
n
t
s
:




 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
w
a
g
e
_
p
r
e
m
i
u
m
 
-
-
-


 
 
 
 
@
p
y
t
e
s
t
.
m
a
r
k
.
p
a
r
a
m
e
t
r
i
z
e
(
"
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
,
 
m
e
d
i
a
n
_
w
a
g
e
,
 
e
x
p
e
c
t
e
d
_
p
r
e
m
i
u
m
"
,
 
[


 
 
 
 
 
 
 
 
(
1
5
0
0
0
0
,
 
1
0
0
0
0
0
,
 
1
0
0
.
0
)
,


 
 
 
 
 
 
 
 
(
1
0
0
0
0
0
,
 
1
0
0
0
0
0
,
 
2
8
.
5
7
1
4
2
8
5
7
1
4
2
8
5
7
)
,


 
 
 
 
 
 
 
 
(
8
0
0
0
0
,
 
1
0
0
0
0
0
,
 
0
.
0
)
,


 
 
 
 
 
 
 
 
(
7
0
0
0
0
,
 
1
0
0
0
0
0
,
 
0
.
0
)
,


 
 
 
 
 
 
 
 
(
2
0
0
0
0
0
,
 
1
0
0
0
0
0
,
 
1
0
0
.
0
)
,


 
 
 
 
 
 
 
 
(
0
,
 
1
0
0
0
0
0
,
 
0
.
0
)
,


 
 
 
 
 
 
 
 
(
1
0
0
0
0
0
,
 
0
,
 
0
.
0
)
,


 
 
 
 
 
 
 
 
(
0
,
 
0
,
 
0
.
0
)


 
 
 
 
]
)


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
w
a
g
e
_
p
r
e
m
i
u
m
(
s
e
l
f
,
 
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
,
 
m
e
d
i
a
n
_
w
a
g
e
,
 
e
x
p
e
c
t
e
d
_
p
r
e
m
i
u
m
)
:


 
 
 
 
 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
'
:
 
a
i
_
s
k
i
l
l
e
d
_
w
a
g
e
,


 
 
 
 
 
 
 
 
 
 
 
 
'
m
e
d
i
a
n
_
w
a
g
e
'
:
 
m
e
d
i
a
n
_
w
a
g
e


 
 
 
 
 
 
 
 
}
)


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
c
a
l
c
u
l
a
t
e
_
w
a
g
e
_
p
r
e
m
i
u
m
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
r
e
s
u
l
t
,
 
(
f
l
o
a
t
,
 
n
p
.
f
l
o
a
t
i
n
g
)
)


 
 
 
 
 
 
 
 
#
 
U
s
e
 
n
p
.
i
s
c
l
o
s
e
 
f
o
r
 
f
l
o
a
t
 
c
o
m
p
a
r
i
s
o
n
s


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
r
e
s
u
l
t
,
 
e
x
p
e
c
t
e
d
_
p
r
e
m
i
u
m
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
0
 
<
=
 
r
e
s
u
l
t
 
<
=
 
1
0
0




 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
 
-
-
-


 
 
 
 
@
p
y
t
e
s
t
.
m
a
r
k
.
p
a
r
a
m
e
t
r
i
z
e
(
"
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
,
 
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
,
 
e
x
p
e
c
t
e
d
_
a
c
c
e
s
s
i
b
i
l
i
t
y
"
,
 
[


 
 
 
 
 
 
 
 
(
1
8
,
 
3
,
 
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
2
1
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
-
1
1
0
,
 
c
l
i
p
p
e
d
 
t
o
 
0


 
 
 
 
 
 
 
 
(
1
2
,
 
0
,
 
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
1
2
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
-
2
0
,
 
c
l
i
p
p
e
d
 
t
o
 
0


 
 
 
 
 
 
 
 
(
0
,
 
0
,
 
1
0
0
.
0
)
,
 
#
 
(
1
 
-
 
(
0
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
1
0
0


 
 
 
 
 
 
 
 
(
1
0
,
 
0
,
 
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
1
0
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
0


 
 
 
 
 
 
 
 
(
8
,
 
1
,
 
1
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
9
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
1
0


 
 
 
 
 
 
 
 
(
1
,
 
1
,
 
8
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
2
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
8
0


 
 
 
 
 
 
 
 
(
2
5
,
 
5
,
 
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
3
0
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
-
2
0
0
,
 
c
l
i
p
p
e
d
 
t
o
 
0


 
 
 
 
 
 
 
 
(
1
4
,
 
1
,
 
0
.
0
)
,
 
 
#
 
H
R
 
S
p
e
c
i
a
l
i
s
t
 
e
x
a
m
p
l
e
:
 
(
1
 
-
 
1
.
5
)
 
*
 
1
0
0
 
=
 
-
5
0
,
 
c
l
i
p
p
e
d
 
t
o
 
0


 
 
 
 
 
 
 
 
(
5
,
 
0
,
 
5
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
5
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
5
0


 
 
 
 
 
 
 
 
(
0
,
 
5
,
 
5
0
.
0
)
,
 
 
#
 
(
1
 
-
 
(
5
 
/
 
1
0
)
)
 
*
 
1
0
0
 
=
 
5
0


 
 
 
 
]
)


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
(
s
e
l
f
,
 
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
,
 
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
,
 
e
x
p
e
c
t
e
d
_
a
c
c
e
s
s
i
b
i
l
i
t
y
)
:


 
 
 
 
 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
:
 
e
d
u
c
a
t
i
o
n
_
y
e
a
r
s
,


 
 
 
 
 
 
 
 
 
 
 
 
'
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s
_
r
e
q
u
i
r
e
d
'
:
 
e
x
p
e
r
i
e
n
c
e
_
y
e
a
r
s


 
 
 
 
 
 
 
 
}
)


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
c
a
l
c
u
l
a
t
e
_
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
r
e
s
u
l
t
,
 
(
f
l
o
a
t
,
 
n
p
.
f
l
o
a
t
i
n
g
)
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
r
e
s
u
l
t
,
 
e
x
p
e
c
t
e
d
_
a
c
c
e
s
s
i
b
i
l
i
t
y
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
0
 
<
=
 
r
e
s
u
l
t
 
<
=
 
1
0
0
d
e
f
 
c
a
l
c
u
l
a
t
e
_
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
,
 
w
e
i
g
h
t
s
)
:


 
 
 
 
"
"
"
A
g
g
r
e
g
a
t
e
s
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s
 
i
n
t
o
 
H
_
b
a
s
e
.
"
"
"


 
 
 
 
a
i
_
e
n
h
a
n
c
e
m
e
n
t
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
e
n
h
a
n
c
e
m
e
n
t
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)


 
 
 
 
_
,
 
j
o
b
_
g
r
o
w
t
h
_
n
o
r
m
a
l
i
z
e
d
 
=
 
c
a
l
c
u
l
a
t
e
_
j
o
b
_
g
r
o
w
t
h
_
n
o
r
m
a
l
i
z
e
d
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)


 
 
 
 
w
a
g
e
_
p
r
e
m
i
u
m
 
=
 
c
a
l
c
u
l
a
t
e
_
w
a
g
e
_
p
r
e
m
i
u
m
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)


 
 
 
 
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
 
=
 
c
a
l
c
u
l
a
t
e
_
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)




 
 
 
 
h
_
b
a
s
e
 
=
 
(


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
w
e
i
g
h
t
'
]
 
*
 
a
i
_
e
n
h
a
n
c
e
m
e
n
t
 
+


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
j
o
b
_
g
r
o
w
t
h
_
w
e
i
g
h
t
'
]
 
*
 
j
o
b
_
g
r
o
w
t
h
_
n
o
r
m
a
l
i
z
e
d
 
+


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
w
a
g
e
_
p
r
e
m
i
u
m
_
w
e
i
g
h
t
'
]
 
*
 
w
a
g
e
_
p
r
e
m
i
u
m
 
+


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
h
_
b
a
s
e
,
 
0
,
 
1
0
0
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y


e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
i
l
o
c
[
0
]


h
_
b
a
s
e
_
s
c
o
r
e
 
=
 
c
a
l
c
u
l
a
t
e
_
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
(
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
,
 
P
A
R
A
M
S
[
'
h
r
_
b
a
s
e
_
w
e
i
g
h
t
s
'
]
)


p
r
i
n
t
(
f
"
T
e
s
t
 
B
a
s
e
 
O
p
p
o
r
t
u
n
i
t
y
 
S
c
o
r
e
 
f
o
r
 
{
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
[
'
o
c
c
u
p
a
t
i
o
n
'
]
}
:
 
{
h
_
b
a
s
e
_
s
c
o
r
e
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
w
i
t
h
 
t
h
e
 
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
 
f
o
r
 
a
l
l
 
o
c
c
u
p
a
t
i
o
n
s


d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
'
]
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
a
p
p
l
y
(
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
(
r
o
w
,
 
P
A
R
A
M
S
[
'
h
r
_
b
a
s
e
_
w
e
i
g
h
t
s
'
]
)
,
 
a
x
i
s
=
1
)




p
r
i
n
t
(
"
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
w
i
t
h
 
'
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
[
'
o
c
c
u
p
a
t
i
o
n
'
,
 
'
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
,
 
l
a
m
b
d
a
_
v
a
l
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
m
a
r
k
e
t
 
m
o
m
e
n
t
u
m
 
g
r
o
w
t
h
 
m
u
l
t
i
p
l
i
e
r
.
"
"
"


 
 
 
 
c
u
r
r
e
n
t
_
p
o
s
t
i
n
g
s
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
j
o
b
_
p
o
s
t
i
n
g
s
_
c
u
r
r
e
n
t
_
m
o
n
t
h
'
]


 
 
 
 
p
r
e
v
_
p
o
s
t
i
n
g
s
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
j
o
b
_
p
o
s
t
i
n
g
s
_
p
r
e
v
_
m
o
n
t
h
'
]




 
 
 
 
i
f
 
p
r
e
v
_
p
o
s
t
i
n
g
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1
.
0
 
#
 
N
o
 
c
h
a
n
g
e
 
i
f
 
n
o
 
p
r
e
v
i
o
u
s
 
d
a
t
a




 
 
 
 
c
h
a
n
g
e
_
f
a
c
t
o
r
 
=
 
(
c
u
r
r
e
n
t
_
p
o
s
t
i
n
g
s
 
/
 
p
r
e
v
_
p
o
s
t
i
n
g
s
)
 
-
 
1


 
 
 
 
m
u
l
t
i
p
l
i
e
r
 
=
 
1
 
+
 
(
l
a
m
b
d
a
_
v
a
l
 
*
 
c
h
a
n
g
e
_
f
a
c
t
o
r
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
m
u
l
t
i
p
l
i
e
r
,
 
0
.
7
,
 
1
.
3
)
 
#
 
C
l
a
m
p
 
t
o
 
r
e
a
s
o
n
a
b
l
e
 
r
a
n
g
e




d
e
f
 
c
a
l
c
u
l
a
t
e
_
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
,
 
g
a
m
m
a
_
v
a
l
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
r
e
g
i
o
n
a
l
 
d
e
m
a
n
d
 
m
u
l
t
i
p
l
i
e
r
.
"
"
"


 
 
 
 
#
 
F
o
r
 
s
i
m
p
l
i
c
i
t
y
,
 
a
s
s
u
m
e
 
L
o
c
a
l
 
D
e
m
a
n
d
 
e
q
u
a
l
s
 
N
a
t
i
o
n
a
l
 
A
v
g
 
D
e
m
a
n
d
 
(
r
a
t
i
o
 
o
f
 
1
.
0
)
 
u
n
l
e
s
s
 
s
p
e
c
i
f
i
e
d
.


 
 
 
 
l
o
c
a
l
_
t
o
_
n
a
t
i
o
n
a
l
_
r
a
t
i
o
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
.
g
e
t
(
'
l
o
c
a
l
_
d
e
m
a
n
d
_
r
a
t
i
o
'
,
 
1
.
0
)


 
 
 
 
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
'
]




 
 
 
 
m
u
l
t
i
p
l
i
e
r
 
=
 
l
o
c
a
l
_
t
o
_
n
a
t
i
o
n
a
l
_
r
a
t
i
o
 
*
 
(
1
 
+
 
(
g
a
m
m
a
_
v
a
l
 
*
 
r
e
m
o
t
e
_
w
o
r
k
_
f
a
c
t
o
r
)
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
m
u
l
t
i
p
l
i
e
r
,
 
0
.
8
,
 
1
.
2
)
 
#
 
C
l
a
m
p
 
t
o
 
r
e
a
s
o
n
a
b
l
e
 
r
a
n
g
e




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
s
 
i
m
m
e
d
i
a
t
e
l
y


e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
i
l
o
c
[
0
]


g
r
o
w
t
h
_
m
u
l
t
 
=
 
c
a
l
c
u
l
a
t
e
_
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
(
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
,
 
P
A
R
A
M
S
[
'
l
a
m
b
d
a
_
g
r
o
w
t
h
'
]
)


r
e
g
i
o
n
a
l
_
m
u
l
t
 
=
 
c
a
l
c
u
l
a
t
e
_
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
(
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
,
 
P
A
R
A
M
S
[
'
g
a
m
m
a
_
r
e
g
i
o
n
a
l
'
]
)


p
r
i
n
t
(
f
"
T
e
s
t
 
G
r
o
w
t
h
 
M
u
l
t
i
p
l
i
e
r
 
f
o
r
 
{
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
[
'
o
c
c
u
p
a
t
i
o
n
'
]
}
:
 
{
g
r
o
w
t
h
_
m
u
l
t
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
T
e
s
t
 
R
e
g
i
o
n
a
l
 
M
u
l
t
i
p
l
i
e
r
 
f
o
r
 
{
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
[
'
o
c
c
u
p
a
t
i
o
n
'
]
}
:
 
{
r
e
g
i
o
n
a
l
_
m
u
l
t
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
w
i
t
h
 
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
 
a
n
d
 
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
 
f
o
r
 
a
l
l
 
o
c
c
u
p
a
t
i
o
n
s


d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
'
]
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
a
p
p
l
y
(
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
(
r
o
w
,
 
P
A
R
A
M
S
[
'
l
a
m
b
d
a
_
g
r
o
w
t
h
'
]
)
,
 
a
x
i
s
=
1
)


d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
'
]
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
.
a
p
p
l
y
(
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
(
r
o
w
,
 
P
A
R
A
M
S
[
'
g
a
m
m
a
_
r
e
g
i
o
n
a
l
'
]
)
,
 
a
x
i
s
=
1
)




p
r
i
n
t
(
"
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
w
i
t
h
 
'
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
'
 
a
n
d
 
'
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
'
:
"
)


p
r
i
n
t
(
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
[
'
o
c
c
u
p
a
t
i
o
n
'
,
 
'
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
'
,
 
'
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
s
y
s
t
e
m
a
t
i
c
_
o
p
p
o
r
t
u
n
i
t
y
(
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
t
o
t
a
l
 
H
R
^
R
 
f
o
r
 
a
 
t
a
r
g
e
t
 
o
c
c
u
p
a
t
i
o
n
.
"
"
"


 
 
 
 
b
a
s
e
_
s
c
o
r
e
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
b
a
s
e
_
o
p
p
o
r
t
u
n
i
t
y
_
s
c
o
r
e
'
]


 
 
 
 
g
r
o
w
t
h
_
m
u
l
t
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
g
r
o
w
t
h
_
m
u
l
t
i
p
l
i
e
r
'
]


 
 
 
 
r
e
g
i
o
n
a
l
_
m
u
l
t
 
=
 
o
c
c
u
p
a
t
i
o
n
_
d
a
t
a
_
r
o
w
[
'
r
e
g
i
o
n
a
l
_
m
u
l
t
i
p
l
i
e
r
'
]




 
 
 
 
h
r
_
r
 
=
 
b
a
s
e
_
s
c
o
r
e
 
*
 
g
r
o
w
t
h
_
m
u
l
t
 
*
 
r
e
g
i
o
n
a
l
_
m
u
l
t


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
h
r
_
r
,
 
0
,
 
1
0
0
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y
 
(
u
s
i
n
g
 
a
 
m
e
r
g
e
d
 
r
o
w
 
f
o
r
 
s
i
m
p
l
i
c
i
t
y
 
i
n
 
t
e
s
t
)


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
j
o
b
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
i
l
o
c
[
0
]
[
'
j
o
b
_
r
o
l
e
'
]


e
x
a
m
p
l
e
_
h
r
_
r
o
w
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
o
c
c
u
p
a
t
i
o
n
'
]
 
=
=
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
j
o
b
]
.
i
l
o
c
[
0
]


e
x
a
m
p
l
e
_
h
r
_
r
 
=
 
c
a
l
c
u
l
a
t
e
_
s
y
s
t
e
m
a
t
i
c
_
o
p
p
o
r
t
u
n
i
t
y
(
e
x
a
m
p
l
e
_
h
r
_
r
o
w
)


p
r
i
n
t
(
f
"
T
e
s
t
 
H
R
^
R
 
s
c
o
r
e
 
f
o
r
 
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
j
o
b
}
:
 
{
e
x
a
m
p
l
e
_
h
r
_
r
:
.
2
f
}
"
)
#
 
I
t
e
r
a
t
e
 
t
h
r
o
u
g
h
 
d
f
_
e
m
p
l
o
y
e
e
s
 
t
o
 
c
a
l
c
u
l
a
t
e
 
H
R
^
R
 
s
c
o
r
e
s


d
f
_
e
m
p
l
o
y
e
e
s
[
'
h
r
_
r
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
'
j
o
b
_
r
o
l
e
'
]
.
a
p
p
l
y
(


 
 
 
 
l
a
m
b
d
a
 
j
o
b
_
r
o
l
e
:


 
 
 
 
 
 
 
 
c
a
l
c
u
l
a
t
e
_
s
y
s
t
e
m
a
t
i
c
_
o
p
p
o
r
t
u
n
i
t
y
(
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
o
c
c
u
p
a
t
i
o
n
'
]
 
=
=
 
j
o
b
_
r
o
l
e
]
.
i
l
o
c
[
0
]
)


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
h
r
_
r
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
h
r
_
r
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p


i
m
p
o
r
t
 
p
y
t
e
s
t


i
m
p
o
r
t
 
r
a
n
d
o
m




#
 
D
e
f
i
n
e
 
d
e
f
a
u
l
t
 
p
a
r
a
m
e
t
e
r
s
 
f
o
r
 
\
a
l
p
h
a
 
a
n
d
 
\
b
e
t
a
 
(
f
r
o
m
 
C
e
l
l
 
5
)


#
 
T
h
i
s
 
P
A
R
A
M
S
 
d
i
c
t
i
o
n
a
r
y
 
i
s
 
c
r
u
c
i
a
l
 
f
o
r
 
t
h
e
 
f
u
n
c
t
i
o
n
s
 
t
o
 
b
e
 
t
e
s
t
e
d
 
a
n
d
 
t
h
e
i
r
 
d
e
p
e
n
d
e
n
c
i
e
s


P
A
R
A
M
S
 
=
 
{


 
 
 
 
'
a
l
p
h
a
'
:
 
0
.
6
,


 
 
 
 
'
b
e
t
a
'
:
 
0
.
1
5
,


 
 
 
 
'
l
a
m
b
d
a
_
g
r
o
w
t
h
'
:
 
0
.
3
,


 
 
 
 
'
g
a
m
m
a
_
r
e
g
i
o
n
a
l
'
:
 
0
.
2
,


 
 
 
 
'
h
r
_
b
a
s
e
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
a
i
_
e
n
h
a
n
c
e
m
e
n
t
_
w
e
i
g
h
t
'
:
 
0
.
3
0
,


 
 
 
 
 
 
 
 
'
j
o
b
_
g
r
o
w
t
h
_
w
e
i
g
h
t
'
:
 
0
.
3
0
,


 
 
 
 
 
 
 
 
'
w
a
g
e
_
p
r
e
m
i
u
m
_
w
e
i
g
h
t
'
:
 
0
.
2
5
,


 
 
 
 
 
 
 
 
'
e
n
t
r
y
_
a
c
c
e
s
s
i
b
i
l
i
t
y
_
w
e
i
g
h
t
'
:
 
0
.
1
5


 
 
 
 
}
,


 
 
 
 
'
t
h
e
t
a
_
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
w
e
i
g
h
t
'
:
 
0
.
3
0
,


 
 
 
 
 
 
 
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
w
e
i
g
h
t
'
:
 
0
.
3
5
,


 
 
 
 
 
 
 
 
'
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
w
e
i
g
h
t
'
:
 
0
.
2
0
,


 
 
 
 
 
 
 
 
'
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
w
e
i
g
h
t
'
:
 
0
.
1
5


 
 
 
 
}
,


 
 
 
 
'
g
a
m
m
a
_
e
x
p
e
r
i
e
n
c
e
_
d
e
c
a
y
'
:
 
0
.
1
5
,


 
 
 
 
'
d
o
m
a
i
n
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
p
o
r
t
f
o
l
i
o
_
w
e
i
g
h
t
'
:
 
0
.
4
,


 
 
 
 
 
 
 
 
'
r
e
c
o
g
n
i
t
i
o
n
_
w
e
i
g
h
t
'
:
 
0
.
3
,


 
 
 
 
 
 
 
 
'
c
r
e
d
e
n
t
i
a
l
s
_
w
e
i
g
h
t
'
:
 
0
.
3


 
 
 
 
}
,


 
 
 
 
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
4
5
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
3
5
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
2
0


 
 
 
 
}


}




#
 
T
h
e
 
f
u
n
c
t
i
o
n
s
 
t
o
 
b
e
 
t
e
s
t
e
d
 
(
r
e
d
e
f
i
n
e
d
 
f
o
r
 
s
e
l
f
-
c
o
n
t
a
i
n
m
e
n
t
 
i
n
 
u
n
i
t
 
t
e
s
t
s
)


d
e
f
 
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
S
_
i
,
1
 
(
T
e
c
h
n
i
c
a
l
 
A
I
 
S
k
i
l
l
s
)
.
"
"
"


 
 
 
 
s
c
o
r
e
s
 
=
 
[


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
t
o
o
l
s
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
]


 
 
 
 
]


 
 
 
 
r
e
t
u
r
n
 
n
p
.
m
e
a
n
(
s
c
o
r
e
s
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
S
_
i
,
2
 
(
A
I
-
A
u
g
m
e
n
t
e
d
 
P
r
o
d
u
c
t
i
v
i
t
y
)
.
"
"
"


 
 
 
 
r
e
t
u
r
n
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
]




d
e
f
 
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
S
_
i
,
3
 
(
C
r
i
t
i
c
a
l
 
A
I
 
J
u
d
g
m
e
n
t
)
.
"
"
"


 
 
 
 
e
r
r
o
r
s
_
c
a
u
g
h
t
_
s
c
o
r
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
]


 
 
 
 
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
s
c
o
r
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
]


 
 
 
 
r
e
t
u
r
n
 
n
p
.
m
e
a
n
(
[
e
r
r
o
r
s
_
c
a
u
g
h
t
_
s
c
o
r
e
,
 
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
s
c
o
r
e
]
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
S
_
i
,
4
 
(
A
I
 
L
e
a
r
n
i
n
g
 
V
e
l
o
c
i
t
y
)
.
"
"
"


 
 
 
 
l
e
a
r
n
i
n
g
_
r
a
t
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
]


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
l
e
a
r
n
i
n
g
_
r
a
t
e
 
*
 
1
0
0
 
*
 
0
.
8
,
 
0
,
 
1
0
0
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
t
h
e
t
a
_
w
e
i
g
h
t
s
)
:


 
 
 
 
"
"
"
A
g
g
r
e
g
a
t
e
s
 
S
_
i
,
k
 
i
n
t
o
 
A
I
-
F
l
u
e
n
c
y
.
"
"
"


 
 
 
 
s
1
 
=
 
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)


 
 
 
 
s
2
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)


 
 
 
 
s
3
 
=
 
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)


 
 
 
 
s
4
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)




 
 
 
 
a
i
_
f
l
u
e
n
c
y
 
=
 
(


 
 
 
 
 
 
 
 
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
w
e
i
g
h
t
'
]
 
*
 
s
1
 
+


 
 
 
 
 
 
 
 
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
s
2
 
+


 
 
 
 
 
 
 
 
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
w
e
i
g
h
t
'
]
 
*
 
s
3
 
+


 
 
 
 
 
 
 
 
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
s
4


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
a
i
_
f
l
u
e
n
c
y
,
 
0
,
 
1
0
0
)




#
 
P
y
t
e
s
t
 
u
n
i
t
 
t
e
s
t
s


c
l
a
s
s
 
T
e
s
t
A
I
F
l
u
e
n
c
y
C
o
m
p
o
n
e
n
t
s
:




 
 
 
 
#
 
F
i
x
t
u
r
e
 
t
o
 
p
r
o
v
i
d
e
 
s
a
m
p
l
e
 
e
m
p
l
o
y
e
e
 
d
a
t
a
 
r
o
w
 
f
o
r
 
c
o
n
s
i
s
t
e
n
t
 
t
e
s
t
i
n
g


 
 
 
 
@
p
y
t
e
s
t
.
f
i
x
t
u
r
e


 
 
 
 
d
e
f
 
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
p
a
n
d
a
s
 
S
e
r
i
e
s
 
w
i
t
h
 
a
l
l
 
r
e
q
u
i
r
e
d
 
k
e
y
s
 
a
n
d
 
s
a
m
p
l
e
 
v
a
l
u
e
s


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
8
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
7
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
9
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
7
5
,


 
 
 
 
 
 
 
 
 
 
 
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
:
 
8
5
,


 
 
 
 
 
 
 
 
 
 
 
 
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
:
 
7
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
:
 
8
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
0
.
2
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
h
o
u
r
s
_
i
n
v
e
s
t
e
d
'
:
 
2
0
0
 
#
 
N
o
t
 
d
i
r
e
c
t
l
y
 
u
s
e
d
 
i
n
 
c
u
r
r
e
n
t
 
S
4
 
c
a
l
c
u
l
a
t
i
o
n
,
 
b
u
t
 
p
a
r
t
 
o
f
 
c
o
n
t
e
x
t


 
 
 
 
 
 
 
 
}
)




 
 
 
 
@
p
y
t
e
s
t
.
f
i
x
t
u
r
e


 
 
 
 
d
e
f
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
P
A
R
A
M
S
[
'
t
h
e
t
a
_
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
s
'
]




 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
 
-
-
-


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
t
y
p
i
c
a
l
(
s
e
l
f
,
 
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
1
 
=
 
(
8
0
 
+
 
7
0
 
+
 
9
0
 
+
 
7
5
)
 
/
 
4


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
,
 
e
x
p
e
c
t
e
d
_
s
1
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
e
d
g
e
_
m
i
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
0
,
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
0
,
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
0
,
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
0


 
 
 
 
 
 
 
 
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)
,
 
0
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
e
d
g
e
_
m
a
x
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
1
0
0
,
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
1
0
0
,
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
1
0
0
,
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
1
0
0


 
 
 
 
 
 
 
 
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)
,
 
1
0
0
)




 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
 
-
-
-


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
t
y
p
i
c
a
l
(
s
e
l
f
,
 
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
,
 
8
5
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
e
d
g
e
_
m
i
n
_
m
a
x
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
m
i
n
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
:
 
0
}
)


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
m
a
x
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
:
 
1
0
0
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
m
i
n
)
,
 
0
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
m
a
x
)
,
 
1
0
0
)




 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
 
-
-
-


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
t
y
p
i
c
a
l
(
s
e
l
f
,
 
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
3
 
=
 
(
7
0
 
+
 
8
0
)
 
/
 
2


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
,
 
e
x
p
e
c
t
e
d
_
s
3
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
e
d
g
e
_
m
i
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
:
 
0
,
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
:
 
0
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)
,
 
0
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
e
d
g
e
_
m
a
x
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
:
 
1
0
0
,
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
:
 
1
0
0
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)
,
 
1
0
0
)




 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
 
-
-
-


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
t
y
p
i
c
a
l
(
s
e
l
f
,
 
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
4
 
=
 
n
p
.
c
l
i
p
(
0
.
2
0
 
*
 
1
0
0
 
*
 
0
.
8
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
,
 
e
x
p
e
c
t
e
d
_
s
4
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
e
d
g
e
_
m
i
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
0
.
0
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)
,
 
0
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
e
d
g
e
_
m
a
x
_
c
l
i
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
1
.
0
}
)
 
#
 
A
 
l
e
a
r
n
i
n
g
 
r
a
t
e
 
t
h
a
t
 
r
e
s
u
l
t
s
 
i
n
 
s
c
o
r
e
 
8
0


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
4
 
=
 
n
p
.
c
l
i
p
(
1
.
0
 
*
 
1
0
0
 
*
 
0
.
8
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
)
,
 
e
x
p
e
c
t
e
d
_
s
4
)




 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
o
v
e
r
_
c
l
i
p
 
=
 
p
d
.
S
e
r
i
e
s
(
{
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
1
.
5
}
)
 
#
 
V
a
l
u
e
 
t
h
a
t
 
s
h
o
u
l
d
 
c
l
i
p
 
t
o
 
1
0
0


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
o
v
e
r
_
c
l
i
p
)
,
 
1
0
0
)






 
 
 
 
#
 
-
-
-
 
T
e
s
t
s
 
f
o
r
 
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
 
-
-
-


 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
_
t
y
p
i
c
a
l
(
s
e
l
f
,
 
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
:


 
 
 
 
 
 
 
 
s
1
 
=
 
c
a
l
c
u
l
a
t
e
_
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)


 
 
 
 
 
 
 
 
s
2
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)


 
 
 
 
 
 
 
 
s
3
 
=
 
c
a
l
c
u
l
a
t
e
_
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)


 
 
 
 
 
 
 
 
s
4
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)




 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
 
=
 
(


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
w
e
i
g
h
t
'
]
 
*
 
s
1
 
+


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
s
2
 
+


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
w
e
i
g
h
t
'
]
 
*
 
s
3
 
+


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
s
4


 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
,
 
n
p
.
c
l
i
p
(
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
,
 
0
,
 
1
0
0
)
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
0
 
<
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
s
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
 
<
=
 
1
0
0




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
_
e
d
g
e
_
a
l
l
_
z
e
r
o
(
s
e
l
f
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
0
,
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
0
,
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
0
,
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
:
 
0
,
 
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
:
 
0
,
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
:
 
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
0
.
0


 
 
 
 
 
 
 
 
}
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
,
 
0
)




 
 
 
 
d
e
f
 
t
e
s
t
_
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
_
e
d
g
e
_
a
l
l
_
m
a
x
_
s
c
o
r
e
s
_
w
i
t
h
i
n
_
c
l
i
p
(
s
e
l
f
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
:


 
 
 
 
 
 
 
 
#
 
C
r
e
a
t
e
 
a
n
 
e
m
p
l
o
y
e
e
 
w
i
t
h
 
m
a
x
 
v
a
l
u
e
s
 
f
o
r
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s
,
 
c
h
e
c
k
i
n
g
 
i
f
 
t
o
t
a
l
 
c
l
i
p
s
 
t
o
 
1
0
0


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
p
d
.
S
e
r
i
e
s
(
{


 
 
 
 
 
 
 
 
 
 
 
 
'
p
r
o
m
p
t
i
n
g
_
s
c
o
r
e
'
:
 
1
0
0
,
 
'
t
o
o
l
s
_
s
c
o
r
e
'
:
 
1
0
0
,
 
'
u
n
d
e
r
s
t
a
n
d
i
n
g
_
s
c
o
r
e
'
:
 
1
0
0
,
 
'
d
a
t
a
_
l
i
t
_
s
c
o
r
e
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
n
o
r
m
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
e
r
r
o
r
s
_
c
a
u
g
h
t
_
n
o
r
m
'
:
 
1
0
0
,
 
'
t
r
u
s
t
_
d
e
c
i
s
i
o
n
s
_
n
o
r
m
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
 
 
 
 
'
l
e
a
r
n
i
n
g
_
r
a
t
e
'
:
 
1
.
0
 
#
 
S
4
 
w
i
l
l
 
b
e
 
8
0
,
 
n
o
t
 
1
0
0


 
 
 
 
 
 
 
 
}
)


 
 
 
 
 
 
 
 
s
1
_
v
a
l
 
=
 
1
0
0
.
0


 
 
 
 
 
 
 
 
s
2
_
v
a
l
 
=
 
1
0
0
.
0


 
 
 
 
 
 
 
 
s
3
_
v
a
l
 
=
 
1
0
0
.
0


 
 
 
 
 
 
 
 
s
4
_
v
a
l
 
=
 
8
0
.
0
 
#
 
F
r
o
m
 
n
p
.
c
l
i
p
(
1
.
0
 
*
 
1
0
0
 
*
 
0
.
8
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
 
=
 
(


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
t
e
c
h
n
i
c
a
l
_
a
i
_
s
k
i
l
l
s
_
w
e
i
g
h
t
'
]
 
*
 
s
1
_
v
a
l
 
+


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
a
i
_
a
u
g
m
e
n
t
e
d
_
p
r
o
d
u
c
t
i
v
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
s
2
_
v
a
l
 
+


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
c
r
i
t
i
c
a
l
_
a
i
_
j
u
d
g
m
e
n
t
_
w
e
i
g
h
t
'
]
 
*
 
s
3
_
v
a
l
 
+


 
 
 
 
 
 
 
 
 
 
 
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
[
'
a
i
_
l
e
a
r
n
i
n
g
_
v
e
l
o
c
i
t
y
_
w
e
i
g
h
t
'
]
 
*
 
s
4
_
v
a
l


 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
a
l
c
u
l
a
t
e
d
 
v
a
l
u
e
 
i
s
 
c
o
r
r
e
c
t
l
y
 
c
l
i
p
p
e
d
 
i
f
 
i
t
 
e
x
c
e
e
d
s
 
1
0
0
,
 
o
r
 
w
i
t
h
i
n
 
b
o
u
n
d
s
 
o
t
h
e
r
w
i
s
e


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
,
 
n
p
.
c
l
i
p
(
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
,
 
0
,
 
1
0
0
)
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
,
 
s
a
m
p
l
e
_
t
h
e
t
a
_
w
e
i
g
h
t
s
)
 
<
=
 
1
0
0
#
 
U
p
d
a
t
e
 
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
t
h
e
 
c
a
l
c
u
l
a
t
e
d
 
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
 
f
o
r
 
a
l
l
 
e
m
p
l
o
y
e
e
s


d
f
_
e
m
p
l
o
y
e
e
s
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(


 
 
 
 
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
a
i
_
f
l
u
e
n
c
y
(
r
o
w
,
 
P
A
R
A
M
S
[
'
t
h
e
t
a
_
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
s
'
]
)
,


 
 
 
 
a
x
i
s
=
1


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
e
d
u
c
a
t
i
o
n
a
l
_
f
o
u
n
d
a
t
i
o
n
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
E
_
e
d
u
c
a
t
i
o
n
 
b
a
s
e
d
 
o
n
 
e
d
u
c
a
t
i
o
n
 
l
e
v
e
l
.
"
"
"


 
 
 
 
e
d
u
c
a
t
i
o
n
_
m
a
p
 
=
 
{


 
 
 
 
 
 
 
 
'
H
S
+
C
o
u
r
s
e
w
o
r
k
'
:
 
0
.
5
0
,


 
 
 
 
 
 
 
 
'
A
s
s
o
c
i
a
t
e
\
'
s
/
C
e
r
t
i
f
i
c
a
t
e
'
:
 
0
.
6
0
,


 
 
 
 
 
 
 
 
'
B
a
c
h
e
l
o
r
\
'
s
'
:
 
0
.
7
0
,


 
 
 
 
 
 
 
 
'
M
a
s
t
e
r
\
'
s
'
:
 
0
.
8
5
,


 
 
 
 
 
 
 
 
'
P
h
D
'
:
 
1
.
0


 
 
 
 
}


 
 
 
 
r
e
t
u
r
n
 
e
d
u
c
a
t
i
o
n
_
m
a
p
.
g
e
t
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
e
d
u
c
a
t
i
o
n
_
l
e
v
e
l
'
]
,
 
0
.
5
0
)
 
*
 
1
0
0
 
#
 
S
c
a
l
e
 
t
o
 
0
-
1
0
0




d
e
f
 
c
a
l
c
u
l
a
t
e
_
p
r
a
c
t
i
c
a
l
_
e
x
p
e
r
i
e
n
c
e
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
g
a
m
m
a
_
e
x
p
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
E
_
e
x
p
e
r
i
e
n
c
e
 
w
i
t
h
 
d
i
m
i
n
i
s
h
i
n
g
 
r
e
t
u
r
n
s
.
"
"
"


 
 
 
 
y
e
a
r
s
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
]


 
 
 
 
e
x
p
e
r
i
e
n
c
e
_
s
c
o
r
e
 
=
 
1
 
-
 
n
p
.
e
x
p
(
-
g
a
m
m
a
_
e
x
p
 
*
 
y
e
a
r
s
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
e
x
p
e
r
i
e
n
c
e
_
s
c
o
r
e
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
d
e
p
t
h
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
w
e
i
g
h
t
s
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
E
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
 
b
a
s
e
d
 
o
n
 
p
o
r
t
f
o
l
i
o
,
 
r
e
c
o
g
n
i
t
i
o
n
,
 
a
n
d
 
c
r
e
d
e
n
t
i
a
l
s
.
"
"
"


 
 
 
 
p
o
r
t
f
o
l
i
o
_
s
c
o
r
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
d
o
m
a
i
n
_
p
o
r
t
f
o
l
i
o
_
s
c
o
r
e
'
]


 
 
 
 
r
e
c
o
g
n
i
t
i
o
n
_
s
c
o
r
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
d
o
m
a
i
n
_
r
e
c
o
g
n
i
t
i
o
n
_
s
c
o
r
e
'
]


 
 
 
 
c
r
e
d
e
n
t
i
a
l
s
_
s
c
o
r
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
d
o
m
a
i
n
_
c
r
e
d
e
n
t
i
a
l
s
_
s
c
o
r
e
'
]




 
 
 
 
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
d
e
p
t
h
 
=
 
(


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
p
o
r
t
f
o
l
i
o
_
w
e
i
g
h
t
'
]
 
*
 
p
o
r
t
f
o
l
i
o
_
s
c
o
r
e
 
+


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
r
e
c
o
g
n
i
t
i
o
n
_
w
e
i
g
h
t
'
]
 
*
 
r
e
c
o
g
n
i
t
i
o
n
_
s
c
o
r
e
 
+


 
 
 
 
 
 
 
 
w
e
i
g
h
t
s
[
'
c
r
e
d
e
n
t
i
a
l
s
_
w
e
i
g
h
t
'
]
 
*
 
c
r
e
d
e
n
t
i
a
l
s
_
s
c
o
r
e


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
d
e
p
t
h
,
 
0
,
 
1
0
0
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
g
a
m
m
a
_
e
x
p
,
 
d
o
m
a
i
n
_
w
e
i
g
h
t
s
)
:


 
 
 
 
"
"
"
A
g
g
r
e
g
a
t
e
s
 
t
h
e
 
t
h
r
e
e
 
s
u
b
-
f
a
c
t
o
r
s
 
i
n
t
o
 
D
o
m
a
i
n
-
E
x
p
e
r
t
i
s
e
.
"
"
"


 
 
 
 
e
_
e
d
u
c
a
t
i
o
n
 
=
 
c
a
l
c
u
l
a
t
e
_
e
d
u
c
a
t
i
o
n
a
l
_
f
o
u
n
d
a
t
i
o
n
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
 
/
 
1
0
0
 
#
 
B
a
c
k
 
t
o
 
0
-
1
 
f
o
r
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n


 
 
 
 
e
_
e
x
p
e
r
i
e
n
c
e
 
=
 
c
a
l
c
u
l
a
t
e
_
p
r
a
c
t
i
c
a
l
_
e
x
p
e
r
i
e
n
c
e
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
g
a
m
m
a
_
e
x
p
)
 
/
 
1
0
0
 
#
 
B
a
c
k
 
t
o
 
0
-
1


 
 
 
 
e
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
 
=
 
c
a
l
c
u
l
a
t
e
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
d
e
p
t
h
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
d
o
m
a
i
n
_
w
e
i
g
h
t
s
)
 
/
 
1
0
0
 
#
 
B
a
c
k
 
t
o
 
0
-
1




 
 
 
 
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
 
=
 
e
_
e
d
u
c
a
t
i
o
n
 
*
 
e
_
e
x
p
e
r
i
e
n
c
e
 
*
 
e
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)
 
#
 
F
i
n
a
l
 
s
c
o
r
e
 
0
-
1
0
0




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
s
 
i
m
m
e
d
i
a
t
e
l
y
 
w
i
t
h
 
a
n
 
e
x
a
m
p
l
e
 
e
m
p
l
o
y
e
e


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
i
l
o
c
[
0
]


e
d
u
c
a
t
i
o
n
_
s
c
o
r
e
 
=
 
c
a
l
c
u
l
a
t
e
_
e
d
u
c
a
t
i
o
n
a
l
_
f
o
u
n
d
a
t
i
o
n
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
)


e
x
p
e
r
i
e
n
c
e
_
s
c
o
r
e
 
=
 
c
a
l
c
u
l
a
t
e
_
p
r
a
c
t
i
c
a
l
_
e
x
p
e
r
i
e
n
c
e
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
,
 
P
A
R
A
M
S
[
'
g
a
m
m
a
_
e
x
p
e
r
i
e
n
c
e
_
d
e
c
a
y
'
]
)


s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
s
c
o
r
e
 
=
 
c
a
l
c
u
l
a
t
e
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
d
e
p
t
h
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
,
 
P
A
R
A
M
S
[
'
d
o
m
a
i
n
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
w
e
i
g
h
t
s
'
]
)


d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
 
=
 
c
a
l
c
u
l
a
t
e
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
,
 
P
A
R
A
M
S
[
'
g
a
m
m
a
_
e
x
p
e
r
i
e
n
c
e
_
d
e
c
a
y
'
]
,
 
P
A
R
A
M
S
[
'
d
o
m
a
i
n
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
w
e
i
g
h
t
s
'
]
)




p
r
i
n
t
(
f
"
T
e
s
t
 
E
_
e
d
u
c
a
t
i
o
n
 
f
o
r
 
E
M
P
0
0
0
:
 
{
e
d
u
c
a
t
i
o
n
_
s
c
o
r
e
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
T
e
s
t
 
E
_
e
x
p
e
r
i
e
n
c
e
 
f
o
r
 
E
M
P
0
0
0
:
 
{
e
x
p
e
r
i
e
n
c
e
_
s
c
o
r
e
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
T
e
s
t
 
E
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
 
f
o
r
 
E
M
P
0
0
0
:
 
{
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
s
c
o
r
e
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
T
e
s
t
 
D
o
m
a
i
n
-
E
x
p
e
r
t
i
s
e
 
s
c
o
r
e
 
f
o
r
 
E
M
P
0
0
0
:
 
{
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
t
h
e
 
c
a
l
c
u
l
a
t
e
d
 
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
 
f
o
r
 
a
l
l
 
e
m
p
l
o
y
e
e
s


d
f
_
e
m
p
l
o
y
e
e
s
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(


 
 
 
 
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
(
r
o
w
,
 
P
A
R
A
M
S
[
'
g
a
m
m
a
_
e
x
p
e
r
i
e
n
c
e
_
d
e
c
a
y
'
]
,
 
P
A
R
A
M
S
[
'
d
o
m
a
i
n
_
s
p
e
c
i
a
l
i
z
a
t
i
o
n
_
w
e
i
g
h
t
s
'
]
)
,


 
 
 
 
a
x
i
s
=
1


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
A
d
a
p
t
i
v
e
-
C
a
p
a
c
i
t
y
 
a
s
 
a
n
 
a
v
e
r
a
g
e
 
o
f
 
t
h
r
e
e
 
m
e
t
a
-
s
k
i
l
l
s
.
"
"
"


 
 
 
 
c
_
c
o
g
n
i
t
i
v
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
c
o
g
n
i
t
i
v
e
_
f
l
e
x
i
b
i
l
i
t
y
'
]


 
 
 
 
c
_
s
o
c
i
a
l
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
s
o
c
i
a
l
_
e
m
o
t
i
o
n
a
l
'
]


 
 
 
 
c
_
s
t
r
a
t
e
g
i
c
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
s
t
r
a
t
e
g
i
c
_
c
a
r
e
e
r
'
]




 
 
 
 
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
 
=
 
n
p
.
m
e
a
n
(
[
c
_
c
o
g
n
i
t
i
v
e
,
 
c
_
s
o
c
i
a
l
,
 
c
_
s
t
r
a
t
e
g
i
c
]
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
,
 
0
,
 
1
0
0
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y
 
w
i
t
h
 
a
n
 
e
x
a
m
p
l
e
 
e
m
p
l
o
y
e
e


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
i
l
o
c
[
0
]


a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
 
=
 
c
a
l
c
u
l
a
t
e
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
)


p
r
i
n
t
(
f
"
T
e
s
t
 
A
d
a
p
t
i
v
e
-
C
a
p
a
c
i
t
y
 
s
c
o
r
e
 
f
o
r
 
E
M
P
0
0
0
:
 
{
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
t
h
e
 
c
a
l
c
u
l
a
t
e
d
 
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
 
f
o
r
 
a
l
l
 
e
m
p
l
o
y
e
e
s


d
f
_
e
m
p
l
o
y
e
e
s
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(


 
 
 
 
c
a
l
c
u
l
a
t
e
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
,
 
a
x
i
s
=
1


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
i
d
i
o
s
y
n
c
r
a
t
i
c
_
r
e
a
d
i
n
e
s
s
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
v
r
_
w
e
i
g
h
t
s
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
t
o
t
a
l
 
V
^
R
 
s
c
o
r
e
 
f
r
o
m
 
i
t
s
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s
.
"
"
"


 
 
 
 
a
i
_
f
l
u
e
n
c
y
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]


 
 
 
 
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]


 
 
 
 
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]




 
 
 
 
v
r
_
s
c
o
r
e
 
=
 
(


 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
a
i
_
f
l
u
e
n
c
y
 
+


 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
 
+


 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
v
r
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y
 
w
i
t
h
 
a
n
 
e
x
a
m
p
l
e
 
e
m
p
l
o
y
e
e


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
i
l
o
c
[
0
]


v
r
_
s
c
o
r
e
_
t
e
s
t
 
=
 
c
a
l
c
u
l
a
t
e
_
i
d
i
o
s
y
n
c
r
a
t
i
c
_
r
e
a
d
i
n
e
s
s
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
,
 
P
A
R
A
M
S
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]
)


p
r
i
n
t
(
f
"
T
e
s
t
 
V
^
R
 
s
c
o
r
e
 
f
o
r
 
E
M
P
0
0
0
:
 
{
v
r
_
s
c
o
r
e
_
t
e
s
t
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
t
h
e
 
c
a
l
c
u
l
a
t
e
d
 
v
r
_
s
c
o
r
e
 
f
o
r
 
a
l
l
 
e
m
p
l
o
y
e
e
s


d
f
_
e
m
p
l
o
y
e
e
s
[
'
v
r
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(


 
 
 
 
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
i
d
i
o
s
y
n
c
r
a
t
i
c
_
r
e
a
d
i
n
e
s
s
(
r
o
w
,
 
P
A
R
A
M
S
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]
)
,


 
 
 
 
a
x
i
s
=
1


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
v
r
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
v
r
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
s
k
i
l
l
s
_
m
a
t
c
h
_
s
c
o
r
e
(
e
m
p
l
o
y
e
e
_
s
k
i
l
l
s
_
s
e
r
i
e
s
,
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
s
_
s
e
r
i
e
s
,
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
s
e
r
i
e
s
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
a
 
s
k
i
l
l
s
 
m
a
t
c
h
 
s
c
o
r
e
 
b
e
t
w
e
e
n
 
a
n
 
e
m
p
l
o
y
e
e
 
a
n
d
 
a
 
j
o
b
 
r
o
l
e
.
"
"
"


 
 
 
 
m
a
t
c
h
_
s
c
o
r
e
 
=
 
0


 
 
 
 
s
k
i
l
l
_
c
o
l
s
 
=
 
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]




 
 
 
 
f
o
r
 
s
k
i
l
l
_
c
o
l
 
i
n
 
s
k
i
l
l
_
c
o
l
s
:


 
 
 
 
 
 
 
 
#
 
E
n
s
u
r
e
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
s
_
s
e
r
i
e
s
 
a
n
d
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
s
e
r
i
e
s
 
a
r
e
 
p
r
o
p
e
r
l
y
 
a
l
i
g
n
e
d


 
 
 
 
 
 
 
 
#
 
I
n
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
s
k
i
l
l
 
i
m
p
o
r
t
a
n
c
e
 
i
s
 
`
s
k
i
l
l
_
X
_
i
m
p
o
r
t
a
n
c
e
`
 
a
n
d
 
r
e
q
u
i
r
e
d
 
s
k
i
l
l
s
 
i
s
 
`
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
X
`


 
 
 
 
 
 
 
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
v
a
l
 
=
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
s
_
s
e
r
i
e
s
[
f
'
r
e
q
u
i
r
e
d
_
{
s
k
i
l
l
_
c
o
l
}
'
]


 
 
 
 
 
 
 
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
v
a
l
 
=
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
s
e
r
i
e
s
[
f
'
{
s
k
i
l
l
_
c
o
l
}
_
i
m
p
o
r
t
a
n
c
e
'
]


 
 
 
 
 
 
 
 
i
n
d
i
v
i
d
u
a
l
_
s
k
i
l
l
_
v
a
l
 
=
 
e
m
p
l
o
y
e
e
_
s
k
i
l
l
s
_
s
e
r
i
e
s
[
s
k
i
l
l
_
c
o
l
]




 
 
 
 
 
 
 
 
#
 
M
a
x
 
p
o
s
s
i
b
l
e
 
i
n
d
i
v
i
d
u
a
l
 
s
k
i
l
l
 
i
s
 
1
0
0
,
 
s
o
 
n
o
r
m
a
l
i
z
e
 
t
o
 
0
-
1
 
b
e
f
o
r
e
 
m
i
n
 
o
p
e
r
a
t
i
o
n


 
 
 
 
 
 
 
 
#
 
t
h
e
n
 
m
u
l
t
i
p
l
y
 
b
y
 
1
0
0
 
f
o
r
 
a
 
f
i
n
a
l
 
s
c
o
r
e
 
o
f
 
0
-
1
0
0


 
 
 
 
 
 
 
 
m
a
t
c
h
_
s
c
o
r
e
 
+
=
 
m
i
n
(
i
n
d
i
v
i
d
u
a
l
_
s
k
i
l
l
_
v
a
l
 
/
 
1
0
0
,
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
v
a
l
 
/
 
1
0
0
)
 
*
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
v
a
l




 
 
 
 
#
 
N
o
r
m
a
l
i
z
e
 
t
h
e
 
t
o
t
a
l
 
m
a
t
c
h
_
s
c
o
r
e
 
b
y
 
t
h
e
 
s
u
m
 
o
f
 
i
m
p
o
r
t
a
n
c
e
 
w
e
i
g
h
t
s
 
t
o
 
g
e
t
 
a
 
s
c
o
r
e
 
0
-
1
,
 
t
h
e
n
 
s
c
a
l
e
 
t
o
 
0
-
1
0
0


 
 
 
 
t
o
t
a
l
_
i
m
p
o
r
t
a
n
c
e
 
=
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
s
e
r
i
e
s
[
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]
.
s
u
m
(
)


 
 
 
 
i
f
 
t
o
t
a
l
_
i
m
p
o
r
t
a
n
c
e
 
=
=
 
0
:
 
#
 
A
v
o
i
d
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o
 
i
f
 
n
o
 
s
k
i
l
l
s
 
d
e
f
i
n
e
d


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
(
m
a
t
c
h
_
s
c
o
r
e
 
/
 
t
o
t
a
l
_
i
m
p
o
r
t
a
n
c
e
)
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




d
e
f
 
c
a
l
c
u
l
a
t
e
_
t
i
m
i
n
g
_
f
a
c
t
o
r
(
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
c
a
r
e
e
r
 
s
t
a
g
e
 
t
i
m
i
n
g
 
f
a
c
t
o
r
.
"
"
"


 
 
 
 
i
f
 
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
 
<
=
 
5
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1
.
0


 
 
 
 
e
l
i
f
 
5
 
<
 
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
 
<
=
 
1
5
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1
.
0


 
 
 
 
e
l
s
e
:
 
#
 
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
 
>
 
1
5


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0
.
8




d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
(
s
k
i
l
l
s
_
m
a
t
c
h
_
s
c
o
r
e
,
 
t
i
m
i
n
g
_
f
a
c
t
o
r
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
a
l
i
g
n
m
e
n
t
 
f
a
c
t
o
r
 
b
a
s
e
d
 
o
n
 
s
k
i
l
l
s
 
m
a
t
c
h
 
a
n
d
 
t
i
m
i
n
g
.
"
"
"


 
 
 
 
#
 
S
c
a
l
e
 
s
k
i
l
l
s
_
m
a
t
c
h
_
s
c
o
r
e
 
f
r
o
m
 
0
-
1
0
0
 
t
o
 
0
-
1
 
f
o
r
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n


 
 
 
 
a
l
i
g
n
m
e
n
t
 
=
 
(
s
k
i
l
l
s
_
m
a
t
c
h
_
s
c
o
r
e
 
/
 
1
0
0
)
 
*
 
t
i
m
i
n
g
_
f
a
c
t
o
r


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
a
l
i
g
n
m
e
n
t
,
 
0
,
 
1
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
s
 
i
m
m
e
d
i
a
t
e
l
y
 
w
i
t
h
 
a
n
 
e
x
a
m
p
l
e
 
e
m
p
l
o
y
e
e
 
a
n
d
 
t
h
e
i
r
 
j
o
b
 
r
o
l
e


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
i
l
o
c
[
0
]


e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
_
r
o
w
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
o
c
c
u
p
a
t
i
o
n
'
]
 
=
=
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
j
o
b
_
r
o
l
e
'
]
]
.
i
l
o
c
[
0
]




#
 
E
x
t
r
a
c
t
 
e
m
p
l
o
y
e
e
 
s
k
i
l
l
s
 
f
o
r
 
t
h
e
 
c
a
l
c
u
l
a
t
i
o
n


e
m
p
l
o
y
e
e
_
s
k
i
l
l
_
d
a
t
a
 
=
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]


#
 
E
x
t
r
a
c
t
 
r
e
q
u
i
r
e
d
 
s
k
i
l
l
s
 
a
n
d
 
i
m
p
o
r
t
a
n
c
e
 
f
r
o
m
 
t
h
e
 
o
c
c
u
p
a
t
i
o
n
 
d
a
t
a
 
r
o
w


r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
d
a
t
a
 
=
 
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
_
r
o
w
[
[
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]


s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
d
a
t
a
 
=
 
e
x
a
m
p
l
e
_
o
c
c
u
p
a
t
i
o
n
_
r
o
w
[
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]




s
k
i
l
l
s
_
m
a
t
c
h
 
=
 
c
a
l
c
u
l
a
t
e
_
s
k
i
l
l
s
_
m
a
t
c
h
_
s
c
o
r
e
(
e
m
p
l
o
y
e
e
_
s
k
i
l
l
_
d
a
t
a
,
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
d
a
t
a
,
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
d
a
t
a
)


t
i
m
i
n
g
_
f
a
c
t
o
r
 
=
 
c
a
l
c
u
l
a
t
e
_
t
i
m
i
n
g
_
f
a
c
t
o
r
(
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
]
)


a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
=
 
c
a
l
c
u
l
a
t
e
_
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
(
s
k
i
l
l
s
_
m
a
t
c
h
,
 
t
i
m
i
n
g
_
f
a
c
t
o
r
)




p
r
i
n
t
(
f
"
T
e
s
t
 
S
k
i
l
l
s
 
M
a
t
c
h
 
S
c
o
r
e
 
f
o
r
 
E
M
P
0
0
0
 
(
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
j
o
b
_
r
o
l
e
'
]
}
)
:
 
{
s
k
i
l
l
s
_
m
a
t
c
h
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
T
e
s
t
 
T
i
m
i
n
g
 
F
a
c
t
o
r
 
f
o
r
 
E
M
P
0
0
0
 
(
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
]
}
 
y
e
a
r
s
 
e
x
p
)
:
 
{
t
i
m
i
n
g
_
f
a
c
t
o
r
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
T
e
s
t
 
A
l
i
g
n
m
e
n
t
 
F
a
c
t
o
r
 
f
o
r
 
E
M
P
0
0
0
:
 
{
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
f
o
r
 
a
l
l
 
e
m
p
l
o
y
e
e
s


d
e
f
 
g
e
t
_
a
l
i
g
n
m
e
n
t
_
f
o
r
_
e
m
p
l
o
y
e
e
(
e
m
p
l
o
y
e
e
_
r
o
w
)
:


 
 
 
 
j
o
b
_
r
o
l
e
 
=
 
e
m
p
l
o
y
e
e
_
r
o
w
[
'
j
o
b
_
r
o
l
e
'
]


 
 
 
 
#
 
E
n
s
u
r
e
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
i
s
 
a
c
c
e
s
s
i
b
l
e
 
i
n
 
t
h
i
s
 
s
c
o
p
e
 
(
f
r
o
m
 
p
r
e
v
i
o
u
s
 
c
e
l
l
s
)


 
 
 
 
g
l
o
b
a
l
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s


 
 
 
 
o
c
c
u
p
a
t
i
o
n
_
r
o
w
 
=
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
d
f
_
o
c
c
u
p
a
t
i
o
n
s
[
'
o
c
c
u
p
a
t
i
o
n
'
]
 
=
=
 
j
o
b
_
r
o
l
e
]
.
i
l
o
c
[
0
]




 
 
 
 
#
 
C
o
r
r
e
c
t
e
d
 
f
-
s
t
r
i
n
g
 
s
y
n
t
a
x
 
f
r
o
m
 
\
'
a
\
'
 
t
o
 
"
a
"


 
 
 
 
e
m
p
l
o
y
e
e
_
s
k
i
l
l
_
d
a
t
a
 
=
 
e
m
p
l
o
y
e
e
_
r
o
w
[
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]


 
 
 
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
d
a
t
a
 
=
 
o
c
c
u
p
a
t
i
o
n
_
r
o
w
[
[
f
'
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]


 
 
 
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
d
a
t
a
 
=
 
o
c
c
u
p
a
t
i
o
n
_
r
o
w
[
[
f
'
s
k
i
l
l
_
{
c
h
r
(
o
r
d
(
"
a
"
)
 
+
 
i
)
}
_
i
m
p
o
r
t
a
n
c
e
'
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
0
)
]
]




 
 
 
 
#
 
E
n
s
u
r
e
 
t
h
e
s
e
 
f
u
n
c
t
i
o
n
s
 
a
r
e
 
d
e
f
i
n
e
d
 
a
n
d
 
a
c
c
e
s
s
i
b
l
e
 
(
f
r
o
m
 
p
r
e
v
i
o
u
s
 
c
e
l
l
s
)


 
 
 
 
#
 
T
h
e
y
 
s
h
o
u
l
d
 
h
a
v
e
 
b
e
e
n
 
d
e
f
i
n
e
d
 
i
n
 
p
r
e
v
i
o
u
s
 
c
e
l
l
s
 
o
r
 
i
m
p
o
r
t
e
d
.


 
 
 
 
#
 
F
o
r
 
r
o
b
u
s
t
n
e
s
s
 
i
n
 
a
 
t
e
s
t
 
e
n
v
i
r
o
n
m
e
n
t
,
 
t
h
e
y
 
w
o
u
l
d
 
t
y
p
i
c
a
l
l
y
 
b
e
 
i
m
p
o
r
t
e
d
 
o
r
 
p
a
s
s
e
d
.


 
 
 
 
#
 
A
s
s
u
m
i
n
g
 
t
h
e
y
 
a
r
e
 
g
l
o
b
a
l
l
y
 
a
v
a
i
l
a
b
l
e
 
f
r
o
m
 
t
h
e
 
n
o
t
e
b
o
o
k
'
s
 
e
x
e
c
u
t
i
o
n
 
f
l
o
w
.


 
 
 
 
s
k
i
l
l
s
_
m
a
t
c
h
 
=
 
c
a
l
c
u
l
a
t
e
_
s
k
i
l
l
s
_
m
a
t
c
h
_
s
c
o
r
e
(
e
m
p
l
o
y
e
e
_
s
k
i
l
l
_
d
a
t
a
,
 
r
e
q
u
i
r
e
d
_
s
k
i
l
l
_
d
a
t
a
,
 
s
k
i
l
l
_
i
m
p
o
r
t
a
n
c
e
_
d
a
t
a
)


 
 
 
 
t
i
m
i
n
g
_
f
a
c
t
o
r
 
=
 
c
a
l
c
u
l
a
t
e
_
t
i
m
i
n
g
_
f
a
c
t
o
r
(
e
m
p
l
o
y
e
e
_
r
o
w
[
'
y
e
a
r
s
_
e
x
p
e
r
i
e
n
c
e
'
]
)


 
 
 
 
r
e
t
u
r
n
 
c
a
l
c
u
l
a
t
e
_
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
(
s
k
i
l
l
s
_
m
a
t
c
h
,
 
t
i
m
i
n
g
_
f
a
c
t
o
r
)




d
f
_
e
m
p
l
o
y
e
e
s
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(
g
e
t
_
a
l
i
g
n
m
e
n
t
_
f
o
r
_
e
m
p
l
o
y
e
e
,
 
a
x
i
s
=
1
)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]
]
.
h
e
a
d
(
)
)
d
e
f
 
c
a
l
c
u
l
a
t
e
_
s
y
n
e
r
g
y
(
v
r
_
s
c
o
r
e
,
 
h
r
_
s
c
o
r
e
,
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
S
y
n
e
r
g
y
%
.
"
"
"


 
 
 
 
#
 
E
n
s
u
r
e
 
v
r
_
s
c
o
r
e
 
a
n
d
 
h
r
_
s
c
o
r
e
 
a
r
e
 
b
e
t
w
e
e
n
 
0
-
1
0
0


 
 
 
 
v
r
_
n
o
r
m
 
=
 
v
r
_
s
c
o
r
e
 
/
 
1
0
0


 
 
 
 
h
r
_
n
o
r
m
 
=
 
h
r
_
s
c
o
r
e
 
/
 
1
0
0




 
 
 
 
s
y
n
e
r
g
y
 
=
 
(
v
r
_
n
o
r
m
 
*
 
h
r
_
n
o
r
m
)
 
*
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
s
y
n
e
r
g
y
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
i
l
o
c
[
0
]


s
y
n
e
r
g
y
_
s
c
o
r
e
_
t
e
s
t
 
=
 
c
a
l
c
u
l
a
t
e
_
s
y
n
e
r
g
y
(


 
 
 
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
v
r
_
s
c
o
r
e
'
]
,


 
 
 
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,


 
 
 
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]


)


p
r
i
n
t
(
f
"
T
e
s
t
 
S
y
n
e
r
g
y
 
S
c
o
r
e
 
f
o
r
 
E
M
P
0
0
0
:
 
{
s
y
n
e
r
g
y
_
s
c
o
r
e
_
t
e
s
t
:
.
2
f
}
"
)
#
 
U
p
d
a
t
e
 
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
t
h
e
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
s
y
n
e
r
g
y
_
s
c
o
r
e
 
f
o
r
 
a
l
l
 
e
m
p
l
o
y
e
e
s


d
f
_
e
m
p
l
o
y
e
e
s
[
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(


 
 
 
 
l
a
m
b
d
a
 
r
o
w
:
 
c
a
l
c
u
l
a
t
e
_
s
y
n
e
r
g
y
(
r
o
w
[
'
v
r
_
s
c
o
r
e
'
]
,
 
r
o
w
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,
 
r
o
w
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]
)
,


 
 
 
 
a
x
i
s
=
1


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
n
e
w
l
y
 
c
a
l
c
u
l
a
t
e
d
 
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
v
r
_
s
c
o
r
e
'
,
 
'
h
r
_
r
_
s
c
o
r
e
'
,
 
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
,
 
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)
#
 
T
h
e
 
`
c
a
l
c
u
l
a
t
e
_
a
i
_
r
`
 
f
u
n
c
t
i
o
n
 
w
a
s
 
a
l
r
e
a
d
y
 
d
e
f
i
n
e
d
 
i
n
 
S
e
c
t
i
o
n
 
1
.


#
 
N
o
w
,
 
a
p
p
l
y
 
i
t
 
t
o
 
a
l
l
 
e
m
p
l
o
y
e
e
s
 
i
n
 
d
f
_
e
m
p
l
o
y
e
e
s
.




d
f
_
e
m
p
l
o
y
e
e
s
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
a
p
p
l
y
(


 
 
 
 
l
a
m
b
d
a
 
r
o
w
:


 
 
 
 
 
 
 
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
[
'
v
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
[
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
P
A
R
A
M
S
[
'
a
l
p
h
a
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
P
A
R
A
M
S
[
'
b
e
t
a
'
]


 
 
 
 
 
 
 
 
)
,


 
 
 
 
a
x
i
s
=
1


)




p
r
i
n
t
(
"
d
f
_
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
a
l
l
 
c
a
l
c
u
l
a
t
e
d
 
A
I
-
R
 
c
o
m
p
o
n
e
n
t
s
 
a
n
d
 
f
i
n
a
l
 
s
c
o
r
e
:
"
)


p
r
i
n
t
(
d
f
_
e
m
p
l
o
y
e
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
d
e
p
a
r
t
m
e
n
t
'
,
 
'
v
r
_
s
c
o
r
e
'
,
 
'
h
r
_
r
_
s
c
o
r
e
'
,
 
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
,
 
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
)




#
 
C
a
l
c
u
l
a
t
e
 
a
n
d
 
p
r
i
n
t
 
t
h
e
 
a
v
e
r
a
g
e
 
A
I
-
R
 
s
c
o
r
e
 
f
o
r
 
t
h
e
 
e
n
t
i
r
e
 
w
o
r
k
f
o
r
c
e


a
v
e
r
a
g
e
_
a
i
_
r
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
.
m
e
a
n
(
)


p
r
i
n
t
(
f
"
\
n
A
v
e
r
a
g
e
 
A
I
-
R
 
s
c
o
r
e
 
f
o
r
 
t
h
e
 
e
n
t
i
r
e
 
w
o
r
k
f
o
r
c
e
:
 
{
a
v
e
r
a
g
e
_
a
i
_
r
:
.
2
f
}
"
)
d
e
f
 
g
e
n
e
r
a
t
e
_
a
i
_
r
_
r
e
p
o
r
t
_
s
u
m
m
a
r
y
(
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
)
:


 
 
 
 
"
"
"
A
g
g
r
e
g
a
t
e
s
 
A
I
-
R
 
s
c
o
r
e
s
 
b
y
 
g
r
o
u
p
 
(
e
.
g
.
,
 
d
e
p
a
r
t
m
e
n
t
,
 
j
o
b
 
r
o
l
e
)
.
"
"
"


 
 
 
 
s
u
m
m
a
r
y
_
d
f
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
.
g
r
o
u
p
b
y
(
[
'
d
e
p
a
r
t
m
e
n
t
'
,
 
'
j
o
b
_
r
o
l
e
'
]
)
.
a
g
g
(


 
 
 
 
 
 
 
 
a
v
e
r
a
g
e
_
c
u
r
r
e
n
t
_
a
i
_
r
=
(
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
,
 
'
m
e
a
n
'
)
,


 
 
 
 
 
 
 
 
a
v
e
r
a
g
e
_
v
r
_
s
c
o
r
e
=
(
'
v
r
_
s
c
o
r
e
'
,
 
'
m
e
a
n
'
)
,


 
 
 
 
 
 
 
 
a
v
e
r
a
g
e
_
h
r
_
r
_
s
c
o
r
e
=
(
'
h
r
_
r
_
s
c
o
r
e
'
,
 
'
m
e
a
n
'
)
,


 
 
 
 
 
 
 
 
a
v
e
r
a
g
e
_
s
y
n
e
r
g
y
_
s
c
o
r
e
=
(
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
,
 
'
m
e
a
n
'
)
,


 
 
 
 
 
 
 
 
n
u
m
_
e
m
p
l
o
y
e
e
s
=
(
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
c
o
u
n
t
'
)


 
 
 
 
)
.
r
e
s
e
t
_
i
n
d
e
x
(
)


 
 
 
 
r
e
t
u
r
n
 
s
u
m
m
a
r
y
_
d
f
.
r
o
u
n
d
(
2
)




d
e
f
 
p
l
o
t
_
s
k
i
l
l
s
_
g
a
p
_
h
e
a
t
m
a
p
(
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
,
 
g
r
o
u
p
_
b
y
_
c
o
l
u
m
n
)
:


 
 
 
 
"
"
"
V
i
s
u
a
l
i
z
e
s
 
s
t
r
e
n
g
t
h
s
 
a
n
d
 
w
e
a
k
n
e
s
s
e
s
 
o
f
 
V
^
R
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s
 
u
s
i
n
g
 
a
 
h
e
a
t
m
a
p
.
"
"
"


 
 
 
 
v
r
_
s
u
b
_
c
o
m
p
o
n
e
n
t
s
 
=
 
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
,
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
,
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]


 
 
 
 
h
e
a
t
m
a
p
_
d
a
t
a
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
.
g
r
o
u
p
b
y
(
g
r
o
u
p
_
b
y
_
c
o
l
u
m
n
)
[
v
r
_
s
u
b
_
c
o
m
p
o
n
e
n
t
s
]
.
m
e
a
n
(
)




 
 
 
 
p
l
t
.
f
i
g
u
r
e
(
f
i
g
s
i
z
e
=
(
1
0
,
 
6
)
)


 
 
 
 
s
n
s
.
h
e
a
t
m
a
p
(
h
e
a
t
m
a
p
_
d
a
t
a
,
 
a
n
n
o
t
=
T
r
u
e
,
 
c
m
a
p
=
'
v
i
r
i
d
i
s
'
,
 
f
m
t
=
"
.
1
f
"
,
 
l
i
n
e
w
i
d
t
h
s
=
.
5
)


 
 
 
 
p
l
t
.
t
i
t
l
e
(
f
'
A
v
e
r
a
g
e
 
V
^
R
 
S
u
b
-
C
o
m
p
o
n
e
n
t
 
S
c
o
r
e
s
 
b
y
 
{
g
r
o
u
p
_
b
y
_
c
o
l
u
m
n
}
'
)


 
 
 
 
p
l
t
.
y
l
a
b
e
l
(
g
r
o
u
p
_
b
y
_
c
o
l
u
m
n
)


 
 
 
 
p
l
t
.
x
l
a
b
e
l
(
'
V
^
R
 
S
u
b
-
C
o
m
p
o
n
e
n
t
'
)


 
 
 
 
p
l
t
.
x
t
i
c
k
s
(
r
o
t
a
t
i
o
n
=
4
5
,
 
h
a
=
'
r
i
g
h
t
'
)


 
 
 
 
p
l
t
.
t
i
g
h
t
_
l
a
y
o
u
t
(
)


 
 
 
 
p
l
t
.
s
h
o
w
(
)




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
s
 
i
m
m
e
d
i
a
t
e
l
y


p
r
i
n
t
(
"
T
e
s
t
 
S
u
m
m
a
r
y
 
R
e
p
o
r
t
:
"
)


p
r
i
n
t
(
g
e
n
e
r
a
t
e
_
a
i
_
r
_
r
e
p
o
r
t
_
s
u
m
m
a
r
y
(
d
f
_
e
m
p
l
o
y
e
e
s
)
.
h
e
a
d
(
)
)




#
 
N
o
 
p
l
o
t
 
g
e
n
e
r
a
t
e
d
 
d
u
r
i
n
g
 
t
e
s
t
,
 
o
n
l
y
 
f
o
r
 
e
x
e
c
u
t
i
o
n
 
c
e
l
l
#
 
G
e
n
e
r
a
t
e
 
a
n
d
 
d
i
s
p
l
a
y
 
t
h
e
 
s
u
m
m
a
r
y
 
t
a
b
l
e


a
i
_
r
_
s
u
m
m
a
r
y
_
r
e
p
o
r
t
 
=
 
g
e
n
e
r
a
t
e
_
a
i
_
r
_
r
e
p
o
r
t
_
s
u
m
m
a
r
y
(
d
f
_
e
m
p
l
o
y
e
e
s
)


p
r
i
n
t
(
"
W
o
r
k
f
o
r
c
e
 
A
I
-
R
e
a
d
i
n
e
s
s
 
S
u
m
m
a
r
y
 
R
e
p
o
r
t
 
b
y
 
D
e
p
a
r
t
m
e
n
t
 
a
n
d
 
J
o
b
 
R
o
l
e
:
"
)


p
r
i
n
t
(
a
i
_
r
_
s
u
m
m
a
r
y
_
r
e
p
o
r
t
.
t
o
_
s
t
r
i
n
g
(
)
)




#
 
G
e
n
e
r
a
t
e
 
t
h
e
 
s
k
i
l
l
s
 
g
a
p
 
h
e
a
t
m
a
p


p
l
o
t
_
s
k
i
l
l
s
_
g
a
p
_
h
e
a
t
m
a
p
(
d
f
_
e
m
p
l
o
y
e
e
s
,
 
'
j
o
b
_
r
o
l
e
'
)


p
l
o
t
_
s
k
i
l
l
s
_
g
a
p
_
h
e
a
t
m
a
p
(
d
f
_
e
m
p
l
o
y
e
e
s
,
 
'
d
e
p
a
r
t
m
e
n
t
'
)
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p


i
m
p
o
r
t
 
p
y
t
e
s
t


i
m
p
o
r
t
 
r
a
n
d
o
m


i
m
p
o
r
t
 
m
a
t
p
l
o
t
l
i
b
.
p
y
p
l
o
t
 
a
s
 
p
l
t


i
m
p
o
r
t
 
s
e
a
b
o
r
n
 
a
s
 
s
n
s


i
m
p
o
r
t
 
c
o
p
y




#
 
-
-
-
 
R
e
-
d
e
f
i
n
i
n
g
 
d
e
p
e
n
d
e
n
t
 
f
u
n
c
t
i
o
n
s
 
f
o
r
 
s
e
l
f
-
c
o
n
t
a
i
n
e
d
 
t
e
s
t
s
 
-
-
-




#
 
F
r
o
m
 
C
e
l
l
 
4


d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(
v
r
_
s
c
o
r
e
,
 
h
r
_
s
c
o
r
e
,
 
s
y
n
e
r
g
y
_
s
c
o
r
e
,
 
a
l
p
h
a
,
 
b
e
t
a
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
t
h
e
 
o
v
e
r
a
l
l
 
A
I
-
R
e
a
d
i
n
e
s
s
 
S
c
o
r
e
.
"
"
"


 
 
 
 
v
r
_
s
c
o
r
e
 
=
 
n
p
.
c
l
i
p
(
v
r
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)


 
 
 
 
h
r
_
s
c
o
r
e
 
=
 
n
p
.
c
l
i
p
(
h
r
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)


 
 
 
 
s
y
n
e
r
g
y
_
s
c
o
r
e
 
=
 
n
p
.
c
l
i
p
(
s
y
n
e
r
g
y
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)


 
 
 
 
a
i
_
r
 
=
 
(
a
l
p
h
a
 
*
 
v
r
_
s
c
o
r
e
)
 
+
 
(
(
1
 
-
 
a
l
p
h
a
)
 
*
 
h
r
_
s
c
o
r
e
)
 
+
 
(
b
e
t
a
 
*
 
s
y
n
e
r
g
y
_
s
c
o
r
e
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
a
i
_
r
,
 
0
,
 
1
0
0
)




#
 
F
r
o
m
 
C
e
l
l
 
4
5


d
e
f
 
c
a
l
c
u
l
a
t
e
_
i
d
i
o
s
y
n
c
r
a
t
i
c
_
r
e
a
d
i
n
e
s
s
(
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
,
 
v
r
_
w
e
i
g
h
t
s
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
t
o
t
a
l
 
V
^
R
 
s
c
o
r
e
 
f
r
o
m
 
i
t
s
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s
.
"
"
"


 
 
 
 
a
i
_
f
l
u
e
n
c
y
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]


 
 
 
 
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]


 
 
 
 
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
 
=
 
e
m
p
l
o
y
e
e
_
d
a
t
a
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]


 
 
 
 
v
r
_
s
c
o
r
e
 
=
 
(


 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
a
i
_
f
l
u
e
n
c
y
 
+


 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
 
+


 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
v
r
_
s
c
o
r
e
,
 
0
,
 
1
0
0
)




#
 
F
r
o
m
 
C
e
l
l
 
5
3


d
e
f
 
c
a
l
c
u
l
a
t
e
_
s
y
n
e
r
g
y
(
v
r
_
s
c
o
r
e
,
 
h
r
_
s
c
o
r
e
,
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
)
:


 
 
 
 
"
"
"
C
o
m
p
u
t
e
s
 
S
y
n
e
r
g
y
%
.
"
"
"


 
 
 
 
v
r
_
n
o
r
m
 
=
 
v
r
_
s
c
o
r
e
 
/
 
1
0
0


 
 
 
 
h
r
_
n
o
r
m
 
=
 
h
r
_
s
c
o
r
e
 
/
 
1
0
0


 
 
 
 
s
y
n
e
r
g
y
 
=
 
(
v
r
_
n
o
r
m
 
*
 
h
r
_
n
o
r
m
)
 
*
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r


 
 
 
 
r
e
t
u
r
n
 
n
p
.
c
l
i
p
(
s
y
n
e
r
g
y
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




#
 
T
h
e
 
f
u
n
c
t
i
o
n
 
t
o
 
b
e
 
t
e
s
t
e
d
:
 
p
l
o
t
_
c
u
r
r
e
n
t
_
v
s
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r


#
 
T
h
i
s
 
i
s
 
a
 
p
l
o
t
t
i
n
g
 
f
u
n
c
t
i
o
n
,
 
p
e
r
 
r
e
q
u
i
r
e
m
e
n
t
 
#
5
,
 
w
e
 
r
e
t
u
r
n
 
'
N
O
_
T
E
S
T
S
_
N
E
E
D
E
D
'
 
f
o
r
 
i
t


#
 
H
o
w
e
v
e
r
,
 
f
o
r
 
c
o
m
p
l
e
t
e
n
e
s
s
 
w
i
t
h
i
n
 
t
h
e
 
t
e
s
t
 
s
u
i
t
e
 
s
t
r
u
c
t
u
r
e
,
 
w
e
 
k
e
e
p
 
i
t
s
 
d
e
f
i
n
i
t
i
o
n


#
 
b
u
t
 
d
o
 
n
o
t
 
g
e
n
e
r
a
t
e
 
e
x
p
l
i
c
i
t
 
t
e
s
t
s
 
t
h
a
t
 
r
e
l
y
 
o
n
 
m
a
t
p
l
o
t
l
i
b
.
s
h
o
w
(
)
.


d
e
f
 
p
l
o
t
_
c
u
r
r
e
n
t
_
v
s
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
(
c
u
r
r
e
n
t
_
s
c
o
r
e
s
,
 
p
r
o
j
e
c
t
e
d
_
s
c
o
r
e
s
,
 
s
c
e
n
a
r
i
o
_
n
a
m
e
s
)
:


 
 
 
 
"
"
"
C
o
m
p
a
r
e
s
 
c
u
r
r
e
n
t
 
v
s
.
 
p
r
o
j
e
c
t
e
d
 
A
I
-
R
 
f
o
r
 
a
n
 
i
n
d
i
v
i
d
u
a
l
 
o
r
 
g
r
o
u
p
.
"
"
"


 
 
 
 
l
a
b
e
l
s
 
=
 
[
'
C
u
r
r
e
n
t
 
A
I
-
R
'
]
 
+
 
[
f
'
P
r
o
j
e
c
t
e
d
 
A
I
-
R
 
(
{
s
}
)
'
 
f
o
r
 
s
 
i
n
 
s
c
e
n
a
r
i
o
_
n
a
m
e
s
]


 
 
 
 
v
a
l
u
e
s
 
=
 
[
c
u
r
r
e
n
t
_
s
c
o
r
e
s
]
 
+
 
p
r
o
j
e
c
t
e
d
_
s
c
o
r
e
s




 
 
 
 
p
l
t
.
f
i
g
u
r
e
(
f
i
g
s
i
z
e
=
(
8
,
 
5
)
)


 
 
 
 
p
l
t
.
b
a
r
(
l
a
b
e
l
s
,
 
v
a
l
u
e
s
,
 
c
o
l
o
r
=
[
'
s
k
y
b
l
u
e
'
]
 
+
 
[
'
l
i
g
h
t
c
o
r
a
l
'
]
 
*
 
l
e
n
(
p
r
o
j
e
c
t
e
d
_
s
c
o
r
e
s
)
)


 
 
 
 
p
l
t
.
y
l
a
b
e
l
(
'
A
I
-
R
e
a
d
i
n
e
s
s
 
S
c
o
r
e
'
)


 
 
 
 
p
l
t
.
t
i
t
l
e
(
'
C
u
r
r
e
n
t
 
v
s
.
 
P
r
o
j
e
c
t
e
d
 
A
I
-
R
e
a
d
i
n
e
s
s
 
S
c
o
r
e
'
)


 
 
 
 
p
l
t
.
y
l
i
m
(
0
,
 
1
0
0
)


 
 
 
 
p
l
t
.
g
r
i
d
(
a
x
i
s
=
'
y
'
,
 
l
i
n
e
s
t
y
l
e
=
'
-
-
'
,
 
a
l
p
h
a
=
0
.
7
)


 
 
 
 
#
 
p
l
t
.
s
h
o
w
(
)
 
#
 
C
o
m
m
e
n
t
 
o
u
t
 
p
l
t
.
s
h
o
w
(
)
 
f
o
r
 
t
e
s
t
i
n
g
 
e
n
v
i
r
o
n
m
e
n
t
s




#
 
T
h
e
 
m
a
i
n
 
f
u
n
c
t
i
o
n
 
t
o
 
b
e
 
t
e
s
t
e
d
 
i
n
 
t
h
i
s
 
c
e
l
l


d
e
f
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(
e
m
p
l
o
y
e
e
_
i
d
,
 
p
a
t
h
w
a
y
_
i
d
,
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
,
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,
 
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
,
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
_
d
a
t
a
,
 
d
f
_
p
a
t
h
w
a
y
s
_
d
a
t
a
,
 
p
a
r
a
m
s
)
:


 
 
 
 
"
"
"
S
i
m
u
l
a
t
e
s
 
t
h
e
 
i
m
p
a
c
t
 
o
f
 
a
 
l
e
a
r
n
i
n
g
 
p
a
t
h
w
a
y
 
o
n
 
a
n
 
i
n
d
i
v
i
d
u
a
l
'
s
 
A
I
-
R
 
s
c
o
r
e
.
"
"
"


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
o
r
i
g
i
n
a
l
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
[
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
]
.
i
l
o
c
[
0
]


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
 
=
 
e
m
p
l
o
y
e
e
_
r
o
w
_
o
r
i
g
i
n
a
l
.
c
o
p
y
(
d
e
e
p
=
T
r
u
e
)




 
 
 
 
p
a
t
h
w
a
y
_
i
n
f
o
 
=
 
d
f
_
p
a
t
h
w
a
y
s
_
d
a
t
a
[
d
f
_
p
a
t
h
w
a
y
s
_
d
a
t
a
[
'
p
a
t
h
w
a
y
_
i
d
'
]
 
=
=
 
p
a
t
h
w
a
y
_
i
d
]
.
i
l
o
c
[
0
]




 
 
 
 
#
 
A
p
p
l
y
 
i
m
p
a
c
t
 
t
o
 
V
R
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
]
 
*
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
*
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
)


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
]
 
*
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
*
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
)


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
]
 
*
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
*
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
)




 
 
 
 
#
 
R
e
c
a
l
c
u
l
a
t
e
 
V
R
 
s
c
o
r
e


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
v
r
_
s
c
o
r
e
'
]
 
=
 
c
a
l
c
u
l
a
t
e
_
i
d
i
o
s
y
n
c
r
a
t
i
c
_
r
e
a
d
i
n
e
s
s
(
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
,
 
p
a
r
a
m
s
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]
)




 
 
 
 
#
 
R
e
c
a
l
c
u
l
a
t
e
 
S
y
n
e
r
g
y
 
(
w
h
i
c
h
 
d
e
p
e
n
d
s
 
o
n
 
V
R
)


 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
 
=
 
c
a
l
c
u
l
a
t
e
_
s
y
n
e
r
g
y
(


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
v
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]


 
 
 
 
)




 
 
 
 
#
 
R
e
c
a
l
c
u
l
a
t
e
 
o
v
e
r
a
l
l
 
A
I
-
R
 
s
c
o
r
e


 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
v
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
r
o
w
_
s
i
m
[
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
p
a
r
a
m
s
[
'
a
l
p
h
a
'
]
,


 
 
 
 
 
 
 
 
p
a
r
a
m
s
[
'
b
e
t
a
'
]


 
 
 
 
)




 
 
 
 
d
e
l
t
a
_
a
i
_
r
 
=
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
-
 
e
m
p
l
o
y
e
e
_
r
o
w
_
o
r
i
g
i
n
a
l
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]




 
 
 
 
r
e
t
u
r
n
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
d
e
l
t
a
_
a
i
_
r
,
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
p
a
t
h
w
a
y
_
n
a
m
e
'
]




#
 
-
-
-
 
P
y
t
e
s
t
 
f
i
x
t
u
r
e
s
 
a
n
d
 
t
e
s
t
s
 
-
-
-




@
p
y
t
e
s
t
.
f
i
x
t
u
r
e


d
e
f
 
m
o
c
k
_
p
a
r
a
m
s
(
)
:


 
 
 
 
"
"
"
M
o
c
k
 
P
A
R
A
M
S
 
d
i
c
t
i
o
n
a
r
y
 
w
i
t
h
 
r
e
l
e
v
a
n
t
 
w
e
i
g
h
t
s
 
f
o
r
 
t
e
s
t
i
n
g
.
"
"
"


 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
'
a
l
p
h
a
'
:
 
0
.
6
,


 
 
 
 
 
 
 
 
'
b
e
t
a
'
:
 
0
.
1
5
,


 
 
 
 
 
 
 
 
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
:
 
{


 
 
 
 
 
 
 
 
 
 
 
 
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
4
5
,


 
 
 
 
 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
3
5
,


 
 
 
 
 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
:
 
0
.
2
0


 
 
 
 
 
 
 
 
}


 
 
 
 
}




@
p
y
t
e
s
t
.
f
i
x
t
u
r
e


d
e
f
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
(
)
:


 
 
 
 
"
"
"
M
o
c
k
 
d
f
_
e
m
p
l
o
y
e
e
s
 
D
a
t
a
F
r
a
m
e
 
w
i
t
h
 
n
e
c
e
s
s
a
r
y
 
c
o
l
u
m
n
s
.
"
"
"


 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
{


 
 
 
 
 
 
 
 
'
e
m
p
l
o
y
e
e
_
i
d
'
:
 
[
'
E
M
P
0
0
1
'
,
 
'
E
M
P
0
0
2
'
]
,


 
 
 
 
 
 
 
 
'
j
o
b
_
r
o
l
e
'
:
 
[
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
,
 
'
H
R
 
S
p
e
c
i
a
l
i
s
t
'
]
,


 
 
 
 
 
 
 
 
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
:
 
[
6
0
.
0
,
 
4
0
.
0
]
,


 
 
 
 
 
 
 
 
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
:
 
[
7
0
.
0
,
 
3
0
.
0
]
,


 
 
 
 
 
 
 
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
:
 
[
6
5
.
0
,
 
5
0
.
0
]
,


 
 
 
 
 
 
 
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
:
 
[
7
5
.
0
,
 
4
5
.
0
]
,


 
 
 
 
 
 
 
 
'
h
r
_
r
_
s
c
o
r
e
'
:
 
[
8
0
.
0
,
 
5
5
.
0
]
,


 
 
 
 
 
 
 
 
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
:
 
[
0
.
8
,
 
0
.
6
]
,


 
 
 
 
 
 
 
 
'
v
r
_
s
c
o
r
e
'
:
 
[
0
.
0
,
 
0
.
0
]
,
 
#
 
T
h
e
s
e
 
w
i
l
l
 
b
e
 
r
e
c
a
l
c
u
l
a
t
e
d
 
o
r
 
o
v
e
r
w
r
i
t
t
e
n


 
 
 
 
 
 
 
 
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
:
 
[
0
.
0
,
 
0
.
0
]
 
#
 
T
h
e
s
e
 
w
i
l
l
 
b
e
 
r
e
c
a
l
c
u
l
a
t
e
d
 
o
r
 
o
v
e
r
w
r
i
t
t
e
n


 
 
 
 
}
)




@
p
y
t
e
s
t
.
f
i
x
t
u
r
e


d
e
f
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
(
)
:


 
 
 
 
"
"
"
M
o
c
k
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
D
a
t
a
F
r
a
m
e
 
(
m
i
n
i
m
a
l
 
f
o
r
 
t
h
i
s
 
t
e
s
t
'
s
 
n
e
e
d
s
)
.
"
"
"


 
 
 
 
#
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
d
o
e
s
n
'
t
 
d
i
r
e
c
t
l
y
 
u
s
e
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
 
d
a
t
a
 
b
e
s
i
d
e
s
 
e
m
p
l
o
y
e
e
 
j
o
b
_
r
o
l
e
 
l
o
o
k
u
p
.


 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
{


 
 
 
 
 
 
 
 
'
o
c
c
u
p
a
t
i
o
n
'
:
 
[
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
,
 
'
H
R
 
S
p
e
c
i
a
l
i
s
t
'
]


 
 
 
 
}
)




@
p
y
t
e
s
t
.
f
i
x
t
u
r
e


d
e
f
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
(
)
:


 
 
 
 
"
"
"
M
o
c
k
 
d
f
_
p
a
t
h
w
a
y
s
 
D
a
t
a
F
r
a
m
e
 
w
i
t
h
 
p
a
t
h
w
a
y
 
i
m
p
a
c
t
 
c
o
e
f
f
i
c
i
e
n
t
s
.
"
"
"


 
 
 
 
r
e
t
u
r
n
 
p
d
.
D
a
t
a
F
r
a
m
e
(
{


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
i
d
'
:
 
[
'
P
A
T
H
0
1
'
,
 
'
P
A
T
H
0
2
'
]
,


 
 
 
 
 
 
 
 
'
p
a
t
h
w
a
y
_
n
a
m
e
'
:
 
[
'
A
I
 
F
u
n
d
a
m
e
n
t
a
l
s
'
,
 
'
D
o
m
a
i
n
 
D
e
e
p
 
D
i
v
e
'
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
:
 
[
1
0
,
 
2
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
:
 
[
5
,
 
1
5
]
,


 
 
 
 
 
 
 
 
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
:
 
[
3
,
 
5
]


 
 
 
 
}
)






c
l
a
s
s
 
T
e
s
t
S
i
m
u
l
a
t
e
P
a
t
h
w
a
y
I
m
p
a
c
t
:




 
 
 
 
d
e
f
 
t
e
s
t
_
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
_
b
a
s
i
c
_
f
u
l
l
_
c
o
m
p
l
e
t
i
o
n
(
s
e
l
f
,
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
 
=
 
'
E
M
P
0
0
1
'


 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
d
 
=
 
'
P
A
T
H
0
1
'


 
 
 
 
 
 
 
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
=
 
1
.
0


 
 
 
 
 
 
 
 
m
a
s
t
e
r
y
_
s
c
o
r
e
 
=
 
1
.
0




 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
 
=
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
]
.
i
l
o
c
[
0
]


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]




 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
n
f
o
 
=
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
[
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
[
'
p
a
t
h
w
a
y
_
i
d
'
]
 
=
=
 
p
a
t
h
w
a
y
_
i
d
]
.
i
l
o
c
[
0
]




 
 
 
 
 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
d
e
l
t
a
_
a
i
_
r
,
 
p
a
t
h
w
a
y
_
n
a
m
e
 
=
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
,
 
p
a
t
h
w
a
y
_
i
d
,
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
,
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
p
a
t
h
w
a
y
_
n
a
m
e
 
=
=
 
'
A
I
 
F
u
n
d
a
m
e
n
t
a
l
s
'


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
(
f
l
o
a
t
,
 
n
p
.
f
l
o
a
t
i
n
g
)
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
i
s
i
n
s
t
a
n
c
e
(
d
e
l
t
a
_
a
i
_
r
,
 
(
f
l
o
a
t
,
 
n
p
.
f
l
o
a
t
i
n
g
)
)




 
 
 
 
 
 
 
 
#
 
M
a
n
u
a
l
l
y
 
c
a
l
c
u
l
a
t
e
 
e
x
p
e
c
t
e
d
 
v
a
l
u
e
s
 
f
o
r
 
v
e
r
i
f
i
c
a
t
i
o
n


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
]
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
]
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
]
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
_
s
i
m
 
+


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
i
m
 
+


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
i
m
,


 
 
 
 
 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
h
r
_
r
_
s
c
o
r
e
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
h
r
_
r
_
s
c
o
r
e
'
]


 
 
 
 
 
 
 
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
y
n
e
r
g
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
(
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
/
 
1
0
0
 
*
 
h
r
_
r
_
s
c
o
r
e
 
/
 
1
0
0
)
 
*
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
a
l
p
h
a
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
a
l
p
h
a
'
]


 
 
 
 
 
 
 
 
b
e
t
a
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
b
e
t
a
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
(
a
l
p
h
a
 
*
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
)
 
+


 
 
 
 
 
 
 
 
 
 
 
 
(
(
1
 
-
 
a
l
p
h
a
)
 
*
 
h
r
_
r
_
s
c
o
r
e
)
 
+


 
 
 
 
 
 
 
 
 
 
 
 
(
b
e
t
a
 
*
 
e
x
p
e
c
t
e
d
_
s
y
n
e
r
g
y
_
s
i
m
)
,


 
 
 
 
 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
d
e
l
t
a
_
a
i
_
r
,
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
-
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
0
 
<
=
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
<
=
 
1
0
0




 
 
 
 
d
e
f
 
t
e
s
t
_
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
_
p
a
r
t
i
a
l
_
c
o
m
p
l
e
t
i
o
n
(
s
e
l
f
,
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
 
=
 
'
E
M
P
0
0
1
'


 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
d
 
=
 
'
P
A
T
H
0
1
'


 
 
 
 
 
 
 
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
=
 
0
.
5


 
 
 
 
 
 
 
 
m
a
s
t
e
r
y
_
s
c
o
r
e
 
=
 
0
.
8




 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
 
=
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
]
.
i
l
o
c
[
0
]


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]




 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
n
f
o
 
=
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
[
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
[
'
p
a
t
h
w
a
y
_
i
d
'
]
 
=
=
 
p
a
t
h
w
a
y
_
i
d
]
.
i
l
o
c
[
0
]




 
 
 
 
 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
d
e
l
t
a
_
a
i
_
r
,
 
_
 
=
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
,
 
p
a
t
h
w
a
y
_
i
d
,
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
,
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
#
 
M
a
n
u
a
l
l
y
 
c
a
l
c
u
l
a
t
e
 
e
x
p
e
c
t
e
d
 
v
a
l
u
e
s
 
f
o
r
 
v
e
r
i
f
i
c
a
t
i
o
n


 
 
 
 
 
 
 
 
i
m
p
a
c
t
_
f
a
c
t
o
r
 
=
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
*
 
m
a
s
t
e
r
y
_
s
c
o
r
e


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
]
 
*
 
i
m
p
a
c
t
_
f
a
c
t
o
r
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
]
 
*
 
i
m
p
a
c
t
_
f
a
c
t
o
r
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
_
i
n
f
o
[
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
]
 
*
 
i
m
p
a
c
t
_
f
a
c
t
o
r
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
_
s
i
m
 
+


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
i
m
 
+


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
i
m
,


 
 
 
 
 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
h
r
_
r
_
s
c
o
r
e
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
h
r
_
r
_
s
c
o
r
e
'
]


 
 
 
 
 
 
 
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
y
n
e
r
g
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
(
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
/
 
1
0
0
 
*
 
h
r
_
r
_
s
c
o
r
e
 
/
 
1
0
0
)
 
*
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
a
l
p
h
a
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
a
l
p
h
a
'
]


 
 
 
 
 
 
 
 
b
e
t
a
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
b
e
t
a
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
(
a
l
p
h
a
 
*
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
)
 
+


 
 
 
 
 
 
 
 
 
 
 
 
(
(
1
 
-
 
a
l
p
h
a
)
 
*
 
h
r
_
r
_
s
c
o
r
e
)
 
+


 
 
 
 
 
 
 
 
 
 
 
 
(
b
e
t
a
 
*
 
e
x
p
e
c
t
e
d
_
s
y
n
e
r
g
y
_
s
i
m
)
,


 
 
 
 
 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
d
e
l
t
a
_
a
i
_
r
,
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
-
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
)




 
 
 
 
d
e
f
 
t
e
s
t
_
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
_
z
e
r
o
_
i
m
p
a
c
t
_
f
a
c
t
o
r
s
(
s
e
l
f
,
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
 
=
 
'
E
M
P
0
0
1
'


 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
d
 
=
 
'
P
A
T
H
0
1
'


 
 
 
 
 
 
 
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
=
 
0
.
0
 
#
 
Z
e
r
o
 
c
o
m
p
l
e
t
i
o
n


 
 
 
 
 
 
 
 
m
a
s
t
e
r
y
_
s
c
o
r
e
 
=
 
1
.
0




 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
 
=
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
]
.
i
l
o
c
[
0
]


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]




 
 
 
 
 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
d
e
l
t
a
_
a
i
_
r
,
 
_
 
=
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
,
 
p
a
t
h
w
a
y
_
i
d
,
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
,
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
d
e
l
t
a
_
a
i
_
r
,
 
0
.
0
)




 
 
 
 
d
e
f
 
t
e
s
t
_
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
_
m
a
x
_
s
c
o
r
e
s
_
c
l
i
p
p
i
n
g
(
s
e
l
f
,
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s
)
:


 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
 
=
 
'
E
M
P
0
0
1
'


 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
d
 
=
 
'
P
A
T
H
0
1
'
 
#
 
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
=
1
0
,
 
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
=
5
,
 
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
=
3


 
 
 
 
 
 
 
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
=
 
1
.
0


 
 
 
 
 
 
 
 
m
a
s
t
e
r
y
_
s
c
o
r
e
 
=
 
1
.
0




 
 
 
 
 
 
 
 
#
 
M
o
d
i
f
y
 
e
m
p
l
o
y
e
e
 
t
o
 
h
a
v
e
 
h
i
g
h
 
i
n
i
t
i
a
l
 
s
c
o
r
e
s
 
t
h
a
t
 
w
o
u
l
d
 
e
x
c
e
e
d
 
1
0
0
 
w
i
t
h
 
p
a
t
h
w
a
y
 
i
m
p
a
c
t


 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
.
l
o
c
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
,
 
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
=
 
9
5


 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
.
l
o
c
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
,
 
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
=
 
9
8


 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
.
l
o
c
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
,
 
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
=
 
9
9


 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
.
l
o
c
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
,
 
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
 
=
 
9
0




 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
 
=
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
]
.
i
l
o
c
[
0
]


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
c
u
r
r
e
n
t
_
a
i
_
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]




 
 
 
 
 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
d
e
l
t
a
_
a
i
_
r
,
 
_
 
=
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
 
 
 
 
 
 
 
 
e
m
p
l
o
y
e
e
_
i
d
,
 
p
a
t
h
w
a
y
_
i
d
,
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
,
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
#
 
E
x
p
e
c
t
e
d
 
V
R
 
s
u
b
-
c
o
m
p
o
n
e
n
t
s
 
s
h
o
u
l
d
 
b
e
 
c
l
i
p
p
e
d
 
t
o
 
1
0
0


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
_
s
i
m
 
=
 
1
0
0
.
0
 
#
 
9
5
 
+
 
1
0
 
=
 
1
0
5
 
-
>
 
1
0
0


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
i
m
 
=
 
1
0
0
.
0
 
#
 
9
8
 
+
 
5
 
=
 
1
0
3
 
-
>
 
1
0
0


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
i
m
 
=
 
1
0
0
.
0
 
#
 
9
9
 
+
 
3
 
=
 
1
0
2
 
-
>
 
1
0
0




 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
i
_
f
l
u
e
n
c
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
a
i
_
f
l
u
e
n
c
y
_
s
i
m
 
+


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
i
m
 
+


 
 
 
 
 
 
 
 
 
 
 
 
v
r
_
w
e
i
g
h
t
s
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
w
e
i
g
h
t
_
v
r
'
]
 
*
 
e
x
p
e
c
t
e
d
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
i
m
,


 
 
 
 
 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
=
=
 
1
0
0
.
0
 
#
 
S
u
m
 
o
f
 
w
e
i
g
h
t
s
 
i
s
 
1
.
0
,
 
s
o
 
1
0
0
 
*
 
1
.
0
 
=
 
1
0
0




 
 
 
 
 
 
 
 
h
r
_
r
_
s
c
o
r
e
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
h
r
_
r
_
s
c
o
r
e
'
]


 
 
 
 
 
 
 
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
=
 
c
u
r
r
e
n
t
_
e
m
p
l
o
y
e
e
_
r
o
w
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
s
y
n
e
r
g
y
_
s
i
m
 
=
 
n
p
.
c
l
i
p
(
(
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
 
/
 
1
0
0
 
*
 
h
r
_
r
_
s
c
o
r
e
 
/
 
1
0
0
)
 
*
 
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
 
*
 
1
0
0
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
a
l
p
h
a
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
a
l
p
h
a
'
]


 
 
 
 
 
 
 
 
b
e
t
a
 
=
 
m
o
c
k
_
p
a
r
a
m
s
[
'
b
e
t
a
'
]


 
 
 
 
 
 
 
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
(
a
l
p
h
a
 
*
 
e
x
p
e
c
t
e
d
_
v
r
_
s
i
m
)
 
+


 
 
 
 
 
 
 
 
 
 
 
 
(
(
1
 
-
 
a
l
p
h
a
)
 
*
 
h
r
_
r
_
s
c
o
r
e
)
 
+


 
 
 
 
 
 
 
 
 
 
 
 
(
b
e
t
a
 
*
 
e
x
p
e
c
t
e
d
_
s
y
n
e
r
g
y
_
s
i
m
)
,


 
 
 
 
 
 
 
 
 
 
 
 
0
,
 
1
0
0


 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
n
p
.
i
s
c
l
o
s
e
(
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
e
x
p
e
c
t
e
d
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
)


 
 
 
 
 
 
 
 
a
s
s
e
r
t
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
<
=
 
1
0
0
 
#
 
F
i
n
a
l
 
A
I
-
R
 
s
h
o
u
l
d
 
a
l
s
o
 
b
e
 
c
l
i
p
p
e
d




 
 
 
 
d
e
f
 
t
e
s
t
_
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
_
n
o
_
e
m
p
l
o
y
e
e
_
f
o
u
n
d
(
s
e
l
f
,
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s
)
:


 
 
 
 
 
 
 
 
w
i
t
h
 
p
y
t
e
s
t
.
r
a
i
s
e
s
(
I
n
d
e
x
E
r
r
o
r
,
 
m
a
t
c
h
=
"
s
i
n
g
l
e
-
r
o
w
 
D
a
t
a
F
r
a
m
e
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
N
O
N
_
E
X
I
S
T
E
N
T
_
E
M
P
'
,
 
'
P
A
T
H
0
1
'
,
 
1
.
0
,
 
1
.
0
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s


 
 
 
 
 
 
 
 
 
 
 
 
)




 
 
 
 
d
e
f
 
t
e
s
t
_
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
_
n
o
_
p
a
t
h
w
a
y
_
f
o
u
n
d
(
s
e
l
f
,
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s
)
:


 
 
 
 
 
 
 
 
w
i
t
h
 
p
y
t
e
s
t
.
r
a
i
s
e
s
(
I
n
d
e
x
E
r
r
o
r
,
 
m
a
t
c
h
=
"
s
i
n
g
l
e
-
r
o
w
 
D
a
t
a
F
r
a
m
e
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
E
M
P
0
0
1
'
,
 
'
N
O
N
_
E
X
I
S
T
E
N
T
_
P
A
T
H
'
,
 
1
.
0
,
 
1
.
0
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
o
c
k
_
d
f
_
e
m
p
l
o
y
e
e
s
,
 
m
o
c
k
_
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
m
o
c
k
_
d
f
_
p
a
t
h
w
a
y
s
,
 
m
o
c
k
_
p
a
r
a
m
s


 
 
 
 
 
 
 
 
 
 
 
 
)
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
.
i
l
o
c
[
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
0
,
 
l
e
n
(
d
f
_
e
m
p
l
o
y
e
e
s
)
-
1
)
]


c
u
r
r
e
n
t
_
a
i
_
r
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
]
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
.
i
l
o
c
[
0
]




#
 
S
e
l
e
c
t
 
a
 
p
a
t
h
w
a
y
 
r
a
n
d
o
m
l
y
 
f
o
r
 
d
e
m
o
n
s
t
r
a
t
i
o
n


s
e
l
e
c
t
e
d
_
p
a
t
h
w
a
y
 
=
 
d
f
_
p
a
t
h
w
a
y
s
.
s
a
m
p
l
e
(
1
)
.
i
l
o
c
[
0
]


s
e
l
e
c
t
e
d
_
p
a
t
h
w
a
y
_
i
d
 
=
 
s
e
l
e
c
t
e
d
_
p
a
t
h
w
a
y
[
'
p
a
t
h
w
a
y
_
i
d
'
]




c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
 
=
 
0
.
9


m
a
s
t
e
r
y
_
s
c
o
r
e
 
=
 
0
.
8
5




p
r
o
j
e
c
t
e
d
_
a
i
_
r
,
 
d
e
l
t
a
_
a
i
_
r
,
 
p
a
t
h
w
a
y
_
n
a
m
e
 
=
 
s
i
m
u
l
a
t
e
_
p
a
t
h
w
a
y
_
i
m
p
a
c
t
(


 
 
 
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
,
 
s
e
l
e
c
t
e
d
_
p
a
t
h
w
a
y
_
i
d
,
 
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
,
 
m
a
s
t
e
r
y
_
s
c
o
r
e
,


 
 
 
 
d
f
_
e
m
p
l
o
y
e
e
s
,
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
d
f
_
p
a
t
h
w
a
y
s
,
 
P
A
R
A
M
S


)




p
r
i
n
t
(
f
"
S
i
m
u
l
a
t
i
n
g
 
i
m
p
a
c
t
 
f
o
r
 
e
m
p
l
o
y
e
e
 
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
}
:
"
)


p
r
i
n
t
(
f
"
 
 
C
u
r
r
e
n
t
 
A
I
-
R
:
 
{
c
u
r
r
e
n
t
_
a
i
_
r
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
 
 
C
h
o
s
e
n
 
P
a
t
h
w
a
y
:
 
{
p
a
t
h
w
a
y
_
n
a
m
e
}
 
(
I
D
:
 
{
s
e
l
e
c
t
e
d
_
p
a
t
h
w
a
y
_
i
d
}
)
"
)


p
r
i
n
t
(
f
"
 
 
C
o
m
p
l
e
t
i
o
n
 
R
a
t
e
:
 
{
c
o
m
p
l
e
t
i
o
n
_
r
a
t
e
}
,
 
M
a
s
t
e
r
y
 
S
c
o
r
e
:
 
{
m
a
s
t
e
r
y
_
s
c
o
r
e
}
"
)


p
r
i
n
t
(
f
"
 
 
P
r
o
j
e
c
t
e
d
 
A
I
-
R
:
 
{
p
r
o
j
e
c
t
e
d
_
a
i
_
r
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
 
 
C
h
a
n
g
e
 
i
n
 
A
I
-
R
 
(
\
u
0
3
9
4
A
I
-
R
)
:
 
{
d
e
l
t
a
_
a
i
_
r
:
.
2
f
}
"
)




#
 
C
r
e
a
t
e
 
a
 
c
o
m
p
a
r
a
t
i
v
e
 
b
a
r
 
c
h
a
r
t


p
l
o
t
_
c
u
r
r
e
n
t
_
v
s
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
(
c
u
r
r
e
n
t
_
a
i
_
r
,
 
[
p
r
o
j
e
c
t
e
d
_
a
i
_
r
]
,
 
[
p
a
t
h
w
a
y
_
n
a
m
e
]
)
d
e
f
 
o
p
t
i
m
i
z
e
_
p
a
t
h
w
a
y
_
s
e
q
u
e
n
c
e
(
e
m
p
l
o
y
e
e
_
i
d
,
 
c
u
r
r
e
n
t
_
a
i
_
r
,
 
a
v
a
i
l
a
b
l
e
_
p
a
t
h
w
a
y
s
_
d
f
,
 
T
_
m
a
x
_
h
o
u
r
s
,
 
c
o
s
t
_
w
e
i
g
h
t
_
l
a
m
b
d
a
,
 
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
,
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
_
d
a
t
a
,
 
p
a
r
a
m
s
,
 
m
a
x
_
s
t
e
p
s
=
3
)
:


 
 
 
 
"
"
"
I
d
e
n
t
i
f
i
e
s
 
o
p
t
i
m
a
l
 
s
e
q
u
e
n
c
e
 
o
f
 
l
e
a
r
n
i
n
g
 
i
n
v
e
s
t
m
e
n
t
s
 
u
s
i
n
g
 
a
 
g
r
e
e
d
y
 
a
p
p
r
o
a
c
h
.
"
"
"


 
 
 
 
b
e
s
t
_
p
a
t
h
w
a
y
s
_
s
e
q
u
e
n
c
e
 
=
 
[
]


 
 
 
 
m
a
x
_
a
i
_
r
_
i
m
p
r
o
v
e
m
e
n
t
 
=
 
0


 
 
 
 
c
u
r
r
e
n
t
_
t
i
m
e
_
s
p
e
n
t
 
=
 
0


 
 
 
 
c
u
r
r
e
n
t
_
c
o
s
t
_
s
p
e
n
t
 
=
 
0


 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
=
 
c
u
r
r
e
n
t
_
a
i
_
r




 
 
 
 
#
 
D
e
e
p
 
c
o
p
y
 
e
m
p
l
o
y
e
e
 
d
a
t
a
 
f
o
r
 
s
i
m
u
l
a
t
i
o
n
 
s
t
a
t
e
 
a
c
r
o
s
s
 
s
t
e
p
s


 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
[
d
f
_
e
m
p
l
o
y
e
e
s
_
d
a
t
a
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
m
p
l
o
y
e
e
_
i
d
]
.
i
l
o
c
[
0
]
.
c
o
p
y
(
d
e
e
p
=
T
r
u
e
)




 
 
 
 
#
 
I
t
e
r
a
t
e
 
f
o
r
 
a
 
f
i
x
e
d
 
n
u
m
b
e
r
 
o
f
 
s
t
e
p
s
 
(
s
i
m
p
l
i
f
i
e
d
 
f
o
r
 
d
e
m
o
)


 
 
 
 
f
o
r
 
s
t
e
p
 
i
n
 
r
a
n
g
e
(
m
a
x
_
s
t
e
p
s
)
:


 
 
 
 
 
 
 
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
b
e
s
t
_
p
a
t
h
w
a
y
_
v
a
l
u
e
 
=
 
-
n
p
.
i
n
f
 
#
 
M
a
x
i
m
i
z
e
 
v
a
l
u
e


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
s
t
e
p
_
a
i
_
r
_
g
a
i
n
 
=
 
0




 
 
 
 
 
 
 
 
#
 
C
o
n
s
i
d
e
r
 
a
l
l
 
a
v
a
i
l
a
b
l
e
 
p
a
t
h
w
a
y
s


 
 
 
 
 
 
 
 
f
o
r
 
i
d
x
,
 
p
a
t
h
w
a
y
 
i
n
 
a
v
a
i
l
a
b
l
e
_
p
a
t
h
w
a
y
s
_
d
f
.
i
t
e
r
r
o
w
s
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
i
d
 
=
 
p
a
t
h
w
a
y
[
'
p
a
t
h
w
a
y
_
i
d
'
]


 
 
 
 
 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
t
i
m
e
 
=
 
p
a
t
h
w
a
y
[
'
t
i
m
e
_
h
o
u
r
s
'
]


 
 
 
 
 
 
 
 
 
 
 
 
p
a
t
h
w
a
y
_
c
o
s
t
 
=
 
p
a
t
h
w
a
y
[
'
c
o
s
t
'
]




 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
u
r
r
e
n
t
_
t
i
m
e
_
s
p
e
n
t
 
+
 
p
a
t
h
w
a
y
_
t
i
m
e
 
<
=
 
T
_
m
a
x
_
h
o
u
r
s
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
S
i
m
u
l
a
t
e
 
i
m
p
a
c
t
 
o
n
 
t
h
e
 
c
u
r
r
e
n
t
 
s
i
m
u
l
a
t
e
d
 
s
t
a
t
e
 
o
f
 
t
h
e
 
e
m
p
l
o
y
e
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
t
e
m
p
o
r
a
r
y
 
d
e
e
p
 
c
o
p
y
 
f
o
r
 
t
h
i
s
 
s
p
e
c
i
f
i
c
 
p
a
t
h
w
a
y
 
s
i
m
u
l
a
t
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
 
=
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
.
c
o
p
y
(
d
e
e
p
=
T
r
u
e
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
[
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
]
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
[
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
]
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
+
 
p
a
t
h
w
a
y
[
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
]
,
 
0
,
 
1
0
0
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
R
e
c
a
l
c
u
l
a
t
e
 
V
R
 
f
o
r
 
t
e
m
p
 
s
t
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
v
r
_
s
c
o
r
e
'
]
 
=
 
c
a
l
c
u
l
a
t
e
_
i
d
i
o
s
y
n
c
r
a
t
i
c
_
r
e
a
d
i
n
e
s
s
(
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
,
 
p
a
r
a
m
s
[
'
v
r
_
c
o
m
p
o
n
e
n
t
_
w
e
i
g
h
t
s
'
]
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
R
e
c
a
l
c
u
l
a
t
e
 
S
y
n
e
r
g
y
 
(
u
s
i
n
g
 
o
r
i
g
i
n
a
l
 
H
R
 
a
n
d
 
a
l
i
g
n
m
e
n
t
 
a
s
 
t
h
e
s
e
 
d
o
n
'
t
 
c
h
a
n
g
e
 
b
y
 
V
R
 
p
a
t
h
w
a
y
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
 
=
 
c
a
l
c
u
l
a
t
e
_
s
y
n
e
r
g
y
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
v
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
a
l
i
g
n
m
e
n
t
_
f
a
c
t
o
r
'
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
R
e
c
a
l
c
u
l
a
t
e
 
o
v
e
r
a
l
l
 
A
I
-
R
 
f
o
r
 
t
e
m
p
 
s
t
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
=
 
c
a
l
c
u
l
a
t
e
_
a
i
_
r
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
v
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
h
r
_
r
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
_
e
m
p
l
o
y
e
e
_
s
i
m
_
s
t
a
t
e
[
'
s
y
n
e
r
g
y
_
s
c
o
r
e
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
a
m
s
[
'
a
l
p
h
a
'
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
a
m
s
[
'
b
e
t
a
'
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
i
_
r
_
g
a
i
n
 
=
 
t
e
m
p
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
-
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
D
e
f
i
n
e
 
"
v
a
l
u
e
"
 
m
e
t
r
i
c
:
 
A
I
-
R
 
g
a
i
n
 
p
e
r
 
(
c
o
s
t
 
+
 
t
i
m
e
_
c
o
s
t
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
a
 
s
m
a
l
l
 
e
p
s
i
l
o
n
 
t
o
 
t
i
m
e
 
t
o
 
a
v
o
i
d
 
d
i
v
i
s
i
o
n
 
b
y
 
z
e
r
o


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
i
m
e
_
c
o
s
t
_
e
q
u
i
v
a
l
e
n
t
 
=
 
p
a
t
h
w
a
y
_
t
i
m
e
 
/
 
1
0
 
#
 
C
o
n
v
e
r
t
 
h
o
u
r
s
 
t
o
 
a
 
r
o
u
g
h
 
m
o
n
e
t
a
r
y
 
e
q
u
i
v
a
l
e
n
t
 
f
o
r
 
r
a
t
i
o
 
(
e
.
g
.
,
 
$
1
0
/
h
o
u
r
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
(
a
i
_
r
_
g
a
i
n
 
-
 
c
o
s
t
_
w
e
i
g
h
t
_
l
a
m
b
d
a
 
*
 
p
a
t
h
w
a
y
_
c
o
s
t
)
 
/
 
(
p
a
t
h
w
a
y
_
c
o
s
t
 
+
 
t
i
m
e
_
c
o
s
t
_
e
q
u
i
v
a
l
e
n
t
 
+
 
1
e
-
6
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
v
a
l
u
e
 
>
 
b
e
s
t
_
p
a
t
h
w
a
y
_
v
a
l
u
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
e
s
t
_
p
a
t
h
w
a
y
_
v
a
l
u
e
 
=
 
v
a
l
u
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
 
=
 
p
a
t
h
w
a
y


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
s
t
e
p
_
a
i
_
r
_
g
a
i
n
 
=
 
a
i
_
r
_
g
a
i
n




 
 
 
 
 
 
 
 
i
f
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
 
i
s
 
N
o
n
e
:
 
#
 
N
o
 
p
a
t
h
w
a
y
 
f
o
u
n
d
 
t
h
a
t
 
f
i
t
s
 
c
r
i
t
e
r
i
a


 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k




 
 
 
 
 
 
 
 
#
 
A
p
p
l
y
 
t
h
e
 
b
e
s
t
 
p
a
t
h
w
a
y
 
f
o
u
n
d
 
t
o
 
t
h
e
 
s
i
m
u
l
a
t
e
d
 
e
m
p
l
o
y
e
e
 
s
t
a
t
e
 
a
n
d
 
a
c
c
u
m
u
l
a
t
e
d
 
t
o
t
a
l
s


 
 
 
 
 
 
 
 
b
e
s
t
_
p
a
t
h
w
a
y
s
_
s
e
q
u
e
n
c
e
.
a
p
p
e
n
d
(
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
[
'
p
a
t
h
w
a
y
_
n
a
m
e
'
]
)


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
t
i
m
e
_
s
p
e
n
t
 
+
=
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
[
'
t
i
m
e
_
h
o
u
r
s
'
]


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
c
o
s
t
_
s
p
e
n
t
 
+
=
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
[
'
c
o
s
t
'
]


 
 
 
 
 
 
 
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
 
+
=
 
c
u
r
r
e
n
t
_
s
t
e
p
_
a
i
_
r
_
g
a
i
n


 
 
 
 
 
 
 
 
m
a
x
_
a
i
_
r
_
i
m
p
r
o
v
e
m
e
n
t
 
+
=
 
c
u
r
r
e
n
t
_
s
t
e
p
_
a
i
_
r
_
g
a
i
n




 
 
 
 
 
 
 
 
#
 
U
p
d
a
t
e
 
t
h
e
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
 
w
i
t
h
 
t
h
e
 
g
a
i
n
s
 
f
r
o
m
 
t
h
e
 
c
h
o
s
e
n
 
p
a
t
h
w
a
y


 
 
 
 
 
 
 
 
#
 
T
h
i
s
 
e
n
s
u
r
e
s
 
s
u
b
s
e
q
u
e
n
t
 
s
t
e
p
s
 
b
u
i
l
d
 
o
n
 
t
h
e
 
u
p
d
a
t
e
d
 
s
c
o
r
e
s


 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
[
'
a
i
_
f
l
u
e
n
c
y
_
s
c
o
r
e
'
]
 
+
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
[
'
d
e
l
t
a
_
a
i
_
f
l
u
e
n
c
y
'
]
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
[
'
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
_
s
c
o
r
e
'
]
 
+
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
[
'
d
e
l
t
a
_
d
o
m
a
i
n
_
e
x
p
e
r
t
i
s
e
'
]
,
 
0
,
 
1
0
0
)


 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
=
 
n
p
.
c
l
i
p
(


 
 
 
 
 
 
 
 
 
 
 
 
s
i
m
u
l
a
t
e
d
_
e
m
p
l
o
y
e
e
_
d
a
t
a
[
'
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
_
s
c
o
r
e
'
]
 
+
 
b
e
s
t
_
p
a
t
h
w
a
y
_
f
o
r
_
s
t
e
p
[
'
d
e
l
t
a
_
a
d
a
p
t
i
v
e
_
c
a
p
a
c
i
t
y
'
]
,
 
0
,
 
1
0
0
)




 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
'
r
e
c
o
m
m
e
n
d
e
d
_
s
e
q
u
e
n
c
e
'
:
 
b
e
s
t
_
p
a
t
h
w
a
y
s
_
s
e
q
u
e
n
c
e
,


 
 
 
 
 
 
 
 
'
p
r
o
j
e
c
t
e
d
_
f
i
n
a
l
_
a
i
_
r
'
:
 
p
r
o
j
e
c
t
e
d
_
a
i
_
r
,


 
 
 
 
 
 
 
 
'
t
o
t
a
l
_
c
o
s
t
'
:
 
c
u
r
r
e
n
t
_
c
o
s
t
_
s
p
e
n
t
,


 
 
 
 
 
 
 
 
'
t
o
t
a
l
_
t
i
m
e
_
h
o
u
r
s
'
:
 
c
u
r
r
e
n
t
_
t
i
m
e
_
s
p
e
n
t
,


 
 
 
 
 
 
 
 
'
a
i
_
r
_
i
m
p
r
o
v
e
m
e
n
t
'
:
 
m
a
x
_
a
i
_
r
_
i
m
p
r
o
v
e
m
e
n
t


 
 
 
 
}




#
 
T
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
i
m
m
e
d
i
a
t
e
l
y


e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
_
o
p
t
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
.
i
l
o
c
[
0
]


c
u
r
r
e
n
t
_
a
i
_
r
_
o
p
t
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
_
o
p
t
]
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
.
i
l
o
c
[
0
]


T
_
m
a
x
_
h
o
u
r
s
_
o
p
t
 
=
 
3
0
0


c
o
s
t
_
w
e
i
g
h
t
_
l
a
m
b
d
a
_
o
p
t
 
=
 
0
.
0
0
5
 
#
 
A
d
j
u
s
t
e
d
 
f
o
r
 
a
 
r
e
a
s
o
n
a
b
l
e
 
t
r
a
d
e
-
o
f
f




o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
_
t
e
s
t
 
=
 
o
p
t
i
m
i
z
e
_
p
a
t
h
w
a
y
_
s
e
q
u
e
n
c
e
(


 
 
 
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
_
o
p
t
,
 
c
u
r
r
e
n
t
_
a
i
_
r
_
o
p
t
,
 
d
f
_
p
a
t
h
w
a
y
s
,
 
T
_
m
a
x
_
h
o
u
r
s
_
o
p
t
,


 
 
 
 
c
o
s
t
_
w
e
i
g
h
t
_
l
a
m
b
d
a
_
o
p
t
,
 
d
f
_
e
m
p
l
o
y
e
e
s
,
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
P
A
R
A
M
S


)




p
r
i
n
t
(
f
"
T
e
s
t
 
O
p
t
i
m
i
z
a
t
i
o
n
 
R
e
s
u
l
t
s
 
f
o
r
 
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
_
o
p
t
}
:
"
)


f
o
r
 
k
,
 
v
 
i
n
 
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
_
t
e
s
t
.
i
t
e
m
s
(
)
:


 
 
 
 
p
r
i
n
t
(
f
"
 
 
{
k
}
:
 
{
v
}
"
)
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
.
i
l
o
c
[
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
0
,
 
l
e
n
(
d
f
_
e
m
p
l
o
y
e
e
s
)
-
1
)
]


c
u
r
r
e
n
t
_
a
i
_
r
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
d
f
_
e
m
p
l
o
y
e
e
s
[
'
e
m
p
l
o
y
e
e
_
i
d
'
]
 
=
=
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
]
[
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
.
i
l
o
c
[
0
]




T
_
m
a
x
_
h
o
u
r
s
 
=
 
3
0
0
 
 
#
 
e
.
g
.
,
 
8
 
w
e
e
k
s
 
o
f
 
f
u
l
l
-
t
i
m
e
 
t
r
a
i
n
i
n
g
 
(
4
0
 
h
o
u
r
s
/
w
e
e
k
 
*
 
8
 
=
 
3
2
0
)


c
o
s
t
_
w
e
i
g
h
t
_
l
a
m
b
d
a
 
=
 
0
.
0
0
5
 
#
 
A
 
p
a
r
a
m
e
t
e
r
 
t
o
 
t
r
a
d
e
-
o
f
f
 
A
I
-
R
 
i
m
p
r
o
v
e
m
e
n
t
 
v
s
.
 
c
o
s
t




o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
 
=
 
o
p
t
i
m
i
z
e
_
p
a
t
h
w
a
y
_
s
e
q
u
e
n
c
e
(


 
 
 
 
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
,
 
c
u
r
r
e
n
t
_
a
i
_
r
,
 
d
f
_
p
a
t
h
w
a
y
s
,
 
T
_
m
a
x
_
h
o
u
r
s
,


 
 
 
 
c
o
s
t
_
w
e
i
g
h
t
_
l
a
m
b
d
a
,
 
d
f
_
e
m
p
l
o
y
e
e
s
,
 
d
f
_
o
c
c
u
p
a
t
i
o
n
s
,
 
P
A
R
A
M
S


)




p
r
i
n
t
(
f
"
M
u
l
t
i
-
S
t
e
p
 
P
a
t
h
w
a
y
 
O
p
t
i
m
i
z
a
t
i
o
n
 
R
e
s
u
l
t
s
 
f
o
r
 
E
m
p
l
o
y
e
e
 
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
}
 
(
C
u
r
r
e
n
t
 
A
I
-
R
:
 
{
c
u
r
r
e
n
t
_
a
i
_
r
:
.
2
f
}
)
:
"
)


p
r
i
n
t
(
f
"
 
 
R
e
c
o
m
m
e
n
d
e
d
 
S
e
q
u
e
n
c
e
:
 
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
r
e
c
o
m
m
e
n
d
e
d
_
s
e
q
u
e
n
c
e
'
]
}
"
)


p
r
i
n
t
(
f
"
 
 
P
r
o
j
e
c
t
e
d
 
F
i
n
a
l
 
A
I
-
R
:
 
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
p
r
o
j
e
c
t
e
d
_
f
i
n
a
l
_
a
i
_
r
'
]
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
 
 
T
o
t
a
l
 
C
o
s
t
:
 
$
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
t
o
t
a
l
_
c
o
s
t
'
]
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
 
 
T
o
t
a
l
 
T
i
m
e
 
(
h
o
u
r
s
)
:
 
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
t
o
t
a
l
_
t
i
m
e
_
h
o
u
r
s
'
]
:
.
2
f
}
"
)


p
r
i
n
t
(
f
"
 
 
A
I
-
R
 
I
m
p
r
o
v
e
m
e
n
t
:
 
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
a
i
_
r
_
i
m
p
r
o
v
e
m
e
n
t
'
]
:
.
2
f
}
"
)




#
 
V
i
s
u
a
l
i
z
e
 
t
h
e
 
o
p
t
i
m
i
z
a
t
i
o
n
 
r
e
s
u
l
t
s
 
(
o
p
t
i
o
n
a
l
,
 
c
o
u
l
d
 
b
e
 
a
 
t
a
b
l
e
 
o
r
 
b
a
r
 
c
h
a
r
t
)


p
l
o
t
_
c
u
r
r
e
n
t
_
v
s
_
p
r
o
j
e
c
t
e
d
_
a
i
_
r
(


 
 
 
 
c
u
r
r
e
n
t
_
a
i
_
r
,


 
 
 
 
[
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
p
r
o
j
e
c
t
e
d
_
f
i
n
a
l
_
a
i
_
r
'
]
]
,


 
 
 
 
[
'
O
p
t
i
m
i
z
e
d
 
P
a
t
h
w
a
y
 
S
e
q
u
e
n
c
e
'
]


)
p
r
i
n
t
(
"
#
#
 
S
t
r
a
t
e
g
i
c
 
R
e
c
o
m
m
e
n
d
a
t
i
o
n
s
 
f
o
r
 
A
I
 
W
o
r
k
f
o
r
c
e
 
D
e
v
e
l
o
p
m
e
n
t
\
n
"
)




#
 
I
n
s
i
g
h
t
 
1
:
 
I
d
e
n
t
i
f
y
 
l
o
w
 
A
I
-
R
 
c
o
h
o
r
t
s
 
a
n
d
 
t
h
e
i
r
 
d
r
i
v
e
r
s


l
o
w
_
a
i
_
r
_
c
o
h
o
r
t
s
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
.
s
o
r
t
_
v
a
l
u
e
s
(
b
y
=
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
)
.
h
e
a
d
(
5
)


p
r
i
n
t
(
"
#
#
#
 
1
.
 
T
a
r
g
e
t
 
L
o
w
 
A
I
-
R
 
C
o
h
o
r
t
s
 
w
i
t
h
 
D
r
i
v
e
r
-
S
p
e
c
i
f
i
c
 
I
n
t
e
r
v
e
n
t
i
o
n
s
\
n
"
)


p
r
i
n
t
(
"
I
d
e
n
t
i
f
y
 
e
m
p
l
o
y
e
e
s
 
w
i
t
h
 
s
i
g
n
i
f
i
c
a
n
t
l
y
 
l
o
w
e
r
 
A
I
-
R
 
s
c
o
r
e
s
.
 
A
n
a
l
y
z
e
 
w
h
e
t
h
e
r
 
t
h
e
i
r
 
l
o
w
 
s
c
o
r
e
 
i
s
 
p
r
i
m
a
r
i
l
y
 
d
r
i
v
e
n
 
b
y
 
l
o
w
 
I
d
i
o
s
y
n
c
r
a
t
i
c
 
R
e
a
d
i
n
e
s
s
 
(
V
^
R
)
 
o
r
 
i
n
s
u
f
f
i
c
i
e
n
t
 
S
y
s
t
e
m
a
t
i
c
 
O
p
p
o
r
t
u
n
i
t
y
 
(
H
R
^
R
)
 
i
n
 
t
h
e
i
r
 
c
u
r
r
e
n
t
 
r
o
l
e
.
 
T
a
i
l
o
r
 
i
n
t
e
r
v
e
n
t
i
o
n
s
 
a
c
c
o
r
d
i
n
g
l
y
.
\
n
"
)


p
r
i
n
t
(
"
*
*
E
x
a
m
p
l
e
:
 
T
o
p
 
5
 
E
m
p
l
o
y
e
e
s
 
w
i
t
h
 
L
o
w
e
s
t
 
A
I
-
R
 
S
c
o
r
e
s
*
*
"
)


p
r
i
n
t
(
l
o
w
_
a
i
_
r
_
c
o
h
o
r
t
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
d
e
p
a
r
t
m
e
n
t
'
,
 
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
,
 
'
v
r
_
s
c
o
r
e
'
,
 
'
h
r
_
r
_
s
c
o
r
e
'
]
]
.
t
o
_
s
t
r
i
n
g
(
i
n
d
e
x
=
F
a
l
s
e
)
)


p
r
i
n
t
(
"
\
n
*
 
 
 
*
*
A
c
t
i
o
n
:
*
*
 
F
o
r
 
`
E
M
P
0
2
3
`
 
i
n
 
'
M
a
r
k
e
t
i
n
g
'
 
w
i
t
h
 
l
o
w
 
V
^
R
,
 
r
e
c
o
m
m
e
n
d
 
A
I
-
F
l
u
e
n
c
y
 
f
o
c
u
s
e
d
 
t
r
a
i
n
i
n
g
.
 
F
o
r
 
`
E
M
P
0
1
1
`
 
i
n
 
'
F
i
n
a
n
c
e
'
,
 
w
h
o
s
e
 
H
R
^
R
 
i
s
 
r
e
l
a
t
i
v
e
l
y
 
l
o
w
,
 
c
o
n
s
i
d
e
r
 
i
n
t
e
r
n
a
l
 
m
o
b
i
l
i
t
y
 
o
p
t
i
o
n
s
 
o
r
 
u
p
s
k
i
l
l
i
n
g
 
f
o
r
 
r
o
l
e
s
 
w
i
t
h
 
h
i
g
h
e
r
 
m
a
r
k
e
t
 
o
p
p
o
r
t
u
n
i
t
y
.
\
n
"
)




#
 
I
n
s
i
g
h
t
 
2
:
 
P
i
n
p
o
i
n
t
 
c
r
i
t
i
c
a
l
 
s
k
i
l
l
s
 
g
a
p
s
 
f
r
o
m
 
h
e
a
t
m
a
p


#
 
T
h
i
s
 
r
e
l
i
e
s
 
o
n
 
t
h
e
 
h
e
a
t
m
a
p
 
g
e
n
e
r
a
t
e
d
 
e
a
r
l
i
e
r
,
 
s
o
 
w
e
'
l
l
 
i
n
f
e
r
 
a
n
 
e
x
a
m
p
l
e
.


p
r
i
n
t
(
"
#
#
#
 
2
.
 
A
d
d
r
e
s
s
 
C
r
i
t
i
c
a
l
 
S
k
i
l
l
s
 
G
a
p
s
 
v
i
a
 
T
a
r
g
e
t
e
d
 
U
p
s
k
i
l
l
i
n
g
\
n
"
)


p
r
i
n
t
(
"
T
h
e
 
S
k
i
l
l
s
 
G
a
p
 
H
e
a
t
m
a
p
 
(
S
e
c
t
i
o
n
 
1
6
)
 
r
e
v
e
a
l
e
d
 
c
o
m
m
o
n
 
w
e
a
k
n
e
s
s
e
s
.
 
F
o
r
 
i
n
s
t
a
n
c
e
,
 
i
f
 
'
B
u
s
i
n
e
s
s
 
A
n
a
l
y
s
t
'
 
r
o
l
e
s
 
s
h
o
w
 
l
o
w
e
r
 
'
A
d
a
p
t
i
v
e
-
C
a
p
a
c
i
t
y
'
 
s
c
o
r
e
s
,
 
a
 
t
a
r
g
e
t
e
d
 
t
r
a
i
n
i
n
g
 
p
r
o
g
r
a
m
 
f
o
c
u
s
i
n
g
 
o
n
 
'
S
t
r
a
t
e
g
i
c
 
C
a
r
e
e
r
 
M
a
n
a
g
e
m
e
n
t
'
 
o
r
 
'
C
o
g
n
i
t
i
v
e
 
F
l
e
x
i
b
i
l
i
t
y
'
 
w
o
u
l
d
 
b
e
 
b
e
n
e
f
i
c
i
a
l
.
\
n
"
)


p
r
i
n
t
(
"
*
 
 
 
*
*
E
x
a
m
p
l
e
:
*
*
 
B
a
s
e
d
 
o
n
 
p
r
e
v
i
o
u
s
 
h
e
a
t
m
a
p
,
 
'
D
a
t
a
 
S
c
i
e
n
t
i
s
t
'
 
r
o
l
e
s
 
g
e
n
e
r
a
l
l
y
 
e
x
c
e
l
 
i
n
 
'
A
I
-
F
l
u
e
n
c
y
'
 
b
u
t
 
m
i
g
h
t
 
s
h
o
w
 
g
a
p
s
 
i
n
 
'
D
o
m
a
i
n
-
E
x
p
e
r
t
i
s
e
'
 
(
e
.
g
.
,
 
s
p
e
c
i
f
i
c
 
i
n
d
u
s
t
r
y
 
k
n
o
w
l
e
d
g
e
)
.
 
P
r
i
o
r
i
t
i
z
e
 
a
d
v
a
n
c
e
d
 
d
o
m
a
i
n
-
s
p
e
c
i
f
i
c
 
A
I
 
a
p
p
l
i
c
a
t
i
o
n
s
 
a
n
d
 
c
e
r
t
i
f
i
c
a
t
i
o
n
s
.
\
n
"
)




#
 
I
n
s
i
g
h
t
 
3
:
 
R
e
c
o
m
m
e
n
d
 
s
p
e
c
i
f
i
c
 
l
e
a
r
n
i
n
g
 
p
a
t
h
w
a
y
s
 
f
r
o
m
 
o
p
t
i
m
i
z
a
t
i
o
n
 
r
e
s
u
l
t
s


p
r
i
n
t
(
"
#
#
#
 
3
.
 
I
m
p
l
e
m
e
n
t
 
O
p
t
i
m
i
z
e
d
 
M
u
l
t
i
-
S
t
e
p
 
L
e
a
r
n
i
n
g
 
P
a
t
h
w
a
y
s
\
n
"
)


p
r
i
n
t
(
f
"
F
o
r
 
e
m
p
l
o
y
e
e
 
{
e
x
a
m
p
l
e
_
e
m
p
l
o
y
e
e
_
i
d
}
,
 
t
h
e
 
o
p
t
i
m
i
z
a
t
i
o
n
 
i
d
e
n
t
i
f
i
e
d
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
e
q
u
e
n
c
e
 
t
o
 
m
a
x
i
m
i
z
e
 
A
I
-
R
 
i
m
p
r
o
v
e
m
e
n
t
 
w
i
t
h
i
n
 
b
u
d
g
e
t
 
a
n
d
 
t
i
m
e
 
c
o
n
s
t
r
a
i
n
t
s
:
\
n
"
)


p
r
i
n
t
(
f
"
*
 
 
 
*
*
R
e
c
o
m
m
e
n
d
e
d
 
P
a
t
h
w
a
y
 
S
e
q
u
e
n
c
e
:
*
*
 
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
r
e
c
o
m
m
e
n
d
e
d
_
s
e
q
u
e
n
c
e
'
]
}
"
)


p
r
i
n
t
(
f
"
*
 
 
 
*
*
P
r
o
j
e
c
t
e
d
 
A
I
-
R
 
I
m
p
r
o
v
e
m
e
n
t
:
*
*
 
{
o
p
t
i
m
i
z
a
t
i
o
n
_
r
e
s
u
l
t
s
[
'
a
i
_
r
_
i
m
p
r
o
v
e
m
e
n
t
'
]
:
.
2
f
}
"
)


p
r
i
n
t
(
"
\
n
*
 
 
 
*
*
A
c
t
i
o
n
:
*
*
 
L
e
v
e
r
a
g
e
 
s
u
c
h
 
o
p
t
i
m
i
z
e
d
 
p
a
t
h
w
a
y
s
 
t
o
 
g
u
i
d
e
 
i
n
d
i
v
i
d
u
a
l
 
c
a
r
e
e
r
 
d
e
v
e
l
o
p
m
e
n
t
 
p
l
a
n
s
,
 
b
a
l
a
n
c
i
n
g
 
c
o
s
t
,
 
t
i
m
e
,
 
a
n
d
 
i
m
p
a
c
t
.
\
n
"
)




#
 
I
n
s
i
g
h
t
 
4
:
 
H
i
g
h
l
i
g
h
t
 
r
o
l
e
s
 
w
i
t
h
 
h
i
g
h
 
H
R
^
R
 
b
u
t
 
l
o
w
 
V
^
R


h
i
g
h
_
h
r
_
l
o
w
_
v
r
_
r
o
l
e
s
 
=
 
d
f
_
e
m
p
l
o
y
e
e
s
[
(
d
f
_
e
m
p
l
o
y
e
e
s
[
'
h
r
_
r
_
s
c
o
r
e
'
]
 
>
 
7
0
)
 
&
 
(
d
f
_
e
m
p
l
o
y
e
e
s
[
'
v
r
_
s
c
o
r
e
'
]
 
<
 
6
0
)
]


i
f
 
n
o
t
 
h
i
g
h
_
h
r
_
l
o
w
_
v
r
_
r
o
l
e
s
.
e
m
p
t
y
:


 
 
 
 
p
r
i
n
t
(
"
#
#
#
 
4
.
 
I
n
v
e
s
t
 
S
t
r
a
t
e
g
i
c
a
l
l
y
 
i
n
 
H
i
g
h
 
O
p
p
o
r
t
u
n
i
t
y
,
 
L
o
w
 
R
e
a
d
i
n
e
s
s
 
R
o
l
e
s
\
n
"
)


 
 
 
 
p
r
i
n
t
(
"
I
d
e
n
t
i
f
y
 
j
o
b
 
r
o
l
e
s
 
t
h
a
t
 
h
a
v
e
 
h
i
g
h
 
S
y
s
t
e
m
a
t
i
c
 
O
p
p
o
r
t
u
n
i
t
y
 
(
H
R
^
R
)
 
b
u
t
 
w
h
e
r
e
 
t
h
e
 
c
u
r
r
e
n
t
 
w
o
r
k
f
o
r
c
e
 
h
a
s
 
l
o
w
e
r
 
I
d
i
o
s
y
n
c
r
a
t
i
c
 
R
e
a
d
i
n
e
s
s
 
(
V
^
R
)
.
 
T
h
e
s
e
 
a
r
e
 
p
r
i
m
e
 
c
a
n
d
i
d
a
t
e
s
 
f
o
r
 
s
t
r
a
t
e
g
i
c
 
i
n
v
e
s
t
m
e
n
t
.
\
n
"
)


 
 
 
 
p
r
i
n
t
(
"
*
*
E
x
a
m
p
l
e
:
 
E
m
p
l
o
y
e
e
s
 
i
n
 
H
i
g
h
 
H
R
^
R
 
/
 
L
o
w
 
V
^
R
 
R
o
l
e
s
*
*
"
)


 
 
 
 
p
r
i
n
t
(
h
i
g
h
_
h
r
_
l
o
w
_
v
r
_
r
o
l
e
s
[
[
'
e
m
p
l
o
y
e
e
_
i
d
'
,
 
'
j
o
b
_
r
o
l
e
'
,
 
'
h
r
_
r
_
s
c
o
r
e
'
,
 
'
v
r
_
s
c
o
r
e
'
,
 
'
c
u
r
r
e
n
t
_
a
i
_
r
_
s
c
o
r
e
'
]
]
.
h
e
a
d
(
)
.
t
o
_
s
t
r
i
n
g
(
i
n
d
e
x
=
F
a
l
s
e
)
)


 
 
 
 
p
r
i
n
t
(
"
\
n
*
 
 
 
*
*
A
c
t
i
o
n
:
*
*
 
F
o
r
 
t
h
e
s
e
 
r
o
l
e
s
,
 
f
o
c
u
s
e
d
 
u
p
s
k
i
l
l
i
n
g
 
o
n
 
A
I
-
F
l
u
e
n
c
y
 
a
n
d
 
D
o
m
a
i
n
-
E
x
p
e
r
t
i
s
e
 
(
s
p
e
c
i
f
i
c
 
t
o
 
t
h
e
 
h
i
g
h
 
H
R
^
R
 
a
r
e
a
)
 
w
i
l
l
 
y
i
e
l
d
 
h
i
g
h
 
r
e
t
u
r
n
s
.
\
n
"
)


e
l
s
e
:


 
 
 
 
p
r
i
n
t
(
"
#
#
#
 
4
.
 
A
l
l
 
e
m
p
l
o
y
e
e
s
 
s
e
e
m
 
t
o
 
h
a
v
e
 
b
a
l
a
n
c
e
d
 
H
R
^
R
 
a
n
d
 
V
^
R
 
i
n
 
t
h
i
s
 
s
i
m
u
l
a
t
i
o
n
.
 
N
o
 
e
x
p
l
i
c
i
t
 
h
i
g
h
 
o
p
p
o
r
t
u
n
i
t
y
/
l
o
w
 
r
e
a
d
i
n
e
s
s
 
r
o
l
e
s
 
i
d
e
n
t
i
f
i
e
d
.
\
n
"
)




#
 
I
n
s
i
g
h
t
 
5
:
 
E
m
p
h
a
s
i
z
e
 
a
d
a
p
t
i
v
e
 
c
a
p
a
c
i
t
i
e
s


p
r
i
n
t
(
"
#
#
#
 
5
.
 
F
o
s
t
e
r
 
C
o
n
t
i
n
u
o
u
s
 
L
e
a
r
n
i
n
g
 
a
n
d
 
A
d
a
p
t
i
v
e
 
C
a
p
a
c
i
t
y
\
n
"
)


p
r
i
n
t
(
"
T
h
e
 
r
a
p
i
d
 
p
a
c
e
 
o
f
 
A
I
 
e
v
o
l
u
t
i
o
n
 
n
e
c
e
s
s
i
t
a
t
e
s
 
a
 
w
o
r
k
f
o
r
c
e
 
w
i
t
h
 
s
t
r
o
n
g
 
a
d
a
p
t
i
v
e
 
c
a
p
a
c
i
t
i
e
s
.
 
E
m
p
h
a
s
i
z
e
 
t
r
a
i
n
i
n
g
 
t
h
a
t
 
b
u
i
l
d
s
 
c
o
g
n
i
t
i
v
e
 
f
l
e
x
i
b
i
l
i
t
y
,
 
s
o
c
i
a
l
-
e
m
o
t
i
o
n
a
l
 
i
n
t
e
l
l
i
g
e
n
c
e
 
f
o
r
 
h
u
m
a
n
-
A
I
 
c
o
l
l
a
b
o
r
a
t
i
o
n
,
 
a
n
d
 
s
t
r
a
t
e
g
i
c
 
c
a
r
e
e
r
 
m
a
n
a
g
e
m
e
n
t
 
s
k
i
l
l
s
 
a
c
r
o
s
s
 
a
l
l
 
e
m
p
l
o
y
e
e
 
l
e
v
e
l
s
.
\
n
"
)


p
r
i
n
t
(
"
*
 
 
 
*
*
A
c
t
i
o
n
:
*
*
 
I
n
t
e
g
r
a
t
e
 
'
A
d
a
p
t
i
v
e
-
C
a
p
a
c
i
t
y
'
 
b
o
o
s
t
i
n
g
 
m
o
d
u
l
e
s
 
i
n
t
o
 
a
l
l
 
m
a
j
o
r
 
l
e
a
r
n
i
n
g
 
i
n
i
t
i
a
t
i
v
e
s
 
a
n
d
 
p
r
o
m
o
t
e
 
a
 
c
u
l
t
u
r
e
 
o
f
 
c
o
n
t
i
n
u
o
u
s
 
l
e
a
r
n
i
n
g
 
a
n
d
 
e
x
p
e
r
i
m
e
n
t
a
t
i
o
n
.
\
n
"
)