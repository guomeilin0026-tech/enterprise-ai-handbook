documents = [
    {
        "id": "doc_001",
        "title": "员工手册",
        "content": "员工入职满一年后可享受年假，年假天数根据入职年限计算。",
    },
    {
        "id": "doc_002",
        "title": "报销制度",
        "content": "报销需要提交发票、审批单和费用说明。",
    },
    {
        "id": "doc_003",
        "title": "离职制度",
        "content": "离职工资会在离职手续完成后的下一个工资日发放。",
    },
]


def search_documents(question: str):
    if "年假" in question:
        return documents[0]
    if "报销" in question:
        return documents[1]
    if "离职" in question or "工资" in question:
        return documents[2]
    return None


def answer_question(question: str):
    document = search_documents(question)
    if document is None:
        return {
            "answer": "资料中没有找到相关信息。",
            "source": None,
        }

    return {
        "answer": f"根据《{document['title']}》：{document['content']}",
        "source": document,
    }


if __name__ == "__main__":
    question = input("请输入问题：")
    result = answer_question(question)
    print(result["answer"])
    if result["source"]:
        print("引用来源：", result["source"]["title"])

