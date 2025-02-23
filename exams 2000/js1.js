document.addEventListener('DOMContentLoaded', () => {
  document.body.addEventListener('click', e => {
    if (e.target.matches('a[href^="#"]')) {
      e.preventDefault();
      const t = document.querySelector(e.target.getAttribute('href'));
      if (t) t.scrollIntoView({ behavior: 'smooth' });
    }
  });

  const eb = document.getElementById('englishBtn');
  if (eb) {
    eb.addEventListener('click', e => {
      e.preventDefault();
      let m = document.createElement('div');
      m.className = 'modal';
      m.innerHTML = `<div class="modal-content">
          <span class="modal-close">&times;</span>
          <h2>Redirecting</h2>
          <p>You are about to be redirected to the English version.</p>
          <button id="modalConfirm">Continue</button>
        </div>`;
      document.body.appendChild(m);
      m.style.display = 'block';
      m.querySelector('.modal-close').addEventListener('click', () => m.remove());
      m.addEventListener('click', ev => { if (ev.target === m) m.remove(); });
      document.getElementById('modalConfirm').addEventListener('click', () => {
        window.location.href = eb.getAttribute('href');
      });
    });
  }

  const cf = document.getElementById('contactForm');
  if (cf) {
    cf.addEventListener('submit', ev => {
      ev.preventDefault();
      let valid = true;
      cf.querySelectorAll('.error-message').forEach(e => e.remove());
      const n = document.getElementById('name');
      if (n && n.value.trim() === '') {
        valid = false;
        let err = document.createElement('span');
        err.className = 'error-message';
        err.textContent = 'Name is required.';
        n.parentNode.insertBefore(err, n.nextSibling);
      }
      const em = document.getElementById('email');
      const reg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
      if (em && !reg.test(em.value)) {
        valid = false;
        let err = document.createElement('span');
        err.className = 'error-message';
        err.textContent = 'Please enter a valid email address.';
        em.parentNode.insertBefore(err, em.nextSibling);
      }
      if (valid) {
        let s = document.createElement('div');
        s.className = 'success-message';
        s.textContent = 'Form submitted successfully!';
        cf.appendChild(s);
        cf.reset();
      }
    });
}});