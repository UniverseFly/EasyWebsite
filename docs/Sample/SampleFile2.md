# C/C++ 是如何找头文件的

## Standard Libraries

```cpp
#include <...>
```

找编译器（准确说是**预处理器**）定义的寻找路径。

### Show these paths

#### C++

```bash
clang++ -E -x c++ - -v
cpp -xc++ -v
```

#### C

```bash
clang -E -x c - -v
cpp -v
```

## User-defined Headers

```cpp
#include "..."
```

直接从当前目录开始寻找路径。