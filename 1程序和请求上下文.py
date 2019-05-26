# 在程序实例上调用 app.app_context() 可获得一个程序上下文。
from hello import app
from flask import current_app
# print(current_app.name)
app_ctx = app.app_context()
app_ctx.push()
print(current_app.name)
app_ctx.pop()
