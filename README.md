<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=800&size=40&duration=3500&pause=1500&color=f5af19&center=true&vCenter=true&width=900&height=70&lines=%F0%9F%8E%AC%20Box%20Office%20Predictor" alt="Box Office Predictor"/>

<b><i>Predict movie revenue before the release</i></b>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=%F0%9F%8E%AC%20Predict%20movie%20box-office%20revenue;%F0%9F%93%88%20ML%20regression%20models;%F0%9F%8D%BF%20Genre%20%C2%B7%20Director%20%C2%B7%20Lead%20actor%20%C2%B7%20Country" alt="Typing SVG" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>

<img src="https://img.shields.io/github/stars/PreciousBharath/BOX-OFFICE-PREDICTION?style=social" alt="stars"/> <img src="https://img.shields.io/github/forks/PreciousBharath/BOX-OFFICE-PREDICTION?style=social" alt="forks"/> <img src="https://img.shields.io/github/last-commit/PreciousBharath/BOX-OFFICE-PREDICTION?style=flat-square&color=blueviolet" alt="last commit"/> <img src="https://img.shields.io/github/repo-size/PreciousBharath/BOX-OFFICE-PREDICTION?style=flat-square&color=success" alt="repo size"/>
</div>

---

## 🎬 About the Project

**Box Office Predictor** estimates a movie's **box-office revenue** using machine-learning regression. Users register, log in and enter movie details — title, genre, director, lead actor, country and more — and the trained model returns the predicted revenue instantly.

## ✨ Key Features

- 🔐 Register / login with **SQLite** user store
- 🎭 Encoded categorical features — genre, director, lead actor, country, title
- 📈 Regression model trained & evaluated in `box office.ipynb`
- 💰 Instant **revenue prediction** with a clean result page

## 🧠 How It Works

```mermaid
flowchart LR
I["🎬 Movie Details"] --> E["🔤 Label Encoders"] --> R["📈 Regression Model"] --> O["💰 Predicted Revenue"]
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data & ML | Pandas · NumPy · scikit-learn |
| Notebook | Jupyter |
| Web App | Flask + Jinja2 templates |
| Frontend | HTML5 · CSS3 |
| Database | SQLite (users.db) |

## 📂 Project Structure

```text
box office/
├── app.py                 # Flask app
├── box office.ipynb       # EDA + training
├── model.pkl              # regression model
├── genre.pkl · director.pkl · lead_actor.pkl · country.pkl · title.pkl
├── instance/users.db
├── static/css/style.css
└── templates/  (base, home, login, register, predict, result)
```

## 🚀 Getting Started

```bash
git clone https://github.com/PreciousBharath/BOX-OFFICE-PREDICTION.git
cd "BOX-OFFICE-PREDICTION/box office"
pip install flask flask-sqlalchemy pandas numpy scikit-learn
python app.py
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to ⭐ star the repo and open a pull request.

## 👨‍💻 Author

<div align="center">

**Bharath** — Software Developer · Project Engineer · Technical Trainer

<a href="https://github.com/PreciousBharath"><img src="https://img.shields.io/badge/GitHub-PreciousBharath-181717?style=for-the-badge&logo=github"/></a>
<a href="https://linkedin.com/in/connectbharath"><img src="https://img.shields.io/badge/LinkedIn-connectbharath-0A66C2?style=for-the-badge&logo=linkedin"/></a>

### 🍔 EAT · 💻 CODE · 😴 SLEEP · 🔁 REPEAT

⭐ **If you found this project useful, give it a star!** ⭐

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

</div>
