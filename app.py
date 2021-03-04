from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("home.html", title="home")

@app.route('/projects')
@app.route("/projects/<project>")
def projects(project=None):
    if project == None:
        return render_template("projects.html", title="projects")
    else:
        return render_template(f"projects/{project}", title=project)
