" Vim configuration file
" Date updated:
" Owner: Keith Kee KW

" vim-plug configuration
" ======================
call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'itchyny/lightline.vim'
Plug 'arcticicestudio/nord-vim'

"Initialize plugin system
call plug#end()

" Text Editor settings
filetype indent plugin on
syntax on
set number
set showcmd
set tabstop=4
set softtabstop=4
set expandtab
set cursorline
set wildmenu
set showmatch

" Custom Key Map
nmap <F6> : NERDTreeToggle<CR>

" Plugin Settings
set laststatus=2
colorscheme nord

let g:lightline = {
    \ 'colorscheme': 'nord',
    \ }
