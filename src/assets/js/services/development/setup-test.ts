import { createApp } from 'vue';
import AppVue from './vue/AppVue.vue';

const el = document.getElementById('vue');

if (el) {
  const all = JSON.parse(el.dataset.all);

  console.log('all', all);

  createApp(AppVue, { val1: all.val1 }).mount(el);
}
