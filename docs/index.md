# Notes and Thoughts

## 网站中查看笔记

打开网页 https://github.com/UniverseFly/Ideas 并选择相应目录即可。

**缺点**：有时候比较慢

## 本地保持项目同步

### 克隆项目到本地

打开 Git Bash (windows) 或 Terminal(*nix)，输入：

```bash
git clone https://github.com/UniverseFly/Ideas.git
cd Ideas
```

### 保持远端同步

若运行 `git status` 看到有提示形如 *Your branch is behind...* 时，输入：

```bash
git pull
```

即可更新本地仓库。

### 注意

若手动修改了文件后会导致 `git pull` 失败，出现这种情况的解决方法之一是：

- 删除整个文件夹，并回到第一步重新 `git clone` 整个仓库。

