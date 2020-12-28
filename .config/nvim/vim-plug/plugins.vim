"       _             _           
" _ __ | |_   _  __ _(_)_ __  ___ 
"| '_ \| | | | |/ _` | | '_ \/ __|
"| |_) | | |_| | (_| | | | | \__ \
"| .__/|_|\__,_|\__, |_|_| |_|___/
"|_|            |___/             

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
    Plug 'junegunn/fzf.vim'             " File Finder
    Plug 'jiangmiao/auto-pairs'         " Insert or delete brackets, parens, quotes in pair.
    Plug 'airblade/vim-gitgutter'
    Plug 'tpope/vim-fugitive'
    Plug 'mattn/emmet-vim'
    Plug 'ryanoasis/vim-devicons'
    Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
    Plug 'tpope/vim-surround'
    Plug 'sheerun/vim-polyglot'
    Plug 'vimwiki/vimwiki'
    Plug 'kevinhwang91/rnvimr'
    Plug 'godlygeek/tabular'
    Plug 'plasticboy/vim-markdown'
    Plug 'junegunn/limelight.vim'
    Plug 'junegunn/goyo.vim'
    Plug 'prettier/vim-prettier', { 'do': 'yarn install' }
call plug#end()					        " Initialize Plugins
