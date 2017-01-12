# Table of Contents

- [简介](#introduction)
- [安装](#installation)
- [快速开始](#quick-start)
- [命令行](#shell-access)

# Introduction

Dockerfile to build a jd-backend container image.
Run a container based on this image.

#installation

```bash
docker build -t jd-backend .
```

# Quick Start

Run the jd-backend image
```bash
docker run --rm --name jd-backend -p 80:80 jd-backend
```

# Shell Access

```bash
docker exec -it jd-backend bash
```
