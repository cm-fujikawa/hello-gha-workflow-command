# デバッグメッセージの設定
print(f"::debug::Set the Octocat variable")

# 通知メッセージの設定
print(f"::notice file=app.js,line=1,col=5,endColumn=7::Missing semicolon")

# 警告メッセージの設定
print(f"::warning file=app.js,line=1,col=5,endColumn=7::Missing semicolon")

# エラーメッセージの設定
print(f"::error file=app.js,line=1,col=5,endColumn=7::Missing semicolon")

# ログの行のグループ化
print(f"::group::My title")
print(f"Inside group")
print(f"::endgroup::")

# ログ中の値のマスク
print(f"::add-mask::Mona The Octocat")
