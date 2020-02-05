from config import app
from controller_functions import main, register, add_user, login, login_user, user, child, add_child, logout
app.add_url_rule("/", view_func=main, methods=["GET"])
app.add_url_rule("/register", view_func=register, methods=["GET"])
app.add_url_rule("/register_user", view_func=add_user, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["GET"])
app.add_url_rule("/login_user", view_func=login_user, methods=["POST"])
app.add_url_rule("/user", view_func=user, methods = ["GET"])
app.add_url_rule("/child", view_func=child,methods =["GET"])
app.add_url_rule("/add_child", view_func=add_child, methods=["POST"] )
app.add_url_rule("/logout",view_func=logout, methods = ["GET"])
