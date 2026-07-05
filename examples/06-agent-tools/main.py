def get_order_status(order_id: str):
    return {
        "order_id": order_id,
        "status": "已发货",
        "estimate_time": "明天送达",
    }


def run_agent(user_message: str):
    # This is a rule-based mock agent.
    # In a real project, the LLM decides which tool to call.
    if "订单" in user_message:
        order_id = "10086"
        tool_result = get_order_status(order_id)
        return {
            "tool_called": "get_order_status",
            "tool_result": tool_result,
            "final_answer": (
                f"订单 {tool_result['order_id']} {tool_result['status']}，"
                f"预计{tool_result['estimate_time']}。"
            ),
        }

    return {
        "tool_called": None,
        "tool_result": None,
        "final_answer": "这个问题暂时不需要调用工具。",
    }


if __name__ == "__main__":
    message = input("用户：")
    result = run_agent(message)
    print("调用工具：", result["tool_called"])
    print("最终回答：", result["final_answer"])

