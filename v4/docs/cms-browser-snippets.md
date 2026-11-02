# Browser snippets for CMS research (built-in browser pane or Claude in Chrome)

Use these in the page context with the JavaScript tool, on amazon.com Books pages, after the delivery location is set to a US ZIP and with NO sign-in. They only read pages the owner could read in a private window. Read in small batches (about 8 product pages per call, or run in the background and poll a window variable) to avoid time-outs. Describe in the Research Proof exactly what was done.

## 1. Read a search-result page (titles, price, rating, ASIN)
```js
const out=[];for(const p of [1,2]){const h=await (await fetch('/s?k='+encodeURIComponent('YOUR QUERY')+'&i=stripbooks&page='+p)).text();const d=new DOMParser().parseFromString(h,'text/html');d.querySelectorAll('[data-component-type="s-search-result"]').forEach(e=>out.push({asin:e.dataset.asin,t:(e.querySelector('h2')?.innerText||'').slice(0,110),p:e.querySelector('.a-price .a-offscreen')?.innerText,r:(e.querySelector('[aria-label*="out of 5"]')?.getAttribute('aria-label')||'').slice(0,18),by:(e.innerText.match(/by .*?\|.*?\d{4}/)||[''])[0].slice(0,80)}))}
JSON.stringify(out)
```

## 2. Read product-page facts for a list of ASINs (rank, pages, date, rating)
```js
window.R=[];const f=async(a)=>{try{const h=await (await fetch('/dp/'+a)).text();const d=new DOMParser().parseFromString(h,'text/html');const t=d.body.innerText.replace(/\s+/g,' ');const g=(re)=>(t.match(re)||[''])[0];
window.R.push({a,title:d.title.slice(0,70),bsr:g(/Best Sellers Rank:?.{0,170}/).replace(/Customer Reviews.*/,''),pages:g(/Print length\s*[\d,]+ pages/),pub:g(/Publication date\s*\w+ \d+, \d{4}/),rt:g(/\d\.\d out of 5 stars \(\d[\d,]*\)/),dim:g(/Dimensions\s*[\d. x]+ inches/)})}catch(e){window.R.push({a,err:e.message})}};
window.done=false;(async()=>{for(const a of ['ASIN1','ASIN2']){await f(a)}window.done=true})();'started'
```
Then poll: `JSON.stringify({done:window.done,r:window.R})`.

## 3. Real typed-box autocomplete
Focus the search box, set the value with the native setter, dispatch an `input` event, wait about 1.8 seconds, then read the suggestion rows (`[id^="sac-suggestion-row"]`). Record only suggestions actually shown. Example:
```js
const el=document.querySelector('#twotabsearchtextbox');Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(el,'your seed');el.dispatchEvent(new Event('input',{bubbles:true}));await new Promise(r=>setTimeout(r,1800));
JSON.stringify([...new Set([...document.querySelectorAll('[id^="sac-suggestion-row"], .s-suggestion')].map(e=>e.innerText.trim().split('\n')[0]))])
```

## 4. Confirm the delivery location
`document.querySelector('#glow-ingress-line2')?.innerText` should show a US place and ZIP. If it shows another country, prices are in another currency.

## 5. Exact-title collision count
Run snippet 1 for the exact title and count results whose title starts with the same words.

## 6. Bestseller subcategory
Find the category node from a product page's rank links (`a[href*="bestsellers"]`), then open `/gp/bestsellers/books/<node>/` and read the top entries (`#gridItemRoot`). Guessing node numbers returns empty or wrong categories.

## Limits (honest)
Review pages and some customer views need sign-in: do not sign in; ask the owner to paste. Amazon changes its markup; if a selector returns nothing, say so and fall back to reading visible text. Autocomplete, rank and price are signals only.
