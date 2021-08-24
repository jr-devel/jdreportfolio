var drop_btn = document.querySelector('#drop_btn');
var drop_menu = document.querySelector('#drop_menu');
var icon_bar = document.querySelector('#menuBars');
var icon_bar_quit = document.querySelector('#menuQuit');

drop_btn.addEventListener('click', () => {
    drop_menu.style.display = 'inline-block';
    icon_bar.style.display = 'none';
    icon_bar_quit.style.display = 'inherit';
})

drop_btn.addEventListener('focusout', () => {
    drop_menu.style.display = 'none';
    icon_bar.style.display = 'inherit';
    icon_bar_quit.style.display = 'none';
})