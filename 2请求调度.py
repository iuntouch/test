from hello import app
app.url_map

# / 和 /user/<name> 路由在程序中使用 app.route 修饰器定义。/static/<filename> 路由是 Flask 添加的特殊路由，用于访问静态文件。

# URL 映射中的 HEAD、Options、GET 是请求方法，由路由进行处理。Flask 为每个路由都指 定了请求方法，这样不同的请求方法发送到相同的 URL 上时，会使用不同的视图函数进 行处理。HEAD 和 OPTIONS 方法由 Flask 自动处理，因此可以这么说，在这个程序中，URL 映射中的 3 个路由都使用 GET 方法。

# Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
#  <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
#  <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
