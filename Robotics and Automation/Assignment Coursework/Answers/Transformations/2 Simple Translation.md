> [!Question]
> ![2. Consider the translation P1 to P2](Questions.md#2.%20Consider%20the%20translation%20P1%20to%20P2)

### General Transformation Matrix for Simple Translation
%%[[2025-03-18]] @ 15:36%%

The [figure](image-4-x199-y336.png) shows a simple translation. 

![image-4-x199-y336|400](image-4-x199-y336.png)

This would be represented by the following Homogeneous Transformation Matrix (HTM):

$$\large \text{Simple Translation HTM:} \quad \begin{bmatrix}
1 & 0 & 0 & x_{1}-x_{2} \\ 
0 & 1 & 0 & y_{1}-y_{2} \\ 
0 & 0 & 1 & z_{1}-z_{2} \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}$$

That could be applied in the form:

$$P_{2} = P_{1} \begin{bmatrix}
1 & 0 & 0 & x_{1}-x_{2} \\ 
0 & 1 & 0 & y_{1}-y_{2} \\ 
0 & 0 & 1 & z_{1}-z_{2} \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}$$

Where $P_{1}$ & $P_{2}$ are column vectors of homogeneous coordinates in the form:

$$\large\begin{pmatrix}
\newcommand{\G}[1]{{\color{green}#1}}
\newcommand{\S}{{\color{red}s}}
\begin{array}{c}
\G{x}/\S \\ 
\G{y}/\S \\ 
\G{z}/\S \\
\end{array}\\
\color{red}
\S \\
\end{pmatrix}
\quad 
\begin{align*}
& \text{where} 
{\color{green} \begin{pmatrix} x \\ y \\ z \end{pmatrix}}
\ \text{are cartesean coordinates denoting displacemnt from origin} \ O. \\
& \text{and} \ {\color{red} s }\ \text{is a scalar typically 1 or the lowest common denominator of ${\color{green} (x,y,z)}$.}
\end{align*}
$$

### Specific Case 
%%[[2025-03-18]] @ 15:47%%

If the euclidean distance from points $P_{1}$ to $P_{2}$ is $l$ where:

$$l \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3\end{pmatrix} 
\quad \text{and} \quad 
P_{1} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1\end{pmatrix}
, \quad \text{then calculate} \quad 
P_{2}\begin{pmatrix} x \\ y \\ z \end{pmatrix}
.$$

Applying the general form described above in [General Transformation Matrix for Simple Translation](2%20Simple%20Translation.md#General%20Transformation%20Matrix%20for%20Simple%20Translation) the transformation matrix would be:

$$\begin{bmatrix}
1 & 0 & 0 & 1 \\ 
0 & 1 & 0 & 2 \\ 
0 & 0 & 1 & 3 \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}$$

And could be be applied as follows to find $P_{2}:$
$$P_{2} = 
\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1\end{pmatrix}
\begin{bmatrix}
1 & 0 & 0 & 1 \\ 
0 & 1 & 0 & 2 \\ 
0 & 0 & 1 & 3 \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}
=
\begin{pmatrix} 2 \\ 3 \\ 4 \\ 1\end{pmatrix}
$$