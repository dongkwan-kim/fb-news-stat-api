import Vue from 'vue'
import App from './App.vue'
import PortalNews from './PortalNews.vue'

Vue.component('portal', PortalNews);

var app = new Vue({
  el: '#app',
  render : h => h(App),
  data : {
      title : "Facebook Stats"
  }
})
