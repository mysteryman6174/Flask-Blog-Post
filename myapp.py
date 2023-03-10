from flask import Flask, render_template, url_for
from sqlalchemy import create_engine, text

myapp = Flask(__name__)
db_string = "mysql+pymysql://oa9tcjva8jey22fvsyyy:pscale_pw_xqrbaQdLMb1DuYQrIz9F7Cr0BuVgw21vOZpVcPnmhiv@ap-south.connect.psdb.cloud/myblogs?charset=utf8mb4"
engine = create_engine(db_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

@myapp.route("/")
def root_html():
    return render_template("home.html")

@myapp.route("/blogs.html")
def blogs_html():
    with engine.connect() as conn:
        result = conn.execute(text("select * from blogs"))
    blogs = result.mappings().all()
    return render_template("blogs.html", blogs=blogs)

@myapp.route("/blogs/<id>")
def specific_blog(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from blogs where ID={id}"))
        result = dict(result.mappings().all()[0])
    return render_template('blog.html', blog= result)

@myapp.route("/about.html")
def about_html():
    return render_template("about.html")

if __name__ == "__main__":
    myapp.run(debug=True)
