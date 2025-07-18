#TranslatorBuddy 🌍
TranslatorBuddy is a lightweight Python-based tool designed to translate sentences from English, French, or German into a reference language using a custom dictionary. Perfect for travelers, language enthusiasts, or developers needing a simple translation solution without external dependencies. 🚀
## ✨ Features

* Multi-language Translation: Translates words from English, French, or German to a user-defined reference language.
* Custom Dictionary: Supports a user-provided dictionary for flexible translations.
* Punctuation Handling: Automatically handles multi-word translations (e.g., la programmation → laprogrammation).
* Fallback Mechanism: Retains untranslated words as-is if not found in the dictionary.
* No Dependencies: Built using Python’s standard library for maximum portability.

## 📋 Table of Contents

* Installation
* Usage
* Contributing
* License
* Contact
* Acknowledgments

## 🛠 Installation
Get started with TranslatorBuddy in just a few steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/translator-buddy.git
   ```
2. Navigate to the project directory:
  ```bash
  cd translator-buddy
  ```

3. Ensure Python 3.6+ is installed:

* Check your Python version:
```bash
    python --version
```

* No additional dependencies are required, as the project uses Python’s standard library.




## 🚀 Usage
Run the script and provide a dictionary and sentence to translate. Here’s an example:

1. Run the script:
```bash
python translator.py
```

2. Input Format:

* First line: Number of dictionary entries (n).
* Next n lines: Four words per line (reference word, English, French, German translations).
* Final line: Sentence to translate (mix of English, French, or German words).


3. Example: Input:
```plain
4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming
```
### Output:
```plain
man am kheili alaghemand in barnamenevisi
```
For more examples, check the examples folder.

## 🤝 Contributing
We welcome contributions to make TranslatorBuddy even better! To contribute:

1. Fork the repository.
2. Create a feature branch:
```bash
git checkout -b feature/your-feature
```

3. Commit your changes:
```bash
git commit -m "Add your feature"
```
4. Push to the branch:
```bash
git push origin feature/your-feature
```

5. Open a Pull Request.
See our Contributing Guidelines for more details.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact
Have questions or suggestions? Reach out:
* Maintainer: koorosh.nrp@gmail.com
* GitHub: TranslatorBuddy Repository
* Issues: Report bugs or suggest features via GitHub Issues

## 🙌 Acknowledgments

* Built with 💙 using Python’s standard library.
* Inspired by real-world text processing challenges.
* Thanks to all contributors who help improve TranslatorBuddy!


🌟 TranslatorBuddy: Your lightweight companion for custom translations! 🌟
