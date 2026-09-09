#Name: Yuan Yu
#Assignment:  One
#ddl is 22/9/2026 23:59pm


while True:
    print("\n=== 作业 1：Python 基础 ===")
    print("1. 简易计算器")
    print("2. 问答机器人")
    print("3. 退出")

    choice = input("请选择（1-3）：").strip()

    if choice == "1":
        while True:
            print("\n--- 简易计算器 ---")
            count_text = input("你想计算几个数字？（输入 exit 返回主菜单）：").strip()

            if count_text.lower() == "exit":
                break

            try:
                count = int(count_text)
            except ValueError:
                print("请输入整数，例如 2、3 或 4。")
                continue

            if count < 2:
                print("至少需要计算两个数字。")
                continue

            # num 数组保存数字，sy 数组保存数字之间的运算符。
            num = []
            sy = []

            try:
                num.append(float(input("请输入第 1 个数字：")))
            except ValueError:
                print("请输入有效的数字。")
                continue

            # 有 count 个数字，因此数字之间有 count - 1 个运算符。
            for i in range(count - 1):
                while True:
                    symbol = input("请输入运算符（+、-、*、/）：").strip()
                    if symbol in {"+", "-", "*", "/"}:
                        sy.append(symbol)
                        break
                    print("运算符无效，请输入 +、-、* 或 /。")

                while True:
                    try:
                        next_number = float(input(f"请输入第 {i + 2} 个数字："))
                    except ValueError:
                        print("请输入有效的数字。")
                        continue

                    if symbol == "/" and next_number == 0:
                        print("除数不能为 0，请重新输入这个数字。")
                        continue

                    num.append(next_number)
                    break

            # 从第一个数字开始，按照输入顺序循环计算。
            result = num[0]
            for i in range(count - 1):
                if sy[i] == "+":
                    result = result + num[i + 1]
                elif sy[i] == "-":
                    result = result - num[i + 1]
                elif sy[i] == "*":
                    result = result * num[i + 1]
                elif sy[i] == "/":
                    result = result / num[i + 1]

            expression = ""
            for i in range(count):
                expression += f"{num[i]:g}"
                if i < count - 1:
                    expression += f" {sy[i]} "

            print(f"计算结果：{expression} = {result:g}")

            next_action = input("继续计算请输入 y，退出计算器请输入 exit：").strip().lower()
            if next_action == "exit":
                break

    elif choice == "2":
        print("Question Answering Bot")

        while True:
            question = input("Ask me something（输入 exit 返回主菜单）：")

            if question == "exit":
                break
            elif question == "hello":
                print("Bot: Hello! Nice to meet you.")
            elif question == "python":
                print("Bot: Python is a language.")
            elif question == "jetson":
                print("Bot: Jetson Nano is an AI computer.")
            elif question == "ai":
                print("Bot: AI means Artificial Intelligence.")
            elif question == "name":
                print("Bot: My name is Python Bot.")
            else:
                print("Bot: Sorry, I don't understand.")

    elif choice == "3":
        print("程序结束，再见！")
        break

    else:
        print("选择无效，请输入 1、2 或 3。")
