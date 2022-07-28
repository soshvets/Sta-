import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)



const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/departments',
        name: 'departments',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/DepartmentsView.vue')
    },
    {
        path: '/departments/department/:id',
        name: 'department',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/DepartmentItem.vue')
    },
    {
        path: '/workers',
        name: 'workers',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/WorkersView.vue')
    },
    {
        path: '/workerprofile/:pesel',
        name: 'worker',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/WorkerItem.vue')
    },
    {
        path: '/editworker/:pesel',
        name: 'editworker',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../components/WorkerEdit.vue')
    },
    {
        path: '/createworker',
        name: 'createworker',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../components/WorkerCreate.vue')
    },
    {
        path: '/createdepartment',
        name: 'createdepartment',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../components/DepartmentCreate.vue')
    },
    {
        path: '/editdepartment',
        name: 'editepartment',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../components/DepartmentEdit.vue')
    },
    // {
    //   path: '/dircomp',
    //   name: 'dircomp',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ '../components/DirComp.vue')
    // },

]

const router = new VueRouter({
    // mode: 'history',
    // base: process.env.BASE_URL,
    routes
})

export default router
