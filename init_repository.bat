REM initial repository
echo "# ForEis2020" >> README.md
cd ..
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:EIS20172020/ForEis2020.git
git push -u origin master