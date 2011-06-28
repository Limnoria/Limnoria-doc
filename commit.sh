make html
git commit "$@"
cd _build/html
git add .
git commit "$@"
git push
cd ../..
