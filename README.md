# 📚 Make Knowledge Cards

将文章或 Markdown/TXT 文件智能转换为结构化知识卡片的 Claude Code Skill。

## ✨ 功能特点

- 从粘贴的文章内容中自动提取核心知识点
- 读取本地 `.md` 或 `.txt` 文件生成卡片
- 每张卡片聚焦一个知识点，简洁清晰
- 支持中英文内容
- 5-8 张卡片，不多不少

## 📋 卡片结构

每张知识卡片包含：

| 字段 | 说明 |
|------|------|
| 标题 | 知识点的简洁概括 |
| 核心知识 | 一句话本质 |
| 简明解释 | 2-3 句话清晰解释 |
| 例子/自测 | 具体示例或检验问题 |

## 🚀 使用方法

### 方式一：粘贴文章

```
请帮我把这篇文章转换成知识卡片：

[粘贴文章内容]
```

### 方式二：读取本地文件

```
请读取这个文件并生成知识卡片：./docs/article.md
```

## 📤 输出示例

```markdown
# 📚 知识卡片：React Hooks 入门

> 共 6 张卡片 | 来源：react-hooks-guide.md

---

### 卡片 1：useState 的基本用法

**核心知识**：useState 让函数组件拥有自己的状态

**简明解释**：
useState 是 React 最常用的 Hook，它接收一个初始值，
返回当前状态和更新函数。每次调用更新函数都会触发重新渲染。

**例子/自测问题**：
- 例子：const [count, setCount] = useState(0)
- 自测：useState 返回的是数组还是对象？

---
```

## 🔧 验证卡片质量

使用内置验证脚本检查生成的卡片：

```bash
python skills/make-knowledge-cards/quick_validate.py output.md
```

验证内容包括：
- 卡片数量是否在 5-8 张
- 每张卡片是否包含必要字段
- 是否有编造内容的痕迹

## 📁 项目结构

```
make-knowledge-cards/
├── SKILL.md              # Skill 定义文件
├── README.md             # 项目说明
├── quick_validate.py     # 验证脚本
└── agents/
    └── openai.yaml       # Agent 配置
```

## ⚠️ 限制说明

- ❌ 不支持网页抓取（需要用户提供文本）
- ❌ 不支持 PDF 文件解析
- ❌ 不支持导出为 Anki 格式
- ❌ 不提供图形界面

## 📄 License

MIT License
