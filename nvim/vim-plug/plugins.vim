" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')
	Plug 'scrooloose/NERDTree'		    "File Explorer
	Plug 'arcticicestudio/nord-vim'		" Nord Theme
	Plug 'itchyny/lightline.vim'		" Status Line
    Plug 'luochen1990/rainbow'          " Colorize all the brackets
    Plug 'junegunn/fzf.vim'             " File Finder
call plug#end()					        " Initialize Plugins

"Settings for luochen1990/rainbow
let g:rainbow_active=1
