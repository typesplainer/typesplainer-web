<div align="center">
<img src="https://i.imgur.com/5IFkzIf.png" width="128px">
<h1>Typesplainer for the web</h1>
 A Python typehint explainer!

Available [as a cli](https://pypi.org/project/typesplainer), [as a website](https://typesplainer.vercel.app), [as a vscode extension](https://marketplace.visualstudio.com/items?itemName=WasiMaster.typesplainer)

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fwasimaster.xyz%2Ftypesplainer)](https://typesplainer.vercel.app) [![PyPI](https://img.shields.io/pypi/v/typesplainer?label=cli)](https://pypi.org/project/typesplainer) [![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/WasiMaster.typesplainer?label=vscode)](https://marketplace.visualstudio.com/items?itemName=WasiMaster.typesplainer)
</div>

## To run locally

Extremely simple. Clone the repo, install the dependencies from `requirements.txt`, `cd typesplainer-web/src/website`, `flask run`. So basically
```sh
git clone https://github.com/wasi-master/typesplainer-web
pip install -r requirements.txt
cd typesplainer-web/src/website
flask run
```
Production deployment on Vercel uses the Flask app through `api/index.py` and `vercel.json`, not `uWSGI`.
