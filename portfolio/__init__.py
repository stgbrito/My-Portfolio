from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracker.png",
        "hero": "img/habit-tracker-hero.png",
        "categories": ["Python", "Web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-1get.onrender.com",
    },
    {
        "name": "Micro Blog app with Python and MongoDB",
        "thumb": "img/micro-blog.png",
        "hero": "img/micro-blog_hero.png",
        "categories": ["Python", "Web"],
        "slug": "micro-blog",
        "prod": "https://python-web-microblog-9ihi.onrender.com",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance_hero.png",
        "categories": ["JavaScript", "react"],
        "slug": "personal-finance",
    },
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/projects/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404