# 常用函数与记号

> 包含各种性质及其证明。
>
> TODO: 把每个变量定义域规定清楚

## 取整函数

> Wikipedia: [Floor and ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)
>
> - $\lfloor x \rfloor = \max \{i \in \mathbb Z \mid i \le x\}$
> - $\lceil x \rceil = \min \{i \in \mathbb Z \mid i \ge x\}$

$x - 1 < \lfloor x\rfloor \le x \le \lceil x\rceil < x + 1$

- 设 $x = n + \alpha,\ 0 \le \alpha < 1$，则 $\lfloor x\rfloor = n$。
- 则 $x - 1 = n + \alpha - 1 < n$。
- 向上取整设 $x = n - \alpha$ 可证。



$i + \lfloor x \rfloor = \lfloor i + x \rfloor\quad i \in \mathbb Z$

$i + \lceil x \rceil = \lceil i + x \rceil\quad i \in \mathbb Z$

- 设  $x = n + \alpha,\ 0 \le \alpha < 1$ 即可得。
- 向上取整设 $x = n - \alpha$ 可证。



$\lfloor x \rfloor + \lceil -x \rceil = 0$（可以利用数轴记忆）

- 设 $x = n + \alpha,\ 0 \le \alpha < 1$，则 $-x = -n - \alpha$。
- 从而有 $\lfloor x \rfloor = n, \lceil -x \rceil = -n$，所以证明了命题。



$\lfloor n/2 \rfloor + \lceil n/2 \rfloor = n$

$(n \in \Z)$

- $n/2 - 1 < \lfloor n/2 \rfloor \le n/2$
- $n/2 \le \lceil n/2 \rceil < n/2 + 1$
- $n - 1 < \lfloor n/2 \rfloor + \lceil n/2 \rceil < n + 1$
- 由于 $\lfloor n/2 \rfloor + \lceil n/2 \rfloor$ 一定是个整数，所以它的值一定是 $n$。



$\lceil \lceil x\rceil /n\rceil = \lceil x/n \rceil$

$\lfloor \lfloor x\rfloor /n\rfloor = \lfloor x/n \rfloor$

$(n > 0)$

- 设 $x = kn + b + \alpha,\ 0 \le b < n$
- 则 $\lfloor x \rfloor = kn + b$
- 则 $\lfloor \lfloor x\rfloor /n\rfloor = k$
- 同时 $\lfloor x / n \rfloor = k$



$\lceil a/b \rceil \le (a + (b - 1))/b$

$\lfloor a/b \rfloor \ge (a - (b - 1))/b$

$(a, b) \in \N^+ \times \N^+$

- 设 $a = kb + t$
- 则 $\lfloor a/b \rfloor = k$
- $(a - (b - 1))/b = k - 1 + 1/b$

## 模运算

> $a \mod n = a - n\lfloor a/n \rfloor$

由于 $a/n - 1 < \lfloor a/n \rfloor \le a/n$

则 $0 \le a \mod n < n$

## 增长率

设 $a > 1$，则：
$$
\lim_{n \to \infty} \frac{n^b}{a^n} = 0 \\
$$
令 $a = 2^a(a_{\rm right} > 0), n = \log n$，则：
$$
\lim_{n \to \infty}\frac{\log^b n}{n^a} = 0
$$

## 多重函数

$$
f^{(i)}(n) = \begin{cases}
	n &i = 0 \\
	f(f^{(i-1)}(n)) &i > 0 \\
\end{cases}
$$

可以证明，$f^{(a)}(f^{(b)}(n)) = f^{(a + b)}(n)$。

> 对 $a$ 作归纳。

### 多对数

$\log^\star n = \min \{i \ge 0 \mid \log ^{(i)} n \le 1\}$

#### 性质

$\log^\star 2^k = \log^\star k + 1$

> 用 `\star` 代替 `*`，否则 `mkdocs build` 后会识别成 markdown 的斜体表示。

- 设 $\log^\star 2^k = j$
- 则 $\log^{(j)} 2^k = \log ^{(j - 1)} \log 2^k = \log^{(j - 1)} = \log^{(j - 1)} k$
- 所以 $\log ^\star k = j - 1$

## 斯特林（Stirling）近似公式

$$
n! = \sqrt{2\pi n}(\frac{n}{e})^n(1 + \Theta(\frac{1}{n}))
$$

## 斐波那契数

$$
F_0 = 0 \\
F_1 = 1 \\
F_i = F_{i-1} + F_{i-2}
$$

**通项公式**

- 设 $x^2 = x + 1$ 的两个解为 $\phi = (1 + \sqrt 5)/2$ 和 $\hat\phi = (1 - \sqrt 5) / 2$（这里的 $\phi$ 称之为黄金分割率），

- 则 $F_i = (\phi^i - \hat \phi^i) / \sqrt 5$。（数学归纳法）

**通项公式（取整形式）**

- 由于 $|\hat \phi ^ i| / \sqrt 5 <  1 / 2$，

- 则 $\phi^i / \sqrt 5 - 1/2 < \lfloor \phi^i / \sqrt 5 + 1/2 \rfloor \le \phi^i / \sqrt 5 + 1/2$，

- $F_i$ 正好是这个范围内的唯一整数，

- 所以 $F_i = \lfloor \phi^i / \sqrt 5 + 1/2 \rfloor$。

## Exercises

### 单调递增的性质

> 假设 $f$ 和 $g$ 都单调递增（定义域均为 $\mathbb N$），证明 $\lambda n. f(n) + g(n)$、$n \mapsto f(g(n))$ 单调递增。

**Case 1**

- $m \le n \to f(m) \le f(n)$
- $m \le n \to g(m) \le g(n)$
- $m \le n \to f(m) + g(m) \le f(n) + g(n)$。

**Case 2**

- $m \le n \to g(m) \le g(n)$
- $g(m) \le g(n) \to f(g(m)) \le f(g(n))$
- $m \le n \to f(g(m)) \le f(g(n))$

### 证明 $n!$ 相关的渐进性质

> 证明下述命题：
>
> - $\log n! = \Theta(n\log n)$
>
> - $n! = o(n^n)$
> - $n! = \omega(2^n)$

#### 证明命题 1

**利用 Stirling 近似公式**

我们可以得到 $n! = \sqrt{2\pi n}(\frac{n}{e})^n(1 + f(n))\quad f \in \Theta(n \mapsto 1/n)$。

所以有：

- $\log n! = \log \sqrt {2\pi n} + \log((n/e)^n) + \log(1 + f(n))$
- $\log n! = \frac 1 2 \log {2\pi n} + n\log n - n\log e + \log(1 + f(n))$。

当 $n$ 很大的时候有：

- $f(n) \in [c_1/n, c_2 / n]$

- $\log (1 + f(n)) \in [\log(1 + c_1/n), \log(1 + c_2 / n)]$

  > 直观上，这个区间渐进趋近于 $[0, 0]$，因为 $\log 1 = 0$。

- 可以看出 $n\log n$ 是阶数最大的，所以其他每一项都 $\le c_\mathrm{someAnonymous} n\log n$（在这个 $n$ 很大的情况下）。

- 随后改写一下等式有 $\log n! = n\log n + \phi(n)$，其中 $\phi(n) \le cn\log n$

  > $\phi(n) = \frac 1 2 \log {2\pi n} - n\log e + \log(1 + f(n))$

- 因此有 $\log n! \le (1 +c) n\log n$

- 同时由于 $n\log e = o(n\log n)$，因此 $n\log e \le \frac 1 2 n\log n$

- 则有 $\phi(n) \ge 0 - n\log e \ge -\frac 1 2 n\log n$

- 因此有 $\log n! \ge \frac 1 2n\log n$。

**利用积分与求和的不等式关系**

> $$
> \int_{m-1}^n f(x)\mathrm dx \le \sum_{k=m}^nf(k) \le \int_m^{n+1} f(x) \mathrm dx \quad f \text{ is monotonically increasing}\\
> \int_{m}^{n+1} f(x) \mathrm dx \le \sum_{k=m}^nf(k) \le \int_{m-1}^n f(x)\mathrm dx \quad f\text{ is monotonically decreasing}
> $$
>
> 上面的性质可以利用定积分与面积的关系不严谨的得出。

利用上述性质可以得出：

- $\log n! = \sum_{k = 1}^n \log k$
- $\sum_{k=1}^n \log k \le \int_1^{n+1} \log x \mathrm dx = \frac 1 {\ln 2}(x\ln n -x)|_1^{n+1} = (n\ln n - n)/\ln 2 \le n\log n$。
- $\sum_{k=1}^n \log k = \sum_{k=2}^n \log k \ge \int_1^n \log x \mathrm dx = ((n-1)\ln n - (n-1))/\ln 2 = (n-1)\log (n/e)$
- $(n-1)\log (n/e) = n\log n - n\log e - \log n/e$
- 由于 $n\log e$ 和 $\log n/e$ 都是 $o(n\log n)$，则 $n$ 很大时它们都 $\le (n\log n)/4$
- 那么就有 $n\log n - n\log e - \log n/e \ge (n\log n)/2$

因此最后可以得到 $\log n! \in \Theta(n\log n)$。

#### 证明命题 2

- $n! / n^n = n/n \cdot (n-1)/n \cdots 1/n \le n/n \cdot (n - 1) / n \cdot (n - 2) / (n - 1) \cdots 2/3 \cdot 1/2 = 1/n$。
- 所以 $0 \le n!/n^n \le 1/n$，根据夹逼定理有 $\lim_{n \to \infty}n!/n^n = 0$。
- 所以 $n! = o(n^n)$

#### 证明命题 3

- $0 \le 2^n / n! = \frac 2 1 \cdot \frac 2 {2} \cdots \frac 2 n \le \frac 4 n\quad \text{when }n\text{ is large}$（放缩）。
- 根据夹逼定理，它的极限是 $0$。
- 因此有 $2^n = o(n!)$，同时 $n! = \omega(2^n)$。

### $\lceil\log n\rceil!$ 和 $\lceil\log \log n\rceil!$ 是否多项式有界？

> $f$ 多项式有界等价于 $f \in O(n \mapsto n^k)\quad  k \in \mathbb R$。

对于 $\lceil\log n\rceil!$

- 假设 $n = 2^p$，则 $\lceil\log n\rceil! = \lceil p\rceil!$
- $n^k = 2^{pk} = (2^k)^p = c^p\quad c = 2^k$
- 由于阶乘比指数阶数高，有 $\lim_{p \to \infty}\frac {\lceil p\rceil!} {c^p} = \infty$。
- 所以 $\lceil \log n \rceil! = \omega(n^k)$

对于 $\lceil\log\log n\rceil!$，我们令 $k = 1$

- 假设 $n = 2^{2^p}$，则 $\lceil\log\log n\rceil! = \lceil p\rceil!$
- 同时 $n^k = n^1 =  2^{2^p}$
- $p > \lceil p \rceil - 1$，所以 $2^{2^p} > 2^{2^{\lceil p \rceil - 1}}$。
- 数学归纳法可以知道 $2^{2^{\lceil p\rceil - 1}} > \lceil p \rceil!$
- 所以$\lceil p \rceil! \le n$
- $\lceil\log\log n\rceil! = O(n)$。

### $\log\log^\star n$ 和 $\log^\star\log n$ 哪个渐进更大？

> $\log^\star 2^k = \log^\star k + 1$

$$
\begin{aligned}
\lim_{n\to\infty}\frac {\log\log^\star n} {\log^\star\log n} &= \lim_{n\to\infty}\frac{\log(\log^\star n + 1)}{\log^\star n} &n := 2^n\\
  &= \lim_{n\to\infty} \frac {\log(n + 1)} {n} &\log^\star n := n\\
  &= 0
\end{aligned}
$$

所以 $\log\log^\star n = o(\log^\star\log n)$。

### 证明 $k\ln k = \Theta(n) \to k = \Theta(n/\ln n)$

> 这里 $k$ 是关于 $n$ 的表达式。

当 $n$ 很大时：

- $k\ln k \in[c_1n, c_2 n]$
- $k \in [c_1\frac n {\ln k}, c_2\frac n {\ln k}]$
- $\ln k + \ln \ln k \in [\ln c_1n, \ln c_2n]$
- $\ln n \in [\ln k + \ln\ln k - \ln c_2, \ln k + \ln\ln k - c_1]$
- $\ln n = \Theta(\ln k)$
- $\ln k = \Theta(\ln n)$
- $\ln k \in [c_3\ln n, c_4\ln n]$
- $k \in [\frac {c_1}{c_4}\frac n {\ln n}, \frac{c_2}{c_3} \frac n {\ln n}]$

- $k = \Theta(n/\ln n)$

### 渐进记号的补充性质

#### $f = O(g) \to \lambda n. \log f(n) = O(\lambda n. \log g(n))$

> 这里有当 $n$ 很大时，$\log g(n) \ge 1$ 且 $f(n) \ge 1$。

$n$ 很大时：

- $1 \le f(n) \le cg(n)$

- $\log f(n) \le \log cg(n) = \log g(n) + \log c$

  > 如果 $\log c \le 0$，那么 $\log f(n) \le \log g(n)$，命题成立。下面考虑 $\log c > 0$。

- $\log g(n) \ge 1$

- $\log c \log g(n) \ge \log c$

- $\log f(n) \le (1 + \log c)\log g(n)$

所以命题成立。

#### $\Theta(f(n)) \pm o(f(n)) = \Theta(f(n))$

> 严谨的写：$\lambda n. g(n) \pm h(n) \in \Theta(f)\quad g \in \Theta(f), h \in o(f)$。

$n$ 很大时：

- $g(n) \in [c_1f(n), c_2f(n)]$
- $\forall c > 0(h(n) < cf(n))$

$+$ 号的情况

- $0 \le h(n) \le f(n)$
- $g(n) + h(n) \le (c_1 + 1)f(n)$
- $g(n) + h(n) \ge g(n) \ge c_1f(n)$
- 所以 $g(n) + h(n) = \Theta(f(n))$

$-$ 号的情况

- $0 \le h(n) \le \frac {c_1} 2f(n)$
- $g(n) - h(n) \le g(n) \le c_2f(n)$
- $g(n) - h(n) \ge \frac {c_1} 2 f(n)$
- 所以 $g(n) - h(n) = \Theta(f(n))$

### 多重函数的推广

> 对于给定的常量 $c \in \mathbb R$，若 $f$ 单调递增，则 $f_c^\star(x) = \min \{i \ge 0 \mid f^{(i)}(x) \le c\}$。

例如，当 $f(x) = x - 1$，$c = 0$ 时：

- $f^{(i)}(x) = x  - i$（数学归纳法证明）

- $f^\star_0(x) = \min\{i \ge 0 \mid x - i \le 0\} = \min\{i \ge 0 \mid i \ge x\} = \max(0, \lceil x \rceil)$。

  > 如果没有 $i \ge 0$，根据定义结果应该是 $\lceil x\rceil$。因为有 $i \ge 0$，所以会考虑是否 $x > 0$ 两种情况。

又如，当 $f(x) = \sqrt x$，$c = 1$，时：

- 当 $x > 1$ 时，$\sqrt x > 1$，所以 $\sqrt {\sqrt {\cdots \sqrt x}} > 1$，$f^{(i)}(x) > 1$
- 此时 $f_1^\star(x) = \min\{i \ge 0 \mid f^{(i)}(x) \le 1\}$
- 因此当 $x > 1$ 时没有定义。

