#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    # brew outdated pyenv || brew upgrade pyenv
    # brew install pyenv-virtualenv
    brew install cmake || true

    # if which pyenv > /dev/null; then
    #     eval "$(pyenv init -)"
    # fi

    # CFLAGS="-I$(brew --prefix openssl)/include" \
    # LDFLAGS="-L$(brew --prefix openssl)/lib" \
    # pyenv install 2.7.10 --skip-existing
    # pyenv virtualenv 2.7.10 conan --force
    # pyenv rehash
    # pyenv activate conan
fi

pip install conan --upgrade
pip install conan-package-tools

conan user
