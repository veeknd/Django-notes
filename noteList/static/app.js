let themeToggle = document.getElementById('theme');
 let theme = localStorage.getItem('theme');
 console.log(theme)

themeToggle.addEventListener('click',()=>{
    
    if (localStorage.getItem('theme') == 'dark'){
        localStorage.setItem('theme','light');
        toggleTheme()
    }
    else{
        localStorage.setItem('theme','dark');
        toggleTheme()
    }
    
})

let  toggleTheme = async () => {
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
}

if (theme == 'dark'){
    toggleTheme()
}