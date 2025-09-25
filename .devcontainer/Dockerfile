# 使用一个现代、精简的 Python 基础镜像
FROM python:3.11-slim-bookworm

# 设置环境变量，避免安装过程中出现弹窗提问
ENV DEBIAN_FRONTEND=noninteractive

# 设置工作目录
WORKDIR /workspaces/stock_full_stack

# 1. 安装基础系统工具
RUN apt-get update && apt-get install -y git curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. 安装 Poetry (Python 依赖管理工具)
RUN curl -sSL https://install.python-poetry.org | python3 -

# 将 poetry 添加到系统路径中，这样在终端里可以直接使用
ENV PATH="/root/.local/bin:$PATH"