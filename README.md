# ログインページ サンプル

このリポジトリには、シンプルなログインページとそれを支える Flask バックエンドの例が含まれています。

## フロントエンドの実行

`index.html` をブラウザで直接開くか、任意の静的ファイルサーバーで配信してください。

## バックエンドの実行

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

デフォルトでは `http://127.0.0.1:5000` でサーバーが起動します。フロントエンドの JavaScript は同じ URL の `/api/login` に対してリクエストを送信します。

## デモ用アカウント

| ユーザー名 | パスワード | 表示名 |
| --- | --- | --- |
| `demo` | `demo123` | デモ ユーザー |
| `admin` | `secret` | 管理者 |

## 注意事項

- このサンプルでは教育目的のために平文のパスワードを使用しています。実運用では必ずハッシュ化と安全な保管を行ってください。
- CORS を利用する場合は `flask-cors` などを追加で設定してください。
