PYTHON_VERSION="python3.8"

if [ $(dpkg-query -W -f='${Status}' virtualenv 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt install virtualenv;
  . ~/.bash_profile;
fi

dir=venv;
if [ ! -d $dir ]; then
    virtualenv venv -p $PYTHON_VERSION
fi

. ./venv/bin/activate;

pip3 install -r requirements.txt

python3 manage.py migrate