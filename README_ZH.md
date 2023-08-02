# Claude AI Python 客户端



[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Claude AI Python 客户端提供了与 Claude AI API 进行交互的便捷方式，使您可以进行 AI 驱动的聊天对话。该客户端允许您无缝地发送查询并接收 AI 模型的响应。

## 需求

- Python 3.x
- `requests` 库

## 安装

1. 确保已安装 Python 3.x。如果没有，请从 [Python 官方网站](https://www.python.org/downloads/) 下载。

2. 使用 pip 安装所需的 `requests` 库：

```bash
pip install requests
```

## 使用方法

1. 使用您的组织 UUID、对话 UUID 和认证 cookie 初始化 `Claude` 类。

2. 使用 `send_message` 方法向 AI 模型发送查询。如果消息发送成功，它将返回 `True`。

3. 使用 `chat_conversation_history` 方法检索对话历史记录。

4. 使用 `get_last_answer` 方法从对话历史记录中获取最后一条 AI 响应。

5. 将客户端集成到您的应用程序中，以启用 AI 驱动的聊天响应。

## 示例

```python
if __name__ == '__main__':
    org_uuid = "YOUR_ORG_UUID"
    con_uuid = "YOUR_CON_UUID"
    cookie = "YOUR_AUTH_COOKIE"

    main(org_uuid, con_uuid, cookie)
```

将 `"YOUR_ORG_UUID"`、`"YOUR_CON_UUID"` 和 `"YOUR_AUTH_COOKIE"` 替换为您从 Claude AI 获取的组织 UUID、对话 UUID 和认证 cookie。

**注意：**获取组织 UUID、对话 UUID 和认证 cookie 的方法，请参阅 [https://blog.csdn.net/resphina/article/details/132034037?spm=1001.2014.3001.5501](https://blog.csdn.net/resphina/article/details/132034037?spm=1001.2014.3001.5501)。

## 许可证

本项目基于 MIT 许可证 - 请参阅 [LICENSE](LICENSE) 文件了解详细信息。

## 免责声明

本项目与 Claude AI 或其开发人员没有官方关联。使用时请自行承担风险。

---

根据您的特定要求，随意定制此 README 并添加更多详细信息。您可以包含有关如何获取组织 UUID、对话 UUID 和认证 cookie 的信息。此外，您可能希望包含一些对话流程的示例，以使潜在用户更好地了解客户端的工作原理。
