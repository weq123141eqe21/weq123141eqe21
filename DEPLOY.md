# 部署说明

## 1. 创建 GitHub 个人主页仓库
仓库名称必须与你的 GitHub 用户名完全一致。
例如用户名是 `octocat`，仓库就叫 `octocat`，并设为 Public。

## 2. 替换 USERNAME
打开 `README.md`，把所有 `USERNAME` 替换成你的 GitHub 用户名。

## 3. 上传全部文件
保留目录结构：
- README.md
- data.json
- assets/
- scripts/
- .github/workflows/interaction.yml

## 4. 开启 Issues
Repository → Settings → General → Features → 勾选 Issues。

## 5. Actions 权限
工作流中已声明：
- contents: write
- issues: write

如果仓库策略额外限制写权限，到：
Settings → Actions → General → Workflow permissions
允许工作流写入。

## 6. 测试
在个人主页点击任意按钮。
GitHub 会打开一个预填好的 Issue，点击 “Submit new issue”。
随后 Action 会：
1. 识别投票选项和 GitHub 用户
2. 同一账号对同一选项只计一次
3. 更新 data.json
4. 重绘 assets/interaction-stats.svg
5. 提交修改
6. 留言并自动关闭该 Issue

## 7. 自定义
可修改：
- README.md：主页文案和按钮顺序
- data.json：选项及初始数据
- scripts/record_vote.py：选项映射
- assets/btn-*.svg：按钮样式
