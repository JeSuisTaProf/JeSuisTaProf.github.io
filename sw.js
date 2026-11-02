/* Service worker : réseau d'abord (les modifications de la professeure apparaissent tout de suite),
   copie en cache en secours quand l'élève n'a plus de connexion. */
const CACHE='jesuistaprof-v1';
self.addEventListener('install',e=>{self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request,u=new URL(r.url);
  if(r.method!=='GET'||u.origin!==location.origin||u.pathname.includes('/admin/')||r.headers.has('range'))return;
  e.respondWith(fetch(r).then(res=>{
    if(res.ok&&res.status===200){const c=res.clone();caches.open(CACHE).then(x=>x.put(r,c))}
    return res;
  }).catch(()=>caches.match(r)));
});
