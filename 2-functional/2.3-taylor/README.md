## Exercise 3: Approximated Trigonometric Functions

$\sin(x)$ can be approximate by the Taylor's series:

$$
\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots
$$

Let's write a library to implement $\sin(x, n)$ by using the Taylor's series (where n is the level of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).

Let's compare your function with the one implemented in the math module at the growing of the approximation level.

**Hint**. Use a generator for the factorial and a comprehension for the series.