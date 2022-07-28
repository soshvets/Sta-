import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Paginate from 'vuejs-paginate'
import Vuelidate from 'vuelidate'
// import UIkit from 'uikit'

// import Icons from 'uikit/dist/js/uikit-icons'

 
Vue.component('Paginate-cons', Paginate)
// UIkit.use(Icons)
Vue.use(Vuelidate)
Vue.config.productionTip = false


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

