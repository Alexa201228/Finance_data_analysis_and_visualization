from modules.finance_analysis_and_visualization import FinanceAnalysis

if __name__ == '__main__':

    finance_analysis = FinanceAnalysis()
    finance_analysis.get_common_finance_stats()
    finance_analysis.show_price_changes()
    finance_analysis.show_everyday_profit_changes_and_its_hist()
    finance_analysis.analyse_trend()
    finance_analysis.everyday_profit_and_volume()
    finance_analysis.correlation_etf_analysis()
    finance_analysis.volatility_analysis()
