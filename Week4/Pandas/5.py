import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders.order_date.between('2020-02-01', '2020-02-29')]
    res = orders.merge(products, on = 'product_id', how = 'left')
    res = res.groupby('product_name')['unit'].sum().reset_index()

    return res[res.unit >= 100]
