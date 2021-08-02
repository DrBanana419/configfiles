call plug#begin()
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'SirVer/ultisnips'
Plug 'lervag/vimtex'
call plug#end()
let g:deoplete#enable_at_startup = 1
set cursorline
highlight CursorLine cterm=NONE ctermbg=242

