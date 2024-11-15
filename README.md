## 環境構築

- ビルド
    ```
    docker-compose build
    ```
- コンテナの起動
    ```
    docker up -d
    ```

## 動作確認

- 動いたらOK
    ```
    docker-compose exec python-app python ./scripts/test/howToUse_Numpy.py
    ```

## 自分の勉強用としてgit管理
- github gitlab 等でリポジトリ作成
- リポジトリの初期化
    ```
    rm -rf .git
    ```
- 新しいリポジトリを初期化
    ```
    git init
    ```
- すべてのファイルをステージング
    ```
    git add .
    ```
- コミットを作成
    ```
    git commit -m "Initial commit"
    ```
- リモートリポジトリの設定
    ```
    git remote add origin <リモートリポジトリのURL>
    ```

- 最初のプッシュ
    ```
    git push -u origin main
    ```
