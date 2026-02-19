# ICN Programming Course

<p align="center">
    <img width="500" alt="ICN Logo" src="https://github.com/Lenakeiz/ICN_Programming_Course/blob/main/Images/cog_neuro_logo_blue_png_0.png?raw=true">
</p>

---

## About This Course

The **ICN Programming Course** is a comprehensive 10-week introduction to Python programming designed for researchers and students in cognitive neuroscience and related fields. The course takes you from absolute beginner to building interactive experiments using PsychoPy - a powerful library for creating psychology and neuroscience experiments.

### What This Course Offers

- **Foundational Python Skills**: Variables, data types, control flow, functions, and basic concepts of object-oriented programming (functions, classes)
- **Scientific Computing**: NumPy for numerical operations, random number generation, and array manipulation
- **Data Handling**: File I/O, exception handling, and working with structured data using Pandas DataFrames
- **Data Visualization**: Matplotlib and Seaborn for creating publication-quality plots - with exploratory analysis made using the IMDB dataset
- **Version Control**: Git fundamentals for tracking changes and collaborating on code
- **Experiment Building**: PsychoPy for creating visual stimuli, collecting keyboard/mouse input, precise timing, audio output, and participant dialogs
- **Practical Exercises (with solutions)**: Each lecture includes hands-on exercises with provided solutions
- **Full Project Showcases**: During the course we build complete projects from scratch, including:
  - **Grid cell firing rate analysis** — starting from raw data of the [Gardner et al., 2022](https://www.nature.com/articles/s41586-021-04268-7) paper
  - **Exploratory analysis of the IMDB movie dataset** — data visualization and plotting with the [IMDB movie dataset](https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv)
  - **Videogame-inspired experiment** — an interactive videogame-style experiment demo built with PsychoPy

The course is structured around Jupyter notebooks, plus standalone Python scripts for the PsychoPy modules. All materials are designed to run in VS Code, Jupyter, or Google Colab — **except the PsychoPy lectures (weeks 9–10)**, which require the recommended Python version and cannot be run in Google Colab.

---

## Setup Instructions (Pipenv Environment)

This project uses **Pipenv** for dependency management with **Python 3.10** as the recommended version.

### Prerequisites

- **Python 3.10** installed on your system  
  - Download from [python.org](https://www.python.org/downloads/) or use [pyenv](https://github.com/pyenv/pyenv) to manage versions
- **Pipenv** installed  
  - If not installed: `pip install pipenv`

### Step 1: Clone the Repository

```bash
git clone https://github.com/Lenakeiz/ICN_Programming_Course.git
cd ICN_Programming_Course
```

### Step 2: Create and Activate the Pipenv Environment

```bash
# Create virtual environment with Python 3.10 and install dependencies
pipenv install

# Activate the virtual environment (run this before working on the course)
pipenv shell
```

### Step 3: Verify the Setup

```bash
# Check Python version (should be 3.10.x)
python --version

# Run a quick test
python week_1/hello_word.py
```

### Step 4: Open Jupyter notebooks in your IDE

Open the notebook files (`.ipynb`) in your preferred IDE — **VS Code is recommended**. Select the Pipenv environment as the Jupyter kernel so that the notebook uses the correct Python and installed packages. In VS Code, use the kernel picker in the top-right of the notebook and choose the interpreter from your Pipenv virtual environment.

### Useful Pipenv Commands

You can run these commands in a terminal within your IDE (e.g., VS Code's integrated terminal: *Terminal → New Terminal*) or in a standalone terminal.

| Command | Description |
|--------|-------------|
| `pipenv shell` | Activate the virtual environment |
| `pipenv run python script.py` | Run a script without activating the shell |
| `pipenv run jupyter notebook` | Start Jupyter without activating the shell |
| `pipenv install <package>` | Add <package> to the virtual environment |
| `exit` | Deactivate the pipenv shell |

### Dependencies (listed also in the Pipfile inside the project)

- **jupyter**, **ipykernel** — Notebooks and kernels
- **numpy**, **pandas** — Numerical computing and data manipulation
- **matplotlib**, **seaborn** — Data visualization
- **scipy** — Scientific computing
- **psychopy** — Experiment creation (stimuli, timing, input)
- **screeninfo** — Monitor detection for PsychoPy

---

## Week-by-Week Breakdown

| Week | Topics | Link |
|------|--------|------|
| **Week 1** | Python intro, first script, variables, arithmetic, lists (NumPy arrays) | [week_1/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_1) |
| **Week 2** | NumPy mathematical functions, random numbers; Git introduction | [week_2/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_2) |
| **Week 3** | Control flow (`if`/`elif`/`else`), loops, dictionaries, user input | [week_3/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_3) |
| **Week 4** | Object-oriented programming: functions and classes | [week_4/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_4) |
| **Week 5** | File handling, exceptions, working example with [Gardner et al. 2022](https://www.nature.com/articles/s41586-021-04268-7) [dataset](https://figshare.com/articles/dataset/Toroidal_topology_of_population_activity_in_grid_cells/16764508) showing a grid cell firing rate map visualization | [week_5/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_5) |
| **Week 6** | Python recap — expense tracker mini-project (lists, loops, conditionals, dictionaries, functions, files, plots) | [week_6/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_6) |
| **Week 7** | Pandas: DataFrames, Series, data loading, slicing, merging, and manipulation | [week_7/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_7) |
| **Week 8** | Data visualization with Matplotlib and Seaborn; Anscombe's Quartet and the importance of plotting; exploratory analysis with [IMDB movie dataset](https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv) | [week_8/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_8) |
| **Week 9** | PsychoPy Part 1: windows, shapes, lines, fixation crosses, images, text, keyboard input | [week_9/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_9) |
| **Week 10** | PsychoPy Part 2: timing, framerate, mouse/cursor input, audio output, randomization, input dialogs | [week_10/](https://github.com/Lenakeiz/ICN_Programming_Course/tree/main/week_10) |

---

## Repository Structure

```
ICN_Programming_Course/
├── week_1/          # Python basics
├── week_2/           # NumPy, Git
├── week_3/           # Control flow, dictionaries
├── week_4/           # Functions, OOP
├── week_5/           # Files, exceptions, plotting
├── week_6/           # Recap (expense tracker)
├── week_7/           # Pandas
├── week_8/           # Matplotlib, Seaborn
├── week_9/           # PsychoPy visual stimuli
├── week_10/          # PsychoPy timing, input, audio
├── Pipfile            # Pipenv dependencies
├── Pipfile.lock       # Locked dependency versions
└── README.md
```

---

## License

See [LICENSE](LICENSE) for details.
