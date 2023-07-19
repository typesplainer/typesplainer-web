<div align="center">
<img src="https://i.imgur.com/5IFkzIf.png" width="128px">
<h1>Typesplainer for the web</h1>
 A Python typehint explainer!

Available [as a cli](https://pypi.org/project/typesplainer), [as a website](https://wasimaster.xyz/typesplainer/), [as a vscode extension](https://marketplace.visualstudio.com/items?itemName=WasiMaster.typesplainer)

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fwasimaster.xyz%2Ftypesplainer)](https://wasimaster.xyz/typesplainer/) [![PyPI](https://img.shields.io/pypi/v/typesplainer?label=cli)](https://pypi.org/project/typesplainer) [![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/WasiMaster.typesplainer?label=vscode)](https://marketplace.visualstudio.com/items?itemName=WasiMaster.typesplainer)
</div>

## To run locally

Extremely simple. Clone the repo, Install the python packages [`flask`](https://pypi.org/project/flask) and [`typesplainer`](https://pypi.org/project/typesplainer), `cd typesplainer-web/src/website`, `flask run`. So basically
```sh
git clone https://github.com/wasi-master/typesplainer-web
pip install flask
pip install typesplainer
cd typesplainer-web/src/website
flask run
```
The requirements.txt file does have the dependency uwsgi but that's for production deployment, for personal use that's not necessary.
