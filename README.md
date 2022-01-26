README v1.1.0

# 収集くんバックエンド

## 起動方法・環境構築

以下順番に実行してください。

- 本リポジトリをクローンする
- サービスコンテナをビルドする

```
docker-compose build
```

- 全パッケージのインストール

```
docker-compose run --entrypoint "poetry install" shushukun-api
```

- DB の作成

```
docker-compose exec shushukun-api poetry run python -m api.migrate_db
```

- サービスコンテナの起動

```
docker-compose up
```

## 開発方法

基本的には以下の手順に従い開発を行っていく。
branch 命名などは後述する

- issue に assign する
- 開発用 branch を切りそこで作業する（main から分岐する）
- コミットする。コミットには commitizen を用いることを推奨する。

```
git cz
```

- push し pull request を立てる。

  - pull request は作業が完了していなくても draft で立てることを推奨する（進捗が目に見えて分かるため）

- マージする(この時必ず squash merge をする)

## 開発ルール

### ブランチについて

- 基本的には main ブランチからブランチを切る
- 命名は`{build,chore,ci,feat,style,fix,revert,docs}/{ブランチで行う作業}`とする。
  - 例 1: feat/insert-auth
  - 例 2: docs/improve-readme
  - 例 3: ci/insert-github-workflow
- 大きな開発（〜〜ページの作成など）を行うときは例外とし`develop/{ブランチで行う作業}`というブランチを main から分ける
- この時の作業ブランチは`develop/〜〜`から分ける
- `develop/〜〜`から分けた作業ブランチをマージする時は**suquash merge**で良いが`develop/〜〜`を main にマージする時は**普通のマージ**を行うことに注意する

### コミットについて

- 基本的にコミットメッセージは commitizen を扱うことを前提としフォーマットもそれに合わせることとする

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
