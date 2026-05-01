// Mobile nav toggle
const toggle = document.getElementById('navToggle');
const navLinks = document.querySelector('.nav-links');
toggle?.addEventListener('click', () => navLinks.classList.toggle('open'));

// Close mobile nav on link click
navLinks?.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => navLinks.classList.remove('open'));
});

// Auto-dismiss flash messages
document.querySelectorAll('.flash').forEach(el => {
    setTimeout(() => el.style.opacity = '0', 4000);
    setTimeout(() => el.remove(), 4500);
});

// Photo: grayscale → color on first hover, stays color after
document.addEventListener('DOMContentLoaded', () => {
    const photo = document.querySelector('.about-photo');
    if (photo) {
        photo.addEventListener('mouseenter', function handler() {
            photo.classList.add('photo-revealed');
            photo.removeEventListener('mouseenter', handler);
        });
    }
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navAnchors.forEach(a => {
                a.style.color = a.getAttribute('href') === '#' + entry.target.id
                    ? 'var(--accent)' : '';
            });
        }
    });
}, { threshold: 0.4 });

sections.forEach(s => observer.observe(s));
