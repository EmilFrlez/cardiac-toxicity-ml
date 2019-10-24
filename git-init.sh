#echo "# repository-ml" >> README.md
#echo "*.mp4" >> .gitignore
git init
git add .
git commit -m "first commit"

#git remote set-url origin git@github.com/EmilFrlez/lymphopenia-ml.git
git remote add origin https://github.com/EmilFrlez/cardiac-toxicity-ml.git
git remote -v
git push -u origin master
