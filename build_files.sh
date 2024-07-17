# build_files.sh
if ! command -v pip &> /dev/null; then
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     python get-pip.py  --user
fi
pip install -r requirements.txt
# python manage.py migrate
python3.9 manage.py collectstatic
