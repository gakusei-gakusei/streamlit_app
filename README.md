生成AIを使用したかどうか（No）
統計表名：人口ピラミッド（https://dashboard.e-stat.go.jp/pyramidGraph?screenCode=00570&regionCode=00000&pyramidAreaType=2）
データセット名：地域名、時点、年齢区分
データ取得日：2026/1/31
各列の意味：地域の名前（今回は全国のみ）、何年のデータか（5年ごと）、何歳のデータか（5歳ずつ）
単位：なし、年、歳
特記事項：年代ごとに別のデータとなっていたため、各csvファイルを統合、また一部加工。
未使用UI部品の利用：badge（表やグラフが表示されているか確認できるようにそれぞれの場所で使った）、subheader（titleよりも視認性が上がるのではないかと思い最上部で使った）、segmented_control（radioよりも視認性が上がるのではないかと思いサイドバー内で使った）
参考：Stock peer analysis（https://demo-stockpeers.streamlit.app/?ref=streamlit-io-gallery-favorites&stocks=AAPL%2CMSFT%2CGOOGL%2CNVDA%2CAMZN%2CTSLA%2CMETA ）、グラフの見せ方がきれいだと思いグラフのサイズを固定してみた。
