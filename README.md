# 収集くんバックエンド

## 起動方法・環境構築

以下順番に実行してください。

- 全パッケージのインストール

```
docker-compose run --entrypoint "poetry install" shushukun-api
```

- DB の作成

```
docker-compose exec shushukun-api poetry run python -m api.migrate_db
```

- Docker コンテナの起動

```
docker-compose build
docker-compose up
```

## その他コマンド

- 新しいパッケージを追加したい時

```
docker-compose exec shushukun-api poetry add <パッケージ名>
```

- データベース内に入りたい時

```
docker-compose exec db mysql demo
```

## VSCode の pylance がパッケージを読み込んでくれない時

- ルート直下に`.vscode`というディレクトを生成
- その中に`.settings.json`を作成
- 内容を以下のように編集

```json
{
  "python.analysis.extraPaths": [
    // ルート直下に生成された.dockervenv/lib/python3.9/site-packagesのパス
  ]
}
```
