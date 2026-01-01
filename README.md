# LLM-Based WSJ News Sentiment

`python` `pandas` `OpenAI API` `Excel(.xlsx)` `macro-analysis`

## Introduction

本仓库包含一个用于**按指定日期筛选 WSJ 新闻**，并调用 OpenAI 模型对每条新闻做“如果你是当年的经济学家，这条新闻对 GDP 的影响倾向如何？”的自动化分析脚本。

脚本的核心目标：
- 从 Excel 数据集中按日期筛选新闻（标题 + 正文）
- 对筛选出的每条新闻调用模型生成结构化判断：
  - `{increase/decrease/uncertain}: {confidence(0-1)}: {magnitude(0-1)}: {explanation(<25 words)}`

## Methodological Framework（方法框架）

总体流程如下：

1. **读取 Excel**（三列：日期 / 新闻标题 / 新闻内容）
2. **日期清洗与解析**（将“日期”转换为可比较的 datetime）
3. **按指定日期过滤**（仅保留当天新闻）
4. **逐条调用模型分析**（生成结构化输出）
5. **打印结果**（便于终端查看与后续复制保存）

## Repository Structure

```text
.
├── trial2_1.py              # 主脚本：按日期筛选 + 调用模型分析
└── README.md                # 项目说明（本文件）

