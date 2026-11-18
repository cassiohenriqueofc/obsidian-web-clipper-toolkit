const localeMenu=document.getElementById('language');
localeMenu.addEventListener('change',()=>{window.location.href=`../${localeMenu.value}/index.html`;});
const pause=document.getElementById('pause');
const flowImage=document.getElementById('flow-image');
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches&&flowImage){flowImage.src=flowImage.dataset.static;pause.setAttribute('aria-pressed','true');pause.textContent=pause.dataset.resume;}
pause.addEventListener('click',()=>{
 const active=document.documentElement.classList.toggle('paused');
 pause.setAttribute('aria-pressed',String(active));
 pause.textContent=active?pause.dataset.resume:pause.dataset.pause;
 if(flowImage)flowImage.src=active?flowImage.dataset.static:`../assets/feature-flow.gif?play=${Date.now()}`;
});
