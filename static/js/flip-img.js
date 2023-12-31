document.addEventListener('DOMContentLoaded',() => {
        $('.back-face').hide();
    });
function flipCard(card) {
    const cards=document.querySelectorAll('.card');
    cards.forEach( element => {
        if (card == element){
            element.style.height='500px';
            element.querySelector('.back-face').style.display='block';
        }
        if (card == element && element.classList.contains('flipped')){
            card.style.height='333px';
            element.querySelector('.back-face').style.display='none';
        }
        if (element != card && element.classList.contains('flipped')){
            element.style.height='333px';
            element.classList.toggle('flipped');
            element.querySelector('.back-face').style.display='none';
        }
    })
    card.classList.toggle('flipped');
  }