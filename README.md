Claude AI Chatbot
这是一个使用 Python 与 Claude AI 对话的简单聊天机器人。

该项目通过 Claude AI 的 API 接口,实现了一个基础的命令行聊天机器人。主要功能包括:

发送消息给 Claude AI 并获取回复
获取历史聊天记录
使用方法

在 Claude AI 后台获取 org_uuid、con_uuid 和 Cookie
填写 org_uuid、con_uuid 和 Cookie 到 main.py 中对应位置
运行 python main.py
输入消息,获取 Claude AI 的回复


human: 你好
Claude AI: 你好,很高兴认识你。

Claude 类:封装了与 API 的交互逻辑
send_message:发送消息给 Claude AI
chat_conversation_history:获取历史聊天记录
