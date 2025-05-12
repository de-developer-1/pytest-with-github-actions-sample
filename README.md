# pytest-with-github-actions-sample
概要
==============
これは、以下を示すサンプルPythonプロジェクトです：
- Pytestによる単体テスト
- GitHub Actionsを使用した継続的インテグレーション（CI）
- コード品質のためのPre-commitフック

プロジェクト構造
==============
- `app/`: アプリケーションのソースコード
- `tests/`: テストケース
- `.github/workflows/`: GitHub Actions設定
- `.pre-commit-config.yaml`: Pre-commitフック設定

セットアップと導入
==============

前提条件
--------------
- Python 3.8以上
- pip
- poetry（推奨）

ローカル開発セットアップ
--------------
1. リポジトリのクローン
```bash
git clone git@github.com:de-developer-1/pytest-with-github-actions-sample.git
cd pytest-gha-template
```

2. 依存関係のインストール
```bash
# pipを使用
pip install -r requirements.txt

# poetryを使用
poetry install
```

3. pre-commitフックのインストール
```bash
pre-commit install
```

テストの実行
--------------
```bash
# pytestを直接使用
pytest

# poetryを使用
poetry run pytest
```

継続的インテグレーション
==============
このプロジェクトはGitHub Actionsを使用して以下を実行します：
- 複数のPythonバージョンでテストを実行
- コードフォーマットをチェック
- リンターを実行
- カバレッジレポートを生成

Pre-commitフック
==============
以下を実行するように設定：
- Black（コードフォーマット）
- Flake8（リンティング）
- isort（インポートの整理）
- mypyによる型チェック

## リポジトリ構成

```
pytest-with-github-actions-sample/
├── .github/
│   └── workflows/
│       └── python-app.yml     # GitHub Actions設定
├── app/
│   ├── calculator.py           # サンプルアプリケーションコード
│   └── __init__.py
├── tests/
│   ├── test_calculator.py      # テストコード
│   └── __init__.py
├── .pre-commit-config.yaml     # pre-commit設定
├── pyproject.toml              # プロジェクト設定
├── README.md                   # プロジェクト説明書
└── .gitignore
```