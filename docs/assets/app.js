const cards=[...document.querySelectorAll('.card')];
const search=document.querySelector('#search');
const buttons=[...document.querySelectorAll('[data-filter]')];
let layer='All';
function filter(){const query=search.value.trim().toLocaleLowerCase();let count=0;for(const card of cards){const show=(layer==='All'||card.dataset.layer===layer)&&card.textContent.toLocaleLowerCase().includes(query);card.hidden=!show;if(show)count++;}document.querySelector('#count').textContent=`${count} ${count===1?'skill':'skills'}`;document.querySelector('#empty').hidden=count!==0;}
search.addEventListener('input',filter);
for(const button of buttons)button.addEventListener('click',()=>{layer=button.dataset.filter;for(const b of buttons)b.setAttribute('aria-pressed',String(b===button));filter();});
