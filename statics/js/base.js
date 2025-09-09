const menu = document.getElementById('menu');
const sidebar = document.querySelector('.side-bar');
const arowLeft = document.getElementById('arrow-left');
  

menu.addEventListener('click',changeMenu)
arowLeft.addEventListener('click',changeClote)

function changeMenu(){
    menu.style.display = 'none'
    arowLeft.style.display = 'flex'
    sidebar.style.width = "250px";
 }

 function changeClote(){
    menu.style.display = 'flex'
    arowLeft.style.display = 'none'
    sidebar.style.width = "0";
 }


// const menu = document.getElementById('menu');
// const sidebar = document.querySelector('.side-bar');
// const arowLeft = document.getElementById('arrow-left');

// if (menu && sidebar && arowLeft) {
//     menu.addEventListener('click', () => {
//         sidebar.classList.add('active'); // Add 'active' class to slide it in
//     });

//     arowLeft.addEventListener('click', () => {
//         sidebar.classList.remove('active'); // Remove 'active' class to slide it out
//     });
// }
