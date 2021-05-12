from flask import Flask, render_template
import json
import os.path

app = Flask(__name__)
dirpath = os.environ["ASitePATH"] + "/"

@app.route("/")
def root():
    return render_template("home.html", title="home", post=None)

@app.route('/projects')
@app.route("/projects/<project>")
def projects(project=None):
    with open("projects.json", "r") as f:
        project_info = json.loads(f.read())
    if project == None:
        return render_template("projects.html", title="projects", projects=project_info)
    else:
        for p in project_info["projects"]:
            if p["name"] == project:
                if os.path.isfile(f"{dirpath}static/images/{p['name']}.jpg"):
                    image_type = "jpg"
                elif os.path.isfile(f"{dirpath}static/images/{p['name']}.png"):
                    image_type = "png"
                elif os.path.isfile(f"{dirpath}static/images/{p['name']}.gif"):
                    image_type = "gif"
                else:
                    image_type = False
                
                if "link" not in p:
                    p["link"] = None
                
                p["source"] = []
                with open(f"{dirpath}templates/projects/{project}.md", "r") as f:
                    for line in f.readlines():
                        p["source"].append(line.rstrip())
                        p["source"].append("\\n")
                    p["source"] = "".join(p["source"])
                    print(p["source"])
                
                return render_template("project_details.html", title=project, project=p, image=image_type)

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run()
