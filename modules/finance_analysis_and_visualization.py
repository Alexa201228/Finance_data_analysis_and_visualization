"""
Модуль, содержащий класс для анализа и визуализации данных в сфере финансов
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import stats

from modules.utils import load_data


class FinanceAnalysis:

    def __init__(self):
        self._etf = load_data()

    def get_common_finance_stats(self):
        self._etf.describe()

    def show_price_changes(self):

        fig, axs = plt.subplots(3, 2, figsize=(15, 15))
        axs[0, 0].plot(self._etf.index, self._etf['FXGD_cl'], 'tab:blue')
        axs[0, 0].set_title('FXGD')
        axs[0, 1].plot(self._etf.index, self._etf['FXRU_cl'], 'tab:orange')
        axs[0, 1].set_title('FXRU')
        axs[1, 0].plot(self._etf.index, self._etf['FXTB_cl'], 'tab:green')
        axs[1, 0].set_title('FXTB')
        axs[1, 1].plot(self._etf.index, self._etf['FXUS_cl'], 'tab:red')
        axs[1, 1].set_title('FXUS')
        axs[2, 0].plot(self._etf.index, self._etf['FXRL_cl'], 'tab:grey')
        axs[2, 0].set_title('FXRL')
        axs[2, 1].plot(self._etf.index, self._etf['FXCN_cl'], 'tab:purple')
        axs[2, 1].set_title('FXCN')

        for ax in axs.flat:
            ax.set(xlabel='Data', ylabel='Price')

        for ax in axs.flat:
            ax.label_outer()

        plt.show()

    def show_everyday_profit_changes_and_its_hist(self):

        # Вычисляем дневную доходность

        etf_new = self._calculate_everyday_profit()

        # Доходность в виде графика во времени
        fig, axs = plt.subplots(3, 2, figsize=(15, 15))
        axs[0, 0].plot(etf_new.index, etf_new['FXGD_cl_pct'], 'tab:blue')
        axs[0, 0].set_title('FXGD')
        axs[0, 1].plot(etf_new.index, etf_new['FXRL_cl_pct'], 'tab:orange')
        axs[0, 1].set_title('FXRL')
        axs[1, 0].plot(etf_new.index, etf_new['FXTB_cl_pct'], 'tab:green')
        axs[1, 0].set_title('FXTB')
        axs[1, 1].plot(etf_new.index, etf_new['FXUS_cl_pct'], 'tab:red')
        axs[1, 1].set_title('FXUS')
        axs[2, 0].plot(etf_new.index, etf_new['FXRU_cl_pct'], 'tab:grey')
        axs[2, 0].set_title('FXRU')
        axs[2, 1].plot(etf_new.index, etf_new['FXCN_cl_pct'], 'tab:purple')
        axs[2, 1].set_title('FXCN')

        for ax in axs.flat:
            ax.set(xlabel='Data', ylabel='Price')

        for ax in axs.flat:
            ax.label_outer()

        plt.show()

        sns.set(style="darkgrid")

        # Доходность в виде гистограммы
        fig, axs = plt.subplots(3, 2, figsize=(15, 15))

        sns.histplot(data=etf_new['FXGD_cl_pct'], kde=True, color="orange", ax=axs[0, 0])
        axs[0, 0].set_xlim(-10, 10)
        sns.histplot(data=etf_new['FXRL_cl_pct'], kde=True, color="olive", ax=axs[0, 1])
        axs[0, 1].set_xlim(-10, 10)
        sns.histplot(data=etf_new['FXTB_cl_pct'], kde=True, color="gold", ax=axs[1, 0])
        axs[1, 0].set_xlim(-10, 10)
        sns.histplot(data=etf_new['FXUS_cl_pct'], kde=True, color="grey", ax=axs[1, 1])
        axs[1, 1].set_xlim(-10, 10)
        sns.histplot(data=etf_new['FXRU_cl_pct'], kde=True, color="teal", ax=axs[2, 0])
        axs[2, 0].set_xlim(-10, 10)
        sns.histplot(data=etf_new['FXCN_cl_pct'], kde=True, color="brown", ax=axs[2, 1])
        axs[2, 1].set_xlim(-10, 10)

        plt.show()

    def _trend(self, x):
        if -0.5 < x <= 0.5:
            return 'Практически или без изменений'
        elif 0.5 < x <= 1.5:
            return 'Небольшой позитив'
        elif -1.5 < x <= -0.5:
            return 'Небольшой негатив'
        elif 1.5 < x <= 2.5:
            return 'Позитив'
        elif -2.5 < x <= -1.5:
            return 'Негатив'
        elif 2.5 < x <= 5:
            return 'Значительный позитив'
        elif -5 < x <= -2.5:
            return 'Значительный негатив'
        elif x > 5:
            return 'Максимальный позитив'
        elif x <= -5:
            return 'Максимальный негатив'

    def analyse_trend(self):

        etf_new = self._calculate_everyday_profit()

        for stock in etf_new.columns[12:]:
            etf_new["Trend_" + str(stock)] = np.zeros(etf_new[stock].count())
            etf_new["Trend_" + str(stock)] = etf_new[stock].apply(lambda x: self._trend(x))

        sns.set(style="darkgrid")

        fig, axs = plt.subplots(3, 2, figsize=(40, 37))

        axs[0, 0].pie(etf_new['Trend_FXGD_cl_pct'].value_counts(), pctdistance=1.2, autopct="%.2f%%")
        axs[0, 0].set_title('FXGD')

        axs[0, 1].pie(etf_new['Trend_FXRL_cl_pct'].value_counts(), pctdistance=1.2, autopct="%.2f%%")
        axs[0, 1].set_title('FXRL')

        axs[1, 0].pie(etf_new['Trend_FXTB_cl_pct'].value_counts(), pctdistance=1.2, autopct="%.2f%%")
        axs[1, 0].set_title('FXTB')

        axs[1, 1].pie(etf_new['Trend_FXUS_cl_pct'].value_counts(), pctdistance=1.2, autopct="%.2f%%")
        axs[1, 1].set_title('FXUS')

        axs[2, 0].pie(etf_new['Trend_FXRU_cl_pct'].value_counts(), pctdistance=1.2, autopct="%.2f%%")
        axs[2, 0].set_title('FXRU')

        axs[2, 1].pie(etf_new['Trend_FXCN_cl_pct'].value_counts(), pctdistance=1.2, autopct="%.2f%%")

        axs[2, 1].set_title('FXCN')
        labels = etf_new['Trend_FXCN_cl_pct'].value_counts().index
        fig.legend(labels, loc='lower left', prop={'size': 30}, bbox_transform=fig.transFigure)
        plt.show()

    def _calculate_everyday_profit(self) -> pd.DataFrame:

        etf_cl = self._etf[['FXGD_cl', 'FXRL_cl', 'FXTB_cl', 'FXUS_cl', 'FXRU_cl', 'FXCN_cl']]
        etf_cl_pct = etf_cl.pct_change() * 100
        etf_cl_pct.columns = ['FXGD_cl_pct', 'FXRL_cl_pct', 'FXTB_cl_pct', 'FXUS_cl_pct', 'FXRU_cl_pct', 'FXCN_cl_pct']
        etf_vol = self._etf[['FXGD_vol', 'FXRL_vol', 'FXTB_vol', 'FXUS_vol', 'FXRU_vol', 'FXCN_vol']]
        etf_new = pd.concat([etf_cl, etf_vol, etf_cl_pct], axis=1)
        etf_new = etf_new.dropna()
        return etf_new

    def everyday_profit_and_volume(self):

        etf_trend = self._calculate_everyday_profit()
        sns.set(style="darkgrid")

        fig, axs = plt.subplots(6, 1, figsize=(30, 35))

        axs[0].stem(etf_trend.index[-253:], etf_trend['FXGD_cl_pct'][-253:])
        axs[0].plot((etf_trend['FXGD_vol'] / 10000)[-253:], color='green', alpha=0.5)
        axs[0].set_title('FXGD')

        axs[1].stem(etf_trend.index[-253:], etf_trend['FXRL_cl_pct'][-253:])
        axs[1].plot((etf_trend['FXRL_vol'] / 10000)[-253:], color='green', alpha=0.5)
        axs[1].set_title('FXRL')

        axs[2].stem(etf_trend.index[-253:], etf_trend['FXTB_cl_pct'][-253:])
        axs[2].plot((etf_trend['FXTB_vol'] / 10000)[-253:], color='green', alpha=0.5)
        axs[2].set_title('FXTB')

        axs[3].stem(etf_trend.index[-253:], etf_trend['FXUS_cl_pct'][-253:])
        axs[3].plot((etf_trend['FXUS_vol'] / 10000)[-253:], color='green', alpha=0.5)
        axs[3].set_title('FXUS')

        axs[4].stem(etf_trend.index[-253:], etf_trend['FXRU_cl_pct'][-253:])
        axs[4].plot((etf_trend['FXRU_vol'] / 10000)[-253:], color='green', alpha=0.5)
        axs[4].set_title('FXRU')

        axs[5].stem(etf_trend.index[-253:], etf_trend['FXCN_cl_pct'][-253:])
        axs[5].plot((etf_trend['FXCN_vol'] / 10000)[-253:], color='green', alpha=0.5)
        axs[5].set_title('FXCN')

        plt.show()

    def correlation_etf_analysis(self):

        etf_new = self._calculate_everyday_profit()
        pct_chg_etf = etf_new[etf_new.columns[12:]]
        a_1 = pct_chg_etf.FXGD_cl_pct
        b_1 = pct_chg_etf.FXUS_cl_pct
        b_2 = pct_chg_etf.FXCN_cl_pct

        g_1 = sns.jointplot(pct_chg_etf, x='FXGD_cl_pct', y='FXCN_cl_pct', kind='scatter')
        r_1, p_1 = stats.pearsonr(a_1, b_1)
        g_1.ax_joint.annotate(f'$\\rho = {r_1:.3f}, p = {p_1:.3f}$',
                              xy=(0.1, 0.9), xycoords='axes fraction',
                              ha='left', va='center',
                              bbox={'boxstyle': 'round', 'fc': 'powderblue', 'ec': 'navy'})

        g_1.ax_joint.scatter(a_1, b_1)
        g_1.set_axis_labels(xlabel='FXGD', ylabel='FXUS', size=15)

        g_2 = sns.jointplot(pct_chg_etf, x='FXUS_cl_pct', y='FXGD_cl_pct', kind='scatter')
        r_2, p_2 = stats.pearsonr(a_1, b_2)
        g_2.ax_joint.annotate(f'$\\rho = {r_2:.3f}, p = {p_2:.3f}$',
                              xy=(0.1, 0.9), xycoords='axes fraction',
                              ha='left', va='center',
                              bbox={'boxstyle': 'round', 'fc': 'powderblue', 'ec': 'navy'})

        g_2.ax_joint.scatter(a_1, b_2)
        g_2.set_axis_labels(xlabel='FXGD', ylabel='FXCN', size=15)

        plt.tight_layout()

        plt.show()

    def volatility_analysis(self):

        etf_new = self._calculate_everyday_profit()
        pct_chg_etf = etf_new[etf_new.columns[12:]]
        sns.set(style="darkgrid")

        fig, axs = plt.subplots(6, 1, figsize=(30, 35))

        for i, etf in enumerate(pct_chg_etf.columns):
            axs[i].plot(pct_chg_etf[etf].rolling(5).std() * np.sqrt(5))
            axs[i].plot(pct_chg_etf[etf].rolling(7).mean())
            axs[i].set_title(etf[:4], size=20)

        plt.show()
