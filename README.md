# Cognitive Test Suite (Bilişsel Test Kiti)

A Python-based desktop application designed to administer fundamental psychological assessment tests. This project serves as a bridge between **Psychology** and **Software Development**, aiming to digitize standard cognitive tests while exploring GUI programming with Python.

## 🎯 Project Overview

This suite includes three distinct cognitive tests commonly used in experimental psychology to measure attention, working memory, and cognitive flexibility.

### The Tests included:

1.  **Attention Test (Visual Search Task):**
    * **Objective:** Measures selective attention and processing speed.
    * **Mechanism:** The participant must find a specific target letter ("T") hidden among distractor letters ("L") scattered randomly on a canvas. Reaction time is recorded in milliseconds.

2.  **Digit Span Test:**
    * **Objective:** Assesses working memory capacity (part of the WISC/WAIS scales).
    * **Mechanism:** A sequence of numbers appears briefly and then vanishes. The participant must recall and type the sequence. The span (number of digits) increases with every successful attempt.

3.  **Stroop Test:**
    * **Objective:** Measures cognitive interference and inhibition (Stroop Effect).
    * **Mechanism:** Participants are asked to identify the **color** of the text, not the word itself (e.g., the word "RED" printed in blue ink). This tests the brain's ability to inhibit the automatic reading process.

---

## 💡 Technical Focus & Learning Outcomes

This project was developed as a hands-on exercise to master the **Tkinter** library and understand event-driven programming. Key technical concepts implemented include:

* **Multi-Window Management (`Toplevel`):** Created independent windows for different tests and data entry screens while keeping the main application root active.
* **Canvas & Dynamic Graphics:** Utilized `tk.Canvas` for randomized visual stimuli generation (coordinate mapping for the Attention Test).
* **Event Binding:** Implemented custom event handlers for mouse clicks (`<Button-1>`) and UI interactions.
* **State Management:** Used `nonlocal` variables to manage game states, scores, and difficulty progression within nested functions.
* **Timing & Chronometry:** Implemented the `time` module to measure Reaction Times (RT) accurately.

---

## 🛠️ Built With

* **Python 3.x**
* **Tkinter** (Standard GUI toolkit for Python)
* **Random Module** (For stimulus randomization)
* **Time Module** (For performance tracking)

---

## 🚀 How to Run

Follow these steps to run the application on your local machine:

### Prerequisites

Make sure you have Python installed. You can check this by running:
```bash
python --version
Installation & Usage
Clone the repository:
Bash

git clone [https://github.com/your-username/cognitive-test-suite.git](https://github.com/your-username/cognitive-test-suite.git)
Navigate to the project directory:

Bash

cd cognitive-test-suite
Run the application:

Bash

python main.py
(Note: Replace main.py with the actual name of your python file if it differs).

👤 Author
Arda ÜNSAL Psychology Student
