# Wellcome!!!

This application has made for learning purpose

## Preparation

1. Linux/Windows/MacOS OS
2. Already installation python 3 version
3. Already installation pip (usually already installed if you install the python 3)
4. Already installation mysql/mariadb databases or [Xampp](https://www.apachefriends.org/download.html) for developer
5. Connect Internet

## Installation

Installation is easier, follow the instruction

Optional Note: for better development use virtual environment with python on your local computer, follow this [link](https://docs.python.org/3/tutorial/venv.html)

1. Open the project,

2. On root folder of project, run the script to terminal/cmd:

   ```bash
   pip install -r requirements.txt
   ```

3. Setting database mysql/mariadb with configuraion:

   ```
   host: 127.0.0.1
   database_name: apriori
   port: 3306
   username: root
   password: <blank>
   ```

4. Still on root folder project, run the script to terminal/cmd

   ```bash
   flask db upgrade
   ```

5. add file "lid.176.bin" in /root_folder_project/app/utils/model_language, you can [download it](https://drive.google.com/file/d/1SefhKloU4GnQV2EEp7L96Fg70pPsJJHN/view?usp=sharing)

   

## Start

Finally, running the application

```bash
python run.py
```



