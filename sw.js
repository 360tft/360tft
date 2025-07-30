---
layout: null
---

// 360TFT Service Worker for Performance Optimization
const CACHE_NAME = '360tft-v1.0';
const urlsToCache = [
  '{{ "/" | relative_url }}',
  '{{ "/assets/css/main.css" | relative_url }}',
  '{{ "/assets/js/main.js" | relative_url }}',
  '{{ "/assets/images/logo-360tft.png" | relative_url }}',
  '{{ "/about-kevin-middleton/" | relative_url }}',
  '{{ "/game-model/" | relative_url }}',
  '{{ "/328-sessions/" | relative_url }}',
  '{{ "/coaches-compass/" | relative_url }}',
  '{{ "/football-coaching-academy/" | relative_url }}'
];

// Install event - cache resources
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event - serve from cache when possible
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Return cached version or fetch from network
        return response || fetch(event.request);
      }
    )
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});