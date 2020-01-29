# !/usr/bin/env bash
if [ "$RCS_DIR" != "" ]; then
  echo 'Skiping: already installed'
else
  install () {
    echo ''
    echo '# REACT STYLED COMPONENTS CLI CONFIG:';
    printf 'export RCS_DIR="%s"\n' $(pwd);
    echo 'alias rcs="python3 $RCS_DIR/rcs"';
    echo 'alias rcs_config="python3 $RCS_DIR/rcs_config"'
    echo ''
    echo 'clear'
  }
  curr_shell_parts=($(echo $SHELL | tr "/" "\n"))
  size=${#curr_shell_parts[@]}
  curr_shell="${curr_shell_parts[$size]}"
  if [ "$curr_shell" != "zsh" ]; then
    install >> ~/.bashrc && source ~/.bashrc
  else
    install >> ~/.zshrc && source ~/.zshrc
  fi
  echo 'Success: process complete!'
  echo 'Type "rcs help" to see the commands available.'
fi
