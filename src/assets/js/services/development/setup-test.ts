import { createApp } from 'vue';
import AppVue from './vue/AppVue.vue';

import Swiper from 'swiper';
import 'swiper/css/bundle';
import { Autoplay, Pagination } from 'swiper/modules';

const el = document.getElementById('vue');

if (el) {
  const all = JSON.parse(el.dataset.all);

  console.log('all', all);

  createApp(AppVue, { val1: all.val1 }).mount(el);
}

console.log('SlideShow setup');

const swiper = new Swiper('.swiper1', {
  modules: [Autoplay, Pagination],
  loop: true,
  speed: 1000,

  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
  pagination: {
    el: '.swiper-pagination1',
    clickable: true,
  },
});
