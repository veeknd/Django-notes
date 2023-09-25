let theme = document.getElementById('theme');
theme.addEventListener('click',()=>{
    document.body.classList.toggle('dark');
    let navbar = document.getElementById('navbar-theme');
    navbar.classList.toggle('navbar-dark');
    navbar.classList.toggle('bg-dark');
    navbar.classList.toggle('bg-body-tertiary');
    let cards = document.getElementsByClassName('card')
    for(let card of cards){
        card.classList.toggle('bg-dark');
        card.classList.toggle('text-white');
    }
    let title = document.getElementById('id_title');
    let content = document.getElementById('id_content');
    title.classList.toggle('dark');
    content.classList.toggle('dark');
})
