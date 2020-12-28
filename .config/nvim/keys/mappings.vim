"                             _                 
" _ __ ___   __ _ _ __  _ __ (_)_ __   __ _ ___ 
"| '_ ` _ \ / _` | '_ \| '_ \| | '_ \ / _` / __|
"| | | | | | (_| | |_) | |_) | | | | | (_| \__ \
"|_| |_| |_|\__,_| .__/| .__/|_|_| |_|\__, |___/
"                |_|   |_|            |___/     

"Set Leader keys to space
let mapleader = '\'

" Custom Key mapping
" Personal
nnoremap <leader>sp : set spell<CR>
nnoremap <leader>spx : set nospell<CR>
nnoremap <leader>h : split  
nnoremap <leader>v : vsplit 
nnoremap <leader>t : split term://zsh<CR>
nnoremap <leader>s : w<CR>
nnoremap <leader>q : q!<CR>

" Plugins
nnoremap <F5> : source $MYVIMRC<CR>
nnoremap <F6> : NERDTreeToggle<CR>
nnoremap <leader>md : MarkdownPreview<CR>
nnoremap <leader>mds : MarkdownPreviewStop<CR>
nnoremap <leader>rn : NERDTreeRefreshRoot<CR>
nnoremap <space>r : RnvimrToggle<CR>
tnoremap <silent> <M-i> <C-\><C-n>:RnvimrResize<CR>
