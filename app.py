from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("home.html", title="home", post={"title": "something cool", "date":"september 20 2021", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."})

@app.route('/projects')
@app.route("/projects/<project>")
def projects(project=None):
    if project == None:
        return render_template("projects.html", title="projects")
    else:
        return render_template(f"projects/{project}.html", title=project)

if __name__ == "__main__":
    app.run()
