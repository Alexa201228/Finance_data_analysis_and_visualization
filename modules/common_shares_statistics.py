"""
Модуль для построение описательной статистики по акциям
"""
from modules.utils import load_data

def get_common_finance_stats():
    etf = load_data()
    etf.describe()