/* ============================================
   Rotinita - Rotinas Visuais
   Site Scripts
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // --- Hero video playback ---
  const heroVideo = document.querySelector('.hero-video');
  if (heroVideo) {
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const syncVideoPlayback = () => {
      if (reducedMotion.matches) {
        heroVideo.pause();
        return;
      }

      heroVideo.play().catch(() => {});
    };

    reducedMotion.addEventListener('change', syncVideoPlayback);
    syncVideoPlayback();
  }

  // --- Header scroll effect ---
  const header = document.querySelector('.site-header');
  if (header) {
    const hero = document.querySelector('.hero');
    const onScroll = () => {
      const overHero = header.classList.contains('site-header--hero')
        && hero
        && hero.getBoundingClientRect().bottom > header.offsetHeight;

      header.classList.toggle('over-hero', Boolean(overHero));
      header.classList.toggle('scrolled', !overHero && window.scrollY > 10);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    onScroll();
  }

  // --- Mobile nav toggle ---
  const toggle = document.querySelector('.nav-toggle');
  const mobileNav = document.querySelector('.nav-mobile');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      header?.classList.toggle('menu-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });

    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        header?.classList.remove('menu-open');
        document.body.style.overflow = '';
      });
    });
  }

  // --- Back to top ---
  const btt = document.querySelector('.back-to-top');
  if (btt) {
    window.addEventListener('scroll', () => {
      btt.classList.toggle('visible', window.scrollY > 500);
    }, { passive: true });

    btt.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // --- Fade-up on scroll (IntersectionObserver) ---
  const fadeEls = document.querySelectorAll('.fade-up');
  if (fadeEls.length && 'IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    fadeEls.forEach(el => obs.observe(el));
  } else {
    fadeEls.forEach(el => el.classList.add('visible'));
  }

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

});
