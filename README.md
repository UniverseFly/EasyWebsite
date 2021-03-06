# EasyWebsite

> [中文版 README](README-ZhCN.md)

You only need ***four*** steps to deploy your personal website, where you can upload your notes, blogs, etc.

### 1. Fork this Repo and Enable GitHub Actions

Click the "Fork" button on the right side, as is showed in the figure below, and wait a second. Then refresh the page, and you will see the forked repo in your own account.

![](Assets/image-20200704171907600.png)

When forking is done, switch to the "Actions" panel in the forked repo, and click the green button in the middle center to enable "GitHub Actions".

![image-20200704182728689](Assets/image-20200704182728689.png)

### 2. Modify Sample Files

In your forked repo, edit one or more of the markdown files in `docs/Sample/` or `docs/Algorithm`, say `docs/Sample/SampleFile1.md`, and change to the content you like (you can `clone` the repo first and then `push`, or simply do modifications in the webpage).

### 3. Setup GitHub Pages

In your forked repo, go to settings and find 'GitHub Pages' option in 'Options'. Change the 'Select source' to 'master branch' first and then switch back to 'gh-pages' (Seems it's a bug of 'GitHub Action', leading to doing so a must).

![image-20200704172935284](Assets/image-20200704172935284.png)

If nothing goes wrong, you will see a 'github-pages' item in your repo 'Environment'. And of course, a 'gh-pages' branch will be available.

![image-20200704173239764](Assets/image-20200704173239764.png)

### 4. Check the Effect

Go to `https://${yourUsername}.github.io/EasyWebsite` (Say my username is 'UniverseFly', I just go to  https://UniverseFly.github.io/EasyWebsite.). Check `导航标题->子标题 1` in the left navigation bar, the content will be updated (Note here you may find a '404' in your webpage, which is because the deployment takes a few minutes. So just wait a minute).

![image-20200704172219944](Assets/image-20200704172219944.png)

## Learn More?

### Methods for Generating the Website

- The website is generated by [mkdocs](https://github.com/mkdocs/mkdocs), a static-site generator, and the whole 'gh-pages' branch are sources of the generated webpage.
- The realization of automatic deployment leverages 'GitHub Action', a new GitHub technique, where `.github/workflows/main.yml` is the deployment script.

### Custom your Website

All the files you need to generate the webpage should be inside the `docs` folder in the repo's root, where `mkdocs.yml` is the configuration file. The 'nav' section in this file defines the navigation rule and pieces of titles you can see in the built webpage.

To custom these stuffs, just simulate the format presented below, and modify the 'nav' section and its corresponding files in `docs` folder (Note don't modify any files in `docs/KatexAddition`, which are used to display maths).

'nav' section in `mkdocs.yml` (These paths are relative to `docs`).

```yml
nav:
  - 主页: index.md

  - 算法:
    - 渐进记号: Algorithm/AsymptoticNotation.md
    - 基本的数学函数: Algorithm/BasicMathFunction.md

  - 导航标题:
    - 子标题 1: Sample/SampleFile1.md
    - 子标题 2: Sample/SampleFile2.md
```

The corresponding navigation bar in the webpage：

![image-20200704175859301](Assets/image-20200704175859301.png)

