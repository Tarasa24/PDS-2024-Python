<center>
<img align="left" width="128px" src="https://i.imgur.com/gH2j4E7.png">
<h1>PDS 2024 - Python</h1>
Parallel and Distributed Systems primiteves using Python. Created as a part of KMI/PDS 2024 course at UPOL University in Olomouc.
</center>
</br>

---

## General info

This repository serves as a a colaboration space for students selected to present Python as a part of the PDS 2024 course at [UPOL University in Olomouc](https://www.inf.upol.cz/). The main goal is to provide a comprehensive overview of parallel and distributed systems primitives using Python programming language. The repository is divided into several sections, each of which covers a specific topic. The topics are presented in the form of a presentation, code examples, and web-handouts.

## How do I...?

### ...view the presentation?
Open the latest release and download the `pdf` file. https://tarasa24.github.io/PDS-2024-Python/

### ...view the code examples?
Navigate to the `code` directory in the [web-handout](https://tarasa24.github.io/PDS-2024-Python/) and select the desired topic.

### ...embed code snippets in my presentation?
Open the [Carbon Code Visualizer](https://carbon.now.sh/) in the browser of your choice. Roughly match the settings to the ones used in the repository. Copy over your code and generate the image. Download the image and embed it in the presentation.

### ...generate the pdf presentation?
Make sure you have TeX Live package installed on your system (texlive-latex-base, texlive-latex-recommended, texlive-fonts-recommended, texlive-latex-extra and texlive-lang-czechslovak). Navigate to the `presentation` directory and run the following commands:

```bash
  pdflatex -file-line-error -output-directory=presentation presentation/prezentace.tex
  pdflatex -file-line-error -output-directory=presentation presentation/prezentace.tex
```

That is not a typo, you need to run the command twice to generate the table of contents.

### ...generate the web-handouts?
Firstly make sure to generate markdown from code snippets using provided `py2md.sh` script. 
```bash
  ./web-handout/py2md.sh codes/ web-handout/quartz/content/codes/
```

Then you can proceed with generating the web-handout as a whole. Navigate to the `web-handout` directory and run the following commands. Make sure you have [Node.js](https://nodejs.org/en/) installed on your system.

```bash
  npm install
  npx quartz build
  # or if you want to serve the web-handout locally
  npm quartz build --serve
```

### ...contribute with least effort?
Simply open new pull request with your changes. Make sure to follow the repository structure and naming conventions. The CI/CD pipeline will take care of the rest.

---

## Technologies

- **Presentation**:
  - [Latex](https://www.latex-project.org/)
  - [Beamer](https://ctan.org/pkg/beamer?lang=en)
- **Code**:
  - [Python](https://www.python.org/)
  - [Carbon Code Visualizer](https://carbon.now.sh/)
- **Web-Handouts**:
  - [Markdown](https://www.markdownguide.org/)
  - [Quartz 4](https://quartz.jzhao.xyz/)