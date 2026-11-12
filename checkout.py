# checkout.py 结算模块
# 新增功能：学生享受10%折扣（9折），非学生原价
def checkout(goods_name, price, count, is_student):
    """
    结算函数：计算总价、自动判断学生折扣，确认支付
    参数：
        goods_name: 商品名称（字符串）
        price: 商品单价
        count: 购买数量
        is_student: bool，True=学生（9折），False=非学生（原价）
    返回值：
        True：确认支付成功
        False：取消支付
    """
    # 原始总价（未打折）
    original_total = price * count

    if is_student:
        discount_rate = 0.9   # 学生 10% 折扣 → 乘以0.9
        final_total = original_total * discount_rate
        discount_money = original_total - final_total
    else:
        discount_rate = 1.0   # 不打折
        final_total = original_total
        discount_money = 0

    print("\n===== 【结算页面】 =====")
    print(f"商品名称：{goods_name}")
    print(f"商品单价：{price} 元")
    print(f"购买数量：{count}")
    print(f"原价合计：{original_total:.2f} 元")

    if is_student:
        print(f"✅ 识别为学生，享受10%折扣！")
        print(f"优惠金额：{discount_money:.2f} 元")
    else:
        print(f"普通用户，无折扣")

    print(f"👉 应付金额：{final_total:.2f} 元")

    confirm = input("请问确认支付吗？输入 y 确认 / n 取消：")
    if confirm.lower() == 'y':
        return True
    else:
        return False
