# shop.py 简易网上购物系统【主程序】
# 功能：展示商品、选择商品、输入数量，调用checkout.py完成结算

# 从同文件夹的checkout文件中，导入checkout函数
from checkout import checkout


def main():
    """主函数：整个购物系统的入口"""
    # 用字典存放所有商品信息
    # 格式：编号 : {"name":商品名, "price":价格}
    goods = {
        1: {"name": "矿泉水", "price": 2},
        2: {"name": "面包", "price": 5},
        3: {"name": "笔记本", "price": 8},
        4: {"name": "中性笔", "price": 3}
    }

    print("===== 简易网上购物系统 =====")

    # while True 无限循环，一直运行购物界面，直到用户选择退出
    while True:
        print("\n---------- 商品列表 ----------")
        # 遍历商品字典，打印所有商品
        # k是商品编号，v是商品信息字典
        for k, v in goods.items():
            print(f"{k}. {v['name']}  价格：{v['price']} 元")
        # 0代表退出系统
        print("0. 退出购物系统")

        # 捕获异常：防止用户输入字母、符号导致程序崩溃
        try:
            # 获取用户输入的商品编号，转成整数
            choice = int(input("\n请输入想要购买的商品编号："))
        except ValueError:
            # 如果输入不能转数字，执行这里
            print("❌ 输入错误！请输入数字！")
            # continue：直接跳过本轮循环，回到开头重新选商品
            continue

        # 判断：输入0，退出循环，结束程序
        if choice == 0:
            print("感谢使用购物系统，再见！")
            break

        # 判断：输入的编号不在商品里面
        if choice not in goods:
            print("❌ 没有这个商品编号，请重新选择！")
            continue

        # 拿到选中商品的全部信息
        buy_good = goods[choice]

        # 输入购买数量，同样做异常捕获
        try:
            num = int(input(f"请输入【{buy_good['name']}】的购买数量："))
        except ValueError:
            print("❌ 数量输入错误！必须输入数字！")
            continue

        # 数量不能小于等于0
        if num <= 0:
            print("❌ 购买数量必须大于0！")
            continue

        # ========== 重点：调用外部文件的结算函数 ==========
        # 把商品名、单价、数量传给 checkout()
        # pay_result 接收 checkout 返回的 True / False
        pay_result = checkout(buy_good["name"], buy_good["price"], num)

        # 根据结算模块返回的结果，提示订单状态
        if pay_result:
            print("✅ 下单成功！订单提交完成！")
        else:
            print("❌ 已取消支付，订单作废！")


# 固定写法：直接运行这个文件的时候，才执行main()
# 如果别的文件导入shop.py，就不会自动运行main
if __name__ == "__main__":
    main()
