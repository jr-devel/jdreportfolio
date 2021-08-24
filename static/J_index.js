var btn = document.querySelector('#drop-proyects-list');
var proyects = document.querySelectorAll('.rep-obj');

btn.addEventListener('click', () => {
    proyects.forEach(proyect => {
        proyect.style.display = 'flex';
        proyect.style.transition = 'display ease 1s';
    });
})