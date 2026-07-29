#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中英文混排空格优化脚本
================================
规则：
1. 汉字与英文字母 / 数字之间加一个空格（中文标点与英文/数字之间不加）。
2. Markdown 行内语法（链接、图片、行内代码、强调/加粗、删除线）与汉字之间
   加空格；链接文本 / 强调内部的可见文本同样套用规则 1。

核心原则：会破坏文档功能/语法的（链接 URL、代码、frontmatter、HTML 标签结构
等）一律不动；会给用户展示的可见内容一定要改。

实现策略：先将所有"功能性片段"替换为占位符，分两类：
  - @@MD<n>@@   Markdown 行内语法（链接、图片、行内代码、强调等），需与
                汉字 / 英文字母之间加空格；
  - @@RAW<n>@@  功能性结构（frontmatter、围栏代码块、HTML / GitBook 标签、
                裸 URL、数学公式等），绝不与相邻文字加空格。
对剩余可见纯文本执行空格调整后还原占位符。
"""

import re
import sys

# CJK 统一表意文字（不含中文标点）
CJK = r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]'

# 占位符
MD_PH = re.compile(r'@@MD\d+@@')
RAW_PH = re.compile(r'@@RAW\d+@@')
ANY_PH = re.compile(r'@@(?:MD|RAW)\d+@@')


class Formatter:
    """对单份 Markdown 文本执行中英混排空格优化。"""

    def __init__(self):
        # 分别保存两类占位符内容
        self.md_placeholders = []   # @@MD<n>@@
        self.raw_placeholders = []  # @@RAW<n>@@

    # ------------------------------------------------------------------
    # 占位符管理
    # ------------------------------------------------------------------
    def _stash_md(self, content):
        idx = len(self.md_placeholders)
        self.md_placeholders.append(content)
        return f'@@MD{idx}@@'

    def _stash_raw(self, content):
        idx = len(self.raw_placeholders)
        self.raw_placeholders.append(content)
        return f'@@RAW{idx}@@'

    def _restore(self, text):
        # 逆序还原，保证嵌套占位符正确展开
        for i in range(len(self.raw_placeholders) - 1, -1, -1):
            text = text.replace(f'@@RAW{i}@@', self.raw_placeholders[i])
        for i in range(len(self.md_placeholders) - 1, -1, -1):
            text = text.replace(f'@@MD{i}@@', self.md_placeholders[i])
        return text

    # ------------------------------------------------------------------
    # 可见文本规则
    # ------------------------------------------------------------------
    def _apply_text_rules(self, text):
        """对"可见纯文本"应用空格规则。"""

        # 规则 2：Markdown 行内语法占位符 <-> 汉字 / 英文字母，加空格
        text = re.sub(rf'({CJK})(@@MD\d+@@)', r'\1 \2', text)
        text = re.sub(rf'(@@MD\d+@@)({CJK})', r'\1 \2', text)
        text = re.sub(r'([A-Za-z])(@@MD\d+@@)', r'\1 \2', text)
        text = re.sub(r'(@@MD\d+@@)([A-Za-z])', r'\1 \2', text)
        # 数字与 Markdown 行内语法之间也加空格（如 1[注] -> 1 [注]）
        text = re.sub(r'([0-9])(@@MD\d+@@)', r'\1 \2', text)
        text = re.sub(r'(@@MD\d+@@)([0-9])', r'\1 \2', text)

        # 规则 1：汉字 <-> 英文字母 / 数字
        text = re.sub(rf'({CJK})([A-Za-z0-9])', r'\1 \2', text)
        text = re.sub(rf'([A-Za-z0-9])({CJK})', r'\1 \2', text)

        return text

    # ------------------------------------------------------------------
    # 各类功能性片段保护
    # ------------------------------------------------------------------
    def _stash_link(self, m):
        """保护普通链接 [text](url)，仅对可见 text 套用规则，URL 不动。"""
        txt = self._apply_text_rules(m.group(1))
        url = m.group(2)
        return self._stash_md(f'[{txt}]({url})')

    def _stash_image(self, m):
        """保护图片 ![alt](src)，仅对可见 alt 套用规则，src 不动。"""
        alt = m.group(1)
        src = m.group(2)
        if alt:
            alt = self._apply_text_rules(alt)
        return self._stash_md(f'![{alt}]({src})')

    def _stash_emph(self, m):
        """保护强调，仅对内部可见文本套用规则。"""
        marker = m.group(1)
        inner = self._apply_text_rules(m.group(2))
        return self._stash_md(f'{marker}{inner}{marker}')

    # ------------------------------------------------------------------
    # 主流程
    # ------------------------------------------------------------------
    def format(self, text):
        # 1. YAML frontmatter（文件开头 --- ... ---）
        text = re.sub(r'\A---\n[\s\S]*?\n---\n?',
                      lambda m: self._stash_raw(m.group(0)), text)

        # 2. 围栏代码块（``` 或 ~~~），整体作为 RAW
        text = re.sub(r'(?m)^```.*$[\s\S]*?^```[ \t]*$',
                      lambda m: self._stash_raw(m.group(0)), text)
        text = re.sub(r'(?m)^~~~.*$[\s\S]*?^~~~[ \t]*$',
                      lambda m: self._stash_raw(m.group(0)), text)

        # 3. 图片 ![alt](src)
        text = re.sub(r'!\[([^\]]*)\]\(([^)]*)\)', self._stash_image, text)

        # 4. 普通链接 [text](url)
        text = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', self._stash_link, text)

        # 5. 行内代码 `code`（内容不动）
        text = re.sub(r'`[^`\n]+`',
                      lambda m: self._stash_md(m.group(0)), text)

        # 6. 块级数学公式 $$...$$
        text = re.sub(r'(?s)\$\$.*?\$\$',
                      lambda m: self._stash_raw(m.group(0)), text)

        # 7. HTML 标签 <...>（结构不动，标签内文本本就不可见）
        text = re.sub(r'<[^>]+>', lambda m: self._stash_raw(m.group(0)), text)

        # 8. GitBook 模板标签 {% ... %}
        text = re.sub(r'{%[^%]*%}', lambda m: self._stash_raw(m.group(0)), text)

        # 9. 裸 URL
        text = re.sub(r'https?://[^\s)>\]]+',
                      lambda m: self._stash_raw(m.group(0)), text)

        # 10. 强调：加粗 **..** / __..__ ，删除线 ~~..~~
        text = re.sub(r'(\*\*)([^*\n]+?)(\*\*)', self._stash_emph, text)
        text = re.sub(r'(__)([^_\n]+?)(__)', self._stash_emph, text)
        text = re.sub(r'(~~)([^~\n]+?)(~~)', self._stash_emph, text)

        # 11. 对剩余可见纯文本套用空格规则
        text = self._apply_text_rules(text)

        # 12. 还原所有占位符
        text = self._restore(text)

        # 收尾：压缩行内多余空格为一个（不动行首/行尾空白）
        text = re.sub(r'(?<=\S)  +(?=\S)', ' ', text)

        return text


def format_file(path):
    """格式化单个文件，返回是否发生改变。"""
    try:
        with open(path, 'r', encoding='utf-8', newline='') as f:
            original = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f'[SKIP] {path}: {e}')
        return False

    formatter = Formatter()
    formatted = formatter.format(original)

    if formatted == original:
        print(f'[OK]   {path}')
        return False

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(formatted)
    print(f'[FIX]  {path}')
    return True


def main(argv):
    if len(argv) < 2:
        print('Usage: python format_cn_en_spacing.py <file.md> [<file.md> ...]')
        return 0

    changed = 0
    for path in argv[1:]:
        if not path.lower().endswith('.md'):
            continue
        if re.search(r'(^|/)(i18n|\.gitbook|\.github|scripts)(/|$)', path):
            continue
        if format_file(path):
            changed += 1

    print(f'\nDone. {changed} file(s) changed.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
