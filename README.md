# How to use #

# Getting started

Windows command prompt:

- [ ] **Make sure you have Python installed:**

   If you don't have Python installed yet, you need to download and install it first. You can download the Python installer from the official website: https://www.python.org/downloads/ . Use Python v 3.9


- [ ] **Clone the test repository:**

    Open the command prompt and navigate to the directory where you want to place the repository. Then, run the following command to clone the repository:
```sh
git clone https://gitlab.com/dymekk/google-maps-tests-python-api.git
```

- [ ] **Navigate to the test directory:**

   In the command prompt, navigate into the directory you just cloned: 
```sh
cd ur\path\google-maps-tests-python-api
  ```
- [ ] **add ur params to .env.example file**
- [ ] **rename .env.example to .env**
- [ ] **To create a folder named "logs" in the root directory of your project** 
- [ ] **Install the dependencies from the requirements.txt file:** 
```sh
pip install -r requirements.txt
```

- [ ] Run the tests: 
```sh
python -m pytest -s -v
```

