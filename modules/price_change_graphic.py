"""
Модуль для построения графиков изменения цены по времени
"""

import matplotlib.pyplot as plt
from modules.utils import load_data


def show_price_changes():
    
    etf = load_data()

    fig, axs = plt.subplots(3, 2, figsize=(15, 15))
    axs[0, 0].plot(etf.index, etf['FXGD_cl'], 'tab:blue')
    axs[0, 0].set_title('FXGD')
    axs[0, 1].plot(etf.index, etf['FXRU_cl'], 'tab:orange')
    axs[0, 1].set_title('FXRU')
    axs[1, 0].plot(etf.index, etf['FXTB_cl'], 'tab:green')
    axs[1, 0].set_title('FXTB')
    axs[1, 1].plot(etf.index, etf['FXUS_cl'], 'tab:red')
    axs[1, 1].set_title('FXUS')
    axs[2, 0].plot(etf.index, etf['FXRL_cl'], 'tab:grey')
    axs[2, 0].set_title('FXRL')
    axs[2, 1].plot(etf.index, etf['FXCN_cl'], 'tab:purple')
    axs[2, 1].set_title('FXCN')

    for ax in axs.flat:
        ax.set(xlabel='Data', ylabel='Price')

    for ax in axs.flat:
        ax.label_outer()

    plt.show()