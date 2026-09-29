#!/usr/bin/env python3
"""
Knowledge Cards Skill 验证脚本
用于验证生成的知识卡片是否符合规范
"""

import re
import sys
from pathlib import Path

# 设置标准输出编码为 UTF-8
sys.stdout.reconfigure(encoding='utf-8')


def validate_card_format(content: str) -> dict:
    """验证知识卡片格式"""
    results = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "stats": {}
    }

    # 检查是否有卡片标题
    card_pattern = r"###\s+卡片\s*\d+[：:]\s*(.+)"
    cards = re.findall(card_pattern, content)
    results["stats"]["card_count"] = len(cards)

    if len(cards) < 1:
        results["errors"].append("未找到任何知识卡片（缺少 '### 卡片 N：' 格式的标题）")
        results["valid"] = False
    elif len(cards) < 5:
        results["warnings"].append(f"卡片数量较少（{len(cards)} 张），建议 5-8 张")
    elif len(cards) > 8:
        results["warnings"].append(f"卡片数量较多（{len(cards)} 张），建议 5-8 张")

    # 检查每张卡片的结构
    for i, card_title in enumerate(cards, 1):
        card_section = _extract_card_section(content, card_title)

        if not card_section:
            results["warnings"].append(f"卡片 {i} 内容可能不完整")
            continue

        # 检查核心知识
        if "**核心知识**" not in card_section:
            results["errors"].append(f"卡片 {i} 缺少 '核心知识' 字段")
            results["valid"] = False

        # 检查简明解释
        if "**简明解释**" not in card_section:
            results["errors"].append(f"卡片 {i} 缺少 '简明解释' 字段")
            results["valid"] = False

        # 检查例子/自测问题
        has_example = "例子" in card_section or "自测" in card_section
        if not has_example:
            results["warnings"].append(f"卡片 {i} 缺少例子或自测问题")

    # 检查是否编造内容（简单检查：是否有明显的虚构标记）
    fabrication_markers = ["虚构", "假设", "假设原文", "根据常识"]
    for marker in fabrication_markers:
        if marker in content:
            results["warnings"].append(f"发现可能的虚构内容标记：'{marker}'")

    return results


def _extract_card_section(content: str, card_title: str) -> str:
    """提取单张卡片的内容"""
    # 找到卡片标题的位置
    pattern = f"###\\s+卡片\\s*\\d+[：:]\\s*{re.escape(card_title)}"
    match = re.search(pattern, content)
    if not match:
        return ""

    start = match.start()
    # 找到下一个卡片标题或文档结尾
    next_card_pattern = r"###\s+卡片\s*\d+[：:]"
    remaining = content[match.end():]
    next_match = re.search(next_card_pattern, remaining)

    if next_match:
        end = match.end() + next_match.start()
    else:
        end = len(content)

    return content[start:end]


def validate_file(file_path: str) -> dict:
    """验证文件中的知识卡片"""
    path = Path(file_path)

    if not path.exists():
        return {"valid": False, "errors": [f"文件不存在: {file_path}"], "warnings": [], "stats": {}}

    if path.suffix not in [".md", ".txt"]:
        return {"valid": False, "errors": [f"不支持的文件类型: {path.suffix}"], "warnings": [], "stats": {}}

    content = path.read_text(encoding="utf-8")
    return validate_card_format(content)


def main():
    if len(sys.argv) < 2:
        print("用法: python quick_validate.py <文件路径>")
        print("示例: python quick_validate.py output.md")
        sys.exit(1)

    file_path = sys.argv[1]
    results = validate_file(file_path)

    print(f"\n{'='*50}")
    print(f"📚 知识卡片验证报告")
    print(f"{'='*50}")
    print(f"文件: {file_path}")
    print(f"卡片数量: {results['stats'].get('card_count', 0)}")
    print(f"状态: {'✅ 通过' if results['valid'] else '❌ 未通过'}")

    if results["errors"]:
        print(f"\n❌ 错误 ({len(results['errors'])}):")
        for error in results["errors"]:
            print(f"  - {error}")

    if results["warnings"]:
        print(f"\n⚠️  警告 ({len(results['warnings'])}):")
        for warning in results["warnings"]:
            print(f"  - {warning}")

    print(f"\n{'='*50}\n")

    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
