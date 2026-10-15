#!/bin/zsh
# Levanta el blog en local: http://localhost:4000
cd "$(dirname "$0")"
export PATH=/opt/homebrew/opt/ruby/bin:$PATH
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
export RUBYOPT="-r$PWD/.local/ruby_compat.rb"
bundle exec jekyll serve --livereload "$@"
