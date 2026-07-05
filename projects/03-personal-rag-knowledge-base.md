# 项目 3：个人知识库问答系统

## 项目目标

掌握 RAG 完整流程。

## 用户故事

作为用户，我希望上传自己的文档，然后向 AI 提问，AI 根据文档回答并显示引用来源。

## 功能清单

- [ ] 上传 txt / markdown / PDF
- [ ] 文档解析
- [ ] 文本切分
- [ ] Embedding 向量化
- [ ] 存入 Qdrant
- [ ] 用户提问
- [ ] 检索相关片段
- [ ] 大模型基于资料回答
- [ ] 展示引用来源
- [ ] 删除文档

## RAG 流程

```text
文档上传
-> 解析
-> 切分
-> 向量化
-> 入库
-> 提问
-> 检索
-> 生成回答
```

## 后端接口

```text
POST /api/documents/upload
GET /api/documents
DELETE /api/documents/{id}
POST /api/knowledge/chat
```

## 验收标准

- [ ] 文档能成功入库
- [ ] 问相关问题能找到片段
- [ ] 回答有引用来源
- [ ] 问资料外问题能拒答

