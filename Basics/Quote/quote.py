
# quoteは"", ''どちらでも用いることができます
quote = "dog"
print(quote)

# quoteの中に"もしくは'を使う場合
# 外側のquoteには内側と別の記号を使う必要があります
# Errorとなるコード例
# quote_in_quote_error = 'Who's dog?'
# print(quote_in_quote)

quote_in_quote = "Who's dog?"
print(quote_in_quote)

# 改行も考慮したquote
triple_quote = """line1

line2"""
print(triple_quote)
