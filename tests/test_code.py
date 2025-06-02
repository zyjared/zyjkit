import pytest
from zyjkit.print.color import Code

STYLES = ['bold', 'dim', 'italic', 'underline', 'blink',
          'blink_fast', 'reverse', 'hidden', 'through']
FG_COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
             'bright_black', 'bright_red', 'bright_green', 'bright_yellow',
             'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']


def test_code_initialization():
    c = Code("Hello")
    assert str(c) == "Hello"

    c = Code()
    assert str(c) == ""

    c = Code(123)
    assert "123" in str(c)

    c = Code(True)
    assert "True" in str(c)


@pytest.mark.parametrize("style", STYLES)
def test_style_operations(style):
    c = Code("test")

    # 初始不应有样式
    assert not c.has_style(style)

    # 添加后应有样式
    c.add_style(style)
    assert c.has_style(style)

    # 移除后应无样式
    c.remove_style(style)
    assert not c.has_style(style)

# 颜色操作测试


@pytest.mark.parametrize("color", FG_COLORS)
def test_color_operations(color):
    c = Code("test")

    # 设置前景色
    c.set_fg(color)
    # 获取前景代码 - 测试代码中存在，但对外不可见
    assert c.fg_code != 0

    # 移除前景色
    c.remove_fg()
    assert c.fg_code == 0

    # 设置背景色
    c.set_bg(color)
    # 获取背景代码 - 测试代码中存在，但对外不可见
    assert c.bg_code != 0

    # 移除背景色
    c.remove_bg()
    assert c.bg_code == 0
