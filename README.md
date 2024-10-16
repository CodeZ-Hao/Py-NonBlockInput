# Py-NonBlockInput

此项目用于为Python提供一种允许用户自定义阻塞条件的终端输入函数，且做了跨平台适配，可以在linux和window上使用。
你可以使用超时或者任何其他自定义条件来结束阻塞，从而实现非阻塞输入。

## 前言

我希望从多个来源（包括终端输入）获取用户输入，当任意来源获取到输入时，我希望其他正在等待输入的来源能够立即结束阻塞，从而实现类似"或"的输入语法。
为了实现这个需求，起初我期望通过强制退出input()函数的阻塞来实现，但是经过尝试，发现Python没有提供这样的方法（尝试了包括线程、异步、signal杀死等）。
因此，我编写了这个包，希望能够帮助到有类似需求的人。

## 安装

在release中下载`NonBlockInput-1.0.0-py3-none-any.whl`文件，使用pip安装：

```shell
pip install NonBlockInput-1.0.0-py3-none-any.whl
```

或者直接使用pip安装：

```shell
pip install NonBlockInput
```

## 使用

### read_line：行输入方法

```python
from nbck_input import read_line

# 获取输入
print("请输入内容: ")
input = read_line() # 等待用户输入，直到用户按下回车键

print("请输入内容（3秒后超时）: ")
input = read_line(timeout=3)  # 超时3秒

print("请输入内容（自定义条件）: ")
signal = [False]
def pre_func(*args):
    return signal[0]

input = read_line(pre_func=pre_func)  # 当signal[0]为True时，提前结束阻塞
```

### read_char：单个字符输入方法

```python
from nbck_input import read_char

print("请输入任意字符:")
input = read_char() # 等待用户输入任意字符，不需要按下回车键
# ... 同样支持超时和自定义条件
```

### 其他自定义方法

```python
from nbck_input import TermInput

def read_until_p(timeout: float = 0) -> str:
    def func(x: bytes) -> bool:
        # 判定条件: 接收到字符为 P
        return x == b"\x1b[@P" # 此处为 ANSI 转义序列，表示按下 P 键
    term_input = TermInput()

    return term_input.read_input(timeout, pre_func=func)

read_until_p()
```

## 注意事项

为了实现对控制按键的支持，此包使用了ANSI转义序列，并以此实现对终端显示效果的控制。

### window

由于window的CMD终端默认不启用ANSI转义序列，因此，如果你的终端上使用此包获取输入时，输入的字符显示为乱码，则需要通过配置注册表来启用ANSI转义序列。

1. 打开注册表编辑器（regedit）
2. 导航到`HKEY_CURRENT_USER\Console`
3. 在右侧找到`VirtualTerminalLevel`，如果不存在，则新建一个DWORD值，并设置其值为1
4. 重启CMD终端

**注意：** 系统版本需要为Windows 10 1709或更高版本，否则无法启用ANSI转义序列。

或者，你也可以使用其他支持ANSI转义序列的终端，如Hyper等。

### linux

由于linux的终端默认输入模式为行输入，本包需要将终端模式设置为字符输入模式，并在程序退出时将其恢复为默认设置。
通常来说，你不需要关注这点，但当程序异常退出时，可能会导致终端模式无法恢复，从而使得该终端显示异常。*如果出现此问题，重新打开新的终端即可。*
此外，由于检测stdin通道使用select模块的局限性，在你尝试在一次输入内输入多个字符时（例如复制粘贴长文本），此时仅会获取第一个字符，但你可以再次按下任意键（如回车），此时会同时获取剩余的所有字符。

## 贡献

如果你有任何建议或者想要贡献代码，欢迎提交issue或者pull request。

## 许可证

本项目采用MIT许可证。
