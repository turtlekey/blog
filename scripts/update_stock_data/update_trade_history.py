import yaml
from datetime import datetime

def extract_data() -> dict:
    """从raw_data.txt中提取数据
    """
    today = datetime.now().strftime('%Y-%m-%d')
    data = {"date": today}
    with open('./raw_data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

        summary_data = lines[0].strip()[5:].split()
        available_money = float(summary_data[1].split(':')[-1])
        capital = float(summary_data[3].split(':')[-1])
        total_assets = float(summary_data[4].split(':')[-1])
        data["total_assets"] = total_assets
        data["capital"] = capital
        data["available_money"] = available_money

        stocks_data = lines[4:]
        data["stocks"] = []
        for stock_data in stocks_data:
            stock_data = stock_data.strip().split()
            stock_name = stock_data[1]
            if "标准券" not in stock_name:
                stock = {
                    "name": stock_name,
                    "symbol": stock_data[0],
                    "capital": float(stock_data[6]),
                    "profit": float(stock_data[7]),
                    "profit_ratio": float(stock_data[8]),
                }
                data["stocks"].append(stock)
    return data


def write_to_yaml(data: dict) -> None:
    """将数据写入到trade_history.yaml中
    """
    with open('../../data/stock/trade_history.yaml', 'a', encoding='utf-8') as f:
        yaml.dump([data], f, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    data = extract_data()
    write_to_yaml(data)