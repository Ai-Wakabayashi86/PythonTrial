# ========== 1. データの読み取り ==========
logs = []

# 対象ファイルを開く(r: 読み取り専用)
f = open("testdata_1.txt", "r")

#　1行目から最後の行まで繰り返す
for line in f:
    # 単語ごとに分ける
    # (strip: 前後の空白や改行を取り除く)
    # (split: スペースで区切ってリストにする)
    parts = line.strip().split()

    # それぞれのデータに名前を付けてわかりやすい辞書にしている
    log = {
        "date": parts[0],
        "status": int(parts[3]),
        "path": parts[4]
    }
    # 次の行の処理に移行する
    logs.append(log)
# 対象ファイルを閉じる
f.close()


# ========== 2. ステータス集計 ==========
status_count = {}

#　1行目から最後の行まで繰り返す
for log in logs:
    status = log["status"]
    # logのstatusの要素数を出す
    if status not in status_count:
        status_count[status] = 0

    status_count[status] += 1

print(status_count)


# ========== 3. エラー抽出 ==========
errors = []

#　logの1行目から最後の行まで繰り返す
for log in logs:
    # statusが400以上の場合errorsにlogの要素を追加する
    if log["status"] >= 400:
        errors.append(log)

print(errors)