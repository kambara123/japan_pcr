# 国内PCR検査の実施人数(日毎)
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.mhlw.go.jp/content/pcr_case_daily.csv"
# データフレームの生成
df = pd.read_csv(url)
def main():
#    df.plt.title('グラフタイトル')
    df.plot.line(x="日付", y=["計"], figsize=(12, 8), title="国内PCR検査の実施人数(日毎)")


if __name__ == '__main__':
    main()
