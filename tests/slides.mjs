// Executa os scripts de docs/index.html com um DOM mínimo e imprime, em JSON,
// a página inicial e o HTML de cada slide. Usado por tests/apresentacao.py.
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const pagina = readFileSync(new URL('../docs/index.html', import.meta.url), 'utf8');
const scripts = [...pagina.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);

const elementos = {};
const elemento = () => ({
  innerHTML: '', textContent: '', dataset: {}, style: {}, content: '',
  classList: { add() {}, remove() {}, toggle() {} },
  toggleAttribute() {}, setAttribute() {}, addEventListener() {},
  querySelectorAll: () => [], replaceChildren() {}, get offsetWidth() { return 0; },
});
const document = {
  documentElement: { dataset: {} },
  getElementById: id => (elementos[id] ??= elemento()),
  querySelector: () => elemento(),
  querySelectorAll: () => [],
  addEventListener() {},
  createElement: () => elemento(),
};
const contexto = {
  document,
  location: { hash: '#/' },
  history: { replaceState() {} },
  localStorage: { getItem: () => null, setItem() {} },
  matchMedia: () => ({ matches: false, addEventListener() {} }),
  getComputedStyle: () => ({ getPropertyValue: () => '#0F120D' }),
  window: { addEventListener() {}, scrollTo() {} },
  console,
};
vm.createContext(contexto);
// const/let do script principal ficam no escopo global do contexto, como no navegador.
vm.runInContext(scripts.join('\n;\n') + '\n;globalThis.__ALL = ALL;', contexto);

const slides = [];
for (const d of contexto.__ALL) {
  d.slides.forEach((s, i) => {
    contexto.renderSlide(d, i);
    slides.push({ key: d.key, n: d.n, i, h: s.h, eyebrow: s.eyebrow || '', html: elementos.slide.innerHTML });
  });
}
const exercicios = contexto.__ALL.map(d => ({
  key: d.key, n: d.n, title: d.title, time: d.time, antes: !!d.antes, mod: d.mod,
  entrega: d.entrega || '', slides: d.slides.map(s => ({ h: s.h, eyebrow: s.eyebrow || '' })),
}));
console.log(JSON.stringify({ home: elementos.home.innerHTML, exercicios, slides }));
