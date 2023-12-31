# Claude AI Python Client
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![简体中文 badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-Simplified%20Chinese-blue)](./README_ZH.md)


## 2023.08 26 更新，可正常使用！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Ensure you have Python 3.x installed. If not, download it from [Python's official website](https://www.python.org/downloads/).

2. Install the required `requests` library using pip:

```bash
pip install requests
```

## Usage

1. Initialize the `Claude` class with your organization UUID, conversation UUID, and authentication cookie.

2. Utilize the `send_message` method to send a query to the AI model. It returns `True` if the message is sent successfully.

3. Retrieve the conversation history using the `chat_conversation_history` method.

4. Get the last AI response from the conversation history using the `get_last_answer` method.

5. Integrate the client into your application to enable AI-powered chat responses.

## Example
To use the Claude AI Python Client, replace `"YOUR_ORG_UUID"`, `"YOUR_CON_UUID"`, and `"YOUR_AUTH_COOKIE"` with your own organization UUID, conversation UUID, and authentication cookie obtained from Claude AI.
reffer this blog to get the info above  https://blog.csdn.net/resphina/article/details/132034037?spm=1001.2014.3001.5501

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not officially associated with Claude AI or its developers. Use it at your own risk.

---

Feel free to customize this README according to your specific requirements and add more details if needed. You can include information about how to obtain the organization UUID, conversation UUID, and authentication cookie. Additionally, you might want to include some examples of the conversation flow to give potential users a better understanding of how the client works.


