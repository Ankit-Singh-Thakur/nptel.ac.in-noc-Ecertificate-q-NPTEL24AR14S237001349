echo "BUILD START"
python3.12 -m pip install -r requirents.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"