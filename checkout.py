# checkout.py 结算模块
def checkout(goods_name, price, count):
    total = price * count
    print("\n===== 结算页面 =====")
    print(f"商品：{goods_name}")
    print(f"单价：{price} 元")
    print(f"数量：{count}")
    print(f"总价：{total} 元")
    confirm = input("确认支付？(y/n)：")
    if confirm.lower() == 'y':
        return True
    else:
        return False
