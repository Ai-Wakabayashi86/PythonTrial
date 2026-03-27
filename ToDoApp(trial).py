tasks = []

# 処理内容の選択
while True:
    print("="*10 + "メニュー" + "="*10)
    print("1:タスクの一覧表示")
    print("2:タスクの追加")
    print("3:タスクの削除")
    print("0:終了")

    choice = input("\n選んでください: ")


    # タスク一覧表示
    if choice == "1":
        # タスクがない場合
        if len(tasks) == 0:
            print("\nタスクがありません\n")
        # タスクがある場合
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    # タスク追加
    elif choice == "2":
        # 追加するタスクの入力
        add_task = input("\nタスクを入力してください: ")
        # 入力されたタスクが重複した場合
        if add_task in tasks:
            print("\nこのタスクは既に登録されています\n")
        # 入力されたタスクが重複していない場合
        else:
            tasks.append(add_task)
            print(f"\n「{add_task}」を追加しました\n")

    # 削除処理
    elif choice == "3":
        #タスクがない場合
        if len(tasks) == 0:
            print("\nタスクがありません\n")
        # タスクがある場合
        else:
            # タスク一覧を表示
            for i, task in enumerate(tasks,start=1):
                print(i, task)
            # 削除するインデックス番号を指定
            num = int(input("\n削除する番号を入力してください: "))
            index = num - 1
            # インデックス番号にタスクがある場合は削除
            if 0 <= index < len(tasks):
                delete_task = tasks.pop(index)
                print(f"\n「{delete_task}」を削除しました\n")
            # インデックス番号にタスクがない場合
            else:
                print("\n無効な番号です\n")
    # 処理を終了
    elif choice == "0":
        print("\n終了します\n")
        break

    # 0,1,2,3以外が入力された場合
    else:
        print("\n無効な入力です\n")
