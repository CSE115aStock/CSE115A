## OSX environment setup.
### Install mambaforge
```shell
brew install --cask mambaforge
```
### create and source `~/.zshrc` file
```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/usr/local/Caskroom/mambaforge/base/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/usr/local/Caskroom/mambaforge/base/etc/profile.d/conda.sh" ]; then
        . "/usr/local/Caskroom/mambaforge/base/etc/profile.d/conda.sh"
    else
        export PATH="/usr/local/Caskroom/mambaforge/base/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
export PATH="/opt/homebrew/Caskroom/mambaforge/base/bin:$PATH"
```
### Install the stocks environment
```shell
mamba env create -f $HOME/repos/CSE115a/environment.yaml
```
### Activate your new python environment
```shell
conda activate stocks
```
### Run app
```shell
export PYTHONPATH=path to cse115a folder
streamlit run streamlit_app.py
```
