set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin '907th/vim-auto-save'
Plugin 'SirVer/ultisnips'
Plugin 'lervag/vimtex'
Plugin 'Shougo/deoplete.nvim'
Plugin 'roxma/nvim-yarp'
Plugin 'roxma/vim-hug-neovim-rpc'
Plugin 'morhetz/gruvbox'
Plugin 'ap/vim-css-color'
Plugin 'chrisbra/unicode.vim'
call vundle#end()
filetype plugin indent on

let g:gruvbox_termcolors=16
let g:tex_flavor = 'latex'
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:deoplete#enable_at_startup = 1
let g:vimtex_quickfix_autoclose_after_keystrokes= 1

syntax enable
autocmd vimenter * ++nested colorscheme gruvbox

set termguicolors
set background=dark
set mouse=a

execute "set t_8f=\e[38;2;%lu;%lu;%lum"
execute "set t_8b=\e[48;2;%lu;%lu;%lum"

:set number
