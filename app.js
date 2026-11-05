/** Trilok — accessible, progressive motion and room exploration. */
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let motionPaused = reducedMotion.matches;
document.addEventListener('DOMContentLoaded', () => {
  initMotion(); initNavbar(); initScrollReveals(); initBeforeAfterSliders();
  initTransformTabs(); initSpaceCurator(); initContactForm(); initScrollTop();
});
function initMotion() {
  const root = document.documentElement;
  const button = document.querySelector('.motion-toggle');
  const update = () => {
    root.classList.toggle('motion-paused', motionPaused);
    button?.setAttribute('aria-pressed', String(motionPaused));
    button?.setAttribute('aria-label', motionPaused ? 'Resume animations' : 'Pause animations');
    if (button) button.innerHTML = motionPaused ? '▶ <span>Resume motion</span>' : 'Ⅱ <span>Pause motion</span>';
    if (motionPaused) document.querySelectorAll('.reveal-on-scroll').forEach(el => el.classList.add('is-revealed'));
  };
  button?.addEventListener('click', () => { motionPaused = !motionPaused; update(); });
  reducedMotion.addEventListener('change', e => { motionPaused = e.matches; update(); });
  update();
  const scenes = document.querySelectorAll('.hero-scene');
  const controls = document.querySelectorAll('.scene-button');
  controls.forEach(button => button.addEventListener('click', () => {
    scenes.forEach((scene, i) => scene.classList.toggle('is-active', i === Number(button.dataset.scene)));
    controls.forEach(control => { const active = control === button; control.classList.toggle('is-active', active); control.setAttribute('aria-pressed', String(active)); });
  }));
  let queued = false;
  const progress = document.querySelector('.reading-progress');
  const hero = document.querySelector('.hero-keynote');
  const frame = () => {
    const y = window.scrollY;
    const distance = document.documentElement.scrollHeight - innerHeight;
    if (progress) progress.style.transform = `scaleX(${distance > 0 ? y / distance : 0})`;
    if (hero) hero.style.setProperty('--hero-offset', !motionPaused && innerWidth > 991 ? `${Math.min(y, innerHeight) * .14}px` : '0px');
    document.querySelector('#navbarApple')?.classList.toggle('scrolled', y > 40);
    queued = false;
  };
  window.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(frame); } }, {passive: true});
  frame();
}
function initNavbar() {
  const toggle = document.getElementById('appleNavToggle');
  const links = document.getElementById('appleNavLinks');
  if (!toggle || !links) return;
  toggle.setAttribute('aria-controls', links.id);
  const setOpen = open => { toggle.classList.toggle('active', open); links.classList.toggle('active', open); toggle.setAttribute('aria-expanded', String(open)); };
  setOpen(false);
  toggle.addEventListener('click', () => setOpen(!links.classList.contains('active')));
  links.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && links.classList.contains('active')) { setOpen(false); toggle.focus(); } });
  document.addEventListener('click', e => { if (!e.target.closest('.navbar-apple')) setOpen(false); });
}
function initScrollReveals() {
  if (motionPaused || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('motion-ready');
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('is-revealed'); observer.unobserve(entry.target); }
  }), {threshold: .06, rootMargin: '0px 0px -24px 0px'});
  document.querySelectorAll('.reveal-on-scroll').forEach(el => {
    if (el.parentElement.classList.contains('row')) el.style.setProperty('--reveal-delay', `${[...el.parentElement.children].indexOf(el) % 3 * 80}ms`);
    observer.observe(el);
  });
}
function initBeforeAfterSliders() {
  document.querySelectorAll('.ba-slider-container').forEach(container => {
    const handle = container.querySelector('.ba-handle');
    let value = 50;
    handle.tabIndex = 0; handle.setAttribute('role', 'slider');
    handle.setAttribute('aria-label', 'Compare room design directions');
    handle.setAttribute('aria-valuemin', '0'); handle.setAttribute('aria-valuemax', '100');
    const update = next => { value = Math.max(0, Math.min(100, next)); container.style.setProperty('--split', `${value}%`); handle.setAttribute('aria-valuenow', String(Math.round(value))); };
    const move = e => { const rect = container.getBoundingClientRect(); update((e.clientX - rect.left) / rect.width * 100); };
    container.addEventListener('pointerdown', e => { if (e.button !== 0) return; container.setPointerCapture(e.pointerId); move(e); });
    container.addEventListener('pointermove', e => { if (container.hasPointerCapture(e.pointerId)) move(e); });
    handle.addEventListener('keydown', e => {
      const steps = {ArrowLeft: -5, ArrowDown: -5, ArrowRight: 5, ArrowUp: 5};
      if (e.key in steps) { e.preventDefault(); update(value + steps[e.key]); }
      if (e.key === 'Home' || e.key === 'End') { e.preventDefault(); update(e.key === 'Home' ? 0 : 100); }
    });
    update(50);
  });
}
function initTransformTabs() {
  const buttons = [...document.querySelectorAll('.transform-tab-btn')];
  document.querySelector('.transform-tab-buttons')?.setAttribute('role', 'tablist');
  const activate = button => {
    buttons.forEach(b => { const active = b === button; b.classList.toggle('active', active); b.setAttribute('aria-selected', String(active)); b.tabIndex = active ? 0 : -1; const panel = document.getElementById(b.dataset.tab); panel?.classList.toggle('active', active); });
  };
  buttons.forEach((button, index) => {
    button.id = `room-tab-${index}`; button.setAttribute('role', 'tab'); button.setAttribute('aria-controls', button.dataset.tab);
    const panel = document.getElementById(button.dataset.tab); panel?.setAttribute('role', 'tabpanel'); panel?.setAttribute('aria-labelledby', button.id);
    button.addEventListener('click', () => activate(button));
    button.addEventListener('keydown', e => { if (['ArrowLeft','ArrowRight','Home','End'].includes(e.key)) { e.preventDefault(); const next = e.key === 'Home' ? 0 : e.key === 'End' ? buttons.length - 1 : (index + (e.key === 'ArrowRight' ? 1 : -1) + buttons.length) % buttons.length; activate(buttons[next]); buttons[next].focus(); } });
  });
  if (buttons[0]) activate(buttons[0]);
}
function initSpaceCurator() {
  const propInputs = document.querySelectorAll('input[name="curator_prop"]');
  const scopeInputs = document.querySelectorAll('input[name="curator_scope"]');
  const styleInputs = document.querySelectorAll('input[name="curator_style"]');
  const areaSlider = document.getElementById('areaRange');
  const areaDisplay = document.getElementById('areaDisplay');

  const bpProp = document.getElementById('bpProp');
  const bpScope = document.getElementById('bpScope');
  const bpStyle = document.getElementById('bpStyle');
  const bpArea = document.getElementById('bpArea');
  const waBtn = document.getElementById('blueprintWaBtn');

  function updateBlueprint() {
    let propVal = '3 BHK Flat (~1650 sqft)';
    propInputs.forEach((input) => {
      if (input.checked) propVal = input.value;
    });

    let scopeVal = 'Turnkey Civil Construction + Interiors';
    scopeInputs.forEach((input) => {
      if (input.checked) scopeVal = input.value;
    });

    let styleVal = 'Modern Fluted Luxury (Walnut)';
    styleInputs.forEach((input) => {
      if (input.checked) styleVal = input.value;
    });

    const areaVal = areaSlider ? `${parseInt(areaSlider.value, 10).toLocaleString()} sq.ft` : '1,650 sq.ft';

    if (areaDisplay) areaDisplay.textContent = areaVal;
    if (bpProp) bpProp.textContent = propVal;
    if (bpScope) bpScope.textContent = scopeVal;
    if (bpStyle) bpStyle.textContent = styleVal;
    if (bpArea) bpArea.textContent = areaVal;

    const waText = encodeURIComponent(
      `Hello Trilok Team, I would like to inquire about an estimated budget for my home project:\n\n` +
      `• Property Layout: ${propVal}\n` +
      `• Scope of Work: ${scopeVal}\n` +
      `• Preferred Style: ${styleVal}\n` +
      `• Built-up Area: ${areaVal}\n` +
      `• Service Region: Telangana & AP\n\n` +
      `Please provide an itemized proposal and discuss a 3D design consultation.`
    );

    if (waBtn) {
      waBtn.href = `https://wa.me/918332098477?text=${waText}`;
    }
  }

  propInputs.forEach((r) => r.addEventListener('change', updateBlueprint));
  scopeInputs.forEach((r) => r.addEventListener('change', updateBlueprint));
  styleInputs.forEach((r) => r.addEventListener('change', updateBlueprint));
  if (areaSlider) {
    areaSlider.addEventListener('input', updateBlueprint);
  }

  updateBlueprint();
}

/* ==========================================================================
   9. INTERACTIVE CONTACT LEAD FORM
   ========================================================================== */
function initContactForm() {
  const form = document.getElementById('contactFormLead');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('leadName')?.value.trim();
    const phone = document.getElementById('leadPhone')?.value.trim();
    const location = document.getElementById('leadLocation')?.value;
    const service = document.getElementById('leadService')?.value;
    const notes = document.getElementById('leadNotes')?.value.trim();

    if (!name || !phone || !location || !service) {
      alert('Please fill out all required fields.');
      return;
    }

    const message = encodeURIComponent(
      `Hello Trilok Team, I am requesting a Site Consultation:\n\n` +
      `• Name: ${name}\n` +
      `• WhatsApp Number: ${phone}\n` +
      `• Location: ${location}\n` +
      `• Required Service: ${service}\n` +
      (notes ? `• Details/Notes: ${notes}\n` : '') +
      `\nPlease connect with me regarding next steps.`
    );

    window.open(`https://wa.me/918332098477?text=${message}`, '_blank');
  });
}

/* ==========================================================================
   10. SCROLL TO TOP DOCK BUTTON
   ========================================================================== */
function initScrollTop() {
  const btn = document.getElementById('btnScrollTop');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: motionPaused ? 'instant' : 'smooth' });
  });
}
