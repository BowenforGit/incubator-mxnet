import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

if __name__ == "__main__":
    colors = ['#6187a5', '#896689', '#f4a680', '#cec591']
    df = pd.read_csv("logs/resnet101v1-cifar10.csv")
    fig, ax = plt.subplots()
    width = 0.35
    for i, mode in enumerate(['sync', 'synccol', 'async', 'asynccol']):
        df_tmp = df[df['Mode'] == mode]
        ax.bar(df_tmp['Workers']+width*(i-1.5), df_tmp['Time'], width, label=mode, color=colors[i])
    ax.set_xticks([2,4,6,8])
    ax.set_ylabel('Time (s)')
    ax.set_title('ResNet101v1 CIFAR10 1 epoch')
    ax.set_xlabel('Number of workers (= number of servers)')
    ax.legend()
    plt.savefig('logs/resnet101v1cifar10.png', dpi=1600)
    plt.show()
