# Pytest と GitHub Actions の実践リポジトリ

## 概要
このリポジトリは、PythonプロジェクトにおけるpytestとGitHub Actionsを使った継続的インテグレーションのデモンストレーション用です。

## リポジトリ構成
```
pytest-with-github-actions-sample/
│
├── .github/
│   └── workflows/
│       └── python-app.yml        # GitHub Actions ワークフロー設定
│
├── app/
│   ├── calculator.py              # メインアプリケーションロジック
│   └── __init__.py
│
├── tests/
│   ├── test_calculator.py         # テストケース
│   └── __init__.py
│
├── requirements.txt               # 依存関係の定義
└── .gitignore
```

## 機能
- 基本的な算術演算を行う電卓クラス
- pytestを使用した包括的なテストスイート
- 自動テスト用のGitHub Actionsワークフロー

## はじめに

### 前提条件
- Python 3.9以上
- pip

### インストール
1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/pytest-gha-template.git
cd pytest-gha-template
```

2. （オプション）仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
```

3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### テストの実行
```bash
pytest
```

## GitHub Actions
このリポジトリは、以下のタイミングで自動的にテストを実行するGitHub Actionsを使用：
- mainブランチへのプッシュ時
- mainブランチへのプルリクエスト時

## 注意点
- このテンプレートは学習と実践のためのサンプルプロジェクトです
- 実際のプロジェクトに適用する際は、必要に応じてカスタマイズしてください