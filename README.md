# 最小化 Python 开发环境

这是一个使用 VS Code Dev Containers 和 Poetry 搭建的最小化 Python 开发环境。

## 目标

提供一个包含 Python 3.11 和 Poetry 的、隔离的、可复现的开发环境。

## 运行开发环境

### 先决条件

1.  安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2.  安装 [Visual Studio Code](https://code.visualstudio.com/)
3.  在 VS Code 中安装 [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 扩展

### 启动步骤

1.  使用 VS Code 打开本项目文件夹。

2.  VS Code 右下角会弹出一个提示，询问你是否 "Reopen in Container"。点击它。
    *(如果没看到提示, 按 `F1` 并输入 `Dev Containers: Reopen in Container`)*

3.  等待 VS Code 根据配置自动构建 Docker 镜像。这个过程在第一次启动时会需要几分钟。

### 验证环境

环境启动成功后，VS Code 会连接到容器内部。
1.  打开一个新的 VS Code 终端 (`Ctrl+`` `)。
2.  在终端中输入以下命令来验证工具是否安装成功：

    ```bash
    # 检查 Python 版本
    python --version

    # 检查 Poetry 版本
    poetry --version
    ```
如果都能正确显示版本号，那么你的开发环境就成功启动了！