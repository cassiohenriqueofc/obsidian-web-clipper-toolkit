const localeMenu=document.getElementById('language');
localeMenu.addEventListener('change',()=>{window.location.href=`../${localeMenu.value}/index.html`;});
const pause=document.getElementById('pause');
pause.addEventListener('click',()=>{
 const active=document.documentElement.classList.toggle('paused');
 pause.setAttribute('aria-pressed',String(active));
 pause.textContent=active?pause.dataset.resume:pause.dataset.pause;
});
