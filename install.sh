#!/bin/sh

cd `dirname $0`

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install pyenv

echo 'export PYENV_ROOT=/usr/local/var/pyenv' >> ~/.bash_profile
echo 'if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi' >> ~/.bash_profile
. ~/.bash_profile

pyenv install 3.6.5
pyenv local 3.6.5

pip install slackclient --user
